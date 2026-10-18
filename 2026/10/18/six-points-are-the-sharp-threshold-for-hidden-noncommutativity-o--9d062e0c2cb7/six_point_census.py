"""Six-point complete census up to simultaneous conjugacy for two bijections."""
from collections import Counter, defaultdict
from itertools import permutations


def partitions(total, at_least=1):
    if total == 0:
        yield ()
        return
    for first in range(at_least, total + 1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def standard_permutation(parts):
    n = sum(parts)
    f = list(range(n))
    begin = 0
    for length in parts:
        for j in range(length):
            f[begin + j] = begin + (j + 1) % length
        begin += length
    return tuple(f)


def commute(f, g):
    return all(f[g[x]] == g[f[x]] for x in range(len(f)))


def colored_masks(f, g):
    n = len(f)
    fi, gi = [0]*n, [0]*n
    for x in range(n):
        fi[f[x]], gi[g[x]] = x, x
    return [[16*(x == y) + (f[x] == y) + 2*(g[x] == y)
             + 4*(fi[x] == y) + 8*(gi[x] == y)
             for y in range(n)] for x in range(n)]


def stable_quotient(f, g):
    """Canonical quotient of the coarsest pair-atomic-type equitable partition."""
    n = len(f)
    masks = colored_masks(f, g)
    colors = (0,) * n
    for _ in range(n + 2):
        signatures = []
        for x in range(n):
            tally = Counter((colors[y], masks[x][y]) for y in range(n))
            signatures.append((colors[x], tuple(sorted(tally.items()))))
        palette = {k: i for i, k in enumerate(sorted(set(signatures)))}
        following = tuple(palette[k] for k in signatures)
        if following == colors:
            counts = Counter(colors)
            quotient = []
            for c in sorted(counts):
                x = colors.index(c)
                tally = Counter((colors[y], masks[x][y]) for y in range(n))
                quotient.append((counts[c], tuple(sorted(tally.items()))))
            return tuple(quotient)
        assert len(set(following)) >= len(set(colors))
        colors = following
    raise AssertionError('refinement did not stabilize')


def joint_equivalence(first, second):
    (f,g), (h,k) = first,second
    n = len(f)
    bigf = tuple(f) + tuple(n+v for v in h)
    bigg = tuple(g) + tuple(n+v for v in k)
    masks = colored_masks(bigf,bigg)
    colors = (0,) * (2*n)
    for _ in range(2*n+2):
        signatures=[]
        for x in range(2*n):
            tallies=Counter((colors[y],masks[x][y]) for y in range(2*n))
            signatures.append((colors[x],tuple(sorted(tallies.items()))))
        palette={s:i for i,s in enumerate(sorted(set(signatures)))}
        updated=tuple(palette[s] for s in signatures)
        if updated==colors:
            return Counter(colors[:n])==Counter(colors[n:])
        colors=updated
    raise AssertionError('joint refinement did not stabilize')


def conjugate(g, h):
    n=len(g)
    inv=[0]*n
    for x,y in enumerate(h):inv[y]=x
    return tuple(h[g[inv[i]]] for i in range(n))


def main():
    n = 6
    all_g = list(permutations(range(n)))
    grouped = defaultdict(lambda: {'commuting':[], 'noncommuting':[]})
    total_presentations=0
    canonical_representatives=0
    for shape in partitions(n):
        f=standard_permutation(shape)
        centralizer=[h for h in all_g if commute(f,h)]
        for g in all_g:
            key=stable_quotient(f,g)
            name='commuting' if commute(f,g) else 'noncommuting'
            total_presentations+=1
            if g==min(conjugate(g,h) for h in centralizer):
                grouped[key][name].append((shape,f,g))
                canonical_representatives+=1
    ambiguous=[(q,entry) for q,entry in grouped.items()
               if entry['commuting'] and entry['noncommuting']]
    ambiguous.sort(key=lambda x:x[0])
    assert total_presentations==7920
    assert canonical_representatives==901
    assert len(grouped)==860
    assert len(ambiguous)==3
    print('presentations:',total_presentations)
    print('simultaneous_conjugacy_classes:',canonical_representatives)
    print('stable_C2_quotient_signatures:',len(grouped))
    print('mixed_C2_quotient_signatures:',len(ambiguous))
    for i,(q,entry) in enumerate(ambiguous,1):
        cc=len(entry['commuting']);nn=len(entry['noncommuting'])
        assert (cc,nn) in [(2,2),(4,3)]
        for a in entry['commuting']:
            for b in entry['noncommuting']:
                assert joint_equivalence((a[1],a[2]),(b[1],b[2]))
        print(f'mixed_class_{i}: quotient={q}, commuting_types={cc}, noncommuting_types={nn}')
        print('  canonical_commuting_pairs=', [(a[1],a[2]) for a in entry['commuting']])
        print('  canonical_noncommuting_pairs=', [(a[1],a[2]) for a in entry['noncommuting']])
    assert sorted((len(x['commuting']),len(x['noncommuting']))
                  for _,x in ambiguous)==[(2,2),(2,2),(4,3)]
    print('SIX_POINT_CENSUS_PASS')


if __name__=='__main__':
    main()
