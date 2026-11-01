"""Exact-arithmetic tests for two-cell averaging on finite cyclic signals.
No numerical test substitutes for the proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def variation(x):
    return sum(abs(x[(i + 1) % len(x)] - x[i]) for i in range(len(x)))


def runs(labels):
    n = len(labels)
    return sum(labels[i] != labels[(i + 1) % n] for i in range(n)) // 2


def averaged(labels, masses, x):
    a = sum(masses[i] for i in range(len(labels)) if labels[i])
    b = sum(masses[i] for i in range(len(labels)) if not labels[i])
    A = sum(masses[i] * x[i] for i in range(len(labels)) if labels[i]) / a
    B = sum(masses[i] * x[i] for i in range(len(labels)) if not labels[i]) / b
    return [A if z else B for z in labels]


def formula(labels, masses):
    n = len(labels)
    a = sum(masses[i] for i in range(n) if labels[i])
    b = sum(masses[i] for i in range(n) if not labels[i])
    s = F(0)
    prefs = [s]
    for i in range(n):
        s += masses[i] / (a if labels[i] else -b)
        prefs.append(s)
    assert s == 0
    return runs(labels) * (max(prefs) - min(prefs))


def run_masses(labels, masses, target):
    n = len(labels)
    starts = [i for i in range(n) if labels[i] == target and labels[(i - 1) % n] != target]
    values = []
    for i in starts:
        k = i
        v = F(0)
        while labels[k] == target:
            v += masses[k]
            k = (k + 1) % n
        values.append(v)
    return values


def stable_from_runs(labels, masses):
    r = runs(labels)
    A = run_masses(labels, masses, True)
    B = run_masses(labels, masses, False)
    return all(r * z == sum(A) for z in A) and all(r * z == sum(B) for z in B)


def brute_arc(labels, masses):
    n = len(labels)
    best = F(0)
    witness = None
    for start in range(n):
        for size in range(1, n):
            x = [F(0)] * n
            for k in range(size):
                x[(start+k)%n] = F(1)
            ratio = variation(averaged(labels, masses, x)) / variation(x)
            if ratio > best:
                best, witness = ratio, (start, size)
    return best, witness


def main():
    checks=0
    for n in range(3,10):
        for tail in product((False, True), repeat=n-1):
            labels=(True,)+tail
            if all(labels):
                continue
            families = [[F(1)] * n, [F(1+i%3) for i in range(n)]]
            for masses in families:
                v=formula(labels,masses)
                brute,_=brute_arc(labels,masses)
                assert v==brute,(labels,masses,v,brute)
                assert (v==1)==stable_from_runs(labels,masses)
                r=runs(labels)
                assert F(1)<=v<=r
                checks+=1
    rng=Random(72814)
    for n in (10,12,15,22):
        for _ in range(250):
            labels=[bool(rng.randrange(2)) for __ in range(n)]
            if len(set(labels))<2:
                continue
            masses=[F(rng.randint(1,30),rng.randint(1,20)) for __ in range(n)]
            v=formula(labels,masses)
            brute,_=brute_arc(labels,masses)
            assert v==brute
            assert (v==1)==stable_from_runs(labels,masses)
            checks+=1
    # Imbalanced six-cycle: sharp 4/3, then balance by masses despite unequal run lengths.
    labels=(True,True,False,True,False,False)
    assert formula(labels,[F(1)]*6)==F(4,3)
    masses=list(map(F,(1,1,2,2,1,1)))
    assert formula(labels,masses)==1
    # At fixed r>=2, ratios approach r with strictly positive masses.
    for r in range(2,11):
        labels=tuple(i%2==0 for i in range(2*r))
        ms=[F(1,100000)]*(2*r)
        ms[0]=F(1);ms[1]=F(1)
        assert formula(labels,ms)>F(999,1000)*r
        checks+=1
    print('PASS', checks,'partition/weight families, exact arc norms and rigidity checks')

if __name__=='__main__':
    main()
