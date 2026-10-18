#!/usr/bin/env python3
"""Exact finite simplicial and integral Morse-chain certificate for a triangle-free two-matching complex."""
import itertools
import hashlib
from collections import Counter,defaultdict,deque
from functools import lru_cache
from math import factorial

N=7
EDGES=list(itertools.combinations(range(N),2))
NE=len(EDGES)


def enumerate_faces():
    result=set()
    def rec(i,dg,nb,s):
        if i==NE:
            if s: result.add(s)
            return
        rec(i+1,dg,nb,s)
        a,b=EDGES[i]
        if dg[a]<2 and dg[b]<2 and not (nb[a]&nb[b]):
            dg[a]+=1;dg[b]+=1;nb[a]|=1<<b;nb[b]|=1<<a
            rec(i+1,dg,nb,s|(1<<i))
            dg[a]-=1;dg[b]-=1;nb[a]^=1<<b;nb[b]^=1<<a
    rec(0,[0]*N,[0]*N,0)
    return result

F=enumerate_faces()
assert len(F)==14430
fv=Counter(s.bit_count()-1 for s in F)
assert [fv[i] for i in range(7)]==[21,210,1155,3570,5607,3507,360]
# All minimal missing faces have three vertices: 140 three-edge stars and 35 cycles.
forbidden_star=0
forbidden_triangle=0
for triple in itertools.combinations(range(NE),3):
    s=sum(1<<j for j in triple)
    if s in F:continue
    deg=Counter(v for j in triple for v in EDGES[j])
    if max(deg.values())==3:forbidden_star+=1
    elif sorted(deg.values())==[2,2,2]:forbidden_triangle+=1
    else:raise AssertionError(('unexpected forbidden triple',triple,deg))
assert (forbidden_star,forbidden_triangle)==(140,35)

for s in F:
    for j in range(NE):
        if (s>>j)&1 and s^(1<<j):assert (s^(1<<j)) in F

# The greedy lexicographic elementary toggle matching is built on all *nonempty* faces.
U=set(F)
P=[]
for bit in range(NE):
    z=1<<bit
    for s in sorted(U):
        if not (s&z) and (s|z) in U:
            U.remove(s);U.remove(s|z);P.append((s,s|z))
assert len(P)==7018 and len(U)==394
assert Counter(s.bit_count()-1 for s in U)=={0:1,4:124,5:269}
UP=dict(P)
DOWN={b:a for a,b in P}
assert len(UP)==len(DOWN)==len(P)

# Full Hasse-diagram orientation: matched cover points upward, every other cover downward.
faces_sorted=sorted(F)
index={s:i for i,s in enumerate(faces_sorted)}
adj=[[] for _ in faces_sorted]
indeg=[0]*len(F)
cover_count=0
for top in faces_sorted:
    for j in range(NE):
        if (top>>j)&1:
            bot=top^(1<<j)
            if bot==0: continue
            cover_count+=1
            if UP.get(bot)==top:src,dst=index[bot],index[top]
            else:src,dst=index[top],index[bot]
            adj[src].append(dst);indeg[dst]+=1
q=deque(i for i in range(len(F)) if indeg[i]==0)
visited=0
while q:
    v=q.popleft();visited+=1
    for j in adj[v]:
        indeg[j]-=1
        if indeg[j]==0:q.append(j)
assert visited==len(F),'Gradient Hasse graph is cyclic'

def face_sign(top,lower):
    missing=top^lower
    assert missing.bit_count()==1
    return -1 if (top&(missing-1)).bit_count()%2 else 1

# Algebraic elementary cancellations induce the following normal form over integers.
@lru_cache(None)
def normalize(s):
    if s in U:return {s:1}
    if s in DOWN:return {}
    top=UP[s]
    out=defaultdict(int)
    for i in range(NE):
        if (top>>i)&1:
            lower=top^(1<<i)
            if lower==s:continue
            c=-face_sign(top,s)*face_sign(top,lower)
            for crit,a in normalize(lower).items():out[crit]+=c*a
    return {j:a for j,a in out.items() if a}

critical_4=sorted(s for s in U if s.bit_count()==5)
critical_5=sorted(s for s in U if s.bit_count()==6)
row_index={s:i for i,s in enumerate(critical_4)}
B=[[0]*len(critical_5) for _ in critical_4]
for j,top in enumerate(critical_5):
    val=defaultdict(int)
    for i in range(NE):
        if (top>>i)&1:
            lower=top^(1<<i)
            for t,a in normalize(lower).items():val[t]+=face_sign(top,lower)*a
    for t,a in val.items():B[row_index[t]][j]=a
nnz=sum(z!=0 for row in B for z in row)
assert nnz==3171 and max(abs(z) for row in B for z in row)==3
original_matrix_hash=hashlib.sha256('\n'.join(','.join(map(str,row)) for row in B).encode()).hexdigest()

# Unimodular row/column pivots prove all 123 nonzero integral Smith factors are units.
R=len(B);C=len(B[0]);rank=0
for i in range(R):
    pivot=next(((j,k) for j in range(i,R) for k in range(i,C) if abs(B[j][k])==1),None)
    if pivot is None:break
    j,k=pivot
    B[i],B[j]=B[j],B[i]
    for row in B:row[i],row[k]=row[k],row[i]
    p=B[i][i]
    for j in range(i+1,R):
        c=B[j][i]*p
        if c:
            for k in range(i,C):B[j][k]-=c*B[i][k]
    rank+=1
assert rank==123 and all(all(x==0 for x in row) for row in B[rank:])

