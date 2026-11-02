"""Exact finite-size checks for near-complete copying in a two-state walk.
Standalone: Python 3 standard library only; rational arithmetic throughout.
These checks establish finite identities, not the infinite limit theorem.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial

checks = 0

def ok(cond, msg):
    global checks
    if not cond:
        raise AssertionError(msg)
    checks += 1

def sizes(parents):
    n = len(parents)+1
    subtree = [1]*n
    for v in range(n-1,0,-1):
        subtree[parents[v-1]] += subtree[v]
    return subtree

def direct_odd_character(n, q):
    alpha=1-q
    probs = [F(1,2),F(1,2)]
    for t in range(2,n+1):
        new = [F(0) for _ in range(t+1)]
        for k, pk in enumerate(probs):
            r = q/2 + alpha*F(k,t-1)
            new[k] += pk*(1-r)
            new[k+1] += pk*r
        probs = new
    return sum(((-1)**k)*pk for k,pk in enumerate(probs))

def forest_even_character(n, q):
    ret=F(0)
    for parent in product(*(range(j) for j in range(1,n))):
        for mask in range(1<<(n-1)):
            cut = mask.bit_count()
            # A component's root is the lowest-label vertex in the component.
            counts = [0]*n
            for v in range(n):
                r=v
                while r and not (mask>>(r-1)&1):
                    r=parent[r-1]
                counts[r]+=1
            if all(z%2==0 for z in counts):
                ret += q**cut * (1-q)**(n-1-cut)
    return ret/F(factorial(n-1))

for n in range(2,8):
    acc=[0]*(n+1)
    trees=0
    for parent in product(*(range(j) for j in range(1,n))):
        sz=sizes(parent)
        for x in sz[1:]:
            acc[x]+=1
        trees+=1
    ok(trees==factorial(n-1),f'tree count n={n}')
    for k in range(1,n):
        ok(F(acc[k],trees)==F(n,k*(k+1)),f'fringe n={n}, k={k}')
    ok(sum(acc)==trees*(n-1),f'fringe mass n={n}')

for n in range(2,7):
    for q in [F(1,n),F(1,2*n),F(1,3)]:
        via_walk = direct_odd_character(n,q)
        via_forest = forest_even_character(n,q)
        ok(via_walk==via_forest,f'walk/forest n={n} q={q}: {via_walk}!={via_forest}')
        if n%2:
            ok(via_walk==0,f'odd-time exact uniform n={n}')
        else:
            ok(0<=via_walk<=1,f'even-time positive character n={n}')

print('PASS:',checks,'exact rational assertions')
print('Finite walk-parity/forest identity checked for sizes 2..6 and three cutting probabilities per size.')
print('Exact fringe expectation checked for sizes 2..7.')
