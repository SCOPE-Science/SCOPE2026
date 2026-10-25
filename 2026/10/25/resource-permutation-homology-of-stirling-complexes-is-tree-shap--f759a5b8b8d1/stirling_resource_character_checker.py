"""Exact finite checks for resource-permutation characters of Stirling complexes.

All arithmetic is integral. Cells are n-tuples of vertices or edges. Tree edges
are represented by separate symbols because only their number affects traces.
"""
from itertools import permutations, product
from math import comb, factorial

def cycles(perm):
    n=len(perm); seen=set(); blocks=[]
    for i in range(n):
        if i not in seen:
            block=[]; x=i
            while x not in seen:
                seen.add(x); block.append(x); x=perm[x]
            blocks.append(block)
    return blocks

def parity(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

def f(m,k):
    return sum((-1)**(m+a+1)*comb(m,a+1)*a**k for a in range(1,m))

def occupancy_count(m,k):
    return sum((-1)**j*comb(m,j)*(m-j)**k for j in range(m+1))

def actual_trace(m,n,p):
    # Edge labels m,..,2*m-2. Every graph edge has one orientation fixed initially.
    total=0
    for t in product(range(2*m-1), repeat=n):
        if not set(range(m)).issubset(t):
            continue
        if any(t[i]!=t[p[i]] for i in range(n)):
            continue
        edge_positions=[i for i in range(n) if t[i]>=m]
        orientation=parity([p[i] for i in edge_positions])
        total+=(-1)**len(edge_positions)*orientation
    return total

def verify():
    for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4),(4,5)]:
        traces=[]
        for p in permutations(range(n)):
            c=len(cycles(p)); sgn=parity(p)
            expected=1+(-1)**(n-m)*sgn*f(m,c)
            actual=actual_trace(m,n,p)
            assert actual==expected, (m,n,p,actual,expected)
            # Second independently computed inclusion-exclusion formula.
            independent=sum((-1)**j*comb(c,j)*(m-1)**j*occupancy_count(m,c-j) for j in range(c+1))
            assert actual==independent,(m,n,p,actual,independent)
            traces.append(sgn*f(m,c))
        assert sum(traces)==0,(m,n,sum(traces))
        if m==n: assert f(m,n)==factorial(m)-1
        print(f'PASS m={m} n={n}: permutations={factorial(n)}, character_degree={f(m,n)}, invariants=0')
    print('STIRLING_RESOURCE_CHARACTERS_OK')

if __name__=='__main__': verify()