# Independently compute the mod-two boundary ranks of the original simplicial chains.
fs_by_size={k:sorted(s for s in F if s.bit_count()==k) for k in range(1,8)}
def rank_F2(vectors):
    basis={}
    for x in vectors:
        while x:
            i=x.bit_length()-1
            if i in basis:x^=basis[i]
            else:
                basis[i]=x
                break
    return len(basis)
boundary_ranks={}
for k in range(2,8):
    rid={s:i for i,s in enumerate(fs_by_size[k-1])}
    cols=[]
    for s in fs_by_size[k]:
        c=0
        for j in range(NE):
            if (s>>j)&1:c^=1<<rid[s^(1<<j)]
        cols.append(c)
    boundary_ranks[k-1]=rank_F2(cols)
assert [boundary_ranks[i] for i in range(1,7)]==[20,190,965,2605,3001,360]

@lru_cache(None)
def partitions(n,ub=None):
    if n==0:return ((),)
    if ub is None:ub=n
    return tuple((k,)+p for k in range(min(n,ub),0,-1) for p in partitions(n-k,k))

def cells(lam):return {(i,j) for i,a in enumerate(lam) for j in range(a)}
@lru_cache(None)
def specht(lam,mu):
    if not mu:return int(not lam)
    r=mu[0];res=0
    for nu in partitions(sum(lam)-r):
        if len(nu)>len(lam) or any(nu[i]>lam[i] for i in range(len(nu))):continue
        skew=cells(lam)-cells(nu)
        if len(skew)!=r:continue
        seen={next(iter(skew))};q=list(seen)
        while q:
            a,b=q.pop()
            for v in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)):
                if v in skew and v not in seen:seen.add(v);q.append(v)
        if len(seen)!=r:continue
        if any((i,j+1) in skew and (i+1,j) in skew and (i+1,j+1) in skew for i,j in skew):continue
        res+=(-1)**(len({i for i,j in skew})-1)*specht(nu,mu[1:])
    return res

def z(mu):
    c=Counter(mu)
    v=1
    for i,k in c.items():v*=i**k*factorial(k)
    return v

classes=partitions(N)
assert len(classes)==15
# Full irreducible character matrix orthogonality check.
for a in classes:
    for b in classes:
        v=sum(specht(a,mu)*specht(b,mu)*factorial(N)//z(mu) for mu in classes)
        assert v==factorial(N)*int(a==b)

idx_e={x:i for i,x in enumerate(EDGES)}
def permutation(mu):
    perm=list(range(N));i=0
    for k in mu:
        for j in range(k):perm[i+j]=i+(j+1)%k
        i+=k
    return perm

def signed_fixed_trace(p):
    em=[idx_e[tuple(sorted((p[a],p[b])))] for a,b in EDGES]
    trace=0
    for s in F:
        target=0;image_indices=[]
        for i in range(NE):
            if (s>>i)&1:
                j=em[i];target|=1<<j;image_indices.append(j)
        if target!=s:continue
        inv=sum(image_indices[i]>image_indices[j] for i in range(len(image_indices)) for j in range(i+1,len(image_indices)))
        # reduced alternating chain trace: -1 from the empty face's contribution
        trace+=(-1)**(s.bit_count()-1+inv)
    return trace-1

L={mu:signed_fixed_trace(permutation(mu)) for mu in classes}
assert L[(1,)*7]==-145
expected={(7,):2,(6,1):1,(5,2):0,(5,1,1):0,(4,3):1,(4,2,1):1,(4,1,1,1):1,(3,3,1):-1,(3,2,2):-1,(3,2,1,1):1,(3,1,1,1,1):-1,(2,2,2,1):7,(2,2,1,1,1):11,(2,1,1,1,1,1):-5,(1,1,1,1,1,1,1):-145}
assert L==expected

def multiplicities(sign_4):
    # L(σ)=χ_H4(σ)-χ_H5(σ)
    character={mu:(1 if sign_4=='trivial' else (-1)**(N-len(mu)))-L[mu] for mu in classes}
    ret={}
    for lam in classes:
        a=sum(character[mu]*specht(lam,mu)*factorial(N)//z(mu) for mu in classes)
        assert a%factorial(N)==0
        ret[lam]=a//factorial(N)
    return ret
trivial=multiplicities('trivial')
sign=multiplicities('sign')
assert sign[(7,)]==-1 # impossible negative multiplicity excludes sign action on H4.
nonzero={k:v for k,v in trivial.items() if v}
assert nonzero=={(5,1,1):1,(4,2,1):1,(4,1,1,1):2,(3,3,1):1,(3,2,1,1):1}
assert sum(specht(k,(1,)*N)*v for k,v in nonzero.items())==146
print('PASS: 21 edges; 175 forbidden triples (140 stars plus 35 triangles); 14430 simplices; f=', [fv[i] for i in range(7)])
print('PASS: 7018 matched pairs; 1 critical vertex, 124 critical dimension-4 cells, 269 critical dimension-5 cells')
print('PASS: full Hasse acyclicity:',visited,'vertices,',cover_count,'cover relations')
print('PASS: signed Morse boundary:',R,'x',C,'nonzero=',nnz,'sha256=',original_matrix_hash)
print('PASS: 123 unimodular pivots, remaining zero row; integer homology H4=Z, H5=Z^146')
print('PASS: original mod-2 boundary ranks:',[boundary_ranks[i] for i in range(1,7)])
print('PASS: all 15 S7 Lefschetz classes; 15x15 Specht orthogonality')
print('PASS: H4 trivial; H5 Specht decomposition:',sorted(nonzero.items(),reverse=True))
