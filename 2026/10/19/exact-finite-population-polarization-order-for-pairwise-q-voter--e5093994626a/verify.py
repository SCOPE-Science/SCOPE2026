"""Exact rational checks for sampling-composition ordering in finite noisy q-voter dynamics.

Only Python 3 standard library is required. This checker corroborates finite
instances; the all-population theorem follows from the independent proof.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from math import comb

CHECKS = 0

def check(condition, why):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(why)


def unanimous_probability(j, m, q, repetitions):
    if repetitions:
        return Q(j, m)**q
    return Q(comb(j, q), comb(m, q)) if j >= q else Q(0)


def jump_probabilities(n, p, q, repetitions, k):
    m = n - 1
    a, b = p / 2, 1 - p
    plus = Q(n-k, n) * (a + b*unanimous_probability(k, m, q, repetitions))
    minus = Q(k, n) * (a + b*unanimous_probability(n-k, m, q, repetitions))
    return plus, minus


def stationary(n, p, q, repetitions):
    weights = [Q(1)]
    for k in range(n):
        u = jump_probabilities(n, p, q, repetitions, k)[0]
        v = jump_probabilities(n, p, q, repetitions, k+1)[1]
        weights.append(weights[-1]*u/v)
    norm = sum(weights)
    weights = [v/norm for v in weights]
    check(sum(weights) == 1, 'normalization')
    for k in range(n+1):
        check(weights[k] == weights[n-k], 'spin-flip symmetry')
    for k in range(n):
        check(weights[k]*jump_probabilities(n,p,q,repetitions,k)[0] ==
              weights[k+1]*jump_probabilities(n,p,q,repetitions,k+1)[1],
              'stationary detailed balance')
    return weights


def variance(weights):
    n = len(weights)-1
    return sum(weights[k]*(Q(k)-Q(n,2))**2 for k in range(n+1))


def radius_tails(weights):
    n = len(weights)-1
    levels = sorted(set(abs(Q(k)-Q(n,2)) for k in range(n+1)))
    return [(r,sum(weights[k] for k in range(n+1) if abs(Q(k)-Q(n,2)) > r))
            for r in levels[:-1]]


def check_pair_comparison(n,p):
    pw=stationary(n,p,2,True)
    pn=stationary(n,p,2,False)
    mw=n-1; a=p/2; b=1-p
    def T(j):
        return (a+b*Q(j,mw)**2) / (a+b*Q(j*(j-1),mw*(mw-1)))
    for j in range(mw+1):
        correction = b*Q(j*(mw-j),mw*mw*(mw-1))
        denominator = a+b*Q(j*(j-1),mw*(mw-1))
        check(T(j) == 1+correction/denominator,'T identity')
    for k in range(n):
        check((pw[k+1]/pn[k+1])/(pw[k]/pn[k]) == T(k)/T(mw-k),
              'likelihood-ratio recurrence')
    for r1,r2 in zip(radius_tails(pw),radius_tails(pn)):
        check(r1[0]==r2[0] and r1[1]<=r2[1], 'radius-tail ordering')
    if n==3:
        check(pw==pn,'N=3 equality')
    else:
        check(variance(pw)<variance(pn),'strict q=2 variance ordering')


def micro_jump_probabilities(n,p,q,repetitions,k):
    # Reconstruct the transition from one explicit configuration, enumerating
    # focal agent and every ordered influence tuple, independently of the
    # count-process formula.
    opinions=[1]*k+[0]*(n-k)
    up=down=Q(0)
    for target in range(n):
        a=p/(2*n)
        if opinions[target]: down += a
        else: up += a
        neighbors=[j for j in range(n) if j!=target]
        groups=(product(neighbors,repeat=q) if repetitions else permutations(neighbors,q))
        ngroups=(n-1)**q if repetitions else (comb(n-1,q)*__import__('math').factorial(q))
        per=(1-p)/Q(n*ngroups)
        for group in groups:
            bits=[opinions[j] for j in group]
            if all(v==1 for v in bits) and not opinions[target]: up += per
            if all(v==0 for v in bits) and opinions[target]: down += per
    return up,down


def main():
    for n in range(3,22):
        for p in (Q(1,13),Q(1,5),Q(1,2),Q(11,13)):
            check_pair_comparison(n,p)
    for n in range(3,8):
        for repetitions in (False,True):
            for k in range(n+1):
                check(micro_jump_probabilities(n,Q(3,11),2,repetitions,k)
                      ==jump_probabilities(n,Q(3,11),2,repetitions,k),
                      'microscopic ordered-tuple enumeration')
    for p in (Q(1,11),Q(1,3),Q(1,2),Q(9,11)):
        pw=stationary(4,p,3,True)
        pn=stationary(4,p,3,False)
        check(variance(pw)>variance(pn),'reversed q=3 variance ordering')
        for k in range(5):
            check((pw[k]/pn[k] > pw[2]/pn[2]) if k!=2 else True,
                  'q=3 center-ratio strict reversal')
        for rep in (True,False):
            for k in range(5):
                check(micro_jump_probabilities(4,p,3,rep,k)
                      ==jump_probabilities(4,p,3,rep,k), 'q=3 microenumeration')
    print('PASS: ',CHECKS,' exact rational checks; q=2 N=3..21 and four noise values,')
    print('microstate transitions N=3..7, and sharp q=3 N=4 reversal.')

if __name__=='__main__':main()
