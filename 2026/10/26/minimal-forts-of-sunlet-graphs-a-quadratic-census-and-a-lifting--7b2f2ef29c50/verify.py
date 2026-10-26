"""Reproducible enumeration of minimal forts in cycle-corona graphs.

No third-party dependencies. Run: python verify.py
"""
from itertools import combinations


def adjacencies(n, corona=True):
    order = 2*n if corona else n
    adj = [set() for _ in range(order)]
    for i in range(n):
        for j in ((i - 1) % n, (i + 1) % n):
            adj[i].add(j)
            adj[j].add(i)
        if corona:
            adj[i].add(n+i)
            adj[n+i].add(i)
    return tuple(tuple(sorted(v)) for v in adj)


def fort(mask, neighbors):
    if not mask:
        return False
    return all((sum((mask >> j)&1 for j in neigh) != 1)
               for i, neigh in enumerate(neighbors)
               if not (mask >> i)&1)


def canonical(n, X):
    full = X
    for i in range(n):
        inside = (X >> i)&1
        prev = (X >> ((i-1)%n))&1
        next_ = (X >> ((i+1)%n))&1
        if inside or (not inside and prev+next_==1):
            full |= 1 << (n+i)
    return full


def graph_connected(n, X):
    if not X: return False
    first = (X & -X).bit_length()-1
    seen = 1<<first
    frontier = [first]
    while frontier:
        i=frontier.pop()
        for j,middle in (((i-2)%n,(i-1)%n),((i+2)%n,(i+1)%n)):
            if ((X>>j)&1) and not ((X>>middle)&1) and not ((seen>>j)&1):
                seen |= 1<<j
                frontier.append(j)
    return seen == X


def predicted(n):
    return n*(n+1)//2 if n%2 else n*(n-2)//2 + 2


def exact_min_forts(n):
    """Direct full graph examination, no use of canonical or connectivity."""
    a = adjacencies(n)
    all_forts = [S for S in range(1,1<<(2*n)) if fort(S,a)]
    minimal = []
    for S in sorted(all_forts, key=int.bit_count):
        if not any((T & S)==T for T in minimal):
            minimal.append(S)
    return set(minimal),len(all_forts)


def run():
    totals=0
    for n in range(3,10):
        minimal, all_forts = exact_min_forts(n)
        candidate = {canonical(n,X) for X in range(1,1<<n) if graph_connected(n,X)}
        assert minimal == candidate, (n,len(minimal),len(candidate), sorted(minimal^candidate)[:3])
        assert len(candidate) == predicted(n), (n,len(candidate),predicted(n))
        totals += (1<<(2*n))-1
        print(f'BRUTE_OK n={n} fort_count={all_forts} minimal={len(minimal)} checked_nonempty_subsets={(1<<(2*n))-1}')
    for n in range(10,19):
        count=sum(graph_connected(n,X) for X in range(1,1<<n))
        assert count==predicted(n),(n,count,predicted(n))
        print(f'CONNECTED_SUPPORT_OK n={n} count={count}')
    # Six-rim-vertex witness; check minimality in the original cycle by inspecting every subset.
    n=6
    X=sum(1<<i for i in (0,1,3,4))
    small=sum(1<<i for i in (1,3))
    cyc = adjacencies(n,False)
    assert fort(X,cyc)
    assert not any(fort(Y,cyc) for Y in range(1,1<<n) if Y!=X and (Y&X)==Y)
    lifted=X|sum(1<<(n+i) for i in (0,1,3,4))
    sub=canonical(n,small)
    assert fort(lifted,adjacencies(n)) and fort(sub,adjacencies(n))
    assert sub!=lifted and (sub&lifted)==sub
    assert predicted(18)==146
    print('COUNTEREXAMPLE_OK n=6 rim_minimal={0,1,3,4} lifted={0,1,3,4,6,7,9,10} strict_subfort={1,3,6,7,9,10}')
    print(f'VERIFICATION_OK complete_graph_subsets={totals} canonical_supports_18={1<<18}')

if __name__=='__main__':
    run()
