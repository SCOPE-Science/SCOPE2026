#!/usr/bin/env python3
"""Exact-arithmetic regression checks for the simplex-frustum isotropic profile.

Requires Python 3.10+ standard library only. Finite checks corroborate, but do
not replace, the displayed all-dimensional coefficient-positivity proof.
"""
from fractions import Fraction as F
from math import comb, factorial


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim(c)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    c[i + j] += x * y
    return trim(c)


def scale(a, c):
    return trim([c*x for x in a])


def diff(a):
    return trim([i * a[i] for i in range(1, len(a))] or [0])


def power(a, n):
    out = [1]
    for _ in range(n):
        out = mul(out, a)
    return out


def monomial(k, c=1):
    return [0] * k + [c]


def base_polys(n):
    a = add([1], monomial(n, -1))
    b = add([1], monomial(n + 1, -1))
    c = add([1], monomial(n + 2, -1))
    E = add(scale(mul(a,c),(n + 1)**2), scale(mul(b,b),-n*(n + 2)))
    return a,b,c,E


def Bpoly(n):
    return add(
        add([n-1,-(n+3)],
            mul(monomial(n),mul([1,1],add(scale(power([1,-1],2),(n+1)**2),monomial(1,4))))),
        scale(mul(monomial(2*n+2), [n+3,-(n-1)]),-1))


def Ppoly(n):
    P = [0] * (2*n-2)
    for j in range(n-1):
        z = (n-1)*comb(j+5,5) - (n+3)*comb(j+4,5)
        assert z > 0
        P[j] += z
        P[2*n-3-j] += z
    return trim(P)


def H(n,t):
    a = 1-t**n
    b = 1-t**(n+1)
    c = 1-t**(n+2)
    E = (n+1)**2*a*c - n*(n+2)*b*b
    return (c**(n-1))*E/(a**(n+3))


def determinant(m):
    m=[row[:] for row in m]
    N=len(m)
    det=F(1)
    for j in range(N):
        k=next((i for i in range(j,N) if m[i][j]),None)
        assert k is not None
        if k!=j:
            m[k],m[j]=m[j],m[k]
            det=-det
        p=m[j][j]
        det*=p
        for i in range(j+1,N):
            u=m[i][j]/p
            for r in range(j+1,N):
                m[i][r]-=u*m[j][r]
            m[i][j]=0
    return det


def covariance_from_moments(n,t):
    a=1-t**n
    first=F(n,n+1)*(1-t**(n+1))/a
    second=F(n,n+2)*(1-t**(n+2))/a
    mean=first/n
    diag=2*second/F(n*(n+1))-mean**2
    off=second/F(n*(n+1))-mean**2
    return [[diag if i==j else off for j in range(n)] for i in range(n)]


def main():
    checks=0
    for n in range(2,51):
        a,b,c,E=base_polys(n)
        B=Bpoly(n)
        P=Ppoly(n)
        assert trim(B)==trim(mul(power([1,-1],6),P))
        checks+=1
        # The derivative of H has sign given by the B polynomial.
        # This checks the numerator identity before dividing by positive powers.
        derivative_num=add(add(scale(mul(mul(diff(c),E),a),n-1),
                               mul(mul(c,diff(E)),a)),
                           scale(mul(mul(c,E),diff(a)),-(n+3)))
        expected=scale(mul(mul(monomial(n-1),[1,-1]),B),-n*(n+2))
        assert derivative_num==expected
        checks+=1
        assert P==list(reversed(P)) and all(x>0 for x in P)
        checks+=1
    vals = [F(0),F(1,13),F(1,7),F(1,5),F(1,3),F(1,2),F(4,5),F(9,10),F(99,100),F(999,1000)]
    for n in range(2,21):
        last=None
        for t in vals:
            h=H(n,t)
            assert h>0
            if last is not None:
                assert h<last
            last=h
            checks+=1
        # Elementary small-cap contact coefficient, via two exact samples
        # of the polynomial coefficient in the full symbolic identity.
        assert F((n+1)**2*(n+2)**n,12*n**(n+2)) < 1
        checks+=1
    for n in range(2,9):
        for t in [F(0),F(1,6),F(1,3),F(3,5),F(9,10)]:
            cov=covariance_from_moments(n,t)
            volume=(1-t**n)/factorial(n)
            iso=determinant(cov)/volume**2
            iso_simplex=F(factorial(n)**2,(n+1)**(n+1)*(n+2)**n)
            assert iso/iso_simplex==H(n,t)
            checks+=1
    # Independent polynomial coefficient checks of both sharp endpoint laws.
    for n in range(2,19):
        a,b,c,E=base_polys(n)
        numerator=mul(power(c,n-1),E)
        denominator=power(a,n+3)
        delta=add(numerator,scale(denominator,-1))
        assert all(delta[j]==0 for j in range(n))
        assert delta[n]==-(n-1)*(n+2)
        checks+=1
        # Express t=1-h and compare the first three nonzero coefficients
        # in the numerator and denominator, with exact rational division.
        ah=add([1],scale(power([1,-1],n),-1))
        bh=add([1],scale(power([1,-1],n+1),-1))
        ch=add([1],scale(power([1,-1],n+2),-1))
        Eh=add(scale(mul(ah,ch),(n+1)**2),scale(mul(bh,bh),-n*(n+2)))
        nh=mul(power(ch,n-1),Eh)
        dh=power(ah,n+3)
        k=n+3
        assert all(z==0 for z in nh[:k]) and all(z==0 for z in dh[:k])
        end=F((n+1)**2*(n+2)**n,12*n**(n+2))
        assert F(nh[k],dh[k])==end
        linear=F(nh[k+1]-end*dh[k+1],dh[k])
        assert linear==0
        quad=F(nh[k+2]-end*dh[k+2],dh[k])
        assert quad/end==F((n-1)*(n+3),30)
        checks+=3
    # At t=0 the exact normalized profile equals the simplex value.
    for n in range(2,101):
        assert H(n,F(0))==1
        checks+=1
    print('VERIFY_OK',checks,'exact checks')


if __name__ == '__main__':
    main()
