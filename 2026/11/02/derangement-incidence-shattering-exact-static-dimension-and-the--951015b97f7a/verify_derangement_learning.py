"""Reproducible exact tests for derangement edge-membership shattering.
Run: python verify_derangement_learning.py derangement_depth4_witness.json
"""
import itertools,json,sys

def concepts(n):
    return [p for p in itertools.permutations(range(n)) if all(p[i]!=i for i in range(n))]

def vc_dim(ps,n):
    edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
    rows=[sum(1<<a for a,e in enumerate(edges) if p[e[0]]==e[1]) for p in ps]
    best=0
    for k in range(1,n):
        good=False
        for subset in itertools.combinations(range(len(edges)),k):
            pat={sum((int(bool(b&(1<<a)))<<c) for c,a in enumerate(subset)) for b in rows}
            if len(pat)==(1<<k):
                good=True;break
        if not good:break
        best=k
    return best

def check_tree(node,history,remaining):
    if 'permutation' in node:
        p=tuple(node['permutation'])
        assert p in remaining
        assert all(int(p[i]==j)==bit for (i,j),bit in history)
        return [p]
    i,j=node['query']
    assert i!=j
    zeros=[p for p in remaining if p[i]!=j]
    ones=[p for p in remaining if p[i]==j]
    assert zeros and ones
    a=check_tree(node['zero'],history+[((i,j),0)],zeros)
    b=check_tree(node['one'],history+[((i,j),1)],ones)
    assert len(a)==len(b)
    return a+b

for n in range(2,6):
    ps=concepts(n)
    vc=vc_dim(ps,n)
    assert vc==max(0,n-2),(n,vc)
    print('exact_VC',n,len(ps),vc)

for n in range(3,9):
    ps=concepts(n)
    S=[(i,(i+1)%n) for i in range(n-2)]
    pats={tuple(int(p[i]==j) for i,j in S) for p in ps}
    assert len(pats)==2**(n-2),(n,len(pats))
    print('cyclic_support',n,len(ps),len(pats))

ps=concepts(5)
assert len(ps)==44
for i in range(5):
    for j in range(5):
        if i!=j:
            assert sum(p[i]==j for p in ps)==11
w=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'derangement_depth4_witness.json'))
leaves=check_tree(w,[],ps)
assert len(leaves)==16 and len(set(leaves))==16
print('adaptive_depth4_leaf_witnesses',len(leaves))
print('upper_depth5_by_branch_size',11,'<',16)
print('DERANGEMENT_SHATTERING_ALL_CHECKS_PASS')
