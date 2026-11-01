#!/usr/bin/env python3
"""Exact polynomial identities and rational witnesses for the stated BCNF theorem.
No third-party packages. An algebraic identity check, not an independent audit.
"""
from fractions import Fraction as Q
from collections import defaultdict

ZERO = ()
def mon(c=0, ex=(0,0,0,0)):
    return {ex:c} if c else {}
def plus(a,b):
    d=defaultdict(int,a)
    for k,v in b.items(): d[k]+=v
    return {k:v for k,v in d.items() if v}
def neg(a): return {k:-v for k,v in a.items()}
def sub(a,b): return plus(a,neg(b))
def mul(a,b):
    d=defaultdict(int)
    for x,c in a.items():
        for y,e in b.items(): d[tuple(i+j for i,j in zip(x,y))]+=c*e
    return {k:v for k,v in d.items() if v}
def power(a,n):
    p=ONE
    for _ in range(n):p=mul(p,a)
    return p
ONE=mon(1)
u,v,r,t=[mon(1,tuple(int(i==j) for i in range(4))) for j in range(4)]
alpha=sub(mul(plus(ONE,u),sub(ONE,v)),mul(r,t))
A_L=[[t,ONE],[u,{}]]
A_R=[[neg(r),ONE],[neg(v),{}]]
b=[ONE,{}]
def mm(A,B):return [[plus(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
def mv(A,w):return [plus(mul(A[i][0],w[0]),mul(A[i][1],w[1])) for i in range(2)]
def det(A):return sub(mul(A[0][0],A[1][1]),mul(A[0][1],A[1][0]))
M=[[ONE,{}],[{},ONE]]; shift=[{},{}]
for A in [A_L,A_R,A_R,A_R]:
    M=mm(A,M);shift=[plus(x,y) for x,y in zip(mv(A,shift),b)]
I_minus_M=[[sub(ONE,M[0][0]),neg(M[0][1])],[neg(M[1][0]),sub(ONE,M[1][1])]]
D=det(I_minus_M)
adj=[[I_minus_M[1][1],neg(I_minus_M[0][1])],[neg(I_minus_M[1][0]),I_minus_M[0][0]]]
z_num=mv(adj,shift)
trace=plus(M[0][0],M[1][1]);d4=det(M)
claimed_trace=plus(neg(mul(mul(r,t),sub(power(r,2),mul(mon(2),v)))),mul(sub(u,v),sub(power(r,2),v)))
claimed_D=sub(sub(ONE,claimed_trace),mul(u,power(v,3)))
assert not sub(trace,claimed_trace)
assert not plus(d4,mul(u,power(v,3)))
assert not sub(D,claimed_D)
claimed_x0=neg(mul(sub(sub(r,v),ONE),plus(power(r,2),power(sub(v,ONE),2))))
assert not sub(z_num[0],claimed_x0)
z1_num=[plus(x,y) for x,y in zip(mv(A_L,z_num),[D,{}])]
z2_num=[plus(x,y) for x,y in zip(mv(A_R,z1_num),[D,{}])]
claimed_x2=neg(mul(sub(sub(r,v),ONE),alpha))
assert not sub(z2_num[0],claimed_x2)
# Universal trace ceiling from alpha<0 and r>1+v is algebraic.
Tcorner=plus(sub(neg(ONE),neg(mul(u,power(v,3)))),mul(mon(2),mul(v,sub(u,v))))
Tlimit=plus(neg(mul(mul(plus(ONE,u),sub(ONE,v)),sub(power(plus(ONE,v),2),mul(mon(2),v)))),mul(sub(u,v),sub(power(plus(ONE,v),2),v)))
assert not sub(Tcorner,Tlimit)

# Exact rational orbit witness and Schur inequalities.
def evaluate(poly, vals):
    out=Q(0)
    for ex,c in poly.items():
        prod=Q(c)
        for x,p in zip(vals,ex): prod*=x**p
        out+=prod
    return out
for vals in [(Q(3,4),Q(1,4),Q(63,50),Q(53,50)),
             (Q(9,10),Q(2,5),Q(141,100),Q(41,50)),
             (Q(3,5),Q(1,5),Q(121,100),Q(23,20))]:
    uu,vv,rr,tt=vals
    assert Q(0)<vv<uu<Q(1) and rr>1+vv and tt>1-uu
    Delta=evaluate(D,vals);tr=evaluate(trace,vals)
    assert -1+uu*vv**3 <tr <1-uu*vv**3 and Delta>0
    zz=[evaluate(w,vals)/Delta for w in z_num]
    points=[zz]
    for A in [A_L,A_R,A_R]:
        points.append([(evaluate(A[i][0],vals)*zz[0]+evaluate(A[i][1],vals)*zz[1])+([Q(1),Q(0)][i]) for i in range(2)])
        zz=points[-1]
    assert points[0][0]<0 and all(p[0]>0 for p in points[1:])
    last=[evaluate(A_R[i][0],vals)*zz[0]+evaluate(A_R[i][1],vals)*zz[1]+([Q(1),Q(0)][i]) for i in range(2)]
    assert last==points[0]
print('PASS: 6 exact multivariate polynomial identities and three rational period-four witnesses')
