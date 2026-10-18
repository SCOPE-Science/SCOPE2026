"""Exact rational checks for the two-bank cross-holding phase theorem.

Run: python verify.py. Uses Python 3 standard library and sympy for symbolic identities.
Finite tests supplement, and do not replace, the analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import sympy as sp

T=F(1); L=F(4,5); H=F(7,5); BETA=F(3,8)
checks=0

def require(cond, desc='assertion'):
    global checks
    assert cond,desc
    checks+=1

def candidate(a,b,c,failed):
    """Exact linear solution under assigned failed indicators."""
    d1,d2=failed
    x=(1-c)*a-BETA*d1
    y=(1-c)*b-BETA*d2
    return ((x+c*y)/(1-c*c), (y+c*x)/(1-c*c))

def valid(v,flags):
    return all((x<T)==bool(d) for x,d in zip(v,flags))

def possibilities(a,b,c):
    return [(d,candidate(a,b,c,d)) for d in product((0,1),repeat=2)
            if valid(candidate(a,b,c,d),d)]

def maximal(a,b,c):
    opts=possibilities(a,b,c)
    require(bool(opts),'no equilibrium')
    maxes=[(d,v) for d,v in opts if all(v[0]>=w[0] and v[1]>=w[1] for _,w in opts)]
    require(len(maxes)==1,'maximal equity outcome not unique')
    return maxes[0]

cvar=sp.symbols('c',real=True)
a,b,beta,t=sp.symbols('a b beta t', positive=True)
x,y=sp.symbols('x y')
M=sp.Matrix([[1,-cvar],[-cvar,1]])
for d1,d2 in product((0,1),repeat=2):
    rhs=sp.Matrix([(1-cvar)*a-beta*d1,(1-cvar)*b-beta*d2])
    v=sp.simplify(M.inv()*rhs)
    require(all(sp.simplify((M*v-rhs)[i])==0 for i in (0,1)), 'linear equations')

A=H-T; D=T-L
threshold=D/A
crit=(A-D)**2*(A+D)/(A*D)
require(threshold==F(1,2),'rescue point')
require(crit==F(3,10),'distress-cost threshold')
require(BETA>crit,'nonempty contagion band')
cs=(39-sqrt(1009))/16
require(F(9,20)<cs<F(23,50),'root interval')
require(cs < float(threshold),'root below rescue')

# All 0.00..0.53 gridpoints that do not land exactly on an irrational boundary.
for j in range(54):
    c=F(j,100)
    f=A-(A+D+BETA)*c+D*c*c
    expected=1 if f>0 and c<threshold else (2 if c<threshold else 0)
    sols=possibilities(L,H,c)
    d,v=maximal(L,H,c)
    require(sum(d)==expected,f'phase {c}: {sols}')
    require(all(z>=0 for z in v),'nonnegative max values')
    require(all(z>=0 for z in maximal(H,H,c)[1]),'both-high nonnegative')
    require(all(z>=0 for z in maximal(L,L,c)[1]),'both-low nonnegative')
    require(maximal(H,H,c)[0]==(0,0),'both high solvent')
    require(maximal(L,L,c)[0]==(1,1),'both low default')
    require(sum(maximal(H,L,c)[0])==expected,'symmetric one shock')
    # finite-grid validation of correlation derivative at rational probability pairs
    for p,q in [(F(1,2),F(1,4)),(F(1,2),F(1,8)),(F(1,2),F(3,8)),(F(1,4),F(1,16))]:
        no=1-2*p+q; one=p-q; both=q
        require(no>=0 and one>=0 and both>=0,'admissible shock law')
        dn=sum(maximal(H,H,c)[0]); ds=sum(maximal(L,H,c)[0]);
        db=sum(maximal(L,L,c)[0]);
        exact=no*dn+2*one*ds+both*db
        require(exact==2*(p-q)*expected+2*q,'correlation law')

# Test independent dimensions of the exact inequalities over many positive rational parameter sets.
for ai in range(2,10):
 for bi in range(1,ai):
  for be in range(1,18):
   aa=F(ai,10); bb=F(bi,10); bet=F(be,20)
   center=bb/aa
   f=lambda c: aa-(aa+bb+bet)*c+bb*c*c
   ca=bb/aa
   if ca<1:
    boundary=(aa-bb)**2*(aa+bb)/(aa*bb)
    require((f(ca)<0)==(bet>boundary),'general threshold identity')
   for c in (F(0),F(1,10),F(1,4),F(2,5),F(1,2),F(3,4),F(9,10)):
    if ca<1 and c>=ca:
     predicted=0
    else:
     predicted=1 if f(c)>=0 else 2
    # general equilibrium calculator independent of BETA
    a0=1-bb; h0=1+aa
    opts=[]
    for d0,d1 in product((0,1),repeat=2):
     t0=(1-c)*a0-bet*d0; t1=(1-c)*h0-bet*d1
     v0=(t0+c*t1)/(1-c*c); v1=(t1+c*t0)/(1-c*c)
     if (v0<1)==bool(d0) and (v1<1)==bool(d1): opts.append(((d0,d1),(v0,v1)))
    maxes=[dv for dv in opts if all(dv[1][0]>=w[0] and dv[1][1]>=w[1] for _,w in opts)]
    require(len(maxes)==1 and sum(maxes[0][0])==predicted, f'general {ai} {bi} {be} {c}: {opts}')

print(f'PASS: {checks} finite exact-rational and symbolic checks')
print('Example thresholds: c_star=(39-sqrt(1009))/16, c_all=1/2, beta_crit=3/10')
