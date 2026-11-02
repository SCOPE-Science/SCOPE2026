"""Self-contained finite verification of exact star proxy voting pivot laws.

Run: python3 check_heterogeneous_proxy.py
All finite checks use fractions.Fraction with no floating-point rounding.
"""
from fractions import Fraction
from itertools import product
from math import comb


def pb_distribution(probabilities):
    """Probabilities of the sum of independent Bernoulli variables."""
    out = [Fraction(1)]
    for q in probabilities:
        nxt = [Fraction(0)] * (len(out) + 1)
        for i, pi in enumerate(out):
            nxt[i] += pi * (1-q)
            nxt[i+1] += pi * q
        out = nxt
    return out


def exact_formula(p):
    m = len(p)
    h = (m+1)//2 + 1
    q = [(1-x)/2 for x in p]
    dist = pb_distribution(q)
    root = 1 - sum(dist[h:], Fraction(0)) - sum(dist[m+2-h:], Fraction(0))
    leaves = []
    for j in range(m):
        dd = pb_distribution(q[:j]+q[j+1:])
        leaves.append((dd[m-h+1] if 0<=m-h+1<len(dd) else Fraction(0))/2
                      + (dd[h-1] if 0<=h-1<len(dd) else Fraction(0))/2)
    return root, leaves


def exhaustive_formula(p):
    m = len(p)
    h = (m+1)//2 + 1
    root = Fraction(0)
    leaves = [Fraction(0)]*m
    # Choice 0=direct NO, 1=direct YES, 2=delegates.
    for code in product(range(3),repeat=m):
        weight = Fraction(1)
        for i, choice in enumerate(code):
            weight *= (1-p[i])/2 if choice<2 else p[i]
        if not weight:
            continue
        def decision(root_vote,changed=-1,leaf_vote=0):
            tally = root_vote
            for i,choice in enumerate(code):
                if i==changed:
                    tally+=leaf_vote
                elif choice==2:
                    tally+=root_vote
                elif choice==1:
                    tally+=1
            return tally>=h
        root += weight * (decision(1)-decision(0))
    for j in range(m):
        others = [i for i in range(m) if i!=j]
        for code_others in product(range(3),repeat=m-1):
            weight = Fraction(1)
            for i,choice in zip(others,code_others):
                weight *= (1-p[i])/2 if choice<2 else p[i]
            if not weight:
                continue
            for rv in (0,1):
                tally = rv
                for choice in code_others:
                    if choice==2:
                        tally+=rv
                    elif choice==1:
                        tally+=1
                leaves[j] += weight/Fraction(2) * (tally==h-1)
    return root, leaves



def run():
    cases=0
    pivots=0
    vals=[Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)]
    for m in range(1,7):
        profiles = [tuple(vals[(i*j+j+2*i) % len(vals)] for j in range(m))
                    for i in range(9)]
        profiles += [tuple(vals[(j*i+1)%len(vals)] for j in range(m))
                     for i in range(1,6)]
        profiles += [tuple([v]*m) for v in vals]
        profiles += [tuple(vals[(j*2+3)%len(vals)] for j in range(m))]
        for p in profiles:
            a=exact_formula(p)
            b=exhaustive_formula(p)
            assert a==b, (m,p,a,b)
            cases += 1
            pivots += m+1
    print(f'PASS: {cases} arbitrary-heterogeneous exact profiles and {pivots} pivotality values')
    print('Boundary examples:')
    for p in [(Fraction(0),Fraction(1)),(Fraction(1),)*3,
              (Fraction(1,3),Fraction(2,3),Fraction(0),Fraction(1)),
              (Fraction(1,2),)*5]:
        print(' ',tuple(str(x) for x in p), '->',exact_formula(p))

if __name__ == '__main__':
    run()
