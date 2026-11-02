"""Independent arithmetic checks for sharp multi-patch Beverton--Holt dispersion ceiling.

Run: python3 VERIFY.py
No external packages required. These tests supplement, not replace, the proof.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from random import Random

getcontext().prec = 65
D = lambda x: Decimal(str(x))

class QS5:
    """Exact a + b sqrt(5) with rational a,b."""
    def __init__(self, a=0, b=0):
        self.a, self.b = Fraction(a), Fraction(b)
    def __add__(self, y):
        y = y if isinstance(y, QS5) else QS5(y)
        return QS5(self.a + y.a, self.b + y.b)
    __radd__ = __add__
    def __neg__(self): return QS5(-self.a, -self.b)
    def __sub__(self, y): return self + (-y if isinstance(y, QS5) else -QS5(y))
    def __rsub__(self, y): return QS5(y) - self
    def __mul__(self, y):
        y = y if isinstance(y, QS5) else QS5(y)
        return QS5(self.a*y.a+5*self.b*y.b, self.a*y.b+self.b*y.a)
    __rmul__ = __mul__
    def __truediv__(self, y):
        y = y if isinstance(y, QS5) else QS5(y)
        det = y.a*y.a-5*y.b*y.b
        assert det
        return self * QS5(y.a/det, -y.b/det)
    def __rtruediv__(self, y): return QS5(y)/self
    def __eq__(self, y):
        y = y if isinstance(y, QS5) else QS5(y)
        return (self.a, self.b) == (y.a, y.b)


def f(x, r, c): return r*x/(1+c*x)


def data(r, c):
    r = tuple(D(z) for z in r)
    c = tuple(D(z) for z in c)
    assert len(r) == len(c) >= 2 and min(r)>1 and min(c)>0
    A = sum((z+1)/q for z,q in zip(r,c))
    B = sum(z.sqrt()/q for z,q in zip(r,c))
    C = sum(1/q for q in c)
    h=A/B
    t=(h-(h*h-4).sqrt())/2
    x=tuple((z.sqrt()/t-1)/q for z,q in zip(r,c))
    K=B/t-C
    return r,c,t,x,K


def envelope(N,r,c):
    """Solve the concave allocation using the marginal-product water-filling rule."""
    lo,hi = D('1e-60'), max(r)
    for _ in range(420):
        mid=(lo+hi)/2
        supply=sum(max(D(0),(z/mid).sqrt()-1)/q for z,q in zip(r,c))
        if supply>N: lo=mid
        else: hi=mid
    lam=(lo+hi)/2
    x=[max(D(0),(z/lam).sqrt()-1)/q for z,q in zip(r,c)]
    return sum(f(y,z,q) for y,z,q in zip(x,r,c))


def checks():
    count=0
    sqrt5=QS5(0,1)
    t=(QS5(3)-sqrt5)/2
    x1=QS5(2)+sqrt5
    x2=(QS5(7)+3*sqrt5)/2
    K=(QS5(11)+5*sqrt5)/2
    assert x1+x2==K
    assert f(x1,QS5(4),QS5(1))+f(x2,QS5(9),QS5(1)) == K
    assert QS5(4)/(1+x1)/(1+x1) == t*t
    assert QS5(9)/(1+x2)/(1+x2) == t*t
    assert x1/K == t
    assert x2/K == (sqrt5-1)/2
    count+=6
    rng=Random(3071)
    for n in range(2,9):
        for _ in range(35):
            r_raw=[rng.randint(11,150)/10 for i in range(n)]
            c_raw=[rng.randint(1,100)/20 for i in range(n)]
            r,c,t,x,K=data(r_raw,c_raw)
            assert all(q>0 for q in x)
            assert abs(sum(x)-K)<D('1e-52')
            assert abs(sum(f(y,z,q) for y,z,q in zip(x,r,c))-K)<D('1e-52')
            assert all(abs(z/(1+q*y)**2-t*t)<D('1e-52') for y,z,q in zip(x,r,c))
            Kiso=sum((z-1)/q for z,q in zip(r,c))
            assert K>=Kiso-D('1e-52')
            if len(set(r))>1: assert K>Kiso+D('1e-35')
            for mult in (D('.5'), D('.95'),D('1'),D('1.07'),D('2')):
                N=K*mult
                h=envelope(N,r,c)
                if mult<1: assert h>N
                elif mult>1: assert h<N
                else: assert abs(h-N)<D('1e-52')
                count+=1
            p=[y/K for y in x]
            N=D('.7')*K
            for _ in range(120):
                N=sum(f(p[i]*N,r[i],c[i]) for i in range(n))
            assert abs(N-K)<D('1e-32')
            count+=6
    return count

if __name__=='__main__':
    print('PASS:',checks(),'independent exact/algebraic and high precision comparisons')
