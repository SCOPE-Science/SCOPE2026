from fractions import Fraction
import math

pi_lo = Fraction(157, 50)
pi_hi = Fraction(22, 7)
assert pi_lo * pi_lo > Fraction(128, 13)

F4 = Fraction(1807104, 2941225)
assert F4 > Fraction(39, 64)
assert Fraction(6, 1) / Fraction(128, 13) == Fraction(39, 64)

cs = [Fraction(2,3),Fraction(73,108),Fraction(13,18),Fraction(949,1296),Fraction(3,4),Fraction(13,16),Fraction(8,9),Fraction(73,81)]
assert all(cs[i] < cs[i+1] for i in range(len(cs)-1))
ratios=[cs[i]/cs[i+1] for i in range(len(cs)-1)]
assert min(ratios)==Fraction(117,128)
assert Fraction(9,1)/Fraction(128,13)==Fraction(117,128)
assert Fraction(73,81) < Fraction(9,1)/(pi_hi*pi_hi)

def factor(n):
    out=[]; d=2
    while d*d<=n:
        if n%d==0:
            a=0
            while n%d==0:
                n//=d; a+=1
            out.append((d,a))
        d += 1 if d==2 else 2
    if n>1: out.append((n,1))
    return out

def local(p,a):
    x=Fraction(1,p*p); s=Fraction(0,1); term=Fraction(1,1)
    for j in range(a+1):
        s += term
        term *= -x
    return s

def sval(n):
    v=Fraction(1,1)
    for p,a in factor(n): v*=local(p,a)
    return v

lo=Fraction(73,81); hi=9/(math.pi**2); mx=0.0; mn=2.0
for n in range(1,200001):
    v=sval(n); f=float(v)
    assert not (v>lo and f<hi)
    if f<=float(lo): mx=max(mx,f)
    if f>=hi: mn=min(mn,f)
print('VERIFY_OK F4=%s min_ratio=%s sample_max_lower=%.12f sample_min_upper=%.12f'%(F4,min(ratios),mx,mn))
