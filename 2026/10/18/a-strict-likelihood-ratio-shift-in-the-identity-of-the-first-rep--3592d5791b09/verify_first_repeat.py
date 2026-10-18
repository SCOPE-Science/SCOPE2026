"""Exact-rational checks for the conditional identity of a first repeated sample.

Run with Python 3. No third-party packages are needed.
"""
from fractions import Fraction
from itertools import product
from math import factorial


def elementary(xs, k):
    if k < 0:
        return Fraction(0)
    e = [Fraction(1)] + [Fraction(0)] * len(xs)
    for a in xs:
        for j in range(len(xs), 0, -1):
            e[j] += a * e[j-1]
    return e[k] if k <= len(xs) else Fraction(0)


def analytic_joint(p, t, i):
    return factorial(t-1)*p[i]**2*elementary(p[:i]+p[i+1:],t-2)


def brute_joint(p, t, i):
    # Enumerate all possible length-t words; retain precisely those whose
    # first repetition occurs at t with repeated symbol i.
    count = Fraction(0)
    for seq in product(range(len(p)), repeat=t):
        if seq[-1] != i or len(set(seq[:-1])) != t-1 or i not in seq[:-1]:
            continue
        value = Fraction(1)
        for s in seq:
            value *= p[s]
        count += value
    return count


def check_case(weights):
    p = [Fraction(w, sum(weights)) for w in weights]
    m = len(p)
    joint = [[Fraction(0)] * m for _ in range(m)]
    for t in range(2, m+2):
        row = [analytic_joint(p,t,i) for i in range(m)]
        for i in range(m):
            assert row[i] == brute_joint(p,t,i), (weights,t,i,row[i])
        joint[t-2] = row
    assert sum(map(sum,joint)) == 1
    posterior = [[x/sum(row) for x in row] for row in joint]
    assert posterior[0] == [x*x/sum(y*y for y in p) for x in p]
    assert posterior[-1] == p
    for a in range(m):
        for b in range(m):
            if a == b:
                continue
            odds = [row[a]/row[b] for row in joint]
            if p[a]<p[b]:
                assert all(odds[j]<odds[j+1] for j in range(m-1))
            elif p[a]==p[b]:
                assert all(x==1 for x in odds)
            else:
                assert all(odds[j]>odds[j+1] for j in range(m-1))
    means=[sum(row[i]*p[i] for i in range(m)) for row in posterior]
    if len(set(weights))==1:
        assert all(means[t]==means[0] for t in range(m))
    else:
        assert all(means[t]>means[t+1] for t in range(m-1))
    return m*(m),sum(len(list(product(range(m),repeat=t))) for t in range(2,m+2))


def main():
    cases=[]
    for m in range(2,6):
        cases.extend([[1]*m,list(range(1,m+1)),[m-j+1 for j in range(m)]])
        cases.append([1,1]+list(range(2,m)))
    total=0
    for ws in cases:
        _,paths=check_case(ws)
        total+=paths
    print(f"PASS: {len(cases)} exact-rational probability vectors, {total} enumerated sample words; all joint laws, likelihood ratios and conditional mean monotonicity checked.")

if __name__=='__main__':
    main()
