"""Exact, dependency-free checks of the binary additive-colouring cycle polynomial."""
from collections import defaultdict
from itertools import product

STATES=list(product((0,1),repeat=3))
INDEX={s:i for i,s in enumerate(STATES)}
EDGES={i:[] for i in range(8)}
for i,(a,b,c) in enumerate(STATES):
    for d in (0,1):
        if a+c!=b+d:
            EDGES[i].append((INDEX[(b,c,d)],d))

# A cycle is uniquely encoded by the rotation whose initial state has minimum index.
CYCLES=set()
for root in range(8):
    def dfs(v,path,wt):
        for w,bit in EDGES[v]:
            if w==root:
                if len(path)>=2:
                    CYCLES.add((tuple(path),wt+bit))
            elif w>root and w not in path:
                dfs(w,path+[w],wt+bit)
    dfs(root,[root],0)
assert sorted((len(c),w) for c,w in CYCLES)==[(2,1),(4,1),(4,3)], CYCLES

# Independent exact determinant via disjoint directed cycles: every subset of
# vertex-disjoint cycles contributes (-1)^number_of_cycles * t^length z^weight.
det=defaultdict(int);det[(0,0)]=1
cs=list(CYCLES)
for mask in range(1,1<<len(cs)):
    chosen=[cs[i] for i in range(len(cs)) if (mask>>i)&1]
    used=[v for cyc,w in chosen for v in cyc]
    if len(used)==len(set(used)):
        det[(sum(map(lambda q:len(q[0]),chosen)),sum(w for cyc,w in chosen))]+=(-1)**len(chosen)
det={k:v for k,v in det.items() if v}
assert det=={(0,0):1,(2,1):-1,(4,1):-1,(4,3):-1,(8,4):1},det

# Transfer trace: enumerates complete closed state walks, with weight based
# on the newly inserted bit at each transition.
def trace(n):
    out=defaultdict(int)
    for start in range(8):
        active={(start,0):1}
        for _ in range(n):
            nxt=defaultdict(int)
            for (v,k),count in active.items():
                for w,b in EDGES[v]:
                    nxt[(w,k+b)]+=count
            active=nxt
        for (v,k),count in active.items():
            if v==start:
                out[k]+=count
    return {k:v for k,v in out.items() if v}

# Independently enumerate all bit words and check every local inequality.
assignments=0
for n in range(3,17):
    brute=defaultdict(int)
    for b in product((0,1),repeat=n):
        assignments+=1
        if all(b[(i-1)%n]+b[(i+1)%n]!=b[i]+b[(i+2)%n] for i in range(n)):
            brute[sum(b)]+=1
    brute={k:v for k,v in brute.items() if v}
    assert brute==trace(n),(n,brute,trace(n))

# Newton identities/trace recurrence from determinant: for n>8,
# T_n=z T_{n-2}+(z+z^3)T_{n-4}-z^4 T_{n-8}.
T={n:trace(n) for n in range(1,9)}
assert T[1]=={} and T[2]=={1:2} and T[3]=={}
for n in range(9,85):
    pred=defaultdict(int)
    for shift,past,sgn in [(1,T[n-2],1),(1,T[n-4],1),(3,T[n-4],1),(4,T[n-8],-1)]:
        for k,c in past.items():
            pred[k+shift]+=sgn*c
    T[n]={k:v for k,v in pred.items() if v}
for n in range(9,37):
    assert T[n]==trace(n),(n,T[n],trace(n))
for n in range(3,85):
    poly=T[n]
    if n%2:
        assert not poly,(n,poly)
    else:
        assert poly and min(poly)==(n+3)//4 and max(poly)==n-(n+3)//4,(n,poly)
        assert poly[min(poly)] == (4 if n%4==0 else n),(n,poly)
        assert all(poly[k]==poly[n-k] for k in poly)
print('VERIFY_OK determinant_cycles=3 independent_assignments=%s n=3..16 transfer_n=1..36 recurrence_n=9..84 extremes_even_n=4..84'%assignments)
