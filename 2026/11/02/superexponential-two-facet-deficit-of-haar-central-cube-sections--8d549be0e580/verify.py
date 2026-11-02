#!/usr/bin/env python3
"""Independent finite checks for the probability asymptotic in RESULT.md.

Run: python3 verify.py. Python standard library only. Random checks are
non-proof diagnostics; the mathematical proof is in RESULT.md.
"""
import itertools
import math
import random
from fractions import Fraction


def x_moments_from_dirichlet(m, kmax=4):
    # Dirichlet(1,...,1): coefficient of t^k in
    # (sum_{j>=0} (2j)!/j! * t^j)^m, times k!/(m)_{2k}.
    poly = [1] + [math.factorial(2*j)//math.factorial(j) for j in range(1, kmax+1)]
    c = [1] + [0]*kmax
    for _ in range(m):
        c = [sum(c[k-j]*poly[j] for j in range(k+1)) for k in range(kmax+1)]
    ans = [Fraction(1)]
    for k in range(1, kmax+1):
        denom = math.prod(m+j for j in range(2*k))
        E_Tk = Fraction(math.factorial(k)*c[k], denom)
        E_R2k = Fraction(math.prod(m+2*j+1 for j in range(k)), 2**k)
        E_Vk = Fraction(m, m+2*k)
        ans.append(E_Tk*E_R2k*E_Vk)
    return ans


def theoretical_x_moments(m):
    return [Fraction(1),
            Fraction(m, m+2),
            Fraction(m*(m+5), (m+2)*(m+4)),
            Fraction(m*(m*m+15*m+74),(m+2)*(m+4)*(m+6)),
            Fraction(m*(m**3+30*m*m+371*m+2118),
                     (m+2)*(m+4)*(m+6)*(m+8))]


def section_facet_count_from_vertices(g):
    d=len(g)
    count=0
    for i in range(d):
        others=[j for j in range(d) if j!=i]
        for fixed in (-1,1):
            vals=[]
            for choices in itertools.product((-1,1),repeat=d-1):
                vals.append(fixed*g[i]+sum(a*g[j] for a,j in zip(choices,others)))
            if min(vals)<0<max(vals):
                count+=1
    return count


def check():
    for m in range(1,31):
        assert x_moments_from_dirichlet(m)==theoretical_x_moments(m)
        a=theoretical_x_moments(m)
        c2=a[2]-2*a[1]+1
        c3=a[3]-3*a[2]+3*a[1]-1
        c4=a[4]-4*a[3]+6*a[2]-4*a[1]+1
        assert c2==Fraction(3*m+8,(m+2)*(m+4))
        assert c3==Fraction(12*(m-4),(m+2)*(m+4)*(m+6))
        assert c4==Fraction(3*(9*m*m+274*m+128),(m+2)*(m+4)*(m+6)*(m+8))
    print('EXACT_MOMENTS_OK: m=1,...,30, orders 1,...,4')
    rng=random.Random(218050)
    for d in range(3,8):
        for _ in range(250):
            g=[rng.gauss(0,1) for _ in range(d)]
            nonzero=sum(abs(x) > sum(abs(y) for j,y in enumerate(g) if i!=j)
                        for i,x in enumerate(g))
            facets=section_facet_count_from_vertices(g)
            assert facets==2*d-2*nonzero
            assert nonzero in (0,1)
    print('GEOMETRY_FACETS_OK: 1250 independent vertex-enumerated sections')
    # An independently normalized size-biased/Dirichlet representation
    # samples the EXACT ratio q_m/B_m, without trying to Monte Carlo
    # the superexponentially rare raw event.
    for m in (1,2,3,40,120):
        count=12000 if m<40 else 6000
        total=0.0
        for _ in range(count):
            r=rng.gammavariate((m+1)/2,2)  # chi-square_{m+1}
            v=rng.random()**(2/m)
            u=[rng.expovariate(1) for _ in range(m)]
            s=sum(u)
            t=sum(z*z for z in u)/(s*s)
            total+=math.exp(-0.5*r*v*t)
        est=total/count
        if m==1: exact_ratio=math.pi/4
        elif m==2: exact_ratio=2*math.asin(1/3)
        elif m==3: exact_ratio=(1/12)*math.pi**1.5*math.gamma(2.5)
        else: exact_ratio=None
        if exact_ratio is not None: assert abs(est-exact_ratio)<0.013
        if m==120: assert abs(est-math.exp(-1)*(1+3.5/m))<0.017
        print(f'MIXTURE_M{m}: ratio={est:.8f} exact_small={exact_ratio} first_order={math.exp(-1)*(1+3.5/m):.8f}')
    print('VERIFY_OK')

if __name__=='__main__':
    check()
