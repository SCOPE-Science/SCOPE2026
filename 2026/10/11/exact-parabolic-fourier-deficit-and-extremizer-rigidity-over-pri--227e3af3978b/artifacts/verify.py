"""Exact arithmetic consistency tests for parabolic fourth-moment fibers over Z/(p^2)."""
from collections import defaultdict
from itertools import product
from math import isclose, pi
from cmath import exp


def energy(f, p):
    q = p * p
    sums = defaultdict(complex)
    for x in range(q):
        for y in range(q):
            sums[((x+y)%q, (x*x+y*y)%q)] += f[x]*f[y]
    return sum(z.real*z.real + z.imag*z.imag for z in sums.values())


def direct_formula(f, p):
    sections = [[f[r+p*a] for a in range(p)] for r in range(p)]
    masses = [sum(abs(z)**2 for z in fs) for fs in sections]
    within = []
    for fs in sections:
        by_sum = [sum(fs[a]*fs[(s-a)%p] for a in range(p)) for s in range(p)]
        within.append(sum(abs(z)**2 for z in by_sum))
    cross = sum(masses[r]*masses[s] for r in range(p) for s in range(r+1,p))
    e = sum(within)+4*cross
    deficit = p*sum(masses)**2-e
    split = 2*(p-2)*cross+sum(p*m*m-w for m,w in zip(masses,within))
    assert isclose(deficit,split,rel_tol=1e-11,abs_tol=1e-8)
    return e,deficit,masses


def synth_moment(f, p):
    q=p*p
    roots=[exp(2j*pi*j/q) for j in range(q)]
    total=0.0
    for u in range(q):
        for v in range(q):
            z=sum(f[t]*roots[(u*t+v*t*t)%q] for t in range(q))
            total+=abs(z)**4
    return total/(q*q)


def trial():
    samples = 0
    for p in (3,5,7):
        q=p*p
        for seed in range(8):
            f=[complex(((3*t+7*seed+5*t*t)%11)-5, ((t*t+2*t*seed+6)%9)-4) for t in range(q)]
            a=energy(f,p)
            b,deficit,masses=direct_formula(f,p)
            assert isclose(a,b,rel_tol=1e-11,abs_tol=1e-7), (p,seed,a,b)
            assert deficit >= -1e-7
            norm2=sum(abs(z)**2 for z in f)
            projmax=0.0
            for r in range(p):
                fs=[f[r+p*a] for a in range(p)]
                for k in range(p):
                    coeff=sum(fs[a]*exp(-2j*pi*k*a/p) for a in range(p))
                    projmax=max(projmax, abs(coeff)**2/(p*norm2))
            dist2=1.0-projmax
            nd=deficit/(norm2*norm2)
            assert dist2 <= (p-1)/(p-2)*nd + 1e-8
            if p <=5 and seed in (0,2):
                direct=synth_moment(f,p)
                assert isclose(direct,a,rel_tol=2e-11,abs_tol=1e-5), (p,seed,direct,a)
            samples+=1
        for r,k in product(range(p),range(p)):
            f=[0j]*q
            for a in range(p):
                f[r+p*a]=exp(2j*pi*k*a/p)
            a=energy(f,p)
            b,deficit,_=direct_formula(f,p)
            assert isclose(a,p**3,rel_tol=1e-11,abs_tol=1e-7)
            assert isclose(b,p**3,rel_tol=1e-11,abs_tol=1e-7)
            assert abs(deficit)<1e-7
            samples+=1
        f=[0j]*q
        f[0]=f[p]=f[2*p]=1+0j
        _,deficit,_=direct_formula(f,p)
        assert deficit >= -1e-7
    print(f'VERIFY_OK cases={samples} primes=3 direct_fourier=4 exact_fiber_deficit_and_packet_tests=passed')

if __name__=='__main__':
    trial()
