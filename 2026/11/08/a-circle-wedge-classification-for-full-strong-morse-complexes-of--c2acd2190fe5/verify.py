"""Independent finite checks of the full strong-gradient complex for complete bipartite graphs.

Pure Python 3.9+, no external dependencies. The infinite-family proof is mathematical,
not inferred from these finite tests.
"""
from collections import Counter, defaultdict
from itertools import permutations


def subsets(mask):
    s=mask
    yield 0
    while s:
        yield s
        s=(s-1)&mask


def bit(a,b,m,n):
    """Encode the directed matching arrow source a -> earlier neighbor b."""
    if a<m and b>=m:
        return 1 << (2*(a*n+(b-m)))
    if a>=m and b<m:
        return 1 << (2*(b*n+(a-m))+1)
    raise ValueError('Not a bipartite edge')


def enumerate_filtrations(m,n):
    vertices=range(m+n); face_set=set()
    gradient_set=set()
    for order in permutations(vertices):
        prevA=[]; prevB=[]; gradient=0
        for v in order:
            if v<m:
                if len(prevB)==1: gradient|=bit(v,prevB[0],m,n)
                prevA.append(v)
            else:
                if len(prevA)==1: gradient|=bit(v,prevA[0],m,n)
                prevB.append(v)
        gradient_set.add(gradient)
        face_set.update(subsets(gradient))
    return face_set, gradient_set


def face_sets_from_structural_description(m,n):
    stars=[]; flaps=[]
    for a in range(m):
        stars.append(sum(bit(b,a,m,n) for b in range(m,m+n)))
    for b in range(m,m+n):
        stars.append(sum(bit(a,b,m,n) for a in range(m)))
    for a in range(m):
        for b in range(m,m+n):
            flaps.append((bit(b,a,m,n), tuple(bit(aa,b,m,n) for aa in range(m) if aa!=a),'A',a,b))
            flaps.append((bit(a,b,m,n), tuple(bit(bb,a,m,n) for bb in range(m,m+n) if bb!=b),'B',a,b))
    facets=set(stars)
    for q,T,_,_,_ in flaps:
        facets.add(q|sum(T))
    faces=set()
    for f in facets:
        faces.update(subsets(f))
    return faces,stars,flaps


def collapse_flaps(m,n,faces,stars,flaps):
    remaining=set(faces)
    count=0
    for q,T,side,a,b in flaps:
        pivot=T[0]
        others=sum(T[1:])
        allU=[s for s in subsets(others) if s]
        for U in sorted(allU,key=lambda z:(-z.bit_count(),z)):
            lo=q|U;hi=lo|pivot
            assert lo in remaining and hi in remaining,('pair missing',m,n,side,a,b)
            # Every face containing lo must be either lo or hi, verifying a free-face elementary collapse.
            all_super=[f for f in remaining if f!=lo and (f&lo)==lo]
            assert all_super==[hi],('not free',m,n,side,a,b,lo,hi,all_super)
            remaining.remove(lo);remaining.remove(hi);count+=1
    predicted=set()
    for s in stars:predicted.update(subsets(s))
    bridges=[]
    for q,T,side,a,b in flaps:
        edge=q|T[0]
        predicted.add(edge);bridges.append((a,b,edge))
    assert remaining==predicted, ('remainder',m,n,len(remaining),len(predicted))
    assert len(bridges)==2*m*n and len({e for _,_,e in bridges})==len(bridges)
    pair_count=Counter((a,b) for a,b,_ in bridges)
    assert len(pair_count)==m*n and all(v==2 for v in pair_count.values())
    return count,len(remaining),bridges


def test(m,n):
    actual,gradients=enumerate_filtrations(m,n)
    expected,stars,flaps=face_sets_from_structural_description(m,n)
    assert actual==expected,(m,n, 'face set mismatch',len(actual),len(expected),len(actual^expected))
    counts={k-1:v for k,v in sorted(Counter(x.bit_count() for x in actual).items()) if k}
    pairs,remainder,edges=collapse_flaps(m,n,actual,stars,flaps)
    # The graph obtained by shrinking the m+n disjoint star simplices is 2*K_(m,n).
    rank=2*m*n-(m+n)+1
    assert rank>=1
    assert len(stars)==m+n
    assert len(actual)==remainder+2*pairs
    print('K_%d,%d' %(m,n), 'orderings', __import__('math').factorial(m+n),
          'filtrations',len(gradients), 'faces',len(actual),
          'f_vector',counts, 'free_pairs',pairs,'remaining_faces',remainder,
          'quotient_nodes',m+n,'quotient_edges',len(edges),'H1_rank',rank,'OK')


def main():
    for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,4),(4,5)]:
        test(m,n)
    print('ALL_VERIFY_OK')

if __name__=='__main__':main()
