"""Reproduce the character and homology calculation of Cl(J(n,3)).
Python 3 standard library only. No external input is needed.
"""
from itertools import combinations
from math import comb


def facets(n):
    triples = list(combinations(range(n), 3))
    stars = [frozenset(t for t in triples if set(p).issubset(t))
             for p in combinations(range(n), 2)]
    tops = [frozenset(t for t in triples if set(t).issubset(q))
            for q in combinations(range(n), 4)]
    return stars + tops


def faces(n):
    result = {()}
    for facet in facets(n):
        vertices = sorted(facet)
        for k in range(1, len(vertices)+1):
            result.update(combinations(vertices, k))
    return result


def sign_image(g, items):
    """Signed permutation of an invariant face (items canonical sorted)."""
    image = [tuple(sorted(g[v] for v in item)) for item in items]
    if sorted(image) != list(items):
        return 0
    return -1 if sum(image[i] > image[j]
                     for i in range(len(image)) for j in range(i+1, len(image))) % 2 else 1


def direct_character(n, g, face_set):
    value = -1  # reduced empty-simplex contribution
    for simplex in face_set:
        if not simplex:
            continue
        value += (-1 if len(simplex) % 2 == 0 else 1) * sign_image(g, simplex)
    return value


def predicted_character(n, g):
    # Relative top-simplex contribution: H1(K4) = C1(K4)-C0(K4)+1.
    relative = 0
    for q in combinations(range(n), 4):
        if tuple(sorted(g[i] for i in q)) != q:
            continue
        edges = tuple(combinations(q, 2))
        pairs_trace = sum((1 if g[e[0]] < g[e[1]] else -1)
                          for e in edges if tuple(sorted(g[i] for i in e)) == e)
        vertex_trace = sum(g[i] == i for i in q)
        relative += pairs_trace - vertex_trace + 1
    c2 = sum(sign_image(g, tuple(combinations(q, 2)))
             for q in combinations(range(n),3)
             if tuple(sorted(g[i] for i in q)) == q)
    # C1: for every distinguished central element i and unordered distinct a,b.
    c1 = 0
    for i in range(n):
        for a,b in combinations([j for j in range(n) if j != i],2):
            edge = tuple(sorted(((i,a) if i<a else (a,i), (i,b) if i<b else (b,i))))
            c1 += sign_image(g, edge)
    c0 = sum(tuple(sorted((g[a],g[b]))) == (a,b)
             for a,b in combinations(range(n),2))
    return relative+c2-c1+c0-1


def representative(n, partition):
    perm = list(range(n))
    offset = 0
    for length in partition:
        for i in range(length):
            perm[offset+i] = offset + (i+1)%length
        offset += length
    return tuple(perm)


def partitions(n, highest=None):
    if n == 0:
        yield ()
    else:
        for k in range(min(n, highest or n), 0, -1):
            for rest in partitions(n-k,k):
                yield (k,)+rest


def mod2_betti(n, face_set):
    by_size={}
    for f in face_set:
        by_size.setdefault(len(f),[]).append(f)
    ranks={}
    for k in range(1,max(by_size)+1):
        dest={face:i for i,face in enumerate(by_size.get(k-1,[]))}
        pivots={}
        for face in by_size.get(k,[]):
            column=0
            for i in range(k):
                column ^= 1 << dest[face[:i]+face[i+1:]]
            while column:
                p=column.bit_length()-1
                if p not in pivots:
                    pivots[p]=column
                    break
                column ^= pivots[p]
        ranks[k]=len(pivots)
    return {k-1:len(v)-ranks.get(k,0)-ranks.get(k+1,0)
            for k,v in by_size.items() if k>0}


def main():
    traces=0
    for n in range(5,9):
        fs=faces(n)
        for part in partitions(n):
            g=representative(n,part)
            lhs=direct_character(n,g,fs)
            rhs=predicted_character(n,g)
            if lhs!=rhs:
                raise AssertionError((n,part,lhs,rhs))
            traces+=1
        betti=mod2_betti(n,fs)
        want=3*comb(n,4)-2*comb(n,3)+comb(n,2)-1
        if betti.get(2,0) != want or any(v for k,v in betti.items() if k!=2):
            raise AssertionError((n,betti,want))
        print(f'n={n}: {len(fs)-1} nonempty simplices, beta_2={want}, {len(list(partitions(n)))} character checks')
    print(f'VERIFY_OK; {traces} class-character comparisons; integral proof not replaced by finite tests')


if __name__ == '__main__':
    main()
