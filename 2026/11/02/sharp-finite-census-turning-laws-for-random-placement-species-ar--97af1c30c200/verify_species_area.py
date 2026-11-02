"""Independent finite checks for a species-area elasticity theorem.

Run with Python 3.10+ and the standard library only. The exact algebraic
identity and combinatorial boundary checks are exhaustive only over the
printed finite ranges; the theorem for every integer n relies on its proof.
"""
from math import comb, log, sqrt
from itertools import product
from random import Random


def convolution(x, y):
    z = [0] * (len(x) + len(y) - 1)
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            z[i+j] += a * b
    return z


def derivative(poly):
    return [j * poly[j] for j in range(1, len(poly))] or [0]


def sub(x, y):
    z = [0] * max(len(x), len(y))
    for j, a in enumerate(x):
        z[j] += a
    for j, b in enumerate(y):
        z[j] -= b
    while len(z) > 1 and z[-1] == 0:
        z.pop()
    return z


def polynomials(n):
    # z(q)=(1+n q^(n-1))/(1+sum_{j=0}^{n-1}q^j).
    N = [1] + [0] * (n - 2) + [n]
    D = [2] + [1] * (n - 1)
    return N, D


def formula_P(n):
    if n == 2:
        return [3]
    return ([-(j+1) for j in range(n-2)]
            + [(n-1) * (2*n-1)]
            + [n * (n-1-j) for j in range(1,n-1)])


def derivative_sign_expression(n, q):
    # Direct N'D-ND', computed from positive geometric sums.
    U = 1.0
    dU = 0.0
    power = 1.0
    for j in range(1, n):
        dU += j * power
        power *= q
        U += power
    return n*(n-1)*q**(n-2)*(1+U)-(1+n*q**(n-1))*dU


def stationary_area(n):
    lo, hi = 0.0, 1.0  # q in (0,1), P(lo)<0<P(hi)
    assert derivative_sign_expression(n,lo)<0
    assert derivative_sign_expression(n,hi)>0
    for _ in range(90):
        mid = (lo+hi)/2
        if derivative_sign_expression(n,mid)<0:
            lo=mid
        else:
            hi=mid
    return 1-(lo+hi)/2


def richness_poly(counts):
    coeff = [0] * (max(counts)+1)
    for n in counts:
        for k in range(1,n+1):
            coeff[k] += (-1)**(k+1)*comb(n,k)
    return coeff


def run():
    # 1. Exact polynomial coefficient identity.
    count_identity = 0
    for n in range(2, 151):
        N,D=polynomials(n)
        actual=sub(convolution(derivative(N),D),
                   convolution(N,derivative(D)))
        expected=formula_P(n)
        assert actual==expected, (n,actual,expected)
        if n>=3:
            assert expected[0]<0 and all(v<0 for v in expected[:n-2])
            assert all(v>0 for v in expected[n-2:])
        count_identity+=1

    # 2. Exact terminal derivatives for 19,607 abundance vectors.
    boundary_checks=0
    for k in range(1,6):
        for counts in product(range(1,8),repeat=k):
            coeff=richness_poly(counts)
            S=sum(coeff)
            Sp=sum(j*c for j,c in enumerate(coeff))
            Spp=sum(j*(j-1)*c for j,c in enumerate(coeff))
            r1=counts.count(1)
            r2=counts.count(2)
            assert (S,Sp,Spp)==(k,r1,-2*r2)
            derivative_numerator=Sp*S+Spp*S-Sp*Sp
            assert derivative_numerator==r1*(k-r1)-2*k*r2
            boundary_checks+=1

    # 3. Exact 4-individual example and ranges across sizes.
    q3=(-5+2*sqrt(7))/3
    a3=1-q3
    assert abs(3*q3*q3+10*q3-1)<1e-13
    assert abs(stationary_area(3)-a3)<1e-12
    for n in range(3,251):
        a=stationary_area(n)
        assert 0<a<1
        q=1-a
        for x in (q/2, q*0.8, (q+1)/2):
            if x<q:
                assert derivative_sign_expression(n,x)<0
            else:
                assert derivative_sign_expression(n,x)>0

    # 4. Large-abundance location and minimum-height asymptotics.
    asymptotic=[]
    for n in (100,1000,10000):
        a=stationary_area(n)
        q=1-a
        t=n*a
        z=(1+n*q**(n-1))/(1+sum(q**j for j in range(n)))
        target=log(n)+log(log(n))
        asymptotic.append((n,round(t,8),round(t-target,8),
                           round(n*z-target-1,8)))
    assert abs(asymptotic[-1][2])<0.3

    # 5. Finite-community census with <=3 individuals is reducible to
    #    singleton-only, one-species or abundance pair (1,2).
    def partitions(n,minpart=1):
        if n==0:
            yield ()
        for k in range(minpart,n+1):
            for p in partitions(n-k,k):
                yield (k,)+p
    small=set()
    for total in range(1,4):
        for counts in partitions(total):
            small.add(counts)
            assert (all(n==1 for n in counts)
                    or len(counts)==1
                    or counts==(1,2)),counts

    print('PASS exact coefficient identities:',count_identity)
    print('PASS independent terminal-jet identities:',boundary_checks)
    print('PASS root sign and uniqueness consistency for n=3,...,250')
    print('PASS all integer community partitions through total abundance 3:',len(small))
    print('n=3 exact area of sole local minimum:',format(a3,'.14f'))
    print('large-n diagnostics (n, n*a, offset, min-height offset):')
    for row in asymptotic:
        print(' ',row)
    print('Finite checks supplement, not replace, the all-n proof.')


if __name__=='__main__':
    run()
