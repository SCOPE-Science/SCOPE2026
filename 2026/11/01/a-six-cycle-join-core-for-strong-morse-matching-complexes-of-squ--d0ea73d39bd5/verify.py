"""Exact finite checks for strong Morse complexes of one-vertex bouquets of squares.

Only the standard library is required. The all-parameter argument is in RESULT.md;
these computations independently validate the order classification for 1 <= k <= 3.
"""
import itertools
from collections import Counter, defaultdict


def graph(k):
    nbr = {v: set() for v in range(1 + 3*k)}
    for i in range(k):
        a, b, c = 3*i+1, 3*i+2, 3*i+3
        for u,v in ((0,a),(a,b),(b,c),(c,0)):
            nbr[u].add(v)
            nbr[v].add(u)
    return nbr


def order_facets(k):
    """Generate from ALL injective vertex orders, not the proposed local model."""
    nbr = graph(k)
    gradients = set()
    for order in itertools.permutations(nbr):
        preceding = set()
        pairs = set()
        for v in order:
            lower_neighbors = nbr[v] & preceding
            if len(lower_neighbors) == 1:
                pairs.add((v, next(iter(lower_neighbors))))
            preceding.add(v)
        gradients.add(frozenset(pairs))
    return {f for f in gradients if not any(f < g for g in gradients)}


def local_pieces(i):
    a,b,c=3*i+1,3*i+2,3*i+3
    e1,e2,e3,e4,e5,e6=(a,0),(b,a),(c,0),(b,c),(a,b),(c,b)
    # Six edges in the link-free local hexagon.
    L=[frozenset(x) for x in ((e1,e2),(e1,e3),(e3,e4),
                                  (e4,e5),(e5,e6),(e6,e2))]
    # A three-edge path when the shared vertex precedes both adjacent ends.
    H=L[:3]
    # Three isolated vertices in either link of a shared-vertex pairing.
    T={(0,a):[e2,e3,e5], (0,c):[e6,e1,e4]}
    return L,H,T


def predicted_facets(k):
    pieces=[local_pieces(i) for i in range(k)]
    ans=set()
    for selected in itertools.product(*(pc[0] for pc in pieces)):
        ans.add(frozenset().union(*selected))
    for i,(_,_,Ti) in enumerate(pieces):
        others=[pieces[j][1] for j in range(k) if j!=i]
        for central,choices in Ti.items():
            for small in choices:
                for selected in itertools.product(*others):
                    ans.add(frozenset({central,small}).union(*selected))
    return ans


def faces(facets):
    out={frozenset()}
    for facet in facets:
        for n in range(1,len(facet)+1):
            out.update(frozenset(sub) for sub in itertools.combinations(facet,n))
    return out


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def model_face_numbers(k):
    L=[1,6,6]
    H=[1,4,3]
    p=[1]
    for _ in range(k):p=mul(p,L)
    h=[1]
    for _ in range(k-1):h=mul(h,H)
    added=mul([0,1],mul([1,3],h))
    for j,x in enumerate(added):p[j]+=2*k*x
    return p


def ranks_mod_two(all_faces):
    by_dim=defaultdict(list)
    for f in all_faces:
        if f:by_dim[len(f)-1].append(f)
    boundary_rank={}
    for dim in range(1,max(by_dim)+1):
        idx={f:j for j,f in enumerate(by_dim[dim-1])}
        basis={}
        for simplex in by_dim[dim]:
            column=sum(1 << idx[simplex-{v}] for v in simplex)
            while column:
                pivot=column.bit_length()-1
                if pivot not in basis:
                    basis[pivot]=column
                    break
                column ^=basis[pivot]
        boundary_rank[dim]=len(basis)
    betti={d:len(chain)-boundary_rank.get(d,0)-boundary_rank.get(d+1,0)
           for d,chain in by_dim.items()}
    return betti


def elementary_collapse_to_noncentral(facets,k):
    """Explicit, fully checked free codimension-one pairs, k=2,3."""
    current=set(faces(facets))-{frozenset()}
    central={(0,3*i+1) for i in range(k)}|{(0,3*i+3) for i in range(k)}
    removed=0
    while any(face & central for face in current):
        cofaces=defaultdict(list)
        for face in current:
            if len(face)<2:continue
            for v in face:
                sub=face-{v}
                if sub & central and sub in current:
                    cofaces[sub].append(face)
        free=[(sub,co[0]) for sub,co in cofaces.items() if len(co)==1
              and not any(co[0]<other for other in current)]
        assert free, 'Unable to remove all shared-vertex pairs by free faces'
        lower,upper=max(free,key=lambda pair:(len(pair[0]),tuple(sorted(pair[0]))))
        assert len(upper)==len(lower)+1 and lower < upper
        assert all(not lower < other for other in current if other!=upper), (lower,upper)
        current.remove(lower)
        current.remove(upper)
        removed+=1
    expected={f for f in faces(frozenset().union(*sel)
             for sel in itertools.product(*(local_pieces(i)[0] for i in range(k)))) if f}
    assert current == expected
    return removed


def main():
    for k in (1,2,3):
        observed=order_facets(k)
        predicted=predicted_facets(k)
        assert observed==predicted, (k,len(observed),len(predicted))
        ff=faces(observed)
        counts=Counter(len(f) for f in ff)
        theoretical=model_face_numbers(k)
        assert [counts[i] for i in range(len(theoretical))]==theoretical
        assert len(observed)==6**k+2*k*3**k
        b=ranks_mod_two(ff)
        expected_top = 2*k-1
        expected_rank = 5 if k==1 else 1
        assert b[0]==1
        assert all(b.get(i,0)==(expected_rank if i==expected_top else 0)
                   for i in range(1,max(b)+1)), b
        if k>=2:
            matched=elementary_collapse_to_noncentral(observed,k)
            print('COLLAPSE_OK',k,matched)
        print('ORDER_MODEL_FACES_HOMOLOGY_OK',k,'facets',len(observed),
              'face_counts',theoretical,'mod2_betti',b)
    print('ALL_VERIFY_OK')


if __name__=='__main__':
    main()
