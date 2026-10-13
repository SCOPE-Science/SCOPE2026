#!/usr/bin/env python3
from math import isqrt

def divisors(n):
    out=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            out.append(d)
            if d*d!=n:
                out.append(n//d)
    return out

def sigma(n,k):
    if n<=0:
        return 0
    return sum(d**k for d in divisors(n))

def F(n,k2):
    # Coefficient of the normalized parity-twisted Eisenstein-type series F_{2k}.
    return (2**k2*sigma(n//2,k2-1) if n%2==0 else 0)-sigma(n,k2-1)

def h(n):
    return (2*F(n,6)
            -2*(n*n-n+3)*F(n,4)
            +2*(-n**3+4*n*n-3*n+2)*F(n,2))

def is_prime(n):
    if n<2: return False
    if n%2==0: return n==2
    p=3
    while p*p<=n:
        if n%p==0: return False
        p+=2
    return True

N=20000
assert h(4)==-120
assert h(6)==1488
assert h(9)==6144
nearest=None
odd_eq=[]
two_eq=[]
four_eq=[]
for n in range(2,N+1):
    hv=h(n)
    if is_prime(n):
        assert hv==0, (n,hv)
        continue
    if n%2==1:
        assert hv>=6144, (n,hv)
        if hv==6144: odd_eq.append(n)
    elif n%4==2:
        assert hv>=1488, (n,hv)
        if hv==1488: two_eq.append(n)
    else:
        assert hv<=-120, (n,hv)
        if n>4:
            assert hv<=-144, (n,hv)
        if hv==-120: four_eq.append(n)
    pair=(abs(hv),n,hv)
    if nearest is None or pair<nearest:
        nearest=pair
assert odd_eq==[9]
assert two_eq==[6]
assert four_eq==[4]
assert nearest==(120,4,-120)
print(f"VERIFY_OK n_max={N} h4={h(4)} h6={h(6)} h9={h(9)} nearest_composite={nearest[1]}:{nearest[0]} odd_eq={odd_eq[0]} two_eq={two_eq[0]} four_eq={four_eq[0]}")
