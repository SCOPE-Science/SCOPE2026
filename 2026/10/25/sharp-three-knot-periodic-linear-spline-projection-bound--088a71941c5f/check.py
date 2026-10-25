"""Exact identities for the three-knot periodic linear-spline projector.

Requires Python 3 and SymPy. No external data files.
"""
from fractions import Fraction
from itertools import product
import sympy as s

a,b,c,z,e=s.symbols('a b c z e', positive=True)
D=(a+b+c)*(a*b+a*c+b*c)
A=4*a*b+4*a*c+3*b*b+4*b*c
X=2*a*(b+c)-b*c
Y=2*c*(a+b)-a*b
M=s.Matrix([[(a+c)/3,a/6,c/6], [a/6,(a+b)/3,b/6], [c/6,b/6,(b+c)/3]])
assert s.simplify(6*M.inv()-6*s.Matrix([[A,-X,-Y],[-X,4*a*b+4*a*c+4*b*c+3*c*c, -(2*a*b-a*c+2*b*c)],[-Y, -(2*a*b-a*c+2*b*c),3*a*a+4*a*b+4*a*c+4*b*c]])/D)==s.zeros(3)
assert s.factor(A+X-3*(2*a+b)*(b+c))==0
assert s.factor(A+Y-3*(a+b)*(b+2*c))==0
assert s.factor(Y-X-3*b*(c-a))==0

q_both=(a*X**2/(A+X)+b*(X+Y)+c*Y**2/(A+Y))/(2*D)
poly0=(8*a**3*c**3+20*b*a*a*c*c*(a+c)
       +2*b*b*a*c*(8*a*a+17*a*c+8*c*c)
       +4*b**3*(a+c)*(a*a+4*a*c+c*c)
       +2*b**4*(3*a*a+2*a*c+3*c*c)
       +b**5*(a+c))
den0=6*(a+b)*(2*a+b)*(b+c)*(b+2*c)*(a*b+a*c+b*c)
assert s.factor(s.Rational(2,3)-q_both-poly0/den0)==0
assert all(coefficient>0 for _,coefficient in s.Poly(s.expand(poly0),a,b,c).terms())

q_one=s.factor(Y**2*(b+c)/(6*(c-a)*(a+b)*(b+2*c)*(a*b+a*c+b*c)))
poly1=(6*(b+c)*(b+2*c)**2*(b+3*c)
       +(b+2*c)*(11*b*b+49*b*c+42*c*c)*z
       +4*(b*b+7*b*c+8*c*c)*z*z+4*c*z**3)
den1=6*(b+2*c)*(b+2*c+z)*(2*b+3*c+z)*(3*b+3*c+z)
assert s.factor((s.Rational(2,3)-q_one).subs(a,b*c/(2*(b+c)+z))-poly1/den1)==0
assert all(coefficient>0 for _,coefficient in s.Poly(s.expand(poly1),b,c,z).terms())

# Independently integrate the signed affine kernel on each cell using exact fractions.
def area_abs(length,u,v):
    if u*v>=0: return length*(abs(u)+abs(v))/2
    return length*(u*u+v*v)/(2*(abs(u)+abs(v)))

def area_negative(length,u,v):
    if u>=0 and v>=0:return s.Rational(0)
    if u<=0 and v<=0:return -length*(u+v)/2
    if u>0:return length*v*v/(2*(u-v))
    return length*u*u/(2*(v-u))

checked=0; regimes=set(); maxnorm=s.Rational(0)
for aa,bb,cc in product(range(1,10), repeat=3):
    u,v,w=map(s.Rational,(aa,bb,cc))
    Mm=M.subs({a:u,b:v,c:w}); Im=Mm.inv()
    assert s.factor(Mm.det())>0
    for i in range(3):
        row=list(Im.row(i))
        norm=sum(area_abs(l,row[j],row[(j+1)%3]) for j,l in enumerate((u,v,w)))
        neg=sum(area_negative(l,row[j],row[(j+1)%3]) for j,l in enumerate((u,v,w)))
        assert norm==1+2*neg
        assert norm<s.Rational(7,3)
        maxnorm=max(maxnorm,norm)
        checked+=1
    xx=X.subs({a:u,b:v,c:w}); yy=Y.subs({a:u,b:v,c:w})
    neg0=sum(area_negative(l,Im[0,j],Im[0,(j+1)%3]) for j,l in enumerate((u,v,w)))
    if xx>=0 and yy>=0:
        assert s.factor(neg0-q_both.subs({a:u,b:v,c:w}))==0
        regimes.add('both')
    elif xx<0:
        assert yy>0
        assert s.factor(neg0-q_one.subs({a:u,b:v,c:w}))==0
        regimes.add('X_negative')
    else:
        assert yy<0 and xx>0
        swapped=q_one.subs({a:c,c:a}, simultaneous=True)
        assert s.factor(neg0-swapped.subs({a:u,b:v,c:w}))==0
        regimes.add('Y_negative')

r=s.factor((1+2*q_one).subs({a:e**2,b:1,c:e}))
assert s.limit(r,e,0,dir='+')==s.Rational(7,3)
assert X.subs({a:e**2,b:1,c:e}).subs(e,s.Rational(1,10))<0
assert Y.subs({a:e**2,b:1,c:e}).subs(e,s.Rational(1,10))>0
print('PASS: inverse Gramian; rational-integral identities; two positive certificates')
print('PASS: %s exact vertex kernel integrals; regimes %s' % (checked,sorted(regimes)))
print('PASS: nonattained strict bound and exact hierarchical degeneration limit 7/3')
print('largest sampled vertex norm:',maxnorm)
