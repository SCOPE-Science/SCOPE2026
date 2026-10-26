"""Reproducibility checks for the LCM-top indicator spectral theorem.
Standard library only; finite tests support, but do not replace, the proof.
"""
from math import prod, gcd, isqrt
from decimal import Decimal, getcontext
from collections import Counter
from itertools import product


def prime_powers(n):
    m=n
    out=[]
    p=2
    while p*p<=m:
        if m%p==0:
            a=0
            while m%p==0:
                a+=1;m//=p
            out.append((p,a))
        p=3 if p==2 else p+2
    if m>1:out.append((m,1))
    return out


def divisors(n):
    d=[1]
    for p,a in prime_powers(n):
        d=[v*p**k for v in d for k in range(a+1)]
    return sorted(d)


def lcm_matrix(n):
    ds=divisors(n)
    return [[int(i*j//gcd(i,j)==n) for j in ds] for i in ds]


def mult(X,Y):
    n=len(X)
    Z=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if X[i][k]:
                for j in range(n):Z[i][j]+=X[i][k]*Y[k][j]
    return Z


def matrix_traces(A):
    n=len(A)
    Y=[[int(i==j) for j in range(n)] for i in range(n)]
    out=[]
    for k in range(1,n+1):
        Y=mult(Y,A)
        out.append(sum(Y[i][i] for i in range(n)))
    return out


def local_power_sums(a,limit):
    s=[2,1]
    for k in range(2,limit+1): s.append(s[-1]+a*s[-2])
    return s


def char_from_traces(T):
    coeff=[1]
    for k in range(1,len(T)+1):
        num=-sum(coeff[k-j]*T[j-1] for j in range(1,k+1))
        assert num%k==0
        coeff.append(num//k)
    return coeff


def spectrum_inversion(exponents):
    # Exact theorem uses real eigenvalues. This finite check uses 100-digit
    # decimal approximations and compares reconstructed integer exponents.
    getcontext().prec=100
    sq=[(Decimal(4*a+1)).sqrt() for a in exponents]
    q=[(z-1)/(z+1) for z in sq]
    products=[Decimal(1)]
    for qi in q: products=products+[v*qi for v in products]
    # Recursively peel off the largest nontrivial factor.
    def recover(vs):
        if len(vs)==1:return []
        vs=sorted(vs,reverse=True)
        qi=vs[1]
        leftover=vs[:]
        without=[]
        while leftover:
            v=leftover.pop(0)
            without.append(v)
            target=v*qi
            best=min(range(len(leftover)),key=lambda j:abs(leftover[j]-target))
            assert abs(leftover[best]-target)<Decimal('1e-60')
            leftover.pop(best)
        return [qi]+recover(without)
    found=recover(products)
    recovered=sorted(int((z/(1-z)**2).to_integral_value()) for z in found)
    assert recovered==sorted(exponents),(recovered,exponents)
    return recovered


def run():
    nums=[1,2,4,6,8,12,18,24,36,40,72,96,108,125,240,500]
    for n in nums:
        A=lcm_matrix(n)
        ds=divisors(n)
        assert len(A)==len(ds)
        t=matrix_traces(A)
        exponents=[a for p,a in prime_powers(n)]
        for j,val in enumerate(t,1):
            pred=prod(local_power_sums(a,len(ds))[j] for a in exponents)
            assert val==pred,(n,j,val,pred)
        cp=char_from_traces(t)
        assert cp[0]==1
        assert (cp[-1]==0)==(len(ds)>2**len(exponents))
        spectrum_inversion(exponents)
    # Verify same exponent multiset yields exactly equal characteristic polynomials:
    assert char_from_traces(matrix_traces(lcm_matrix(72)))==char_from_traces(matrix_traces(lcm_matrix(500)))
    assert char_from_traces(matrix_traces(lcm_matrix(12)))==char_from_traces(matrix_traces(lcm_matrix(18)))
    # Same size and same rank need not imply the same spectrum:
    assert len(divisors(72))==len(divisors(96))==12
    assert char_from_traces(matrix_traces(lcm_matrix(72)))!=char_from_traces(matrix_traces(lcm_matrix(96)))
    # Unique reconstruction despite repeated prime exponents and equal subset products:
    for xx in [(1,1,1),(2,2,2),(1,2,4),(2,3,3,5),(1,1,1,2,2)]:
        spectrum_inversion(xx)
    print('VERIFY_OK: exact integer trace/characteristic certificates for 16 divisor lattices; 2 cospectral pairs; five repeated-factor reconstruction cases')

if __name__=='__main__':run()
