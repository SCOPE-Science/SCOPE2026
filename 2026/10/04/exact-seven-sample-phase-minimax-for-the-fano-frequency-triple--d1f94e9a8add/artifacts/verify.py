#!/usr/bin/env python3
from fractions import Fraction as F
import cmath, math

# Laurent polynomials in z,u,v; coefficients are exact rationals.
def add(A,B):
    C=A.copy()
    for k,v in B.items():
        C[k]=C.get(k,F(0))+v
        if not C[k]: del C[k]
    return C

def mul(A,B):
    C={}
    for (az,au,av),ac in A.items():
        for (bz,bu,bv),bc in B.items():
            k=(az+bz,au+bu,av+bv)
            C[k]=C.get(k,F(0))+ac*bc
    return {k:v for k,v in C.items() if v}

def power(A,n):
    R={(0,0,0):F(1)}
    for _ in range(n): R=mul(R,A)
    return R

def sample_mean(A):
    # Average over seventh roots: z^r survives exactly when 7 divides r.
    R={}
    for (ez,eu,ev),c in A.items():
        if ez%7==0:
            k=(eu,ev)
            R[k]=R.get(k,F(0))+c
    return {k:v for k,v in R.items() if v}

P={(0,0,0):F(1),(1,1,0):F(1),(3,0,1):F(1)}
Pc={(0,0,0):F(1),(-1,-1,0):F(1),(-3,0,-1):F(1)}
q=mul(P,Pc)
M=[None]+[sample_mean(power(q,j)) for j in range(1,5)]
assert M[1]=={(0,0):F(3)}
assert M[2]=={(0,0):F(15)}
mons=[(3,-1),(-3,1),(2,-3),(-2,3),(1,2),(-1,-2)]
exp3={(0,0):F(93), **{k:F(3) for k in mons}}
exp4={(0,0):F(639), **{k:F(52) for k in mons}}
assert M[3]==exp3
assert M[4]==exp4
# 3*m4 = 52*m3 - 2919, coefficient by coefficient.
keys=set(M[3])|set(M[4])
for k in keys:
    assert 3*M[4].get(k,F(0)) == 52*M[3].get(k,F(0)) - (F(2919) if k==(0,0) else F(0))
# m3-84 = 3*|1+X+Y^{-1}|^2 with X=u^2 v^-3, Y=u v^2.
abs_sq={(0,0):F(3), **{k:F(1) for k in mons}}
for k in set(M[3])|set(abs_sq):
    lhs=M[3].get(k,F(0))-(F(84) if k==(0,0) else F(0))
    assert lhs==3*abs_sq.get(k,F(0))

# Exact coefficient check for the quartic certificate average.
# Represent a+b*sqrt(21) as a pair of rationals.
def Q(a=0,b=0): return (F(a),F(b))
def qadd(x,y): return (x[0]+y[0],x[1]+y[1])
def qscale(c,x): return (c*x[0],c*x[1])
# h(x)=-x^4 + (21-s)/2 x^3 + (-63+7s)/2 x^2 + (49-7s)/2 x
c4=Q(-1); c3=(F(21,2),F(-1,2)); c2=(F(-63,2),F(7,2)); c1=(F(49,2),F(-7,2))
# m4=(52/3)t-973, m3=t, m2=15, m1=3 -> E h = slope*t + intercept.
slope=qadd(qscale(F(52,3),c4),c3)
intercept=qadd(qscale(F(-973),c4),qadd(qscale(F(15),c2),qscale(F(3),c1)))
target_slope=(F(-41,6),F(-1,2))
target_intercept=qscale(F(-84),target_slope)
assert slope==target_slope and intercept==target_intercept

# Corroborate the explicit witness numerically.
zeta=cmath.exp(2j*math.pi/7)
omega=cmath.exp(2j*math.pi/3)
u=omega**2; v=omega
vals=[abs(1+u*zeta**k+v*zeta**(3*k))**2 for k in range(7)]
A=(7+math.sqrt(21))/2; B=(7-math.sqrt(21))/2
vals_sorted=sorted(vals)
target=sorted([0.0]+[A]*3+[B]*3)
assert max(abs(a-b) for a,b in zip(vals_sorted,target)) < 2e-12
print('VERIFY_OK')
