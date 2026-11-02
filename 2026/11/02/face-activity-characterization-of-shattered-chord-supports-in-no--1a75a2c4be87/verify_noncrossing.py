"""Reproduce finite checks for shattering by noncrossing perfect matchings.

No external packages or files are required. Run with Python 3.10+.
"""
from functools import lru_cache
from itertools import combinations

@lru_cache(maxsize=None)
def matchings(vertices):
    if not vertices:
        return ((),)
    out = []
    for j in range(1, len(vertices), 2):
        a, b = vertices[0], vertices[j]
        for left in matchings(vertices[1:j]):
            for right in matchings(vertices[j+1:]):
                out.append(((a, b),) + left + right)
    return tuple(out)


def noncrossing(S):
    for (a,b),(c,d) in combinations(S,2):
        if len({a,b,c,d})<4 or a<c<b<d or c<a<d<b:
            return False
    return True


def active_face_test(S,n):
    occupied = {v for pair in S for v in pair}
    unmatched = set(range(2*n)) - occupied
    for e in S:
        others = tuple(t for t in S if t != e)
        def region_signature(v):
            return tuple(a<v<b for a,b in others)
        target = region_signature(e[0])
        assert region_signature(e[1]) == target
        if not any(region_signature(v) == target for v in unmatched):
            return False
    return True


def enumerate_supports(n):
    concepts = matchings(tuple(range(2*n)))
    edges = sorted({e for matching in concepts for e in matching})
    incidence = {e:sum(1<<j for j,M in enumerate(concepts) if e in M) for e in edges}
    allconcepts = (1<<len(concepts))-1
    counts=[]
    candidates=0
    for k in range(n+1):
        n_shattered=0
        for S in combinations(edges,k):
            if not noncrossing(S):
                continue
            positive=allconcepts
            for e in S:
                positive &= incidence[e]
            if not positive:
                continue
            candidates+=1
            predicted=(k<n and active_face_test(S,n)) or k==0
            # Independent direct projection of every perfect matching; no
            # geometric-face reasoning is used by this side of the test.
            observed = {
                sum((1<<j) for j,e in enumerate(S) if e in M)
                for M in concepts
            }
            actual=(len(observed)==(1<<k))
            assert predicted==actual,(n,S,predicted,actual)
            if actual:
                n_shattered+=1
        counts.append(n_shattered)
    return counts,candidates,len(concepts)


def rotate_matching(M,n):
    return frozenset(tuple(sorted(((a+1)%(2*n),(b+1)%(2*n)))) for a,b in M)


def rotation_check():
    count=0
    for n in range(2,8):
        c=matchings(tuple(range(2*n)))
        allc={frozenset(M) for M in c}
        for M in c:
            R=rotate_matching(M,n)
            assert R in allc
            assert not (R & frozenset(M)),(n,M,R)
            count+=1
    return count


def ldim_small(n):
    C=matchings(tuple(range(2*n)))
    edges=sorted({e for M in C for e in M})
    inc=tuple(sum(1<<j for j,M in enumerate(C) if e in M) for e in edges)
    allmask=(1<<len(C))-1
    @lru_cache(maxsize=None)
    def d(subset):
        if subset.bit_count()<2: return 0
        best=0
        for a in inc:
            yes=subset&a;no=subset & (allmask^a)
            if yes and no:
                best=max(best,1+min(d(yes),d(no)))
        return best
    return d(allmask)


def main():
    expected = {
        1:[1,0],
        2:[1,4,0],
        3:[1,9,9,0],
        4:[1,16,48,16,0],
        5:[1,25,140,185,25,0],
        6:[1,36,318,860,567,36,0],
    }
    total=0
    for n in range(1,7):
        counts,candidates,concepts=enumerate_supports(n)
        assert counts==expected[n],(n,counts)
        assert counts[-2 if n>1 else 0]==n*n
        total+=candidates
        print('n={} matchings={} positive-compatible-supports={} shattered={}'.format(n,concepts,candidates,counts))
    rot=rotation_check()
    ldim=[ldim_small(n) for n in range(1,6)]
    assert ldim==[0,1,2,3,4],ldim
    print('rotated-edge-disjoint matchings checked={}'.format(rot))
    print('exact Littlestone dimensions n=1..5={}'.format(ldim))
    print('positive-compatible-supports checked={}'.format(total))
    print('NONCROSSING_SHATTERING_ALL_CHECKS_PASS')

if __name__=='__main__':main()
