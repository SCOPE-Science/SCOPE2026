#!/usr/bin/env python3
import hashlib, itertools
from collections import Counter, deque

N=5
PERMS=list(itertools.permutations(range(1,N+1)))
INDEX={p:i for i,p in enumerate(PERMS)}
ID=INDEX[tuple(range(1,N+1))]

def kendall_pair(p,q):
    pp=[0]*(N+1); qq=[0]*(N+1)
    for i,x in enumerate(p): pp[x]=i
    for i,x in enumerate(q): qq[x]=i
    s=0
    for a in range(1,N+1):
        for b in range(a+1,N+1):
            s += ((pp[a]-pp[b])*(qq[a]-qq[b]) < 0)
    return s

def bfs_from(src):
    dist=[-1]*len(PERMS); dist[src]=0; dq=deque([src])
    while dq:
        u=dq.popleft(); p=PERMS[u]
        for j in range(N-1):
            a=list(p); a[j],a[j+1]=a[j+1],a[j]
            v=INDEX[tuple(a)]
            if dist[v] < 0:
                dist[v]=dist[u]+1; dq.append(v)
    return dist

# Independent metric reconstruction via adjacent-transposition graph.
PAIR_CHECKS=0
for i in range(len(PERMS)):
    d=bfs_from(i)
    for j in range(i+1,len(PERMS)):
        assert d[j]==kendall_pair(PERMS[i],PERMS[j])
        PAIR_CHECKS += 1

V=len(PERMS)
ALL=(1<<V)-1
ADJ=[0]*V
for i in range(V):
    for j in range(i+1,V):
        if kendall_pair(PERMS[i],PERMS[j]) >= 3:
            ADJ[i] |= 1<<j; ADJ[j] |= 1<<i

def color_sort(P):
    order=[]; bounds=[]; color=0; rem=P
    while rem:
        color += 1
        q=rem
        while q:
            b=q & -q; v=b.bit_length()-1
            order.append(v); bounds.append(color)
            rem ^= b
            q ^= b
            q &= ~ADJ[v]
    return order,bounds

def exists_target_with_identity(target):
    found=False
    def rec(depth,P):
        nonlocal found
        if found: return
        order,bounds=color_sort(P)
        for k in range(len(order)-1,-1,-1):
            if depth+bounds[k] < target:
                return
            v=order[k]; bv=1<<v
            if not (P & bv): continue
            if depth+1 >= target:
                found=True; return
            Q=P & ADJ[v]
            if Q: rec(depth+1,Q)
            if found: return
            P ^= bv
    rec(1,ADJ[ID])
    return found

assert not exists_target_with_identity(21)
TARGET=20
FOUND=[]
def enum_expand(R,P):
    order,bounds=color_sort(P)
    for k in range(len(order)-1,-1,-1):
        if len(R)+bounds[k] < TARGET:
            return
        v=order[k]; bv=1<<v
        if not (P & bv):
            continue
        R.append(v)
        if len(R)==TARGET:
            FOUND.append(tuple(sorted(R)))
        else:
            Q=P & ADJ[v]
            if Q:
                enum_expand(R,Q)
        R.pop()
        P ^= bv

enum_expand([ID],ADJ[ID])
NORMALIZED=sorted(set(FOUND))
assert len(NORMALIZED)==532

def word(i): return ''.join(map(str,PERMS[i]))
def code_line(code): return ','.join(sorted(word(i) for i in code))
def lines_hash(codes):
    data=('\n'.join(code_line(c) for c in codes)+'\n').encode()
    return hashlib.sha256(data).hexdigest()
NORMAL_HASH=lines_hash(NORMALIZED)
assert NORMAL_HASH=='502486838fdc6f3400e2372677ebb1ebf733bf9bdef71b690d7fad3c84d82eb2'

RELABELS=list(itertools.permutations(range(1,N+1)))
def relabel_perm(p,m): return tuple(m[x-1] for x in p)
def relabel_code(code,m): return tuple(sorted(INDEX[relabel_perm(PERMS[i],m)] for i in code))
def reverse_code(code): return tuple(sorted(INDEX[tuple(reversed(PERMS[i]))] for i in code))

LAB=set()
for c in NORMALIZED:
    for m in RELABELS:
        LAB.add(relabel_code(c,m))
LABELED=sorted(LAB)
assert len(LABELED)==3192
LAB_HASH=lines_hash(LABELED)
assert LAB_HASH=='018236d2efcea3622ecab4ccd90d7334de08a6074a5669452884c2d8d500d2b3'
# Double-count consistency: each code has 20 choices of codeword to map to identity and each normalization has 120 relabelings.
assert len(LABELED)*20 == len(NORMALIZED)*120
for c in LABELED:
    assert len(c)==TARGET
    for a,b in itertools.combinations(c,2): assert ADJ[a] & (1<<b)

def orbit(c):
    out=set()
    for m in RELABELS:
        d=relabel_code(c,m); out.add(d); out.add(reverse_code(d))
    return out
unseen=set(LABELED); ORBITS=[]
while unseen:
    c=min(unseen); o=orbit(c)
    assert o <= LAB
    ORBITS.append((c,o)); unseen -= o
sizes=Counter(len(o) for _,o in ORBITS)
assert len(ORBITS)==24
assert sizes==Counter({240:9,120:5,60:4,48:2,30:3,6:1})
for _,o in ORBITS:
    assert 240 % len(o)==0

PAPER_TXT='''12345 14253 15234 15432 21543 23154 23451 24135 25431 31425 31524 34512 35241 41325 42513 43251 45132 52314 53142 54321'''.split()
PAPER=tuple(sorted(INDEX[tuple(map(int,s))] for s in PAPER_TXT))
assert len(PAPER)==20 and PAPER in LAB
assert all(kendall_pair(PERMS[a],PERMS[b])>=3 for a,b in itertools.combinations(PAPER,2))
PAPER_ORBIT=len(orbit(PAPER))
assert PAPER_ORBIT==120

print('VERIFY_OK vertices=120 pair_checks=%d maximum=20 normalized_maxima=532 labeled_maxima=3192 natural_group=240 orbits=24 orbit_sizes=6x1,30x3,48x2,60x4,120x5,240x9 paper_example_orbit=120 normalized_sha256=%s labeled_sha256=%s' % (PAIR_CHECKS,NORMAL_HASH,LAB_HASH))
