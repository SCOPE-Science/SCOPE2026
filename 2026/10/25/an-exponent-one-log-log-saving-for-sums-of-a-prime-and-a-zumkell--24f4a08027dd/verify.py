"""Independent finite arithmetic checks for the stated prime-block and CRT identities.
These checks complement, but do not replace, the asymptotic proof.
"""
from fractions import Fraction
from math import gcd


def primes_upto(n):
    a=bytearray(b'\x01')*(n+1)
    a[:2]=b'\x00\x00'
    for p in range(2,int(n**.5)+1):
        if a[p]: a[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [p for p in range(n+1) if a[p]]

P=primes_upto(3_000_000)
reports=[]
for k in [3,6,11,21,51,101]:
    start=P[k-1]
    b=Fraction(1)
    c=Fraction(1)
    end=None
    for p in P[k-1:]:
        pre=b
        b*=Fraction(p+1,p)
        c*=Fraction(p*p-1,p*p)
        if b>=2:
            end=p
            assert pre<2<=b<2*Fraction(p+1,p)
            r=c/b
            assert 0<r<Fraction(1,2)
            assert abs(float(r)-.5) < 2/start # crude test
            reports.append((start,end,float(r),float(b)))
            break
    assert end is not None
# Periodic CRT exact residue-product check for arbitrary coprime odd moduli
for zs in [(15,77),(35,99),(13,25),(15,77,221)]:
    assert all(gcd(a,b)==1 for i,a in enumerate(zs) for b in zs[i+1:])
    def phi(n):
        return sum(gcd(a,n)==1 for a in range(n))
    Z=1
    for z in zs: Z*=z
    theoretical=1
    for z in zs: theoretical*=z-phi(z)
    actual=sum(1 for k in range(Z) if all(gcd(k,z)>1 for z in zs))
    assert theoretical==actual,(zs,theoretical,actual)
for z in [6,20,28,945]:
    phi=sum(gcd(a,z)==1 for a in range(z))
    sigma=sum(d for d in range(1,z+1) if z%d==0)
    assert sigma%2==0 and phi*2<z
    assert phi*sigma<z*z
print('VERIFY_OK',len(reports),'prime blocks, 4 CRT configurations, 4 Zumkeller totient inequalities')
print('BLOCKS',reports)
