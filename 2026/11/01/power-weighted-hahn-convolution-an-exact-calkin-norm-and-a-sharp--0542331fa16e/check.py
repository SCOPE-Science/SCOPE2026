"""Finite rational verification of power-Hahn shift conjugacy and compact-defect profile.
Scientific finite checks only; not a substitute for the infinite-dimensional proof.
Run: python check.py
"""
from fractions import Fraction
from math import isclose

checks=0
for alpha in (1, 2, 3, 4):
    for N in (3, 5, 8, 13, 21):
        # Finite y supports. Inverse x_j = sum_{k>=j} y_k/d_k.
        for trial in range(15):
            y=[Fraction(((7*j +3*trial+1) % 13)-6, 7) for j in range(N)]
            d=lambda n:Fraction((n+1)**alpha)
            x=[sum((y[k]/d(k) for k in range(j,N)),Fraction(0)) for j in range(N+1)]
            # Dx=y (including last value zero outside support).
            for j in range(N):
                assert d(j)*(x[j]-x[j+1]) == y[j]
                checks+=1
            # The right shift Sx and the difference D(Sx).
            sx=[Fraction(0)]+x
            z=[d(j)*(sx[j]-sx[j+1]) for j in range(N+1)]
            assert z[0]==-sum((y[j]/d(j) for j in range(N)),Fraction(0))
            checks+=1
            for j in range(1,N+1):
                assert z[j]==d(j)/d(j-1)*y[j-1]
                checks+=1
            # For arbitrary powers, D S^k D^-1 formula.
            for k in (1,2,3):
                ssx=[Fraction(0)]*k+x
                zz=[d(j)*(ssx[j]-ssx[j+1]) for j in range(N+k)]
                for j in range(N+k):
                    goal=(-d(k-1)*x[0] if j==k-1 else d(j)/d(j-k)*y[j-k] if k<=j<k+N else Fraction(0))
                    assert zz[j]==goal,(alpha,N,trial,k,j,zz[j],goal)
                    checks+=1

# The exact norm of V_alpha-U is 2**alpha. Each column has
# absolute sum (j+1)^-alpha + ((j+2)/(j+1))^alpha - 1.
for alpha in (1,2,3,4):
    vals=[Fraction(1,(j+1)**alpha) + Fraction((j+2)**alpha,(j+1)**alpha)-1 for j in range(200)]
    assert vals[0]==2**alpha
    assert all(vals[j]>vals[j+1]>0 for j in range(len(vals)-1))
    checks+=len(vals)

for alpha in (0.25,0.5,1,1.7,2,3,5):
    for n in (1000,5000,10000,50000):
        delta=(1+1/n)**alpha-1
        assert abs(n*delta/alpha-1)<0.02
        checks+=1

print(f'{checks} finite exact-rational and numerical checks passed')
