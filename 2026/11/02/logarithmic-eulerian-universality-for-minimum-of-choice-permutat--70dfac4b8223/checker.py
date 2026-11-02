"""Exact independent finite checks for a k-choice minimum removal model.

Only Python's standard library is needed. The finite checks below complement,
but do not replace, the analytical arguments for unbounded sample sizes.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def rank_mass(m, k, j):
    return Fraction((m-j+1)**k - (m-j)**k, m**k)


def descent_prob(m, k):
    assert m >= 2
    s = sum(((r+1)**k-r**k)*r**k for r in range(m))
    return 1-Fraction(s, m**k*(m-1)**k)


def independent_rank_probability(n, k, perm):
    remaining = list(range(1, n+1))
    weight = Fraction(1)
    for value in perm:
        m = len(remaining)
        j = remaining.index(value)+1
        weight *= rank_mass(m, k, j)
        remaining.remove(value)
    return weight


def adjacent_joint_prob(m, k):
    # P(J_(m-2) < J_(m-1) < J_m), with J_s independent.
    assert m >= 3
    out = Fraction(0)
    for j in range(1, m+1):
        for ell in range(1, j):
            # P(J_(m-2) < ell) is 1 - P(J_(m-2) >= ell).
            if ell > m-2:
                prev = Fraction(1)
            else:
                prev = 1-Fraction((m-ell-1)**k, (m-2)**k)
            out += rank_mass(m,k,j)*rank_mass(m-1,k,ell)*prev
    return out


def predicted_moments(n,k):
    p = {m:descent_prob(m,k) for m in range(2,n+1)}
    mean = sum(p.values(),Fraction(0))
    var = sum((x*(1-x) for x in p.values()),Fraction(0))
    for m in range(3,n+1):
        var += 2*(adjacent_joint_prob(m,k)-p[m]*p[m-1])
    return mean, var


def run():
    tested=0
    for n in range(2,8):
        for k in range(1,5):
            mean=Fraction(0); second=Fraction(0); mass=Fraction(0)
            values=list(permutations(range(1,n+1)))
            conditional={}
            for perm in values:
                p=independent_rank_probability(n,k,perm)
                d=sum(perm[i]>perm[i+1] for i in range(n-1))
                mean += p*d; second += p*d*d; mass += p
                # These are the rank coordinates used by the analytical proof.
                remaining=list(range(1,n+1)); ranks={}
                for v in perm:
                    m=len(remaining); ranks[m]=remaining.index(v)+1; remaining.remove(v)
                assert d==sum(ranks[m-1]<ranks[m] for m in range(2,n+1))
                tested+=1
            assert mass==1
            em,vr=predicted_moments(n,k)
            assert mean==em and second-mean*mean==vr,(n,k,mean,em,second-mean*mean,vr)
            tested+=3
            if k==1:
                assert mean==Fraction(n-1,2)
                assert vr==Fraction(n+1,12)
                tested+=2
            else:
                assert mean<Fraction(n-1,2)
                tested+=1
    for m in range(2,35):
        for k in range(1,8):
            mass=sum((rank_mass(m,k,j) for j in range(1,m+1)),Fraction(0))
            assert mass==1
            p=sum((rank_mass(m,k,j) *
                   (1-Fraction((m-j)**k,(m-1)**k))
                   for j in range(1,m+1)),Fraction(0))
            assert p==descent_prob(m,k)
            assert p==Fraction(1,2) if k==1 else p<Fraction(1,2)
            tested+=3
    print('PASS: exact weighted permutation enumeration and moments,')
    print('finite rank laws, one-step descent probabilities and strict bias.')
    print('Assertions/groups checked:',tested)

if __name__=='__main__':
    run()
