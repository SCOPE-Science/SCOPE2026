from fractions import Fraction
from math import factorial, sqrt

def degree(m,n,r):
    assert 0 <= r <= m <= n
    z=Fraction(1,1)
    for j in range(m-r):
        z *= Fraction(factorial(n+j)*factorial(j), factorial(r+j)*factorial(n-r+j))
    assert z.denominator==1
    return z.numerator

def curvature_formula(m,n,r):
    c=m-r
    return Fraction(c*(n+c)*(n-m+c)*(m-c), (n-m+2*c)**2*((n-m+2*c)**2-1))

checks=0
for m in range(2,24):
    for n in range(m+1,m+18):
        for r in range(1,m):
            lhs=Fraction(degree(m,n,r-1)*degree(m,n,r+1), degree(m,n,r)**2)
            rhs=curvature_formula(m,n,r)
            assert lhs==rhs,(m,n,r,lhs,rhs)
            checks+=1

# Exact Q(sqrt(17)) arithmetic; pairs represent a+b*sqrt(17).
def add(u,v): return (u[0]+v[0],u[1]+v[1])
def neg(u): return (-u[0],-u[1])
def mul(u,v): return (u[0]*v[0]+17*u[1]*v[1],u[0]*v[1]+u[1]*v[0])
def scale(u,q): return (u[0]*q,u[1]*q)
Z=(Fraction(0),Fraction(0)); O=(Fraction(1),Fraction(0))
def padd(p,q):
    z=[Z]*max(len(p),len(q))
    for i in range(len(z)): z[i]=add(p[i] if i<len(p) else Z,q[i] if i<len(q) else Z)
    return z
def pmul(p,q):
    z=[Z]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): z[i+j]=add(z[i+j],mul(a,b))
    return z
def ppow(p,k):
    z=[O]
    for _ in range(k): z=pmul(z,p)
    return z
def pscale(p,q): return [scale(a,q) for a in p]

lam=(Fraction(1,4),Fraction(1,4)); minus1=(Fraction(-1),Fraction(0)); xpoly=[Z,O]
a=padd([add(lam,minus1)],pscale(xpoly,Fraction(2)))
left=ppow(a,4)
term=pmul(xpoly,[lam,O])
term=pmul(term,[add(lam,minus1),O])
term=pmul(term,[O,neg(O)])
F=padd(left,pscale(term,Fraction(-1)))
Q=[(Fraction(51),Fraction(-13)),(Fraction(-102),Fraction(34)),(Fraction(136),Fraction(0))]
Q2=pscale(pmul(Q,Q),Fraction(1,1088))
assert F==Q2,(F,Q2)

lam_star=(1+sqrt(17))/4
def Rlim(lam,x): return x*(lam+x)*(lam-1+x)*(1-x)/(lam-1+2*x)**4
x_star=-sqrt(17)/8 + sqrt(34*sqrt(17)+578)/136 + 3/8
assert 0<x_star<1 and abs(Rlim(lam_star,x_star)-1)<2e-12
for lamv in (1.3,1.5,2.0):
    assert lamv>lam_star and max(Rlim(lamv,i/1000) for i in range(1,1000))<1
for lamv in (1.02,1.1,1.2):
    assert lamv<lam_star and Rlim(lamv,x_star)>1
print('VERIFY_OK','factorial_ratio_checks',checks,'lambda_star',repr(lam_star),'x_star',repr(x_star))
