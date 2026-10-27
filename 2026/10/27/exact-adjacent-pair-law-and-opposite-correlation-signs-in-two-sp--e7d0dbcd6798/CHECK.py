"""Independent finite-ring and analytic tests for adjacent pairs in single-attempt AB adsorption.
Run with Python 3.9+; only standard-library dependencies.
"""
import itertools
import math
import random
from collections import Counter


def analytical(p, t):
    assert 0 < p < 1 and 0 <= t <= 1
    b = 1 - p
    g = math.sqrt(p*b)
    z = g*t
    # Numerically stable enough on the test domain p >= 0.05.
    fa = math.sinh(z)/g - b*(math.cosh(z)-1)/g**2
    fb = math.sinh(z)/g - p*(math.cosh(z)-1)/g**2
    a, d = p*fa, b*fb
    rho_a = (2*p-1)*t/2 + math.sinh(2*z)/(4*g) - math.sinh(z)**2
    rho_b = (1-2*p)*t/2 + math.sinh(2*z)/(4*g) - math.sinh(z)**2
    out = {('A','A'):a*a, ('B','B'):d*d, ('A','B'):0.,('B','A'):0.,
           ('A','X'):rho_a-a*a, ('X','A'):rho_a-a*a,
           ('B','X'):rho_b-d*d, ('X','B'):rho_b-d*d,
           ('X','X'):(1-a-d)**2}
    return out, dict(a=a,b=d,rho_a=rho_a,rho_b=rho_b,
                     cAA=a*a-rho_a*rho_a, cBB=d*d-rho_b*rho_b,
                     cOcc=a*a+d*d-(rho_a+rho_b)**2)


def simulate_ring(p,t,n=96,reps=12000,seed=8):
    rng=random.Random(seed)
    states=['X','A','B']
    counter=Counter()
    for _ in range(reps):
        labels=[1 if rng.random()<p else 2 for _ in range(n)]
        times=[rng.random() for _ in range(n)]
        occ=[0]*n
        for j in sorted(range(n),key=times.__getitem__):
            if times[j]>t: break
            left=occ[(j-1)%n];right=occ[(j+1)%n]
            if left!=3-labels[j] and right!=3-labels[j]:
                occ[j]=labels[j]
        for j in range(n):
            counter[(states[occ[j]],states[occ[(j+1)%n]])]+=1
    return {k:v/(n*reps) for k,v in counter.items()}


def exhaust_symmetric(n):
    counter=Counter();total=0
    states=['X','A','B']
    for labels in itertools.product((1,2),repeat=n):
        for perm in itertools.permutations(range(n)):
            occ=[0]*n
            for j in perm:
                if occ[(j-1)%n]!=3-labels[j] and occ[(j+1)%n]!=3-labels[j]:
                    occ[j]=labels[j]
            counter[(states[occ[0]],states[occ[1]])]+=1
            total+=1
    return {k:v/total for k,v in counter.items()}


def run():
    count=0
    for p,t in [(0.05,1),(.15,.9),(.3,1),(.5,1),(.75,.65),(.9,1),(.95,.2)]:
        law,d=analytical(p,t)
        assert abs(sum(law.values())-1)<2e-13;count+=1
        assert abs(law['A','A']+law['A','X']-d['rho_a'])<1e-13;count+=1
        assert abs(law['B','B']+law['B','X']-d['rho_b'])<1e-13;count+=1
        assert min(law.values())>=-1e-13;count+=1
        assert d['cAA']>0 and d['cBB']>0 and d['cOcc']<0;count+=3
        assert abs(d['rho_a']+d['rho_b'] - (d['a']+d['b']-d['a']*d['b']))<3e-13;count+=1
        mc=simulate_ring(p,t,seed=int(p*10000+t*100))
        for pair,prob in law.items():
            assert abs(mc.get(pair,0)-prob)<.012,(p,t,pair,mc.get(pair,0),prob)
            count+=1
        print('Monte Carlo',p,t,'max-error',max(abs(mc.get(k,0)-v) for k,v in law.items()))
    for n in (5,6,7):
        exact=exhaust_symmetric(n)
        predicted,_=analytical(.5,1)
        for pair,prob in predicted.items():
            assert abs(exact.get(pair,0)-prob)<.004,(n,pair,exact.get(pair,0),prob)
            count+=1
        print('Exact circular enumeration',n,'max-error',max(abs(exact.get(k,0)-v) for k,v in predicted.items()))
    assert abs(analytical(.5,1)[0]['X','X']-(2*math.exp(-.5)-1)**2)<1e-13;count+=1
    print('PASS',count,'assertions')
if __name__=='__main__':run()
