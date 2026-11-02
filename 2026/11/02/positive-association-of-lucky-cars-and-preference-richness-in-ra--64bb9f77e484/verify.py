"""Standalone exact checks for lucky-car/preference-richness dependence.

Run: python3 verify.py
No optional dependencies. Finite checks corroborate, but do not prove, the general theorem.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import exp, sqrt


def circular_joint_counts(n):
    """Exact joint (lucky, richness) counts among (n+1)^n circular inputs."""
    N = n + 1
    states = {(0, 0): 1}
    for i in range(1, n + 1):
        nxt = defaultdict(int)
        for (luck, richness), count in states.items():
            nxt[(luck + 1, richness + 1)] += count * (N - i + 1)
            nxt[(luck, richness + 1)] += count * (i - 1 - richness)
            nxt[(luck, richness)] += count * richness
        states = dict(nxt)
        assert sum(states.values()) == N**i
    return states


def line_data(n):
    """Enumerate all n^n preference lists; retain successful parking functions."""
    count = 0
    joint = Counter()
    total_l = total_m = total_lm = total_l2 = total_m2 = 0
    local_lm = [0] * n
    for prefs in product(range(1, n + 1), repeat=n):
        occupied = set()
        lucky = []
        for preferred in prefs:
            actual = preferred
            while actual in occupied and actual <= n:
                actual += 1
            if actual > n:
                break
            lucky.append(int(actual == preferred))
            occupied.add(actual)
        else:
            assert len(occupied) == n
            l = sum(lucky)
            m = len(set(prefs))
            count += 1
            joint[(l, m)] += 1
            total_l += l
            total_m += m
            total_lm += l*m
            total_l2 += l*l
            total_m2 += m*m
            for k in range(n):
                local_lm[k] += lucky[k]*m
    return count, joint, total_l, total_m, total_lm, total_l2, total_m2, local_lm


def formulas(n):
    N = n + 1
    q = Fraction(n, N)
    mean_l = Fraction(n*(n+3), 2*N)
    mean_m = N*(1-q**n)
    v_l = Fraction(n*(n-1)*(n+4), 6*N*N)
    v_m = N*q**n*(1-q**n) + N*n*(Fraction(n-1,N)**n-q**(2*n))
    local = [Fraction(N-i+1,N)*(1-q**(i-1))*q**(n-i)
             for i in range(1,n+1)]
    cov = (n+2) - Fraction(5*n+7,2)*q**n
    return mean_l, mean_m, v_l, v_m, local, cov


def conditional_richness(n, lucky_vector):
    """Exact conditional M_n law given a complete lucky-car vector."""
    N = n + 1
    assert len(lucky_vector) == n and lucky_vector[0] == 1
    distribution = {0: Fraction(1)}
    for i, is_lucky in enumerate(lucky_vector, 1):
        following = defaultdict(Fraction)
        for m, pr in distribution.items():
            if is_lucky:
                following[m+1] += pr
            else:
                assert i >= 2
                following[m+1] += pr*Fraction(i-1-m, i-1)
                following[m] += pr*Fraction(m, i-1)
        distribution = dict(following)
    assert sum(distribution.values()) == 1
    return distribution


def verify():
    checks = 0
    total_successful = 0
    for n in range(1,8):
        N = n+1
        data = line_data(n)
        count, joint, tot_l, tot_m, tot_lm, tot_l2, tot_m2, local_lm = data
        total_successful += count
        assert count == N**(n-1); checks += 1
        circular = circular_joint_counts(n)
        for key in set(circular) | set(joint):
            assert circular.get(key,0) == N*joint.get(key,0), (n,key)
            checks += 1
        ml, mm, vl, vm, local, cv = formulas(n)
        assert Fraction(tot_l,count) == ml; checks += 1
        assert Fraction(tot_m,count) == mm; checks += 1
        assert Fraction(tot_l2,count)-ml**2 == vl; checks += 1
        assert Fraction(tot_m2,count)-mm**2 == vm; checks += 1
        assert Fraction(tot_lm,count)-ml*mm == cv == sum(local); checks += 1
        for i, num in enumerate(local_lm):
            assert Fraction(num,count)-Fraction(N-i,N)*mm == local[i]
            checks += 1
        if n>=2:
            assert cv > 0; checks += 1
            for power1, power2 in [(1,1),(2,2),(3,1),(1,3)]:
                Ef = sum(Fraction(freq,count)*l**power1 for (l,m),freq in joint.items())
                Eg = sum(Fraction(freq,count)*m**power2 for (l,m),freq in joint.items())
                Efg = sum(Fraction(freq,count)*l**power1*m**power2 for (l,m),freq in joint.items())
                assert Efg > Ef*Eg; checks += 1
        # Check every possible lucky vector's conditional M law against enumeration.
        if n>=2:
            lucky_richness = defaultdict(Counter)
            for prefs in product(range(1,n+1),repeat=n):
                spots=set(); lucky=[]
                for a in prefs:
                    b=a
                    while b in spots and b<=n: b+=1
                    if b>n: break
                    lucky.append(int(a==b));spots.add(b)
                else:
                    lucky_richness[tuple(lucky)][len(set(prefs))] += 1
            assert len(lucky_richness)==2**(n-1); checks += 1
            for pattern, histogram in lucky_richness.items():
                d=conditional_richness(n,pattern)
                denominator=sum(histogram.values())
                for m in range(1,n+1):
                    assert Fraction(histogram[m], denominator) == d.get(m,Fraction(0)), (n, pattern, m)
                    checks += 1
            # Conditional stochastic monotonicity for every neighboring lucky pattern.
            for vector in lucky_richness:
                for i in range(1,n):
                    if vector[i]==0:
                        higher=tuple(vector[j] if j!=i else 1 for j in range(n))
                        low=conditional_richness(n,vector)
                        high=conditional_richness(n,higher)
                        for threshold in range(1,n+1):
                            assert sum(v for m,v in high.items() if m>=threshold) >= sum(v for m,v in low.items() if m>=threshold)
                            checks += 1
        print(f'n={n}: checked {count} successful parking functions, covariance={cv}')

    e=exp(1)
    c=(1-5/(2*e))
    rho=c/sqrt((1/e-2/e**2)/6)
    assert 0.6308 < rho < 0.6310; checks += 1
    for n in [50,500,5000,50000]:
        q=n/(n+1)
        cov=n+2-(5*n+7)/2*q**n
        assert abs(cov/n-c) < 5/n;checks+=1
        max_i=max(range(1,n+1),key=lambda i:(n+2-i)/(n+1)*(1-q**(i-1))*q**(n-i))
        assert abs(max_i/n-0.5671432904097839)<3/sqrt(n); checks+=1
    print('PASS:',checks,'assertions; enumerated',total_successful,'parking functions; correlation limit',rho)


if __name__=='__main__': verify()
