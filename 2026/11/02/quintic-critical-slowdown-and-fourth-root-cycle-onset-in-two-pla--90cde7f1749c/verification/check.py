#!/usr/bin/env python3
"""Exact fifth-order Taylor certificate and high-precision orbit checks.

Requires only the Python 3 standard library.  Coordinates and definitions
are described in RESULT.md.  Run: python verification/check.py
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext

class Quad:
    """Exact rational numbers adjoined with a square root of two."""
    def __init__(self, a=0, b=0):
        if isinstance(a, Quad): self.a, self.b = a.a, a.b
        else: self.a, self.b = Q(a), Q(b)
    def __add__(self, other):
        o=Quad(other); return Quad(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Quad(-self.a,-self.b)
    def __sub__(self,other): return self+(-Quad(other))
    def __rsub__(self,other): return Quad(other)-self
    def __mul__(self,other):
        o=Quad(other)
        return Quad(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,other):
        o=Quad(other); den=o.a*o.a-2*o.b*o.b
        assert den!=0
        return self*Quad(o.a/den,-o.b/den)
    def __rtruediv__(self,other): return Quad(other)/self
    def __eq__(self,other):
        o=Quad(other); return self.a==o.a and self.b==o.b
    def __repr__(self): return f'({self.a})+({self.b})*sqrt(2)'

Z=Quad(0); ONE=Quad(1); RT2=Quad(0,1)
N=6

def add(a,b): return [a[i]+b[i] for i in range(N)]
def mul(a,b):
    return [sum((a[j]*b[i-j] for j in range(i+1)),Z) for i in range(N)]
def series_sqrt1(v):
    assert v[0]==Z
    acc=[Z for _ in range(N)]; power=[ONE]+[Z]*(N-1)
    b=Q(1)
    for k in range(N):
        for j in range(N):acc[j]=acc[j]+b*power[j]
        power=mul(power,v)
        b=b*(Q(1,2)-k)/(k+1)
    return acc

def taylor():
    # At c*=3-2sqrt(2), t=sqrt(y*)=(2+sqrt(2))/4,
    # x*=1/8=t-t*t, and sqrt(x*/c*)=t.
    c=Quad(3,-2); t=Quad(Q(1,2),Q(1,4)); y0=t*t; x0=Quad(Q(1,8))
    assert t-y0==x0 and t*t*c==x0
    v=[Z, ONE/y0]+[Z]*(N-2)
    s_y=series_sqrt1(v)
    dx=[Z]+[t*s_y[j]-(ONE if j==1 else Z) for j in range(1,N)]
    s_x=series_sqrt1([u/x0 for u in dx])
    # F(y0+z)-y0=t*(sqrt(1+dx/x0)-1)-dx.
    f=[Z]+[t*(s_x[i])-dx[i] for i in range(1,N)]
    powers=[[ONE]+[Z]*(N-1)]
    for k in range(1,N):powers.append(mul(powers[-1],f))
    f2=[sum((f[j]*powers[j][i] for j in range(1,N)),Z) for i in range(N)]
    return f,f2

def main():
    f,f2=taylor()
    expected=[Z,Quad(-1),Quad(4,-4),Quad(-48,32),Quad(16,-16),Quad(33472,-23680)]
    assert f==expected,(f,expected)
    K=Quad(50688,-35840)
    assert f2==[Z,ONE,Z,Z,Z,-K], f2
    assert ONE/K==Quad(Q(99,512),Q(70,512))
    cstar=Quad(3,-2)
    # Derivative of lambda(c)=-(c-1)^2/(4c).
    lam=-(cstar-ONE)*(cstar-ONE)/(4*cstar)
    lamprime=(ONE/(cstar*cstar)-ONE)/4
    alpha=2*lamprime
    assert lam==Quad(-1)
    assert lamprime==Quad(4,3)
    assert alpha==Quad(8,6)
    assert alpha/K==Quad(Q(816,256),Q(577,256))
    print('EXACT_TAYLOR_OK; F^2(y*+z)-y*=z-K*z^5+O(z^6)')
    print('K =', K, 'alpha =', alpha, 'A^4 =',alpha/K)
    with localcontext() as dc:
        dc.prec=70
        two=Decimal(2); root=two.sqrt()
        cc=Decimal(3)-two*root
        Kd=Decimal(50688)-Decimal(35840)*root
        alphad=Decimal(8)+Decimal(6)*root
        amp=(alphad/Kd).sqrt().sqrt()
        def ff(c,y):
            assert Decimal(0)<y<Decimal(1),('outside positive-response domain',y)
            x=y.sqrt()-y
            return (x/c).sqrt()-x
        for ds in ['1e-7','1e-9','1e-11']:
            d=Decimal(ds); c=cc-d
            ystar=Decimal(1)/(Decimal(1)+c)**2
            p=amp*d.sqrt().sqrt()
            def H(z): return (ff(c,ff(c,ystar+z))-ystar-z)/z
            def bisect(a,b):
                fa=H(a);fb=H(b)
                assert fa*fb<0,('no bracket',ds,a,b,fa,fb)
                for _ in range(250):
                    m=(a+b)/2; fm=H(m)
                    if fa*fm<=0:b=m
                    else:a=m;fa=fm
                return (a+b)/2
            zn=bisect(-p*Decimal('1.2'),-p*Decimal('0.8'))
            zp=bisect(p*Decimal('0.8'),p*Decimal('1.2'))
            assert abs(ff(c,ystar+zn)-(ystar+zp))<Decimal('1e-55')
            assert abs(ff(c,ystar+zp)-(ystar+zn))<Decimal('1e-55')
            assert abs(zn/p+1)<Decimal('0.03') and abs(zp/p-1)<Decimal('0.03')
            print('BRANCH_OK delta=',ds,'lower_ratio=',format(zn/p,'.12f'),'upper_ratio=',format(zp/p,'.12f'))
    print('ALL_CHECKS_PASS')
if __name__=='__main__':main()
