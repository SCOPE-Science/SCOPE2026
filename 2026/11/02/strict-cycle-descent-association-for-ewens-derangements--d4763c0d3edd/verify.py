"""Exact checks for cycle--descent association in Ewens derangements.

Standard-library only; run with: python3 verify.py
The finite checks supplement, but do not replace, the all-size proof.
"""
from fractions import Fraction
from itertools import permutations
from math import comb

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def cycle_count(p):
    n = len(p)
    seen = [False] * n
    count = 0
    for start in range(n):
        if not seen[start]:
            count += 1
            cur = start
            while not seen[cur]:
                seen[cur] = True
                cur = p[cur] - 1
    return count

def two_cycles(p):
    return sum(1 for i in range(len(p)) for j in range(i+1,len(p))
               if p[i] == j+1 and p[j] == i+1)

def descents(p):
    return sum(p[i] > p[i+1] for i in range(len(p)-1))

def derangements(n):
    return [p for p in permutations(range(1,n+1))
            if all(p[i] != i+1 for i in range(n))]

def Z_and_law(nmax, theta):
    Z = [Fraction(0)]*(nmax+1)
    laws = [{} for _ in range(nmax+1)]
    Z[0],Z[1],Z[2] = Fraction(1),Fraction(0),theta
    laws[2] = {1: Fraction(1)}
    laws[3] = {1: Fraction(1)}
    Z[3] = 2*theta
    for n in range(4,nmax+1):
        Z[n] = (n-1)*(Z[n-1]+theta*Z[n-2])
        a = Z[n-1] / (Z[n-1] + theta*Z[n-2])
        b = 1-a
        d = {}
        for k, v in laws[n-1].items():
            d[k] = d.get(k,Fraction(0)) + a*v
        for k, v in laws[n-2].items():
            d[k+1] = d.get(k+1,Fraction(0)) + b*v
        laws[n] = d
        verify(sum(d.values()) == 1, ('distribution normalization',n,theta))
        verify(Z[n] > 0, ('positive partition function',n,theta))
        # Stochastic sandwich: K[n-1] <=st K[n] <=st 1+K[n-2]
        for cutoff in range(n+2):
            tail1 = sum(v for k,v in laws[n-1].items() if k >= cutoff)
            tail2 = sum(v for k,v in laws[n].items() if k >= cutoff)
            tail3 = sum(v for k,v in laws[n-2].items() if k+1 >= cutoff)
            verify(tail1 <= tail2 <= tail3, ('sandwich',n,theta,cutoff))
    return Z,laws

for theta in (Fraction(1,2),Fraction(1),Fraction(2),Fraction(3)):
    Z,laws = Z_and_law(35,theta)
    for n in range(2,9):
        ps = derangements(n)
        weights = [theta**cycle_count(p) for p in ps]
        denom = sum(weights)
        verify(denom == Z[n], ('recurrence enumeration',theta,n))
        direct = {}
        for p,w in zip(ps,weights):
            k = cycle_count(p)
            direct[k] = direct.get(k,Fraction(0)) + w/denom
        verify(direct == laws[n], ('cycle law',theta,n))
        # Class-conditional Fulman expectation formula.
        by_class = {}
        for p,w in zip(ps, weights):
            key = (cycle_count(p),two_cycles(p))
            acc,tw = by_class.get(key,(Fraction(0),Fraction(0)))
            by_class[key] = (acc+w*descents(p),tw+w)
        for (k,c2),(acc,tw) in by_class.items():
            verify(acc/tw == Fraction(n-1,2) + Fraction(c2,n),
                   ('conditional descent mean',n,theta,k,c2))
        for power in (1,2,3):
            f = lambda k:k**power
            mean_f = sum(w*f(cycle_count(p)) for p,w in zip(ps,weights))/denom
            mean_d = sum(w*descents(p) for p,w in zip(ps,weights))/denom
            cov = sum(w*f(cycle_count(p))*descents(p) for p,w in zip(ps,weights))/denom-mean_f*mean_d
            if n>=4:
                efshift = sum(v*f(k+1) for k,v in laws[n-2].items())
                predicted = Fraction(comb(n,2),n)*theta*Z[n-2]/Z[n]*(efshift-mean_f)
                verify(cov == predicted, ('exact covariance',theta,n,power,cov,predicted))
                verify(cov>0, ('strict positive',theta,n,power))
            else:
                verify(cov==0, ('small boundary',theta,n,power))

# Unconditioned contrast: ordinary permutations have negative cycle--descent covariance.
for n in range(2,9):
    ps = permutations(range(1,n+1))
    A,B,C,count = 0,0,0,0
    for p in ps:
        k,d=cycle_count(p),descents(p)
        A+=k; B+=d; C+=k*d; count+=1
    cov = Fraction(C,count) - Fraction(A*B,count*count)
    verify(cov == -Fraction(1,2*n), ('unconditioned contrast',n,cov))

print('PASS: %d exact checks' % checks)
