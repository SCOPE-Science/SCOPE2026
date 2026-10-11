"""Additional exact integral spot-check using two independent sampling constructions."""
import sympy as s
from fractions import Fraction
u,v,w,x=s.symbols('u v w x')
a=s.Matrix([3,0]);b=s.Matrix([s.Rational(4,5),s.Rational(3,5)])
def mean_poly(expr, variables):
    out=0
    for powers,coefficient in s.Poly(s.expand(expr),*variables).terms():
        m=coefficient
        for power in powers:
            if power%2: m=0;break
            m=m/(power+1)
        out+=m
    return s.simplify(out)
def n4(y,z):
    delta=y-z
    return s.expand((delta.dot(delta))**2)
# Interior: two independent points, each a sum of two independent uniforms.
Ii=mean_poly(n4(a*u+b*v,a*w+b*x),(u,v,w,x))
# Four actual edges, each with the appropriate exact length weight.
edges=[(b+a*u,s.Rational(3,8)),(-b+a*u,s.Rational(3,8)),(a+b*u,s.Rational(1,8)),(-a+b*u,s.Rational(1,8))]
Sb=sum(pi*pj*mean_poly(n4(ei,ej.subs(u,v)),(u,v)) for ei,pi in edges for ej,pj in edges)
A=s.Integer(3);B=s.Integer(1);z=s.Rational(12,5)
expected_i=s.Rational(8,45)*(6*A**4+5*A**2*B**2+6*B**4+10*z**2)
print('spot check actual interior',Ii,'expected',expected_i)
# boundary analytic expression obtained from moments of conditional edges
p=A/(A+B);q=B/(A+B)
mb2=(A+B)**2/3
mb4=p*(B**4+(2*A*A*B*B+4*z*z)/3+A**4/5)+q*(A**4+(2*A*A*B*B+4*z*z)/3+B**4/5)
alpha=(A/3+B)/(A+B);beta=(A+B/3)/(A+B)
expected_b=s.factor(2*mb4+2*mb2**2+4*(alpha**2*A**4+beta**2*B**4+2*alpha*beta*z**2))
print('spot check actual boundary',Sb,'expected',expected_b)
assert Ii==expected_i and Sb==expected_b
print('PARALLELOGRAM_INDEPENDENT_INTEGRAL_CHECK_OK')
