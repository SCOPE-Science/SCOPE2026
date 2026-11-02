#!/usr/bin/env python3
"""Exact checks for fast-refresh random-environment walk diffusivity expansion.

Only Python's standard library is required. The analytic proof is in RESULT.md.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

assertions=0

def check(x, message=''):
    global assertions
    assert x, message
    assertions += 1


def poly_add(a,b,limit=4):
    return [sum((p[i] if i<len(p) else F(0)) for p in (a,b)) for i in range(limit)]


def poly_mul(a,b,limit=4):
    return [sum(a[j]*b[i-j] for j in range(i+1) if j<len(a) and i-j<len(b)) for i in range(limit)]


def annealed_moments(law, N):
    # law = tuple of (weight, rightward transition probability) pairs
    @lru_cache(None)
    def emit(right,left):
        return sum(weight*prob**right*(1-prob)**left for weight,prob in law)
    A=[]; B=[]
    for n in range(1,N+1):
        acc1=F(0);acc2=F(0)
        for increments in product((-1,1), repeat=n):
            counts={};pos=0
            for step in increments:
                if pos not in counts:counts[pos]=[0,0]
                counts[pos][0 if step==1 else 1] += 1
                pos+=step
            weight=F(1)
            for r,l in counts.values():weight*=emit(r,l)
            acc1+=pos*weight;acc2+=pos*pos*weight
        A.append(acc1); B.append(acc2)
    return A,B


def expansion(A,B):
    p2=[F(1),F(-2),F(1)]
    generating_A=[A[i] for i in range(4)]
    v=poly_mul(p2,generating_A)
    v2=poly_mul(v,v)
    inner=[F(0)]*4
    for i in range(4):
        n=i+1
        term=poly_add([B[i]],poly_mul([F(-2*n)*A[i]],v))
        term=poly_add(term,poly_mul([F(n*n)],v2))
        for j in range(4-i):inner[i+j]+=term[j]
    variance=poly_mul(p2,inner)
    return v, variance

laws=[
    ((F(1,2),F(1,4)),(F(1,2),F(3,4))),
    ((F(1,2),F(1,5)),(F(1,2),F(4,5))),
    ((F(1,3),F(1,5)),(F(2,3),F(3,5))),
    ((F(1,4),F(1,9)),(F(3,4),F(5,9))),
    ((F(1,5),F(1,8)),(F(3,5),F(3,8)),(F(1,5),F(7,8))),
    ((F(1,3),F(1,3)),(F(1,3),F(1,2)),(F(1,3),F(4,5))),
    ((F(1),F(1,2)),),
    ((F(1),F(3,4)),),
]
for law in laws:
    mu=sum(w*z for w,z in law); m=2*mu-1
    s=sum(w*(z-mu)**2 for w,z in law)
    A,B=annealed_moments(law,4)
    exA=[m,2*m,(3-2*s)*m,4*(1-s)*m]
    exB=[F(1),2+2*m*m,3+6*m*m,4+12*m*m-8*s*m*m-8*s*s]
    for x,y in zip(A,exA):check(x==y,'first moment mismatch')
    for x,y in zip(B,exB):check(x==y,'second moment mismatch')
    v,var=expansion(A,B)
    for x,y in zip(v,[m,F(0),-2*m*s,F(0)]):check(x==y,'speed series mismatch')
    for x,y in zip(var,[1-m*m,F(0),12*s*m*m,-8*s*s]):check(x==y,'variance series mismatch')

# Direct exact renewal upper/lower bound for a symmetric nondegenerate environment.
# This independently checks that the cubic sign is observable at finite refresh rate.
law=((F(1,2),F(1,5)),(F(1,2),F(4,5)))
q=F(1,10);p=1-q;N=12
A,B=annealed_moments(law,N)
vN=p*p*sum(q**i*A[i] for i in range(N))
sigmaN=p*p*sum(q**i*(B[i]-2*(i+1)*vN*A[i]+(i+1)**2*vN*vN) for i in range(N))
# Sum_{m>N} m q^{m-1} = q^N*((N+1)-Nq)/(1-q)^2
v_error=p*p*q**N*((N+1)-N*q)/(1-q)**2
# Tail of sum_{m>N} m^2 q^{m-1} from the differentiated geometric series.
# Safe (loose) bound: (N+1)^2 q^N/(1-q)^3 * 4.
tail_m2=4*(N+1)**2*q**N/(1-q)**3
sigma_error=4*p*p*(sum((i+1)**2*q**i for i in range(N))*v_error+tail_m2)
check(sigmaN+sigma_error<1,'nondegenerate zero-drift coefficient is not reflected at p=0.9')
print('Exact rational assertions:',assertions)
print('Symmetric environment: mu=1/2, site variance=9/100, q=1/10')
print('Finite block-approximation sigma^2:', float(sigmaN))
print('Rigorous absolute truncation error at N=12:',float(sigma_error))
print('Predicted cubic coefficient:',float(-8*F(9,100)**2))
print('PASS')
