#!/usr/bin/env python3
"""Finite exact checks for the pentagonal real moment-angle surface."""
from itertools import combinations, product
from collections import Counter

N=5

def comps(W):
    W=set(W); unseen=set(W); out=[]
    while unseen:
        seed=min(unseen); stack=[seed]; seen={seed}; unseen.remove(seed)
        while stack:
            x=stack.pop()
            for y in ((x+1)%N,(x-1)%N):
                if y in unseen:
                    unseen.remove(y); seen.add(y); stack.append(y)
        out.append(frozenset(seen))
    return sorted(out,key=lambda c:min(c))

supports=[frozenset(W) for j in range(N+1) for W in combinations(range(N),j) if len(comps(W))==2]
supports.sort(key=lambda w:(len(w),sorted(w)))
assert len(supports)==10 and Counter(map(len,supports))=={2:5,3:5}
idx={W:i for i,W in enumerate(supports)}

def compose(p,q):return tuple(p[q[i]] for i in range(N))
def power(p,k):
    t=tuple(range(N))
    for _ in range(k):t=compose(p,t)
    return t
r=tuple((i+1)%N for i in range(N));s=tuple((-i)%N for i in range(N));ident=tuple(range(N))
assert power(r,5)==ident and power(s,2)==ident and compose(compose(s,r),s)==power(r,4)

def action(p):
    a=[None]*10
    for i,W in enumerate(supports):
        target=frozenset(p[x] for x in W)
        src0=comps(W)[0]
        image=frozenset(p[x] for x in src0)
        sign=1 if image==comps(target)[0] else -1
        a[i]=(idx[target],sign)
    return a

def signed_comp(A,B):return [(A[j][0],u*A[j][1]) for j,u in B]
R=action(r); S=action(s); I=[(i,1) for i in range(10)]
def spower(A,k):
    t=I
    for _ in range(k):t=signed_comp(A,t)
    return t
assert spower(R,5)==I and spower(S,2)==I and signed_comp(signed_comp(S,R),S)==spower(R,4)

# Permutation basis for induced summands: each orbit has one stabilizer point.
for j in (2,3):
    orbit=[W for W in supports if len(W)==j]
    fixed=[W for W in orbit if frozenset(s[x] for x in W)==W]
    assert len(fixed)==1
    i=idx[fixed[0]]; sg=S[i][1]
    assert sg==(-1 if j==2 else 1),(j,sg)

traces=[]
for k in range(5):
    for refl in (False,True):
        p=compose(power(r,k),s) if refl else power(r,k)
        A=action(p)
        tr=sum(sign for i,(j,sign) in enumerate(A) if i==j)
        traces.append(tr)
assert traces[0]==10 and all(t==0 for t in traces[1:]),traces

def modrank(A,p=2):
    rows=[x[:] for x in A];m=len(rows);n=len(rows[0]) if m else 0;k=0
    for col in range(n):
        pivot=next((i for i in range(k,m) if rows[i][col]%p),None)
        if pivot is None:continue
        rows[k],rows[pivot]=rows[pivot],rows[k]
        d=pow(rows[k][col]%p,-1,p)
        rows[k]=[(v*d)%p for v in rows[k]]
        for i in range(k+1,m):
            t=rows[i][col]%p
            if t: rows[i]=[(a-t*b)%p for a,b in zip(rows[i],rows[k])]
        k+=1
        if k==m:break
    return k

def minus_id(A):
    mat=[[0]*len(A) for _ in A]
    for i,(j,t) in enumerate(A):mat[j][i]+=t;mat[i][i]-=1
    return mat
assert modrank(minus_id(S),2)==4
assert modrank(minus_id(S),101)==5

# Free axes of a cube must form a face in the pentagonal simplicial complex.
faces=[frozenset()]+[frozenset([i]) for i in range(N)]+[frozenset([i,(i+1)%N]) for i in range(N)]
faces.sort(key=lambda f:(len(f),tuple(sorted(f))))

def cells(d):
    return [(tuple(sorted(F)),tuple(signs)) for F in faces if len(F)==d for signs in product((-1,1),repeat=N-d)]
C=[cells(d) for d in range(3)]
assert [len(x) for x in C]==[32,80,40]

def boundary(d):
    cols=C[d]; rowidx={c:i for i,c in enumerate(C[d-1])}
    matrix=[[0]*len(cols) for _ in C[d-1]]
    for col,(free,signs) in enumerate(cols):
        for axis_order,x in enumerate(free):
            target=tuple(y for y in free if y!=x)
            other=[y for y in range(N) if y not in free]
            for endpoint in (-1,1):
                vals={a:t for a,t in zip(other,signs)};vals[x]=endpoint
                tgt=(target,tuple(vals[y] for y in range(N) if y not in target))
                row=rowidx[tgt]
                matrix[row][col]+=(-1 if endpoint==-1 else 1)*(-1 if axis_order%2 else 1)
    return matrix
B1=boundary(1);B2=boundary(2)
for j in range(32):
    for k in range(40):
        assert sum(B1[j][h]*B2[h][k] for h in range(80))==0
r1=modrank(B1,101);r2=modrank(B2,101)
assert (r1,r2)==(31,39),(r1,r2)
assert (80-r1-r2,40-r2)==(10,1)
print('disconnected supports: 5 pairs + 5 triples')
print('stabilizer signs: pairs -1; triples +1')
print('D5 relations: verified; H1 trace: regular rational character')
print('reflection mod2 rank on actual homology lattice: 4; integral regular lattice: 5')
print('cubical C0,C1,C2 = 32,80,40; boundary ranks mod101 =',r1,r2)
print('Betti b1,b2 =',80-r1-r2,40-r2)
print('VERIFY_OK')
