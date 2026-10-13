from fractions import Fraction as F
from itertools import permutations, combinations

# Exact rational linear algebra for 3x3 matrices.
def det(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def transpose(M): return [list(r) for r in zip(*M)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def mv(A,v): return [sum(A[i][k]*v[k] for k in range(3)) for i in range(3)]
def inv(M):
    d=det(M); assert d
    C=[[None]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            minor=[[M[r][c] for c in range(3) if c!=j] for r in range(3) if r!=i]
            C[i][j]=((-1)**(i+j))*(minor[0][0]*minor[1][1]-minor[0][1]*minor[1][0])
    return [[C[j][i]/d for j in range(3)] for i in range(3)]
def diag(a,b,c): return [[a,F(0),F(0)],[F(0),b,F(0)],[F(0),F(0),c]]
def cols(*vs): return [[vs[j][i] for j in range(3)] for i in range(3)]
def cross(a,b): return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def peq(v,w): return cross(v,w)==[F(0),F(0),F(0)]
def meq(A,B):
    av=sum(A,[]); bv=sum(B,[])
    for i,b in enumerate(bv):
        if b:
            if not av[i]: return False
            lam=av[i]/b
            return all(av[k]==lam*bv[k] for k in range(9))
    return False

def scalar_matrix(M):
    return all(M[i][j]==0 for i in range(3) for j in range(3) if i!=j) and M[0][0]==M[1][1]==M[2][2]
def mpow(A,n):
    R=[[F(int(i==j)) for j in range(3)] for i in range(3)]
    for _ in range(n): R=mm(R,A)
    return R

# Six line factors from Macinic--Pokora Example 2.8, scaled projectively.
L=[
    [F(0),F(1),F(0)],       # y
    [F(1),F(0),F(1)],       # x+z
    [F(1),F(1),F(-1)],      # x+y-z
    [F(1),F(1),F(1)],       # x+y+z
    [F(1),F(0),F(-1)],      # x-z
    [F(2),F(1),F(0)],       # 2x+y
]

# Symmetric matrices of the six conic factors, with q(x)=x^T Q x.
C=[
 [[F(1),F(1),F(-1,2)],[F(1),F(1),F(0)],[F(-1,2),F(0),F(0)]],
 [[F(1),F(1,2),F(0)],[F(1,2),F(0),F(1)],[F(0),F(1),F(-1)]],
 [[F(1),F(0),F(1,2)],[F(0),F(0),F(1,2)],[F(1,2),F(1,2),F(0)]],
 [[F(1),F(1,2),F(0)],[F(1,2),F(0),F(0)],[F(0),F(0),F(1)]],
 [[F(1),F(1),F(-1,2)],[F(1),F(0),F(1,2)],[F(-1,2),F(1,2),F(0)]],
 [[F(1),F(0),F(1,2)],[F(0),F(-1),F(1)],[F(1,2),F(1),F(0)]],
]
assert [det(Q) for Q in C]==[F(-1,4),F(-3,4),F(-1,4),F(-1,4),F(-3,4),F(-3,4)]

def d3(a,b,c): return det(cols(a,b,c))
def is_frame(idx): return all(d3(L[i],L[j],L[k]) for i,j,k in combinations(idx,3))
frames=[p for p in permutations(range(6),4) if is_frame(p)]
assert len(frames)==72
src=frames[0]

def frame_map(src_idx,tgt_idx):
    ps=[L[i] for i in src_idx]; qs=[L[i] for i in tgt_idx]
    P=cols(*ps[:3]); Q=cols(*qs[:3])
    c=mv(inv(P),ps[3]); d=mv(inv(Q),qs[3])
    assert all(c) and all(d)
    S=diag(d[0]/c[0],d[1]/c[1],d[2]/c[2])
    return mm(mm(Q,S),inv(P))

def line_perm(B):
    out=[]
    for p in L:
        v=mv(B,p)
        matches=[j for j,q in enumerate(L) if peq(v,q)]
        if len(matches)!=1: return None
        out.append(matches[0])
    return tuple(out) if len(set(out))==6 else None

line_stab={}
for tgt in frames:
    B=frame_map(src,tgt)
    p=line_perm(B)
    if p is not None: line_stab[p]=B
assert len(line_stab)==24

# The line skeleton has exactly four triple-concurrency classes (dually, four collinear triples).
T=[]
for tri in combinations(range(6),3):
    if d3(L[tri[0]],L[tri[1]],L[tri[2]])==0: T.append(tri)
assert T==[(0,1,3),(0,2,4),(1,2,5),(3,4,5)]
Tsets=[set(t) for t in T]
def triple_perm(p):
    return tuple(Tsets.index({p[i] for i in tri}) for tri in T)
assert len({triple_perm(p) for p in line_stab})==24

def conic_perm(B):
    out=[]
    Bt=transpose(B)
    for Q in C:
        image=mm(mm(B,Q),Bt) # B=A^{-T}; image under A is B Q B^T
        matches=[j for j,R in enumerate(C) if meq(image,R)]
        if len(matches)!=1: return None
        out.append(matches[0])
    return tuple(out) if len(set(out))==6 else None

arr=[]
for lp,B in line_stab.items():
    cp=conic_perm(B)
    if cp is not None:
        A=transpose(inv(B))
        arr.append((lp,cp,A))
assert len(arr)==6
# Exactly the S4 line-skeleton symmetries fixing the fourth concurrency class survive.
assert {triple_perm(lp) for lp,_,_ in arr}=={
    (0,1,2,3),(1,0,2,3),(0,2,1,3),(2,0,1,3),(1,2,0,3),(2,1,0,3)
}

s=[[F(1),F(1),F(0)],[F(0),F(-1),F(0)],[F(0),F(0),F(-1)]]
t=[[F(1),F(1),F(0)],[F(-1),F(-1),F(1)],[F(-1),F(0),F(0)]]
assert any(meq(A,s) for _,_,A in arr)
assert any(meq(A,t) for _,_,A in arr)
assert scalar_matrix(mpow(s,2))
assert scalar_matrix(mpow(t,3))
assert scalar_matrix(mpow(mm(s,t),2))
assert not meq(mm(s,t),mm(t,s))

# Component orbits under the six stabilizer elements.
def orbits(perms,n):
    unseen=set(range(n)); out=[]
    while unseen:
        a=min(unseen); orb={a}; changed=True
        while changed:
            changed=False
            for p in perms:
                new={p[i] for i in orb}
                if not new<=orb: orb|=new; changed=True
        out.append(tuple(sorted(orb))); unseen-=orb
    return tuple(out)
assert orbits([a[0] for a in arr],6)==((0,1,2),(3,4,5))
assert orbits([a[1] for a in arr],6)==((0,2,3),(1,4,5))


# The two extra lines singled out in Example 2.8 generate complete symmetry orbits.
def pnorm(v):
    for a in v:
        if a:
            return tuple(x/a for x in v)
    raise AssertionError('zero vector')
def dual_from_A(A): return transpose(inv(A))
def line_orbit(v): return {pnorm(mv(dual_from_A(A),v)) for _,_,A in arr}
free_orbit=line_orbit([F(0),F(0),F(1)])
pog_orbit=line_orbit([F(1),F(2),F(4)])
assert free_orbit=={(F(0),F(0),F(1)),(F(1),F(0),F(0)),(F(1),F(1),F(0))}
assert pog_orbit=={
    (F(1),F(-1),F(-4)),
    (F(1),F(1,3),F(-1,6)),
    (F(1),F(1,5),F(-2,5)),
    (F(1),F(2),F(4)),
    (F(1),F(2,3),F(1,6)),
    (F(1),F(4,5),F(2,5)),
}

print('VERIFY_OK')
print('line_stabilizer_order=24')
print('arrangement_stabilizer_order=6')
print('group=S3')
print('line_orbits=(L1,L2,L3);(L4,L5,L6)')
print('conic_orbits=(C1,C3,C4);(C2,C5,C6)')
print('free_addition_orbit_size=3')
print('pog_addition_orbit_size=6')
