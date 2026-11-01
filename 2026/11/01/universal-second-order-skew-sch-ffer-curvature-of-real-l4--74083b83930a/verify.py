"""Finite algebraic and numerical checks supplementing the analytic proof."""
from fractions import Fraction as F
from math import sqrt
from random import Random

def dot(u,v): return sum(a*b for a,b in zip(u,v))
def norm4(z): return sum(v**4 for v in z)**0.25

def check():
    n=0
    rng=Random(4026)
    # Exact rational coefficients in the square identity, with sqrt(2)
    # represented formally as a pair of rational coefficients.
    for _ in range(4000):
        x=F(rng.randint(-7,7), rng.randint(1,8))
        y=F(rng.randint(-7,7), rng.randint(1,8))
        # (x^2+sqrt(2)xy-y^2)^2 = x^4+y^4+2sqrt(2)xy(x^2-y^2)
        assert (x*x-y*y)**2+2*x*x*y*y == x**4+y**4
        assert 2*(x*x-y*y)*x*y == 2*x*y*(x*x-y*y)
        n+=2
    a2=(sqrt(3)-1)/(2*sqrt(2)); b2=(sqrt(3)+1)/(2*sqrt(2))
    a=sqrt(a2);b=sqrt(b2)
    assert abs(a**4+b**4-1)<1e-13
    assert abs(a*b-.5)<1e-13
    p=a**3*b-b**3*a; q=-p; E=2*a*a*b*b
    assert abs(p+1/(2*sqrt(2)))<1e-13
    assert abs(q-1/(2*sqrt(2)))<1e-13
    assert abs(E-.5)<1e-13
    assert abs(3*E-p*p-q*q-1.25)<1e-13
    n+=6
    for h in [2**(-k) for k in range(3,14)]:
        x=(a,b);y=(b,-a)
        u=norm4((x[0]+h*y[0],x[1]+h*y[1]))
        v=norm4((h*x[0]-y[0],h*x[1]-y[1]))
        assert abs(u-v)<1e-12
        target=1-h/sqrt(2)+1.25*h*h
        assert abs(u*u-target)<=24*h**3+2e-13
        n+=2
    for _ in range(1200):
        x=[rng.uniform(-2,2) for _ in range(5)]
        y=[rng.uniform(-2,2) for _ in range(5)]
        nx=norm4(x);ny=norm4(y)
        x=[v/nx for v in x];y=[v/ny for v in y]
        P=sum(i**3*j for i,j in zip(x,y))
        Q=sum(i*j**3 for i,j in zip(x,y))
        E=sum(i*i*j*j for i,j in zip(x,y))
        d=P-Q+1/sqrt(2)
        R=sum((i*i+sqrt(2)*i*j-j*j)**2 for i,j in zip(x,y))
        assert abs(R-2*sqrt(2)*d)<4e-12
        assert d> -2e-12
        assert abs((3*E-P*P-Q*Q)-1.25)<=12*sqrt(max(d,0))+1e-10
        h=rng.uniform(0,1/8)
        u=norm4([i+h*j for i,j in zip(x,y)])
        v=norm4([h*i-j for i,j in zip(x,y)])
        g=(u*u+v*v)/2
        assert abs(g-(1+h*(P-Q)+h*h*(3*E-P*P-Q*Q)))<=24*h**3+2e-12
        n+=4
    print('VERIFY_OK',n)
if __name__=='__main__':check()
