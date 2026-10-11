"""Exact finite checks supporting a graph-square simplicial-collapse theorem.

Uses only the Python standard library. Computations supplement, but do not
replace, the all-parameter fold argument in the accompanying proof.
"""
from itertools import combinations


def original_edges(n):
    edges = set()
    def add(a,b):
        edges.add(tuple(sorted((a,b))))
    for i in range(n):
        add(i, (i+1)%n)
        add(i, n+i)
        add(n+i, n+(i+2)%n)
    return edges


def distance_two_adjacency(n):
    neigh = [set() for _ in range(2*n)]
    for a,b in original_edges(n):
        neigh[a].add(b); neigh[b].add(a)
    ans = [set() for _ in range(2*n)]
    for i in range(2*n):
        ans[i] = (neigh[i] | set().union(*(neigh[x] for x in neigh[i]))) - {i}
    return ans


def formula_adj(a,b,n):
    ta, ia = divmod(a,n)
    tb, ib = divmod(b,n)
    delta = (ib-ia)%n
    if a == b: return False
    if ta == 0 and tb == 0: return delta in (1,2,n-1,n-2)
    if ta == 1 and tb == 1: return delta in (2,4,n-2,n-4)
    return delta in (0,1,2,n-1,n-2)


def folds(i,n):
    U = lambda d: (i+d)%n
    V = lambda d: n+(i+d)%n
    if i <= 1:
        return [(U(1),U(0)),(U(2),V(2)),(U(0),V(-2)),
                (U(-2),V(-2)),(U(-1),V(-2)),(V(4),V(2)),
                (V(2),V(-2)),(V(-4),V(-2))]
    if i <= 3:
        return [(U(-1),U(0)),(U(1),U(0)),(U(2),V(2)),
                (V(4),V(2)),(V(2),U(0)),(U(0),U(-2)),
                (U(-2),V(-4))]
    if i <= n-5:
        return [(U(-2),U(-1)),(U(-1),U(0)),(U(0),U(1)),
                (U(1),U(2)),(U(2),V(2)),(V(2),V(4))]
    if i <= n-3:
        return [(U(-2),U(-1)),(U(-1),U(0)),(U(0),U(1)),
                (U(1),U(2)),(U(2),V(2))]
    return [(U(-2),U(-1)),(U(2),U(1)),
            (U(-1),U(0)),(U(1),U(0))]


def inner_link(i,n):
    S={(i+d)%n for d in (-2,-1,0,1,2)}
    S|={n+(i+d)%n for d in (-4,-2,2,4) if (i+d)%n >= i}
    return S


def check_folds(n):
    adj=distance_two_adjacency(n)
    for i in range(2*n):
        for j in range(i+1,2*n):
            assert (j in adj[i])==formula_adj(i,j,n),(n,i,j,'distance formula')
    counts=[0]*5
    for i in range(n):
        typ=0 if i<=1 else 1 if i<=3 else 2 if i<=n-5 else 3 if i<=n-3 else 4
        counts[typ]+=1
        actual={w for w in adj[n+i] if w<n or (w>=n and w-n>=i)}
        V=inner_link(i,n)
        assert V==actual,(n,i,'link',V,actual)
        fold=folds(i,n)
        assert len(fold)==len(V)-1,(n,i,'fold length')
        for a,b in fold:
            assert a in V and b in V,(n,i,a,b,'absent')
            a_closed=({a}|(adj[a]&V))
            b_closed=({b}|(adj[b]&V))
            assert a_closed <= b_closed,(n,i,a,b,'invalid fold',a_closed-b_closed)
            V.remove(a)
        assert len(V)==1,(n,i,'non-point link')
    return counts


def all_faces_from_adj(adj):
    N=len(adj)
    maximal=[]
    def bronkerbosch(R,P,X):
        if not P and not X:
            maximal.append(tuple(sorted(R)));return
        pivot=max((P|X),key=lambda v:len(P&adj[v]),default=None)
        eligible=(P-adj[pivot]) if pivot is not None else set(P)
        for v in sorted(eligible):
            bronkerbosch(R|{v},P&adj[v],X&adj[v]);P.remove(v);X.add(v)
    bronkerbosch(set(),set(range(N)),set())
    by_dim={}
    for maximal_clique in maximal:
        for k in range(1,len(maximal_clique)+1):
            for face in combinations(maximal_clique,k):
                by_dim.setdefault(k-1,set()).add(face)
    return {dim: sorted(v) for dim,v in by_dim.items()}


def gf2_rank(vectors):
    pivots={}
    for vec in vectors:
        while vec:
            leading=vec.bit_length()-1
            if leading not in pivots:
                pivots[leading]=vec;break
            vec ^= pivots[leading]
    return len(pivots)


def homology_n12():
    faces=all_faces_from_adj(distance_two_adjacency(12))
    dims=sorted(faces)
    assert dims==list(range(max(dims)+1))
    ranks=[1]
    for d in dims[1:]:
        previous={face:j for j,face in enumerate(faces[d-1])}
        columns=[]
        for f in faces[d]:
            x=0
            for k in range(len(f)):
                x ^= (1<<previous[f[:k]+f[k+1:]])
            columns.append(x)
        ranks.append(gf2_rank(columns))
    nums=[len(faces[d]) for d in dims]
    betti=[nums[d]-ranks[d]-(ranks[d+1] if d+1<len(nums) else 0) for d in dims]
    assert nums==[24,108,160,84,12],nums
    assert ranks==[1,23,85,72,12],ranks
    assert betti==[0,0,3,0,0],betti
    return nums,ranks,betti


def main():
    # Every local type is checked repeatedly at different modular wraparound sizes.
    folds_total=0
    for n in range(13,41):
        classes=check_folds(n)
        assert classes==[2,2,n-8,2,2],(n,classes)
        folds_total += n
    faces,ranks,betti=homology_n12()
    print('distance_formula_and_local_fold_sequence=PASS n=13..40')
    print('all_five_link_classes=PASS instances='+str(folds_total))
    print('n12_face_vector='+','.join(map(str,faces)))
    print('n12_reduced_boundary_ranks='+','.join(map(str,ranks)))
    print('n12_reduced_betti='+','.join(map(str,betti)))
    print('VERIFY_OK')

if __name__=='__main__':main()
