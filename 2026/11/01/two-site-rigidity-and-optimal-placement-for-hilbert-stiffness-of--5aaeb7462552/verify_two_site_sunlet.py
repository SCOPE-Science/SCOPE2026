"""Diagnostic checks for two-site strengthening of the cycle sunlet p=1 Gram gap.

Universal mathematical statements are established in the accompanying proof.
Requires Python 3.10+ and NumPy.
"""
import math
from fractions import Fraction
import numpy as np


def distance(n, arms):
    assert len(arms) == n
    D = np.zeros((2*n, 2*n), dtype=float)
    for a in range(2*n):
        for b in range(2*n):
            i, j = a % n, b % n
            v = min((i-j)%n, (j-i)%n)
            if a >= n: v += arms[i]
            if b >= n: v += arms[j]
            if a == b: v = 0.
            D[a,b] = v
    return D


def spectrum(D):
    n = len(D)
    J = np.eye(n) - np.ones((n,n))/n
    return np.linalg.eigvalsh(-.5*J@D@J)


def baseline(n, t):
    if n % 2 == 0: return 0., 0.
    a = 1/(4*math.cos(math.pi/n)**2)
    root = math.hypot(a,t)
    gamma = a*t/(a+t+root)
    q = a/(t+root)
    rho2 = 2*q*q/(n*(1+q*q))
    return gamma, rho2


def exact_distance_cut():
    count=0
    for n in range(4,12):
        for seed in range(4):
            arms=[Fraction((i+1+2*seed)%7+1,10) for i in range(n)]
            cores=[Fraction((-1)**i*(i+1),3) for i in range(n)]
            leaves=[Fraction((-1)**(i+seed)*(i+2),5) for i in range(n)]
            cores[-1]=-sum(cores[:-1])-sum(leaves)
            al=cores+leaves
            Q=Fraction(0)
            for x in range(2*n):
                for y in range(2*n):
                    if x==y:continue
                    i,j=x%n,y%n
                    d=Fraction(min((i-j)%n,(j-i)%n))
                    if x>=n:d+=arms[i]
                    if y>=n:d+=arms[j]
                    Q+=al[x]*al[y]*d
            beta=[cores[i]+leaves[i] for i in range(n)]
            Q0=sum(beta[i]*beta[j]*min((i-j)%n,(j-i)%n) for i in range(n) for j in range(n))
            assert Q == Q0-2*sum(arms[i]*leaves[i]**2 for i in range(n))
            count+=1
    print('EXACT_WEIGHTED_PENDANT_DECOMPOSITION_OK',count)


def spectral_threshold_tests():
    cases=0
    for n in range(4,19):
        for t in (.15,.6,1.8):
            g,rho=baseline(n,t)
            z0=spectrum(distance(n,[t]*n))
            assert abs(z0[1]-g)<5e-9,(n,t,z0[:4],g)
            if n%2: assert sum(abs(x-g)<5e-9 for x in z0)==2
            for extra in (.01,.2,3.):
                arms=[t]*n
                arms[0]+=extra
                g1=spectrum(distance(n,arms))[1]
                assert abs(g1-g)<5e-9,(n,t,extra,g1,g)
                for j in range(1,n):
                    arms2=arms.copy();arms2[j]+=extra
                    g2=spectrum(distance(n,arms2))[1]
                    if n%2:
                        assert g2 > g+1e-8,(n,t,extra,j,g2,g)
                    else:
                        assert abs(g2)<5e-9
                    cases+=1
    print('ONE_VERSUS_TWO_STRONG_SITE_THRESHOLD_OK',cases)


def first_order_and_placement():
    cases=0
    for n in (5,7,9,11,13,17):
        for t in (.2,1.,2.):
            g,rho2=baseline(n,t)
            dvals=[]
            for d in range(1,n):
                arms=[t]*n
                eps=1e-5
                arms[0]+=eps
                arms[d]+=eps
                actual=(spectrum(distance(n,arms))[1]-g)/eps
                pred=rho2*(1-abs(math.cos(4*math.pi*d/n)))
                assert abs(actual-pred)<2e-4,(n,t,d,actual,pred)
                dvals.append((d,pred))
                cases+=1
            best=max(v for d,v in dvals)
            theoretical=rho2*(1-math.sin(math.pi/(2*n)))
            assert abs(best-theoretical)<1e-11,(n,t,best,theoretical)
            # Unequal increments: smaller eigenvalue of the 2x2 compressed update.
            d=(n+1)//2
            aa,bb=.7,2.
            eps=1e-5
            arms=[t]*n; arms[0]+=eps*aa;arms[d]+=eps*bb
            actual=(spectrum(distance(n,arms))[1]-g)/eps
            cosine=math.cos(4*math.pi*d/n)
            pred=.5*rho2*(aa+bb-math.sqrt((aa-bb)**2+4*aa*bb*cosine*cosine))
            assert abs(actual-pred)<2e-4,(n,t,actual,pred)
    print('SHARP_TWO_SITE_PERTURBATION_AND_PLACEMENT_OK',cases)

if __name__=='__main__':
    exact_distance_cut()
    spectral_threshold_tests()
    first_order_and_placement()
    print('ALL_CYCLIC_TWO_SITE_STIFFNESS_CHECKS_OK')
