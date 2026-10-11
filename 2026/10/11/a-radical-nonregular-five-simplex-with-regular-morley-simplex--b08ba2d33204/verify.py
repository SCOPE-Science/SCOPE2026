from fractions import Fraction as F
from decimal import Decimal, getcontext

# Elements p + q*s + r*d + t*s*d, with s^2=2 and d^2=-39+36*s.
class E:
    def __init__(self,p=0,q=0,r=0,t=0):
        self.v=(F(p),F(q),F(r),F(t))
    def __add__(self,o):
        o=co(o); return E(*(a+b for a,b in zip(self.v,o.v)))
    __radd__=__add__
    def __neg__(self): return E(*(-a for a in self.v))
    def __sub__(self,o): return self+(-co(o))
    def __rsub__(self,o): return co(o)-self
    def __mul__(self,o):
        o=co(o); a=self.v; b=o.v
        # Multiply basis using s^2=2, d^2=-39+36s.
        out=[F(0)]*4
        # basis exponents: 1=(0,0), s=(1,0), d=(0,1), sd=(1,1)
        ex=[(0,0),(1,0),(0,1),(1,1)]
        for i,ai in enumerate(a):
            for j,bj in enumerate(b):
                if not ai or not bj: continue
                se=ex[i][0]+ex[j][0]; de=ex[i][1]+ex[j][1]
                coeff=ai*bj
                if de>=2:
                    de-=2
                    # multiply by -39 + 36s
                    # handle as two terms below
                    for c0,add_s in [(F(-39),0),(F(36),1)]:
                        ss=se+add_s; cc=coeff*c0
                        if ss>=2:
                            ss-=2; cc*=2
                        idx={(0,0):0,(1,0):1,(0,1):2,(1,1):3}[(ss,de)]
                        out[idx]+=cc
                    continue
                if se>=2:
                    se-=2; coeff*=2
                idx={(0,0):0,(1,0):1,(0,1):2,(1,1):3}[(se,de)]
                out[idx]+=coeff
        return E(*out)
    __rmul__=__mul__
    def __truediv__(self,o):
        if isinstance(o,(int,F)): return E(*(x/F(o) for x in self.v))
        raise TypeError
    def __pow__(self,n):
        z=E(1); x=self
        while n:
            if n&1: z=z*x
            x=x*x; n//=2
        return z
    def zero(self): return all(x==0 for x in self.v)
    def __repr__(self): return repr(self.v)
def co(x): return x if isinstance(x,E) else E(x)

s=E(0,1); d=E(0,0,1)
A=2*s-1
C=E(F(-3,2),1,F(1,2),0)
T=(C+2)/8
phi=lambda x:(3*x-x**3)/2

assert (A*A+2*A-7).zero()
assert (A*A-A*C-4*A+C*C+2*C+1).zero()
assert (phi(1)+4*phi(A)+phi(C)).zero()

k1=1-C
k2=1-2*A+C
h1=phi(1)-phi(C)
h2=phi(1)-2*phi(A)+phi(C)
assert (h1-4*T*k1*k1).zero()
assert (h2-4*T*k2*k2).zero()

r=[E(1),A,A,C,A,A]
sigma=sum(r,E(0))
for m in range(4):
    S=sum((r[k]*r[(k-m)%6] for k in range(6)),E(0))
    cm=[E(1),A,A,C][m]
    lhs=4*T*S-F(2,3)*T*sigma*sigma-phi(cm)
    assert lhs.zero(), (m,lhs)

getcontext().prec=60
s2=Decimal(2).sqrt()
d2=(-Decimal(39)+Decimal(36)*s2).sqrt()
a=Decimal(2)*s2-Decimal(1)
c=-Decimal(3)/2+s2+d2/2
t=(c+2)/8
assert Decimal(1)<c<a<Decimal(2)
assert t>0
assert 1-c<0
assert 1-2*a+c<0
print('VERIFY_OK')
print('a',a)
print('c',c)
print('T',t)
