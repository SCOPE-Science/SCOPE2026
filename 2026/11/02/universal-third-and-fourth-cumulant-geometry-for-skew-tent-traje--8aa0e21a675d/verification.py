"""Standalone rational verification of polynomial tilted-transfer cumulants.
No scientific provenance, systems, personnel, or workflow assumptions are encoded.
"""
from fractions import Fraction as F
from math import comb

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]+=v*w
    return out

def P(co,a):
    b=1-a
    out=[F(0)]*len(co)
    for m,c in enumerate(co):
        # a*(a x)^m + b*(1-b x)^m
        out[m]+=c*a**(m+1)
        for j in range(m+1):out[j]+=c*b*comb(m,j)*(-b)**j
    return out

def integrate(co):return sum((v/F(i+1) for i,v in enumerate(co)),F(0))

def poly_at(a,N):
    g=[F(-1,2),F(1)]
    powg=[[F(1)]]
    for m in range(1,5):powg.append(mul(powg[-1],g))
    h=[[F(1)]] + [[F(0)] for _ in range(4)]
    for _ in range(N):
        nxt=[]
        for r in range(5):
            total=[F(0)]*(r+1)
            for k in range(r+1):
                term=mul(powg[k],h[r-k]); fac=comb(r,k)
                for j,c in enumerate(term):total[j]+=fac*c
            nxt.append(P(total,a))
        h=nxt
    m=[integrate(p) for p in h]
    # centered since invariant uniform and g centered
    assert m[0]==1 and m[1]==0
    return m[2],m[3],m[4]-3*m[2]**2

def formula(a):
    b=1-a
    return a/(12*b),-a/(24*b*b),a*(19+6*a*b)/(720*b**3)

if __name__=='__main__':
    for a in [F(1,4),F(1,2),F(3,4)]:
        v=four=None
        for N in [1,2,4,8,16,32,64]:
            cumulants=poly_at(a,N)
            if N==1:
                assert cumulants==(F(1,12),F(0),-F(1,120))
            print('a',str(a),'N',N,'rates',tuple(round(float(c/N),9) for c in cumulants))
        print('limit',tuple(round(float(v),9) for v in formula(a)))
    # independent algebraic check of the normalized relation
    for a in [F(1,7),F(2,5),F(1,2),F(4,5)]:
        c2,c3,c4=formula(a)
        assert c3*c3/c2**3==3/(a*(1-a))
        assert c4/c2**2==F(6,5)+F(19,15)*(c3*c3/c2**3)
    print('ALL EXACT TESTS PASSED')

def symbolic_checks():
    """Independently verify the eigenvalue derivatives as polynomial identities."""
    import sympy as s
    x,a=s.symbols('x a')
    b=1-a
    g=x-s.Rational(1,2)
    def transfer(poly):
        return s.expand(a*poly.subs(x,a*x)+b*poly.subs(x,1-b*x))
    def integral(poly):
        return s.integrate(s.expand(poly),(x,0,1))
    c2=a/(12*b)
    c3=-a/(24*b**2)
    c4=a*(19+6*a*b)/(720*b**3)
    H1=s.factor((2*a-1)/(2*b)*(x-s.Rational(1,2)))
    p=(3*a*a-3*a+1)/(3*b*b)
    q=(-6*a*a+5*a-2)/(6*b*b)
    H2=p*(x*x-s.Rational(1,3))+q*(x-s.Rational(1,2))
    u=(4*a**3-6*a*a+4*a-1)/(4*b**3)
    v=(-18*a**3+21*a*a-15*a+4)/(12*b**3)
    w=(24*a**3-12*a*a+18*a-5)/(48*b**3)
    H3=u*(x**3-s.Rational(1,4))+v*(x*x-s.Rational(1,3))+w*(x-s.Rational(1,2))
    def check(z):assert s.cancel(z)==0, s.factor(z)
    for H in [H1,H2,H3]:check(integral(H))
    check(H1-transfer(H1)-transfer(g))
    check(H2-transfer(H2)-transfer(g*g+2*g*H1)+c2)
    check(H3-transfer(H3)-transfer(g**3+3*g*g*H1+3*g*H2)+3*c2*H1+c3)
    check(integral(g*g+2*g*H1)-c2)
    check(integral(g**3+3*g*g*H1+3*g*H2)-c3)
    check(integral(g**4+4*g**3*H1+6*g*g*H2+4*g*H3)-3*c2*c2-c4)
    check(s.factor(c3*c3/c2**3)-3/(a*b))
    check(s.factor(c4/c2**2)-(s.Rational(6,5)+s.Rational(19,15)*(c3*c3/c2**3)))
    print('ALL GENERAL-PARAMETER SYMBOLIC IDENTITIES PASSED')


if __name__=='__main__':
    symbolic_checks()
