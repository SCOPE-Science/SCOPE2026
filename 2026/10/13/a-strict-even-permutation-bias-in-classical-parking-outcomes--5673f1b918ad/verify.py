#!/usr/bin/env python3
"""Exact checks for the signed parking-outcome recurrence.
All arithmetic is integral; finite checks supplement the all-size proof.
"""
from itertools import combinations, permutations, product
from math import comb, factorial


def gaussian_at_minus_one(n, k):
    if n % 2 == 0 and k % 2 == 1:
        return 0
    return comb(n // 2, k // 2)


def signed_outcome_counts(nmax):
    s = [1]
    for n in range(1, nmax + 1):
        s.append(sum(j * (-1)**(n-j) * gaussian_at_minus_one(n-1, j-1)
                     * s[j-1] * s[n-j] for j in range(1, n+1)))
    return s


def parking_outcome(pref):
    n = len(pref)
    spots = [0]*n
    for car, wanted in enumerate(pref, 1):
        idx = wanted-1
        while idx < n and spots[idx]:
            idx += 1
        if idx == n:
            return None
        spots[idx] = car
    return spots


def parity(v):
    return -1 if sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))%2 else 1


def pin_weight(perm):
    weight = 1
    for i,c in enumerate(perm):
        streak = 1
        while streak<=i and perm[i-streak]<c:
            streak += 1
        weight *= streak
    return weight


def check():
    nchecks = 0
    s = signed_outcome_counts(32)
    assert s[:11] == [1,1,1,4,11,72,335,2944,19449,211520,1815089]
    nchecks += 11

    for n in range(1, 8):
        total = signed_sum = 0
        for prefs in product(range(1,n+1), repeat=n):
            outcome = parking_outcome(prefs)
            if outcome is not None:
                total += 1
                signed_sum += parity(outcome)
        assert total == (n+1)**(n-1), (n,total)
        assert signed_sum == s[n], (n,signed_sum,s[n])
        nchecks += 2

    for n in range(1, 9):
        total = signed_sum = 0
        for perm in permutations(range(1,n+1)):
            weight = pin_weight(perm)
            total += weight
            signed_sum += parity(perm)*weight
        assert total == (n+1)**(n-1), (n,total)
        assert signed_sum == s[n], (n,signed_sum,s[n])
        nchecks += 2

    for n in range(0, 13):
        for k in range(n+1):
            signed = 0
            for positions in combinations(range(n), k):
                inv = sum(pos - ix for ix,pos in enumerate(positions))
                signed += (-1)**inv
            assert signed == gaussian_at_minus_one(n, k), (n,k,signed)
            nchecks += 1

    for m in range(0, 15):
        e = s[2*m]
        o = s[2*m+1]
        expected_o = sum((2*a+1)*comb(m,a)*s[2*a]*s[2*(m-a)] for a in range(m+1))
        assert o == expected_o, (m,o,expected_o)
        nchecks += 1
        if m:
            expected_e = sum(comb(m-1,a)*(
                (2*a+2)*s[2*a+1]*s[2*(m-a-1)]
                -(2*a+1)*s[2*a]*s[2*(m-a-1)+1]
            ) for a in range(m))
            assert e==expected_e,(m,e,expected_e)
            nchecks+=1

    # Formal-power-series ODE in integer EGF coefficients.
    # [z^m]E^3 and shifted derivative terms, multiplied by m!, are integers.
    for m in range(0, 15):
        c3 = sum(comb(m,a)*comb(m-a,b)*s[2*a]*s[2*b]*s[2*(m-a-b)]
                 for a in range(m+1) for b in range(m-a+1))
        t1 = 8*m*sum(comb(m-1,a)*s[2*a]*sum(comb(m-1-a,b)*s[2*b]*s[2*(m-1-a-b+1)]
                        for b in range(m-a)) for a in range(m)) if m>=1 else 0
        # E'' term: E_{r+2} multiplied by (m-2)!, then m! = m(m-1).
        t2 = 4*m*(m-1)*sum(comb(m-2,a)*s[2*a]*sum(comb(m-2-a,b)*s[2*b]*s[2*(m-2-a-b+2)]
                         for b in range(m-1-a)) for a in range(m-1)) if m>=2 else 0
        assert s[2*(m+1)] == c3+t1+t2, (m,s[2*(m+1)],c3,t1,t2)
        nchecks += 1

    assert all(v>0 for v in s)
    nchecks += len(s)
    print(f'PASS: {nchecks} exact assertions; direct preference enumeration through n=7; Pinsky weights through n=8; signed subsets through n=12; formal identities through m=14.')
    print('S_0..S_12=',s[:13])

if __name__=='__main__':
    check()
