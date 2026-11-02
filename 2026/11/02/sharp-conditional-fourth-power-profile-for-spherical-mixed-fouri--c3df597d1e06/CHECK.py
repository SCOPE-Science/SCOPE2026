"""Exact rational checks for a sharp spherical mixed Fourier fourth-moment profile.

Only the Python standard library is required. Finite computations test the
constant-mode interaction and exact arithmetic; the all-degree comparison
is the analytical Bessel-moment theorem cited in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb
from random import Random


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    r = [Q(0)] * max(len(p), len(q))
    for i, x in enumerate(p):
        r[i] += x
    for i, x in enumerate(q):
        r[i] += x
    return trim(r)


def scale(p, a):
    return trim([a * x for x in p])


def mul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return trim(out)


def deriv(p):
    return trim([i*p[i] for i in range(1, len(p))] or [Q(0)])


def integrate_0_2(p):
    return sum((v * Q(2**(i+1), i+1) for i, v in enumerate(p)), Q(0))


def legendre(n):
    p0 = [Q(1)]
    if n == 0:
        return p0
    p1 = [Q(0), Q(1)]
    for j in range(1, n):
        p2 = scale(add(scale([Q(0)]+p1, 2*j+1), scale(p0, -j)), Q(1, j+1))
        p0,p1 = p1,p2
    return p1


def convolution_positive_half(P):
    # On 0<=x<=2: F(x)=integral_{x-1}^1 P(t)P(x-t)dt.
    # Each t^a(x-t)^b is integrated algebraically, with rational coefficients.
    out = [Q(0)]*(2*len(P)+1)
    for a,pa in enumerate(P):
        for b,pb in enumerate(P):
            for h in range(b+1):
                c=pa*pb*comb(b,h)*(-1)**h*Q(1,a+h+1)
                n=a+h+1
                z=b-h
                out[z]+=c
                for j in range(n+1):
                    out[z+j]-=c*comb(n,j)*(-1)**(n-j)
    return trim(out)


def pi_times_moment(i,j,F):
    # Bessel identity: pi*int J_{i+1/2}^2 J_{j+1/2}^2 dr
    # = (-1)^(i+j)/2 * integral_0^2 F_i'(x)F_j'(x)dx.
    return Q((-1)**(i+j),2)*integrate_0_2(mul(deriv(F[i]),deriv(F[j])))


def run():
    tests = 0
    max_degree=14
    F=[convolution_positive_half(legendre(j)) for j in range(max_degree+1)]
    assert F[0] == [Q(2),Q(-1)]; tests+=1
    assert F[1] == [Q(-2,3),Q(1),Q(0),Q(-1,6)]; tests+=1
    mat=[[pi_times_moment(i,j,F) for j in range(max_degree+1)] for i in range(max_degree+1)]
    assert mat[0][0] == 1;tests+=1
    assert mat[1][1] == Q(7,15);tests+=1
    assert mat[2][2] == Q(11,35);tests+=1
    for k in range(max_degree+1):
        assert mat[0][k]==Q(1,2*k+1)
        assert mat[k][0]==mat[0][k]
        tests+=2
    for k in range(2,max_degree+1):
        assert mat[k][k]<mat[1][1]
        tests+=1
    for i in range(max_degree+1):
        for j in range(max_degree+1):
            assert mat[i][j] == mat[j][i]
            assert mat[i][j] >= 0
            assert mat[i][j]**2 <= mat[i][i]*mat[j][j]
            tests+=3
    rng=Random(20261031)
    for _ in range(1800):
        # Rational spectral energies, including exact sparse cases.
        w=[rng.randrange(0,20) for _ in range(max_degree+1)]
        if not any(w):w[0]=1
        norm=sum(w)
        p=[Q(z,norm) for z in w]
        b=sum(p[1:])
        actual=sum(p[i]*p[j]*mat[i][j] for i in range(max_degree+1) for j in range(max_degree+1))
        best=1-Q(4,3)*b+Q(4,5)*b*b
        assert actual<=best
        assert (actual==best) == all(w[j]==0 for j in range(2,max_degree+1))
        tests+=2
    for m in range(101):
        b=Q(m,100)
        # All combinations of constant + degree one attain sharpness.
        actual=(1-b)**2*mat[0][0]+2*(1-b)*b*mat[0][1]+b*b*mat[1][1]
        assert actual==1-Q(4,3)*b+Q(4,5)*b*b
        tests+=1
    print(f'CHECK_OK assertions={tests} degrees=0..{max_degree} exact_rational=True')

if __name__ == '__main__':
    run()
