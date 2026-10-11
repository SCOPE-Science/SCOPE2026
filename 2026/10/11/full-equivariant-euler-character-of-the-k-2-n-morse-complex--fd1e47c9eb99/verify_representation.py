"""Independent finite checks for a rational homology-character formula.

Only standard-library arithmetic is used. The mathematical proof is in RESULT.md;
finite tests here are not a substitute for the all-parameter argument.
"""
from itertools import permutations, product
from collections import Counter


def partition_permutations(n):
    def partitions(n, bound=None):
        if n == 0:
            yield ()
            return
        for k in range(min(n, bound if bound is not None else n), 0, -1):
            for other in partitions(n-k, k):
                yield (k,)+other
    for lengths in partitions(n):
        p=list(range(n)); start=0
        for length in lengths:
            for k in range(length):
                p[start+k]=start+(k+1)%length
            start+=length
        yield lengths,tuple(p)


def sign(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1


def direct(n,p,swap):
    """Reduced signed Lefschetz number, by direct invariant acyclic forests."""
    N=n+2
    gp=([1,0] if swap else [0,1])+[2+p[i] for i in range(n)]
    possible=[(-1,)+tuple(range(2,N))]*2+[(-1,0,1)]*n
    total=0; invariant=0
    for parent in product(*possible):
        if any(parent[gp[v]]!=(-1 if parent[v]==-1 else gp[parent[v]]) for v in range(N)):
            continue
        acyclic=True
        for v in range(N):
            seen=set();w=v
            while w!=-1:
                if w in seen:
                    acyclic=False;break
                seen.add(w);w=parent[w]
            if not acyclic:break
        if not acyclic:continue
        invariant+=1
        used=set();cycles=0
        for v in range(N):
            if parent[v]==-1 or v in used:continue
            cycles+=1;w=v
            while w not in used:
                used.add(w);w=gp[w]
        total+=(-1)**cycles
    return (-1)**(n+1)*total,invariant


def formulas(n,p,swap):
    f=sum(i==p[i] for i in range(n))
    t=sum(p[i]!=i and p[p[i]]==i for i in range(n))//2
    s=sign(p)
    if swap:
        return (-1)**(n+1)*s*(1-f+2*t)
    return s*(f*f-1)


def module_trace(n,p,swap):
    f=sum(i==p[i] for i in range(n))
    t=sum(p[i]!=i and p[p[i]]==i for i in range(n))//2
    s=sign(p)
    sym=(f*f-f+2*t)//2
    ext=(f*f-3*f-2*t+2)//2
    other=ext+2*(f-1)
    plus,minus=(sym,other) if n%2 else (other,sym)
    return s*(plus-minus if swap else plus+minus)


def main():
    cases=0; forests=0
    for n in range(3,8):
        for lengths,p in partition_permutations(n):
            for swap in (False,True):
                direct_trace,num=direct(n,p,swap)
                expected=formulas(n,p,swap)
                module=module_trace(n,p,swap)
                assert direct_trace==expected==module,(n,lengths,swap,direct_trace,expected,module)
                cases+=1;forests+=num
        assert formulas(n,tuple(range(n)),False)==n*n-1
    print('checked_range=3..7')
    print('conjugacy_class_swapped_cases=',cases)
    print('invariant_forest_total=',forests)
    print('character_criterion=direct_lefschetz_equals_closed_formula_equals_module')
    print('VERIFY_OK')

if __name__=='__main__':main()
