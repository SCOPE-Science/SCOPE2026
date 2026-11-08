"""Finite checks for Euclidean statistics of Bernoulli vertex-thinned cubes.
Only standard-library dependencies. Tests compare independent exhaustive counts with
closed antipodal-pair probabilities and edge-count moment identities.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, exp, factorial
import random


def hamming(a,b):
    return (a^b).bit_count()


def exact_dimension(d):
    N=1<<d
    pairs=[(u,v,hamming(u,v)) for u in range(N) for v in range(u+1,N)]
    M=1<<(d-1)
    for p in (Fraction(1,4),Fraction(1,2)):
        masses=[0]*(1<<N)
        # Exhaustively tally each subset, by cardinality and antipodal-pair existence.
        histogram={}
        n_exact=0
        for s in range(1<<N):
            k=s.bit_count()
            dist=0
            for u,v,h in pairs:
                if (s>>u)&1 and (s>>v)&1:
                    dist=max(dist,h)
            histogram[(k,dist)]=histogram.get((k,dist),0)+1
            if dist==d:
                n_exact+=1
        probability=sum(Fraction(count)*p**k*(1-p)**(N-k)
                        for (k,dist),count in histogram.items() if dist==d)
        assert probability==1-(1-p*p)**M,(d,p,probability)
    # count edge pairs sharing one endpoint and compare simple graph identity
    for j in range(min(2,d-1)+1):
        K=sum(comb(d,i) for i in range(j+1))
        edges=[(u,v) for u,v,h in pairs if h>=d-j]
        assert len(edges)==N*K//2
        shared=sum(len(set(e)&set(f))==1 for e,f in combinations(edges,2))
        assert shared==N*comb(K,2),(d,j,shared)
    return len(histogram),len(pairs)


def asymptotic_checks():
    for j in range(4):
        for d in (18,36,72,144):
            K=sum(comb(d,i) for i in range(j+1))
            target=1/(2*factorial(j))
            ratio=K/(2*d**j)
            assert abs(ratio-target)<(10*(j+1)**2/d)
    # An independent simulation of the near-diametral contact statistic.
    rng=random.Random(20261104)
    trials=1200
    for d,j,c in ((9,0,1.0),(10,1,1.0),(12,2,1.0)):
        N=1<<d
        p=c*2**(-d/2)*d**(-j/2)
        zero=0
        for _ in range(trials):
            vertices=[v for v in range(N) if rng.random()<p]
            contains_critical_pair=any(hamming(u,v)>=d-j for u,v in combinations(vertices,2))
            zero+=not contains_critical_pair
        lam=(N/2)*sum(comb(d,i) for i in range(j+1))*p*p
        approx=exp(-lam)
        assert abs(zero/trials-approx)<0.12,(d,j,zero/trials,approx)
        print(f'simulation d={d} j={j}: no-critical-pair fraction={zero/trials:.4f}, Poisson approximation={approx:.4f}')


def main():
    for d in (2,3,4):
        h,p=exact_dimension(d)
        print('exhaustive',d,'histogram cells',h,'unordered vertex pairs',p)
    asymptotic_checks()
    print('BERNOULLI_CUBE_METRIC_CHECKS_PASSED')


if __name__=='__main__':
    main()
