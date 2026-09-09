"""Lane 470 emergent verification: finite chromatic profile of Cay(F2,S) + depth-4 spoiler no-go.
S={a,A,b,B,w,W}, w=abAB, W=baBA. Checks:
 (1) girth exactly 5 (no non-backtracking closed 3/4-walks; explicit C5);
 (2) B4 tree-ball (n=161): chi=3 (C5 inside => >=3; loaded coloring => <=3, root 0);
 (3) spoiler no-go: fixed coloring defeats every depth-4 Player-I strategy (strategy-mirror proof + simulation).
Writes VERIFY_OK on success.
"""
import itertools, json, sys
from collections import deque

INV = {'a':'A','A':'a','b':'B','B':'b'}
def red(w):
    out=[]
    for ch in w:
        if out and out[-1]==INV[ch]: out.pop()
        else: out.append(ch)
    return ''.join(out)
def invw(w): return ''.join(INV[c] for c in reversed(w))
W = red('abAB'); Wi = invw(W)
S = ['a','A','b','B',W,Wi]
assert len(set(S))==6

def tree_ball(r):
    seen={'':0}; q=deque([''])
    while q:
        u=q.popleft()
        if seen[u]>=r: continue
        for g in 'aAbB':
            v=red(u+g)
            if v not in seen:
                seen[v]=seen[u]+1; q.append(v)
    return seen
def graph_on(V):
    idx={v:i for i,v in enumerate(V)}
    adj=[set() for _ in range(len(V))]
    for v in V:
        for g in S:
            u=red(v+g)
            if u in idx:
                i,j=idx[v],idx[u]
                if i!=j:
                    adj[i].add(j); adj[j].add(i)
    return adj

# (1) girth
def is_backtrack(p):
    return any(invw(p[i+1])==p[i] for i in range(len(p)-1))
nb3=[p for p in itertools.product(S,repeat=3) if red(''.join(p))=='' and not is_backtrack(p)]
nb4=[p for p in itertools.product(S,repeat=4) if red(''.join(p))=='' and not is_backtrack(p)]
assert len(nb3)==0, nb3
assert len(nb4)==0, nb4
C5=['','a','ab','abA','abAB']
for k in range(5):
    assert red(invw(C5[k])+C5[(k+1)%5]) in S
print(f"(1) girth=5 OK (nb3={len(nb3)}, nb4={len(nb4)}, C5 verified)")

# (2) B4 profile
T4=tree_ball(4); V=sorted(T4); A=graph_on(V)
n=len(V); m=sum(map(len,A))//2
assert n==161, n
print(f"(2a) B4: n={n}, internal S-edges={m}")
# C5 inside B4 => chi>=3
assert all(v in T4 for v in C5)
print("(2b) C5 subset B4 => chi(B4)>=3 OK")
# loaded coloring proper + root 0 => chi<=3
d=json.load(open("output/artifacts/B4_coloring.json"))
c=d["coloring"]; assert d["root"]==''
assert c['']==0
idx={v:i for i,v in enumerate(V)}
bad=0
for v in V:
    for g in S:
        u=red(v+g)
        if u in idx and c[v]==c[u]: bad+=1
bad//=2
assert bad==0, bad
print(f"(2c) loaded B4 coloring: root=0, conflicts={bad} => chi(B4)<=3 OK; chi(B4)=3")

# (3) spoiler no-go simulation.
# Finite game model (faithful to fallback success criterion): 4 rounds; each round I names a
# vertex v in B4, II answers a color; I wins iff final partial coloring is improper or root!=0.
# II mirrors fixed global coloring c*. For ANY I-sequence, II survives => no winning T exists.
import random
rng=random.Random(7)
for trial in range(200):
    seq=[rng.choice(V) for _ in range(4)]
    ans={v:c[v] for v in seq}
    for k in range(4):
        for l in range(k+1,4):
            if red(invw(seq[k])+seq[l]) in S:
                assert ans[seq[k]]!=ans[seq[l]], (seq,ans)
    if '' in seq: assert ans['']==0
print("(3) mirror-simulation: 200 random 4-move I-sequences all survived vs c* OK")
# exhaustive: every pair/triple/quadruple consistent — implied by global properness, but
# explicitly re-verify all S-edges bichromatic (done in (2c)) + root. Formal no-go:
print("NO-GO THEOREM: no Player-I table T wins depth-4 rooted game on B4(e) with c0=0,")
print("  witnessed by defeating coloring c* (output/artifacts/B4_coloring.json).")
print("VERIFY_OK")
