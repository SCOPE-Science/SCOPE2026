"""Reproducible finite checks for edge-query shattering by Eulerian orientations.
Python 3 standard library only; this script verifies finite examples, not the all-n proof.
"""
from itertools import combinations


def edges(n):
    return tuple(combinations(range(n), 2))


def cuts(n):
    ee = edges(n)
    for mask in range(1, 1 << (n-1)):
        yield tuple(i for i, (u,v) in enumerate(ee) if bool(mask & (1 << u)) != bool(mask & (1 << v)))


def cut_condition(n, picked):
    chosen = set(picked)
    return all(2*sum(i in chosen for i in cut) <= len(cut) for cut in cuts(n))


def selected_cliques(n):
    m=(n-1)//2; ee=edges(n)
    return frozenset(i for i,(u,v) in enumerate(ee) if (u<m)==(v<m))


def regular_tournaments(n):
    ee=edges(n)
    result=[]
    for bits in range(1 << len(ee)):
        out=[0]*n
        for i,(u,v) in enumerate(ee):
            if bits >> i & 1:out[u]+=1
            else:out[v]+=1
        if all(x==(n-1)//2 for x in out):result.append(bits)
    return result


def shattered(n, hypotheses, picked):
    qs=tuple(sorted(picked))
    patterns={sum(((h>>q)&1)<<j for j,q in enumerate(qs)) for h in hypotheses}
    return len(patterns)==(1<<len(qs))


def main():
    for n in (3,5,7,9,11):
        picked=selected_cliques(n)
        assert len(picked)==((n-1)//2)**2
        assert cut_condition(n, picked)
        print(f'K{n}: two-clique support {len(picked)}, all {2**(n-1)-1} nontrivial cuts checked')

    for n in (3,5):
        hyp=regular_tournaments(n)
        m=(n-1)//2
        assert len(hyp)==({3:2, 5:24}[n])
        total=1<<len(edges(n));sh=[]
        for s in range(total):
            picked=frozenset(i for i in range(len(edges(n))) if s>>i&1)
            witness=shattered(n,hyp,picked)
            criterion=cut_condition(n,picked)
            assert witness==criterion,(n,s,witness,criterion)
            if witness: sh.append(picked)
        maximum=max(map(len,sh))
        maxsets={s for s in sh if len(s)==maximum}
        extremal=set()
        for first in combinations(range(n),m):
            A=set(first)
            supp=frozenset(i for i,(u,v) in enumerate(edges(n)) if (u in A)==(v in A))
            extremal.add(supp)
        assert maximum==m*m
        assert maxsets==extremal
        print(f'K{n}: {len(hyp)} balanced orientations; {total} supports tested; '
              f'maximum {maximum}; {len(maxsets)} maximizers, all exactly the two-clique partitions')
    print('ALL_EULERIAN_VC_TESTS_PASS')

if __name__ == '__main__':main()
