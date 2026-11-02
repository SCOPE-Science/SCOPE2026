"""Standalone exact tests for a scalar Bernoulli-erasure momentum classification.
Run: python verify.py. Finite checks supplement the analytic proof.
"""
from fractions import Fraction as F
from itertools import product
import sympy as s

b,g,p=s.symbols('b g p',positive=True)
a=1+b-g
v=g*g*(1-p)/p
A=s.Matrix([[a,-b],[1,0]])
P=s.Matrix([[1,-b*a/(1+b)],[-b*a/(1+b),b*b]])
D=2*g*(1-b)-g*g*((1-b)/(1+b)+(1-p)/p)
assert s.simplify((A.T*P*A-P)[0,0]+v+D)==0
for i,j in ((0,1),(1,0),(1,1)):
    assert s.simplify((A.T*P*A-P)[i,j])==0
assert s.simplify(s.det(P)-b*b*g*(2*(1+b)-g)/(1+b)**2)==0
G=2*p*(1-b*b)/(1+b-2*p*b)
assert s.simplify(D.subs(g,G))==0
assert s.simplify(s.diff(D,b)-(-2*g+2*g*g/(1+b)**2))==0
assert s.simplify(s.diff(D,b,2)+4*g*g/(1+b)**3)==0
assert s.simplify(s.diff(G,b)-2*p*((2*p-1)*(1+b*b)-2*b)/(1+b-2*p*b)**2)==0
# Rational benchmarks verify the three competing designs.
p0=F(4,5)
assert F(2)*p0==F(8,5)
assert F(4)*p0/(1+F(2)*F(2,5))==F(16,9)
assert F(2)*p0*(1-F(1,3)**2)/(1+F(1,3)-2*p0*F(1,3))==F(16,9)

def deficit(p,b,g):
    return 2*g*(1-b)-g*g*((1-b)/(1+b)+(1-p)/p)
assert deficit(p0,F(1,4),F(25,16))==F(275,1024)
assert deficit(p0,F(0),F(25,16))==F(75,1024)

def transfer(p,b,g,state):
    av=1+b-g
    vv=g*g*(1-p)/p
    m,r,z=state
    return ((av*av+vv)*m-2*b*av*r+b*b*z,av*m-b*r,m)

def enumerate_moment(p,b,g,n):
    total=F(0)
    for path in product((0,1),repeat=n):
        xprev=x=F(1)
        prob=F(1)
        for hit in path:
            prob*=p if hit else (1-p)
            new=(1+b-g*hit/p)*x-b*xprev
            xprev,x=x,new
        total+=prob*x*x
    return total

count=0
for prob in (F(1,5),F(2,5),F(1,2),F(3,5),F(4,5)):
    for mom in (F(0),F(1,8),F(1,3),F(2,3)):
        for step in (F(1,8),F(1,2),prob,F(1),F(3,2)):
            state=(F(1),F(1),F(1))
            for n in range(1,7):
                state=transfer(prob,mom,step,state)
                brute=enumerate_moment(prob,mom,step,n)
                assert state[0]==brute,(prob,mom,step,n,state[0],brute)
                assert brute>=(1-prob)**n
                if mom==0 and step==prob:
                    assert brute==(1-prob)**n
                if n>=2 and (mom!=0 or step!=prob):
                    assert brute>(1-prob)**n
                count+=1
# Finite exact-rational matrix Lyapunov checks at both sides of the phase boundary.
for prob in (F(1,4),F(2,5),F(1,2),F(3,5),F(4,5),F(9,10)):
    for mom in (F(1,9),F(1,4),F(1,2),F(3,4)):
        frontier=F(2)*prob*(1-mom*mom)/(1+mom-2*prob*mom)
        for scale in (F(1,10),F(3,4),F(1),F(6,5)):
            step=frontier*scale
            aa=1+mom-step
            vv=step*step*(1-prob)/prob
            pp=((F(1),-mom*aa/(1+mom)),(-mom*aa/(1+mom),mom*mom))
            mat=((aa,-mom),(F(1),F(0)))
            # E[A^T P A] where E[a_n]=a, E[a_n^2]=a^2+v
            delta00=(aa*aa+vv)*pp[0][0]+2*aa*pp[0][1]+pp[1][1]-pp[0][0]
            delta01=-mom*(aa*pp[0][0]+pp[0][1])-pp[0][1]
            delta11=mom*mom*pp[0][0]-pp[1][1]
            assert delta00==-deficit(prob,mom,step)
            assert delta01==delta11==0
            count+=1
print('VERIFIED_EXACT',count,'rational and symbolic groups')
