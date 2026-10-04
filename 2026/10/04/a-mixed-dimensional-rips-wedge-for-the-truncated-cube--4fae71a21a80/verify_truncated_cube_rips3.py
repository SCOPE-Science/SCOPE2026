#!/usr/bin/env python3
from collections import Counter, defaultdict, deque
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = json.loads((HERE/'morse_certificate.json').read_text(encoding='utf-8'))

# Vertices are 3*x+i with x in F_2^3 represented by 0..7 and i in {0,1,2}.
# For fixed x, the three (x,i) form the triangle created by truncating cube vertex x.
# Along cube direction i, (x,i) is joined to (x xor 2^i,i).
V = list(range(24))
adj = {v:set() for v in V}
def add(a,b):
    adj[a].add(b); adj[b].add(a)
for x in range(8):
    tri=[3*x+i for i in range(3)]
    for a in range(3):
        for b in range(a+1,3): add(tri[a],tri[b])
    for i in range(3):
        y=x^(1<<i)
        if x<y: add(3*x+i,3*y+i)

assert sum(len(adj[v]) for v in V)//2 == 36
assert sorted(set(len(adj[v]) for v in V)) == [3]

# All-pairs graph distances.
dist={}
for s in V:
    q=deque([s]); d={s:0}
    while q:
        u=q.popleft()
        for w in adj[u]:
            if w not in d:
                d[w]=d[u]+1; q.append(w)
    assert len(d)==24
    dist[s]=d
assert max(dist[u][v] for u in V for v in V)==6

# Third distance power and its clique complex.
pow_adj={v:set() for v in V}
for u in V:
    for v in V:
        if u<v and dist[u][v] <= 3:
            pow_adj[u].add(v); pow_adj[v].add(u)

def enumerate_cliques():
    out=[]
    def rec(prefix, candidates):
        cand=list(candidates)
        for idx,v in enumerate(cand):
            new=prefix+(v,)
            out.append(new)
            tail=[w for w in cand[idx+1:] if w in pow_adj[v] and all(w in pow_adj[z] for z in prefix)]
            rec(new, tail)
    rec((),V)
    return set(out)

simplices=enumerate_cliques()
f=Counter(len(s)-1 for s in simplices)
assert f == Counter({0:24,1:156,2:376,3:372,4:144,5:20}), f

# Deterministic sequential vertex matching. Each stage pairs a remaining simplex sigma
# with sigma union {v} when both remain and the upper simplex exists.
order=CERT['vertex_order']
unmatched=set(simplices)
pairs=[]
for v in order:
    candidates=sorted(
        (s for s in list(unmatched) if v not in s and tuple(sorted(s+(v,))) in unmatched),
        key=lambda s:(len(s),s)
    )
    for s in candidates:
        if s not in unmatched: continue
        t=tuple(sorted(s+(v,)))
        if t in unmatched:
            unmatched.remove(s); unmatched.remove(t); pairs.append((s,t))

critical=sorted(unmatched,key=lambda s:(len(s),s))
expected=[tuple(x) for x in CERT['critical_simplices']]
assert critical == expected, (critical,expected)
assert len(pairs)==542

# Check every matched pair is a codimension-one Hasse edge and no simplex is reused.
seen=set()
for s,t in pairs:
    assert len(t)==len(s)+1 and set(s)<set(t)
    assert s not in seen and t not in seen
    seen.add(s); seen.add(t)

# Explicit acyclicity of the directed Hasse diagram: matched arrows point up,
# every other codimension-one edge points down.
pairset=set(pairs)
indeg={s:0 for s in simplices}
out=defaultdict(list)
for t in simplices:
    if len(t)<=1: continue
    for i in range(len(t)):
        s=t[:i]+t[i+1:]
        if (s,t) in pairset:
            a,b=s,t
        else:
            a,b=t,s
        out[a].append(b); indeg[b]+=1
q=deque([s for s in simplices if indeg[s]==0])
count=0
while q:
    a=q.popleft(); count+=1
    for b in out[a]:
        indeg[b]-=1
        if indeg[b]==0:q.append(b)
assert count==len(simplices), 'matching Hasse orientation has a directed cycle'

# Signed Morse boundary from critical 3-cells to the sole critical 2-cell.
pair_up={s:t for s,t in pairs}
crit2=[s for s in unmatched if len(s)==3]
crit3=[s for s in unmatched if len(s)==4]
assert len(crit2)==1 and len(crit3)==6
c2=crit2[0]

def incidence(t,s):
    assert len(t)==len(s)+1 and set(s)<set(t)
    for i,v in enumerate(t):
        if v not in s:
            return -1 if i%2 else 1
    raise AssertionError

memo={}
visiting=set()
def reduce_2cell(s):
    # coefficient of the critical 2-cell after cancelling matched (2,3)-pairs.
    if s==c2: return 1
    if s not in pair_up:
        # A 2-cell matched downward is removed by a (1,2)-pair and contributes no
        # critical 2-generator.
        return 0
    if s in memo:return memo[s]
    assert s not in visiting, 'cycle in gradient recurrence'
    visiting.add(s)
    t=pair_up[s]
    assert len(s)==3 and len(t)==4
    a=incidence(t,s)
    total=0
    for i in range(len(t)):
        sp=t[:i]+t[i+1:]
        if sp==s: continue
        total += -incidence(t,sp)*reduce_2cell(sp)//a
    visiting.remove(s); memo[s]=total
    return total

boundary={}
for beta in sorted(crit3):
    total=0
    for i in range(len(beta)):
        s=beta[:i]+beta[i+1:]
        total += incidence(beta,s)*reduce_2cell(s)
    boundary[' '.join(map(str,beta))]=total
assert boundary == CERT['critical_3_to_2_boundary'], boundary
assert set(boundary.values())=={0}

print('vertices=24 edges=36 diameter=6')
print('f_vector=' + str([f[i] for i in range(6)]))
print('critical=' + str(critical))
print('morse_d3=' + str(boundary))
print('VERIFY_OK')
