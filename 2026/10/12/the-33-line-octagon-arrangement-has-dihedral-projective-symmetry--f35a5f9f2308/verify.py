from fractions import Fraction as F
from itertools import combinations, permutations
from collections import Counter

# Q(sqrt(2)) as pairs a+b*r.
def q(a=0,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def inv(x):
    d=x[0]*x[0]-2*x[1]*x[1]
    assert d != 0
    return (x[0]/d,-x[1]/d)
def div(x,y): return mul(x,inv(y))
def zero(x): return x==(F(0),F(0))
def eq(x,y): return x==y
ONE=q(1); ZERO=q(0); R=q(0,1)

def cross(a,b):
    return (sub(mul(a[1],b[2]),mul(a[2],b[1])),
            sub(mul(a[2],b[0]),mul(a[0],b[2])),
            sub(mul(a[0],b[1]),mul(a[1],b[0])))
def dot(a,b):
    s=ZERO
    for x,y in zip(a,b): s=add(s,mul(x,y))
    return s

def canon(v):
    for x in v:
        if not zero(x):
            return tuple(div(y,x) for y in v)
    raise ValueError('zero projective vector')

def qp(a,b=0): return q(a,b)
# The 33 line normals from Pokora--Roulleau, with r^2=2.
L=[
(qp(1),qp(1,-1),qp(-1)),
(qp(1),qp(1,1),qp(-3,-2)),
(qp(1),qp(1),qp(0)),
(qp(1),qp(-1,-1),qp(0)),
(qp(1),qp(1,-1),qp(0)),
(qp(1),qp(-1,1),qp(1,1)),
(qp(0),qp(1),qp(0)),
(qp(1),qp(1,-1),qp(-1,-1)),
(qp(1),qp(-1,1),qp(-1,1)),
(qp(1),qp(1,1),qp(-1)),
(qp(1),qp(1,1),qp(1)),
(qp(1),qp(1,1),qp(-1,-1)),
(qp(1),qp(-1,1),qp(-1)),
(qp(1),qp(-1,-1),qp(-1,-1)),
(qp(1),qp(1,1),qp(3,2)),
(qp(1),qp(-1,1),qp(-1,-1)),
(qp(1),qp(-1,-1),qp(-3,-2)),
(qp(1),qp(-1,-1),qp(1)),
(qp(1),qp(1,-1),qp(-1,1)),
(qp(1),qp(-1,-1),qp(1,1)),
(qp(1),qp(-1,1),qp(1)),
(qp(1),qp(1,-1),qp(1)),
(qp(1),qp(0),qp(0)),
(qp(1),qp(1,1),qp(1,1)),
(qp(1),qp(-1,1),qp(0)),
(qp(1),qp(1,1),qp(0)),
(qp(1),qp(1,-1),qp(1,-1)),
(qp(1),qp(-1,-1),qp(-1)),
(qp(1),qp(-1),qp(0)),
(qp(1),qp(-1,1),qp(1,-1)),
(qp(0),qp(0),qp(1)),
(qp(1),qp(1,-1),qp(1,1)),
(qp(1),qp(-1,-1),qp(3,2)),
]
Lset={canon(x) for x in L}
assert len(Lset)==33

# Intersection multiplicities.
P={canon(cross(L[i],L[j])) for i,j in combinations(range(33),2)}
inc={p:tuple(i for i,l in enumerate(L) if zero(dot(l,p))) for p in P}
counts=Counter(len(v) for v in inc.values())
assert counts==Counter({2:108,3:40,5:16,8:5}), counts
P8={p for p,v in inc.items() if len(v)==8}
expected8={
 canon((qp(1),qp(1,1),qp(0))),
 canon((qp(1),qp(1,-1),qp(0))),
 canon((qp(1),qp(-1,1),qp(0))),
 canon((qp(1),qp(-1,-1),qp(0))),
 canon((qp(0),qp(0),qp(1))),
}
assert P8==expected8

# Gaussian nullspace for a 3x4 matrix over Q(sqrt2).
def nullvec(M):
    A=[row[:] for row in M]
    piv=[]; row=0
    for col in range(4):
        pr=next((k for k in range(row,3) if not zero(A[k][col])),None)
        if pr is None: continue
        A[row],A[pr]=A[pr],A[row]
        z=inv(A[row][col]); A[row]=[mul(z,x) for x in A[row]]
        for k in range(3):
            if k!=row and not zero(A[k][col]):
                f=A[k][col]; A[k]=[sub(A[k][j],mul(f,A[row][j])) for j in range(4)]
        piv.append(col); row+=1
        if row==3: break
    free=[c for c in range(4) if c not in piv]
    assert len(free)==1
    f=free[0]; v=[ZERO]*4; v[f]=ONE
    for rr in range(len(piv)-1,-1,-1):
        c=piv[rr]
        s=ZERO
        for j in free: s=add(s,mul(A[rr][j],v[j]))
        v[c]=neg(s)
    return v

sl=[qp(1,1),qp(1,-1),qp(-1,1),qp(-1,-1)]
def mobius(A,t):
    a,b,c,d=A
    return div(add(c,mul(d,t)),add(a,mul(b,t)))

Astab=[]
for perm in permutations(sl):
    M=[]
    for t,u in zip(sl[:3],perm[:3]):
        # -u*a -u*t*b + c + t*d = 0
        M.append([neg(u),neg(mul(u,t)),ONE,t])
    v=nullvec(M)
    if mobius(v,sl[3])==perm[3]:
        cv=canon(v)
        if cv not in Astab: Astab.append(cv)
assert len(Astab)==8

# 2x2 inverse transpose and action on line normals.
def det2(A):
    a,b,c,d=A
    return sub(mul(a,d),mul(b,c))
def invT2(A):
    a,b,c,d=A; D=det2(A)
    # (A^{-1})^T = 1/D [[d,-c],[-b,a]]
    return (div(d,D),div(neg(c),D),div(neg(b),D),div(a,D))
def act_line(A,k,l):
    u,v,w=l
    p,qv,rv,s=invT2(A)
    return canon((add(mul(p,u),mul(qv,v)), add(mul(rv,u),mul(s,v)), div(w,k)))

# For each possible action on the four points at infinity, l1 forces finitely many k.
aut=[]
for A in Astab:
    u,v,w=L[0]
    p,qv,rv,s=invT2(A)
    U=add(mul(p,u),mul(qv,v)); V=add(mul(rv,u),mul(s,v))
    cand=[]
    for T in L:
        a,b,c=T
        if zero(sub(mul(U,b),mul(V,a))) and not zero(c):
            scale=div(a,U) if not zero(U) else div(b,V)
            k=div(mul(scale,w),c)
            if not zero(k) and k not in cand: cand.append(k)
    good=[]
    for k in cand:
        if all(act_line(A,k,l) in Lset for l in L): good.append(k)
    assert len(good)==2
    for k in good: aut.append((A,k))
assert len(aut)==16

# Projective 3x3 matrix arithmetic for group structure.
def mat(A,k):
    a,b,c,d=A
    return [[a,b,ZERO],[c,d,ZERO],[ZERO,ZERO,k]]
def mm(X,Y):
    return [[sumq(mul(X[i][k],Y[k][j]) for k in range(3)) for j in range(3)] for i in range(3)]
def sumq(it):
    s=ZERO
    for x in it: s=add(s,x)
    return s
def meqproj(X,Y):
    lam=None
    for i in range(3):
      for j in range(3):
        if not zero(Y[i][j]): lam=div(X[i][j],Y[i][j]); break
      if lam is not None: break
    return lam is not None and all(X[i][j]==mul(lam,Y[i][j]) for i in range(3) for j in range(3))
I=[[ONE,ZERO,ZERO],[ZERO,ONE,ZERO],[ZERO,ZERO,ONE]]
def order(X):
    P=I
    for n in range(1,33):
        P=mm(P,X)
        if meqproj(P,I): return n
    return None

def pmat(entries): return [[qp(*x) if isinstance(x,tuple) else qp(x) for x in row] for row in entries]
Rmat=pmat([[(1,0),(1,0),0],[(-1,0),(1,0),0],[0,0,(0,1)]])
Smat=pmat([[(1,0),(-1,0),0],[(-1,0),(-1,0),0],[0,0,(0,1)]])
assert order(Rmat)==8 and order(Smat)==2
# Check SRS = R^{-1} by S R S R = 1.
assert meqproj(mm(mm(mm(Smat,Rmat),Smat),Rmat),I)
order_profile=Counter(order(mat(A,k)) for A,k in aut)
assert order_profile==Counter({2:9,8:4,4:2,1:1}), order_profile
print('VERIFY_OK')
print('intersection_counts',dict(sorted(counts.items())))
print('automorphisms',len(aut),'order_profile',dict(sorted(order_profile.items())))
