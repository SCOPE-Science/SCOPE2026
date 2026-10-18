"""Exact identities and non-proof consistency checks for the regular decagon index.

Requires Python 3 and SymPy. The infinite family of rank-one operators is
covered by the analytical inequalities in RESULT.md, not by a finite scan.
"""
import random
import sympy as S

r=(S.sqrt(5)-1)/2
s,t=S.symbols('s t', real=True)
C=[S.Integer(1),S.Integer(1),r,S.Integer(0),-r,-S.Integer(1),-S.Integer(1),-r,S.Integer(0),r]
checks=0

def verify(cond, desc=''):
    global checks
    if cond is not True and cond is not S.true:
        raise AssertionError(desc or repr(cond))
    checks+=1

def eq(a,b,desc=''):
    verify(S.simplify(S.expand(a-b))==0,desc)

def a(j,k):
    return C[(k-j)%10]

def b(j):
    return S.expand((1-s)*a(j,0)+s*a(j,1))

def f(j,k):
    return S.expand((1-t)*a(j,k)+t*a(j+1,k))

# Independent trigonometric derivation of the ten-entry incidence table.
for j in range(10):
    for k in range(10):
        angle=S.Rational(2*k-2*j-1,10)*S.pi
        actual=S.cos(angle)/S.cos(S.pi/10)
        eq(actual,a(j,k),'incidence %d %d'%(j,k))

eq(r*r,1-r)
eq(r*r*r*r,(1-r)**2)
for j in range(10):
    eq(a(j,j),1)
    eq(a(j,j+1),1)
for j in range(5):
    eq(f(j,j+1),1)

# In the reduced sector 0<=s<=1/2 the relevant support values are:
eq(b(0),1)
eq(b(1),r+r*r*s)
eq(b(2),r*s)
eq(b(3),-r*(1-s))
eq(b(4),-1+r*r*s)
eq(b(5),-1)
# Exact values of max(|b(k-1)|,|b(k)|) on the sector:
B1=S.Integer(1)
B2=r+r*r*s
B3=r*(1-s)
B4=1-r*r*s
B5=S.Integer(1)
eq(f(1,1),1-r*r*t)
eq(f(2,2),1-r*r*t)
eq(f(2,4),r+r*r*t)
eq(f(2,3),1)

P2=(1-r*r*t)*B2
P4=(r+r*r*t)*B4
eq(P2.subs(t,s),P4.subs(t,s))
eq(P2.subs(t,s),r+r**4*s*(1-s))
# The two expressions are decreasing/increasing in t, respectively.
verify(S.simplify(S.diff(P2,t)+r*r*B2)==0)
verify(S.simplify(S.diff(P4,t)-r*r*B4)==0)
# Strict case j=3, 1-r^2/2 > r:
verify(float(S.N(1-r*r/2-r,20))>0)
# The extremal vertex-to-normal operator has zero square:
eq(a(2,0),0)

# Finite samples stress-test the quantified inequality and equality rigidity.
random.seed(17)
import math
V=[(math.cos(j*math.pi/5),math.sin(j*math.pi/5)) for j in range(10)]
Q=[(math.cos((j+.5)*math.pi/5)/math.cos(math.pi/10),math.sin((j+.5)*math.pi/5)/math.cos(math.pi/10)) for j in range(10)]
def dot(x,y):return x[0]*y[0]+x[1]*y[1]
def val(j,sv,tv):
    x=tuple((1-sv)*V[0][i]+sv*V[1][i] for i in range(2))
    u=tuple((1-tv)*Q[j][i]+tv*Q[(j+1)%10][i] for i in range(2))
    return max(abs(dot(u,V[k])) * max(abs(dot(Q[k],x)),abs(dot(Q[(k-1)%10],x))) for k in range(10))
for j in range(5):
    for _ in range(150):
        sv=random.random()*.5; tv=random.random()
        verify(val(j,sv,tv)>=float(r)-1e-12)
verify(abs(val(2,0,0)-float(r))<1e-13)
verify(abs(val(1,0,1)-float(r))<1e-13)
print('PASS',checks,'checks; exact incidence, polynomial identities, finite samples')
