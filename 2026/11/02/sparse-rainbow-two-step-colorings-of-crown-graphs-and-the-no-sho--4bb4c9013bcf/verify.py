"""Independent checks for sparse red-blue distance-two rainbow routes on crowns.
Only uses Python's standard library; numerical checks do not replace proof.
"""
from itertools import combinations, permutations
from math import factorial


def graph_check(n, reds):
    """Construct the actual graph and check all pairs at distance exactly two."""
    reds = {frozenset((('a',i),('b',j))) for i,j in reds}
    vertices = [('a',i) for i in range(n)] + [('b',i) for i in range(n)]
    nbr = {v: set() for v in vertices}
    for i in range(n):
        for j in range(n):
            if i != j:
                a,b=('a',i),('b',j)
                nbr[a].add(b);nbr[b].add(a)
    dist2_pairs = 0
    for s,t in combinations(vertices,2):
        if t in nbr[s]: continue
        mids = nbr[s].intersection(nbr[t])
        if not mids: continue
        dist2_pairs += 1
        if not any((frozenset((s,m)) in reds) != (frozenset((m,t)) in reds) for m in mids):
            return False
    assert dist2_pairs == n*(n-1), (n,dist2_pairs)
    return True


def cycle_no_short(p):
    n=len(p); seen=[False]*n
    for i in range(n):
        if seen[i]:continue
        j=i; k=0
        while not seen[j]:
            seen[j]=True; j=p[j]; k+=1
        if k < 3: return False
    return True


def direct(n):
    edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
    for k in range(n+1):
        valid=[]
        for selection in combinations(edges,k):
            if graph_check(n,selection):
                valid.append(frozenset(selection))
        if valid:
            return k,set(valid)
    raise AssertionError('No feasible coloring')


def predicted(n):
    output=set()
    if n==3:
        for p in permutations(range(n)):
            if all(p[i]!=i for i in range(n)) and cycle_no_short(p):
                output.add(frozenset((i,p[i]) for i in range(n)))
    else:
        for z in range(n):
            rem=[i for i in range(n) if i!=z]
            for p in permutations(range(len(rem))):
                if cycle_no_short(p):
                    output.add(frozenset((rem[i],rem[p[i]]) for i in range(len(rem))))
    return output


def cycle_counts(m):
    # Number of permutations of m labels with all cycles of length >=3.
    a=[1]+[0]*m
    for q in range(1,m+1):
        a[q]=sum(factorial(q-1)//factorial(q-j)*a[q-j] for j in range(3,q+1))
    return a[m]


def main():
    for n in range(3,6):
        k,actual=direct(n)
        expect=predicted(n)
        assert actual==expect,(n,len(actual),len(expect),actual.symmetric_difference(expect))
        assert k==(3 if n==3 else n-1)
        assert len(actual)==(2 if n==3 else n*cycle_counts(n-1))
        print('GRAPH_RECONSTRUCTION_EXHAUSTIVE_OK',n,k,len(actual))
    for n in range(6,9):
        expect=predicted(n)
        assert len(expect)==n*cycle_counts(n-1)
        assert all(graph_check(n,c) for c in expect)
        print('INDEPENDENT_GEODESIC_CHECK_ALL_CONSTRUCTED_OK',n,len(expect))
    # Verify the EG-f recurrence by independent partition of permutations for small m.
    for m in range(0,8):
        ct=sum(cycle_no_short(p) for p in permutations(range(m)))
        assert ct==cycle_counts(m)
    print('CYCLE_INDEX_COUNT_CHECK_OK 0..7')
    print('VERIFY_OK')

if __name__=='__main__':main()
