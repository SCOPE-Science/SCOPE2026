from fractions import Fraction
from itertools import combinations, product
from math import comb


def rref_nullspace(rows, ncols):
    A=[[Fraction(x) for x in row] for row in rows]
    m=len(A); piv=[]; r=0
    for c in range(ncols):
        p=next((i for i in range(r,m) if A[i][c]), None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        q=A[r][c]
        A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[A[i][j]-q*A[r][j] for j in range(ncols)]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(ncols) if c not in piv]
    basis=[]
    for f in free:
        v=[Fraction(0) for _ in range(ncols)]; v[f]=1
        for i,c in enumerate(piv): v[c]=-A[i][f]
        basis.append(v)
    return basis

def lin_nonzero_on_basis(coeff,basis):
    return any(sum(Fraction(coeff[j])*v[j] for j in range(len(coeff))) != 0 for v in basis)

def exact_zero_feasible(verts,Z):
    rows=[[1,*verts[i]] for i in Z]
    basis=rref_nullspace(rows,4)
    if not basis: return False
    # time coefficients all nonzero
    for j in range(4):
        e=[0]*4; e[j]=1
        if not lin_nonzero_on_basis(e,basis): return False
    # all outside evaluations nonzero can be simultaneously arranged over Q
    for i,v in enumerate(verts):
        if i not in Z and not lin_nonzero_on_basis([1,*v],basis): return False
    return True

def hd(a,b): return sum(x!=y for x,y in zip(a,b))

cube=list(product([1,-1], repeat=3))
feasible=[]
for mask in range(1<<8):
    Z={i for i in range(8) if mask>>i & 1}
    if exact_zero_feasible(cube,Z): feasible.append(Z)
counts={z:sum(len(Z)==z for Z in feasible) for z in range(9)}
assert counts=={0:1,1:8,2:12,3:8,4:0,5:0,6:0,7:0,8:0}, counts
for Z in feasible:
    if len(Z)==2:
        i,j=sorted(Z); assert hd(cube[i],cube[j])==2
    if len(Z)==3:
        pts=[cube[i] for i in Z]
        assert all(hd(a,b)==2 for a,b in combinations(pts,2))

# Plane case: every nonempty Fourier support T subset F_2^2 is compatible
H4=[]
pts2=list(product([0,1], repeat=2))
for x in pts2:
    H4.append([1 if (x[0]*y[0]+x[1]*y[1])%2==0 else -1 for y in pts2])
plane_counts={j:0 for j in range(1,5)}
for mask in range(1,1<<4):
    T=[i for i in range(4) if mask>>i & 1]
    # variables are Fourier values on T. Need each chosen value and each inverse coefficient nonzero.
    basis=[]
    for idx in T:
        v=[Fraction(0)]*len(T); v[T.index(idx)]=1; basis.append(v)
    # chosen values are coordinate functionals, obviously nonzero
    ok=True
    for xrow in range(4):
        coeff=[H4[xrow][idx] for idx in T]
        if not lin_nonzero_on_basis(coeff,basis): ok=False
    assert ok
    plane_counts[len(T)]+=1
assert plane_counts=={1:4,2:6,3:4,4:1}, plane_counts

# Affine-span orbit counts for 4-subsets in F_2^d.
def gf2_rank(vecs,d):
    rows=[sum((v[i]&1)<<i for i in range(d)) for v in vecs]
    rank=0
    for b in range(d-1,-1,-1):
        p=next((i for i in range(rank,len(rows)) if (rows[i]>>b)&1),None)
        if p is None: continue
        rows[rank],rows[p]=rows[p],rows[rank]
        for i in range(len(rows)):
            if i!=rank and ((rows[i]>>b)&1): rows[i]^=rows[rank]
        rank+=1
    return rank
for d,expected in [(3,(14,56)),(4,(140,1680))]:
    pts=list(range(1<<d)); c2=c3=0
    for S in combinations(pts,4):
        x0=S[0]
        vecs=[]
        for x in S[1:]:
            z=x^x0
            vecs.append([(z>>i)&1 for i in range(d)])
        r=gf2_rank(vecs,d)
        assert r in (2,3)
        if r==2: c2+=1
        else: c3+=1
    assert (c2,c3)==expected,(d,c2,c3)

# Global spectrum predicted by the two local orbit types.
for d in range(3,11):
    plane={j*(1<<(d-2)) for j in (1,2,3,4)}
    simplex={j*(1<<(d-3)) for j in (5,6,7,8)}
    glob=sorted(plane|simplex)
    target=sorted({m*(1<<(d-3)) for m in (2,4,5,6,7,8)})
    assert glob==target

print('CUBE_ZERO_COUNTS', counts)
print('PLANE_SUPPORT_COUNTS', plane_counts)
print('AFFINE_ORBIT_COUNTS d=3 plane=14 simplex=56; d=4 plane=140 simplex=1680')
print('GLOBAL_MULTIPLIERS', [2,4,5,6,7,8])
print('VERIFY_OK')
