"""Reproducibility checks for triple Bargmann phases of quadratic prime-field MUBs.

Only standard Python is needed. Finite computations test cases, not the proof
for every odd prime.
"""
import cmath
import itertools
import math
from collections import Counter


def chi(t, p):
    t %= p
    if t == 0:
        return 0
    return 1 if pow(t, (p-1)//2, p) == 1 else -1


def epsilon(p):
    return 1 if p % 4 == 1 else 1j


def dot(v, w):
    return sum(x.conjugate()*y for x,y in zip(v,w))


def basis_vector(p, a, b):
    if a == p: # index for the computational basis
        return [1.+0j if x == b else 0j for x in range(p)]
    zeta = cmath.exp(2j*math.pi/p)
    return [zeta**((a*x*x+b*x)%p)/math.sqrt(p) for x in range(p)]


def predict_phase(p, a, b, c, i, j, k):
    eps = epsilon(p)
    if a == p or b == p or c == p:
        # rotate bases/labels cyclically to put infinity first
        while a != p:
            a,b,c=b,c,a
            i,j,k=j,k,i
        A = (c-b)%p
        s = (i + (k-j)*pow(2*A, -1, p))%p
        z = (-A*s*s)%p
        return (eps*chi(A,p),z) if s==0 else (eps**3*chi(z,p)*cmath.exp(2j*math.pi*z/p),z)
    A=(b-a)%p
    B=(c-b)%p
    K=(A*B*(A+B))%p
    t=(B*(j-i)-A*(k-j))%p
    z=(-t*t*pow(4*K,-1,p))%p
    return (eps*chi(K,p),0) if t==0 else (eps**3*chi(z,p)*cmath.exp(2j*math.pi*z/p),z)


def key_from_phase(p, w):
    eps=epsilon(p)
    if abs(w-eps)<1e-7: return 'plus_eps'
    if abs(w+eps)<1e-7: return 'minus_eps'
    for z in range(1,p):
        v=eps**3*chi(z,p)*cmath.exp(2j*math.pi*z/p)
        if abs(w-v)<1e-7: return z
    raise AssertionError(('unknown phase',p,w))


def check(p):
    assert p>=3 and p%2==1 and all(p%d for d in range(3,math.isqrt(p)+1,2))
    vec={(a,i):basis_vector(p,a,i) for a in range(p+1) for i in range(p)}
    ip={(a,i,b,j):dot(vec[(a,i)],vec[(b,j)])
        for a in range(p+1) for b in range(p+1) if a!=b
        for i in range(p) for j in range(p)}
    counts=Counter()
    zero_det=0
    compared=0
    for a,b,c in itertools.permutations(range(p+1),3):
        for i,j,k in itertools.product(range(p),repeat=3):
            w=p**1.5*ip[(a,i,b,j)]*ip[(b,j,c,k)]*ip[(c,k,a,i)]
            expected,z=predict_phase(p,a,b,c,i,j,k)
            if abs(w-expected)>5e-8:
                raise AssertionError(('Gauss formula mismatch',p,(a,b,c,i,j,k),w,expected))
            tag=key_from_phase(p,w)
            counts[tag]+=1
            determinant=1-3/p+2*(w.real)/(p**1.5)
            if p==3 and abs(determinant)<1e-8:
                zero_det+=1
            if p>=5 and determinant<=(1-2/math.sqrt(p))**3-1e-7:
                # Gershgorin gives positive smallest eigenvalue, not a determinant cube bound;
                # this conservative determinant check is not used as a proof.
                pass
            compared+=1
    basetriples=(p+1)*p*(p-1)
    assert counts['plus_eps']==counts['minus_eps']==basetriples*p*p//2
    for z in range(1,p):
        assert counts[z]==basetriples*p*p, (p,z,counts[z])
    assert compared==basetriples*p**3
    if p==3:
        assert zero_det==basetriples*p*p==216
        assert zero_det//6==36
    print('CHECK_OK', 'p',p,'ordered_triples',compared,
          'phase_values',p+1,'each_nonzero',basetriples*p*p,
          'each_zero_sign',basetriples*p*p//2,'dependent',zero_det)


if __name__=='__main__':
    for p in (3,5,7):
        check(p)
    print('VERIFY_OK')
