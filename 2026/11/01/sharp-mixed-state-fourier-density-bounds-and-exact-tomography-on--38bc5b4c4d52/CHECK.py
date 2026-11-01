"""Supplementary finite-prime checks for parabolic Fourier-density identities.

Run with Python 3 and its standard library. These checks do not replace the proof
for all odd prime powers or the spectral equality classification.
"""
import cmath
import math
import random


def close(a, b, tol=2e-9):
    if abs(a-b) > tol*max(1, abs(a), abs(b)):
        raise AssertionError((a, b))


def direct_density(A, p):
    root = cmath.exp(2j*math.pi/p)
    return [sum(A[a][b]*root**((x*(a-b)+t*(a*a-b*b))%p)
                for a in range(p) for b in range(p))
            for x in range(p) for t in range(p)]


def theoretical_energy(A, p):
    T = sum(A[a][a].real for a in range(p))
    return T*T+sum(abs(A[a][b])**2 for a in range(p) for b in range(p) if a != b)


def gram_vector(v):
    p=len(v)
    return [[v[a]*v[b].conjugate() for b in range(p)] for a in range(p)]


def add_matrix(A,B):
    return [[A[a][b]+B[a][b] for b in range(len(A))] for a in range(len(A))]


assertions=0
for p in [3,5,7,11,13,17,19]:
    # Distinct ordered off-diagonal pairs give distinct nonzero parabolic differences.
    seen=set()
    for a in range(p):
        for b in range(p):
            if a==b:
                continue
            difference=((a-b)%p,(a*a-b*b)%p)
            assert difference not in seen
            seen.add(difference)
            assertions+=1
    assert len(seen)==p*(p-1)
    assertions+=1

rng=random.Random(20261001)
for p in [3,5,7,11]:
    for case in range(10):
        A=[[0j]*p for _ in range(p)]
        for k in range(1+(case%p)):
            v=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(p)]
            A=add_matrix(A,gram_vector(v))
        vals=direct_density(A,p)
        energy=sum(abs(d)**2 for d in vals)/(p*p)
        exact=theoretical_energy(A,p)
        close(energy,exact)
        assertions+=1
        T=sum(A[a][a].real for a in range(p))
        purity=sum(abs(A[a][b])**2 for a in range(p) for b in range(p))
        diag=sum(A[a][a].real**2 for a in range(p))
        close(exact, T*T+purity-diag)
        close((T*T+purity-T*T/p)-exact,
              sum((A[a][a].real-T/p)**2 for a in range(p)))
        close(exact-T*T, sum(abs(A[a][b])**2 for a in range(p) for b in range(p) if a!=b))
        assert T*T-1e-7<=exact<=T*T+purity-T*T/p+1e-7
        assertions+=4
    for r in range(1,p+1):
        # Coordinate projection attains the minimum for the rank-r spectrum.
        coord=[[complex(1 if a==b and a<r else 0) for b in range(p)] for a in range(p)]
        close(sum(abs(v)**2 for v in direct_density(coord,p))/(p*p),r*r)
        assertions+=1
        # Fourier rank-r projector has constant diagonal and attains the maximum.
        root=cmath.exp(2j*math.pi/p)
        flat=[[sum(root**(k*(a-b)%p) for k in range(r))/p
               for b in range(p)] for a in range(p)]
        close(sum(abs(v)**2 for v in direct_density(flat,p))/(p*p),r*r+r-r*r/p)
        assertions+=1

# Test the complete real Hilbert--Schmidt singular system for small prime orders.
for p in [3,5]:
    basis=[]
    for a in range(p):
        M=[[0j]*p for _ in range(p)]; M[a][a]=1
        basis.append(M)
    for a in range(p):
        for b in range(a+1,p):
            M=[[0j]*p for _ in range(p)]
            M[a][b]=M[b][a]=1/math.sqrt(2)
            basis.append(M)
            N=[[0j]*p for _ in range(p)]
            N[a][b]=1j/math.sqrt(2)
            N[b][a]=-1j/math.sqrt(2)
            basis.append(N)
    images=[direct_density(M,p) for M in basis]
    assert len(images)==p*p
    assertions+=1
    for k,one in enumerate(images):
        for l,two in enumerate(images):
            got=sum(one[j].real*two[j].real for j in range(p*p))/(p*p)
            wanted=(1 if k>=p and k==l else 1 if k<p and l<p else 0)
            close(got,wanted)
            assertions+=1
print('CHECK_OK assertions='+str(assertions))
