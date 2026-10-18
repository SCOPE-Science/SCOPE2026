"""Exact conditional-moment checks for reciprocal two-agent random actions.

Requires Python 3 and sympy. All finite checks use rational arithmetic.
The asymptotic statements in the accompanying proof are analytical.
"""
from fractions import Fraction as F
import itertools
import sympy as s

a,p,q=s.symbols('a p q', real=True)
U=(p*(1-p)+q*(1-q))/2
V=(p-q)**2/4
mat=s.Matrix([[1-a*a,4*a*(1-a)],[a*a/2,(1-2*a)**2]])
up=vp=0
for i,j in itertools.product((0,1),repeat=2):
    prob=(p if i else 1-p)*(q if j else 1-q)
    pn=(1-a)*p+a*j
    qn=(1-a)*q+a*i
    up+=prob*(pn*(1-pn)+qn*(1-qn))/2
    vp+=prob*(pn-qn)**2/4
assert s.factor(up-(mat*s.Matrix([U,V]))[0])==0
assert s.factor(vp-(mat*s.Matrix([U,V]))[1])==0
x=s.symbols('x')
Fpoly=s.factor((mat-x*s.eye(2)).det())
assert s.factor(Fpoly-(-2*a**4+2*a**3-3*a*a*x+3*a*a+4*a*x-4*a+x*x-2*x+1))==0
res=s.factor(s.resultant(Fpoly,s.diff(Fpoly,a),x))
assert res==4*a**3*(a-1)*(34*a*a-47*a+16)
h=s.sqrt(17*a*a-32*a+16)
lam=1-2*a+s.Rational(3,2)*a*a+a*h/2
assert s.simplify(s.diff(lam,a)-((3*a-2)*h+17*a*a-24*a+8)/h)==0
star=(47+s.sqrt(33))/68
starval=(369+99*s.sqrt(33))/1156
assert s.simplify(Fpoly.subs({a:star,x:starval}))==0
assert abs(float(lam.subs(a,star))-float(starval))<1e-12
assert abs(float(star)-0.7756553330373)<1e-12
assert abs(float(starval)-0.8111692923938)<1e-12

# Independent branch enumeration for the first three updates.
def moments(dist):
    u=sum(prob*(x*(1-x)+y*(1-y))/2 for (x,y),prob in dist.items())
    v=sum(prob*(x-y)**2/4 for (x,y),prob in dist.items())
    return s.simplify(u),s.simplify(v)

def step(dist,af):
    nxt={}
    for (x,y),mass in dist.items():
        for i,j in itertools.product((0,1),repeat=2):
            pr=(x if i else 1-x)*(y if j else 1-y)
            key=((1-af)*x+af*j,(1-af)*y+af*i)
            nxt[key]=nxt.get(key,F(0))+mass*pr
    return {key:v for key,v in nxt.items() if v}

cases=0
for af in (F(1,4),F(1,2),F(3,4),F(9,10)):
    for p0 in (F(0),F(1,3),F(1,2),F(1)):
        for q0 in (F(0),F(1,3),F(2,3),F(1)):
            dist={(p0,q0):F(1)}
            u0,v0=moments(dist)
            seed=s.Matrix([s.Rational(u0.numerator,u0.denominator),s.Rational(v0.numerator,v0.denominator)])
            M=mat.subs(a,s.Rational(af.numerator,af.denominator))
            for t in range(4):
                u,v=moments(dist)
                check=M**t*seed
                assert u==check[0] and v==check[1],(af,p0,q0,t)
                assert sum(dist.values())==1
                cases+=1
                if t<3: dist=step(dist,af)
print('PASS: symbolic conditional moments, characteristic and optimizer identities')
print(f'PASS: {cases} exact branch-enumeration moment comparisons')
print('alpha_star =',star,'=',s.N(star,15))
print('lambda_star =',starval,'=',s.N(starval,15))
