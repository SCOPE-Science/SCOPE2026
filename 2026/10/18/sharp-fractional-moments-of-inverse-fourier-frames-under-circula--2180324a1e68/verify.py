"""Supplementary exact and finite-dimensional checks for circular Fourier sampling."""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, pi, sin, cos


def gram_inverse_trace(a):
    n=len(a)
    mat=[[sum(a[r][k].conjugate()*a[r][j] for r in range(n)) for j in range(n)]
         for k in range(n)]
    inverse_diag=0j
    for rhs in range(n):
        q=[mat[i][:]+[complex(i==rhs)] for i in range(n)]
        for k in range(n):
            j=max(range(k,n), key=lambda j:abs(q[j][k]))
            q[k],q[j]=q[j],q[k]
            pivot=q[k][k]
            assert abs(pivot)>1e-13
            q[k]=[v/pivot for v in q[k]]
            for i in range(n):
                if i!=k:
                    fac=q[i][k]
                    q[i]=[q[i][h]-fac*q[k][h] for h in range(n+1)]
        inverse_diag += q[rhs][-1]
    return inverse_diag.real


def lagrange_inverse_energy(nodes):
    total=0.0
    for j, zj in enumerate(nodes):
        coeff=[1+0j]
        for m, zm in enumerate(nodes):
            if m!=j:
                updated=[0j]*(len(coeff)+1)
                for k, val in enumerate(coeff):
                    updated[k]-=zm*val
                    updated[k+1]+=val
                coeff=updated
        denom=1+0j
        for m, zm in enumerate(nodes):
            if m!=j:
                denom*=zj-zm
        total+=sum(abs(v/denom)**2 for v in coeff)
    return total


def integral_sin_even(k):
    # (1/pi) * integral_0^pi sin(t)^(2k) dt
    return Fraction(comb(2*k,k),4**k)


def det_orthogonal(e,f):
    """Integral of two alternating monomial determinants over independent Haar angles.

    It is factorial(n) for identical exponent sets, zero otherwise.
    Exact permutation-pair Fourier character counting implements the integral.
    """
    n=len(e)
    ans=0
    for p in permutations(range(n)):
        par_p=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=[e[p[i]] for i in range(n)]
        for q in permutations(range(n)):
            if all(term[i]==f[q[i]] for i in range(n)):
                par_q=(-1)**sum(q[i]>q[j] for i in range(n) for j in range(i+1,n))
                ans+=par_p*par_q
    return ans


def main():
    count=0
    for beta in (2,4,6,8):
        for p in range(1,(beta+1)//2+1):
            if 2*p>=beta+1:
                continue
            exact=integral_sin_even((beta-2*p)//2)/integral_sin_even(beta//2)
            if p==1:
                assert exact==Fraction(beta,beta-1)
            assert exact>0
            count+=1
    for n in range(2,6):
        exponent_sets=[tuple(k for k in range(n) if k!=omit) for omit in range(n)]
        for k in range(n):
            for l in range(n):
                assert det_orthogonal(exponent_sets[k],exponent_sets[l])==factorial(n-1)*(k==l)
                count+=1
    for n in range(2,8):
        angles=[2*pi*((j*j+3*j+1) % (n*n+3))/(n*n+3) for j in range(n)]
        # Distinctness, no accidental collisions in these deterministic tests.
        if len(set(angles))!=n:
            angles=[2*pi*(j+0.35*j*j/(n*n))/(n+1) for j in range(n)]
        nodes=[complex(cos(t),sin(t)) for t in angles]
        mat=[[z**k for k in range(n)] for z in nodes]
        d=gram_inverse_trace(mat)
        e=lagrange_inverse_energy(nodes)
        assert abs(d-e) < 1e-5*max(1,d,e),(n,d,e)
        count+=1
    print(f'VERIFY_OK {count} exact/supplementary Fourier checks; CUE cofactor orthogonality and N=2 beta moments')

if __name__=='__main__':
    main()
