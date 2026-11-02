"""Independent finite checks for constant-width path and cycle window concepts.
Run: python3 verify_windows.py (standard library only).
"""
from functools import lru_cache
from itertools import combinations
from math import log2


def make_concepts(kind, n, k):
    assert n >= 2 and 1 <= k <= n
    if kind == 'cycle':
        assert k < n
        starts = range(n)
        return tuple(sum(1 << ((a+j) % n) for j in range(k)) for a in starts)
    assert kind == 'path'
    return tuple(sum(1 << (a+j) for j in range(k)) for a in range(n-k+1))


def ldim_exact(concepts, n):
    # Recurrence implemented independently of the proposed closed formula.
    unique = tuple(sorted(set(concepts)))
    @lru_cache(None)
    def rec(state):
        if len(state) <= 1:
            return 0
        best = 0
        for x in range(n):
            yes = tuple(c for c in state if c & (1 << x))
            no = tuple(c for c in state if not c & (1 << x))
            if yes and no:
                best = max(best, 1+min(rec(yes), rec(no)))
        return best
    return rec(unique)


def vc_exact(concepts, n):
    # Brute-force every candidate support (early stop after 3).
    for d in (3, 2, 1):
        for supp in combinations(range(n), d):
            traces = {sum(((c >> x)&1)<<j for j,x in enumerate(supp)) for c in concepts}
            if len(traces) == (1 << d):
                return d
    return 0


def expected(kind, n, k):
    m = n-k+1
    if kind == 'path':
        D = min(m.bit_length()-1, 1+(k.bit_length()-1))
        V = 0 if m == 1 else (2 if k >= 2 and m >= k+2 else 1)
    else:
        D = min(n.bit_length()-1, 1+(min(k, n-k).bit_length()-1))
        V = 2 if 2 <= k <= n-2 else 1
    return V,D


def proof_tree(kind,n,k):
    # Lower-bound certificate via explicitly selected starts and prefix cuts.
    V,D = expected(kind,n,k)
    if D==0: return []
    h=1<<(D-1)
    if kind == 'path':
        selected = list(range(1<<D))
        root = h-1
    else:
        selected = list(range(h))+list(range(k,k+h))
        root = k-1
    C=make_concepts(kind,n,k)
    count=[0]
    leaves=set()
    def walk(block,depth,query=None):
        if depth==0:
            assert len(block)==1
            leaves.add(block[0])
            return
        if query is None:
            query=(block[0]+len(block)//2-1)%n
        yes=[s for s in block if (C[s]>>query)&1]
        no=[s for s in block if not (C[s]>>query)&1]
        assert len(yes)==len(no)==len(block)//2, (kind,n,k,block,query)
        count[0]+=1
        if depth>1:
            assert yes==list(range(yes[0],yes[0]+len(yes)))
            assert no==list(range(no[0],no[0]+len(no)))
        walk(yes,depth-1)
        walk(no,depth-1)
    walk(selected,D,root)
    assert count[0]==(1<<D)-1 and len(leaves)==(1<<D)
    return sorted(leaves)


def main():
    runs=0;tree_leaves=0
    for kind in ('path','cycle'):
        for n in range(2,17):
            for k in range(1, n+1 if kind=='path' else n):
                C=make_concepts(kind,n,k)
                assert len(set(C))==len(C)
                actual=(vc_exact(C,n),ldim_exact(C,n))
                predicted=expected(kind,n,k)
                assert actual==predicted, (kind,n,k,actual,predicted)
                leaves=proof_tree(kind,n,k)
                tree_leaves+=len(leaves)
                runs+=1
        print(kind.upper(), 'ALL_CASES_PASS', 'cases',sum(n if kind=='path' else n-1 for n in range(2,17)))
    print('FIXED_WINDOW_VC_LDIM_AND_TREE_ALL_CHECKS_PASS', runs, tree_leaves)

if __name__=='__main__':
    main()
