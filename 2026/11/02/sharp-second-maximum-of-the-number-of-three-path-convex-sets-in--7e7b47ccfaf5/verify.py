"""Exhaustive finite base case for the number of three-path-convex vertex sets.

Enumerates all unlabelled trees to order 9 by leaf extension and a rooted-tree
isomorphism invariant. Counts convex subsets using the defining local condition.
"""
from collections import Counter

def canonical_tree_code(edges, n):
    adj = [[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)
    def code(v, parent):
        pieces = sorted(code(w,v) for w in adj[v] if w != parent)
        return '(' + ''.join(pieces) + ')'
    return min(code(v,-1) for v in range(n))

def enumerate_trees(N):
    trees = {1:[()]}
    for n in range(2,N+1):
        seen = {}
        for E in trees[n-1]:
            for v in range(n-1):
                F = E + ((v,n-1),)
                seen.setdefault(canonical_tree_code(F,n), F)
        trees[n] = list(seen.values())
    return trees

def convex_set_count(edges,n):
    adj = [0]*n
    for a,b in edges:
        adj[a] |= 1<<b
        adj[b] |= 1<<a
    total=0
    for S in range(1<<n):
        if all((S>>v)&1 or (S&adj[v]).bit_count()<=1 for v in range(n)):
            total+=1
    return total

def classify(edges,n):
    deg = [0]*n
    for a,b in edges:
        deg[a]+=1
        deg[b]+=1
    return tuple(sorted(deg,reverse=True))

def run():
    trees = enumerate_trees(9)
    expected = [1,1,1,2,3,6,11,23,47]
    assert [len(trees[n]) for n in range(1,10)] == expected
    for n in range(6,10):
        sample = sorted(((convex_set_count(E,n),classify(E,n),E) for E in trees[n]), reverse=True)
        stars=[x for x in sample if x[1][0] == n-1]
        nonstars=[x for x in sample if x[1][0] < n-1]
        assert len(stars)==1
        best=max(x[0] for x in nonstars)
        matches=[x for x in nonstars if x[0]==best]
        expected_best={6:37,7:65,8:114,9:208}[n]
        assert best==expected_best
        assert len(matches)==1
        if n==9:
            assert matches[0][1]==(n-2,2)+(1,)*(n-2)
        print('n',n,'nonisomorphic_trees',len(sample),'max_nonstar',best,'uniquely_attained',matches[0][1])
    print('FINITE_BASE_OK')
if __name__=='__main__':run()

def broom_edges(n):
    # hub=0, exceptional middle=1, exceptional end=2; leaves 3,...,n-1.
    return [(0,1),(1,2)] + [(0,j) for j in range(3,n)]

def adj_masks(E,n):
    a=[0]*n
    for x,y in E: a[x]|=1<<y; a[y]|=1<<x
    return a

def profile(E,n,v):
    a=adj_masks(E,n); A=D=0
    for S in range(1<<n):
        if not all((S>>u)&1 or (S&a[u]).bit_count()<=1 for u in range(n)):
            continue
        if (S>>v)&1: A+=1
        elif (S&a[v]).bit_count()==1: D+=1
    return A,D

def extra_checks():
    trees=enumerate_trees(9)
    for E in trees[5]:
        for v in range(5):
            assert profile(E,5,v)[0]>=8
    print('ROOTED_CONTAINING_LEMMA_BASE_OK',len(trees[5]))
    for m in range(6,10):
        for E in trees[m]:
            if max(classify(E,m))==m-1:continue
            for v in range(m):
                assert profile(E,m,v)[1]>=2*m-4
                F=E+((v,m),)
                assert convex_set_count(F,m+1)==2*convex_set_count(E,m)-profile(E,m,v)[1]
    print('DEFECT_AND_LEAF_IDENTITY_OK lengths_6_to_9')
    for m in range(6,14):
        E=broom_edges(m)
        assert convex_set_count(E,m)==3*2**(m-3)+2*m-2
        predicted=[2*m-4,2**(m-3)+m-2,2**(m-3)+1]+[3*2**(m-4)]*(m-3)
        for v in range(m): assert profile(E,m,v)[1]==predicted[v],(m,v)
    print('BROOM_CLOSED_FORMS_OK lengths_6_to_13')
    # Verify graph extension via the star plus exactly one edge.
    for n in range(6,14):
        H=[(0,i) for i in range(1,n)]+[(1,2)]
        assert convex_set_count(H,n)==2**(n-2)+n
    print('ONE_EXTRA_EDGE_FORMULA_OK lengths_6_to_13')
    print('ONE_PASS')

if __name__=='__main__':extra_checks()
