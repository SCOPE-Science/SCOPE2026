"""Replay: triple-C5 wedge G0 in T0 has reg(S/I)=4, im=3. Exact QQ + exhaustive im."""
from fractions import Fraction
import itertools

# G0: three C5 lobes sharing vertex 0
edges=[(0,1),(1,2),(2,3),(3,4),(4,0),(0,5),(5,6),(6,7),(7,8),(8,0),(0,9),(9,10),(10,11),(11,12),(12,0)]
n=13
adj=[0]*n
for u,v in edges:
    adj[u]|=(1<<v); adj[v]|=(1<<u)

# scope
V=(1<<n)-1
E=[(i,j) for i in range(n) for j in range(i+1,n) if (adj[i]>>j)&1]
seen={0}; st=[0]
while st:
    x=st.pop()
    for y in range(n):
        if (adj[x]>>y)&1 and y not in seen: seen.add(y); st.append(y)
cyc=len(E)-n+1
print(f'G0: n={n} m={len(E)} connected={len(seen)==n} cyc={cyc} T0={len(seen)==n and cyc==3}')

# im: exhaustive over edge subsets
def is_ind(S):
    vs=set()
    for e in S:
        if e[0] in vs or e[1] in vs: return False
        vs.add(e[0]); vs.add(e[1])
    for a in range(len(S)):
        for b in range(a+1,len(S)):
            for x in S[a]:
                for y in S[b]:
                    if (adj[x]>>y)&1: return False
    return True
best=0; ex=None; n4=0
for r in range(len(E)+1):
    for S in itertools.combinations(E,r):
        if r==4: n4+=1
        if is_ind(S) and r>best: best=r; ex=S
print(f'im={best} e.g.{ex}  (#4-sets checked={n4}, none induced)')
# confirm no induced 4-set
bad=[S for S in itertools.combinations(E,4) if is_ind(S)]
print(f'induced 4-sets: {len(bad)}')

# Hochster full-set homology over QQ (Fraction)
def faces(W):
    L=[v for v in range(n) if (W>>v)&1]
    F={0:[()]}
    for k in range(1,len(L)+1):
        fk=[tuple(sorted(c)) for c in itertools.combinations(sorted(L),k)
            if all(not ((adj[a]>>b)&1) for a in c for b in c if b!=a)]
        if fk: F[k]=fk
    return F
def rankQ(M):
    if not M or not M[0]: return 0
    M=[[Fraction(x) for x in row] for row in M]
    R,C=len(M),len(M[0]); rk=0
    for j in range(C):
        p=None
        for i in range(rk,R):
            if M[i][j]!=0: p=i;break
        if p is None: continue
        M[rk],M[p]=M[p],M[rk]
        iv=M[rk][j]; M[rk]=[x/iv for x in M[rk]]
        for i in range(R):
            if i!=rk and M[i][j]!=0:
                f=M[i][j]; M[i]=[a-f*b for a,b in zip(M[i],M[rk])]
        rk+=1
    return rk
F=faces(V)
ranks={}
for j in range(1,max(F)+1):
    Fk=F.get(j,[]); Fm=F.get(j-1,[])
    if j==1: ranks[1]=1 if Fk else 0; continue
    if not Fk or not Fm: ranks[j]=0; continue
    idx={f:i for i,f in enumerate(Fm)}
    M=[[0]*len(Fk) for _ in range(len(Fm))]
    for jj,f in enumerate(Fk):
        for t in range(len(f)):
            g=f[:t]+f[t+1:]; i=idx.get(g)
            if i is not None: M[i][jj]=1 if t%2==0 else -1
    ranks[j]=rankQ(M)
dims={}
for k in range(1,max(F)+1):
    Fk=F.get(k,[])
    if not Fk: continue
    h=len(Fk)-ranks.get(k,0)-ranks.get(k+1,0)
    if h>0: dims[k-1]=h
print(f'face sizes={ {k:len(v) for k,v in F.items()} }')
print(f'boundary ranks={ranks}')
print(f'Htilde(full set)={dims} -> beta_{{9,13}}>=1 -> reg(S/I)>=4')

# deletion upper bound (exact theorem, min over choice vertices)
from functools import lru_cache
memo={}
def R(V):
    if V==0: return 0
    if V in memo: return memo[V]
    if not any((V>>v)&1 and (adj[v]&V) for v in range(n)): memo[V]=0; return 0
    best=10**9; bv=-1
    for v in range(n):
        if (V>>v)&1:
            val=max(R(V^(1<<v)), R(V&~((1<<v)|(adj[v]&V)))+1)
            if val<best: best=val; bv=v
    memo[V]=best; return best
print(f'deletion-exact reg={R(V)} (states={len(memo)})')
print('CONCLUSION: G0 in T0, reg=4, im=3, gap=1 -> T0 equality FALSE')
