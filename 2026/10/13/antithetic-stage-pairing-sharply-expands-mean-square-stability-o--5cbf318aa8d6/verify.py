"""Exact reproducibility checks for the antithetic randomized RK2 scalar result."""
import sympy as sp
x,t=sp.symbols('x t',real=True)
p=lambda z: 1-x+x*x*z
m=1-x+x*x/sp.Integer(2)
b=x*x
A=sp.factor(sp.integrate((p(t)*p(1-t))**2,(t,0,1)))
I=sp.factor(sp.integrate(p(t)**2,(t,0,1))**2)
assert sp.factor(A-(m**4-b*b*m*m/6+b**4/sp.Integer(80)))==0
assert sp.factor(I-(m*m+b*b/sp.Integer(12))**2)==0
assert sp.factor(I-A-b*b*(60*m*m-b*b)/180)==0
assert sp.factor(4*m-b-(x-2)**2)==0
H=sp.factor((A-1)*30/x)
assert sp.expand(H)==x**7-10*x**6+50*x**5-140*x**4+250*x**3-300*x**2+240*x-120
sturm=sp.sturm(H,x)
def sign(z):
    return sp.sign(z)
def changes(signs):
    cleaned=[z for z in signs if z!=0]
    return sum(a!=b for a,b in zip(cleaned,cleaned[1:]))
assert changes([sign(sp.Poly(q,x).eval(0)) for q in sturm])==4
assert changes([sign(sp.LC(sp.Poly(q,x))) for q in sturm])==3
assert H.subs(x,sp.Rational(18965,10000))<0
assert H.subs(x,sp.Rational(18966,10000))>0
assert sp.factor(A.subs(x,sp.Rational(9,5)))==sp.Rational(2551507,3906250)
assert sp.factor(I.subs(x,sp.Rational(9,5)))==sp.Rational(935089,390625)
assert sp.factor((m*m+b*b/12)-1)==x*(x**3-3*x**2+6*x-6)/3
print('VERIFIED: exact moments, strict comparison, one positive root, bracket, rational witness')
