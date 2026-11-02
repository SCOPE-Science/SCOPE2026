"""Independent exhaustive verifier for the finite ternary betweenness certificates.
Usage: python verify_certificate.py certificates.json
Does not use the certificate construction algorithm.
"""
import sys,json,itertools,math
from pathlib import Path


def query_list(n):
    return [x for t in itertools.combinations(range(n),3)
            for x in ((t[0],t[1],t[2]),(t[1],t[0],t[2]),(t[0],t[2],t[1]))]

def canonical_orders(n):
    return [p for p in itertools.permutations(range(n)) if p[0]<p[-1]]

def evalq(p,trip):
    # deliberately independent of constructing query masks
    a,b,c=trip
    return (p.index(a)<p.index(b)<p.index(c)) or (p.index(c)<p.index(b)<p.index(a))

def verify_one(e):
    n,d=e['n'],e['depth']
    ps=canonical_orders(n)
    qs=query_list(n)
    nodes=e['node_queries']; leaves=e['leaf_permutation_indices']
    assert len(nodes)==2**d-1 and len(leaves)==2**d
    assert len(set(ps))==math.factorial(n)//2
    assert all(0<=j<len(qs) for j in nodes)
    assert all(0<=j<len(ps) for j in leaves)
    assert len(set(leaves))==len(leaves), 'witnesses of distinct leaves cannot coincide'
    for k,pidx in enumerate(leaves):
        p=ps[pidx]
        node=1
        for shift in range(d-1,-1,-1):
            required_yes=not bool((k>>shift)&1)
            assert evalq(p,qs[nodes[node-1]])==required_yes, (n,k,node)
            node=node*2+(0 if required_yes else 1)
    # Each possible query is a middle-of-three assertion, hence 1/3 true.
    for q in qs:
        assert sum(evalq(p,q) for p in ps)==math.factorial(n)//6
    max_possible=1+int(math.log2(math.factorial(n)//6))
    assert max_possible==d,(n,d,max_possible)
    print('TREE_OK',n,'dimension',d,'leaf_witnesses',len(leaves),'concepts',len(ps),'root_positive',math.factorial(n)//6)


def vc(n):
    ps=canonical_orders(n);qs=query_list(n)
    positive=[]
    for q in qs:
        m=0
        for i,p in enumerate(ps):
            if evalq(p,q):m|=1<<i
        positive.append(m)
    full=(1<<len(ps))-1
    max_dimension=0;witness=[];counts={}
    def rec(start,cells,picks):
        nonlocal max_dimension,witness
        k=len(picks);counts[k]=counts.get(k,0)+1
        if k>max_dimension:
            max_dimension=k;witness=picks
        for j in range(start,len(qs)):
            q=positive[j]; new=[]
            for cell in cells:
                yes=cell&q
                if yes==0 or yes==cell: break
                new.extend((yes,cell^yes))
            else:
                rec(j+1,new,picks+[j])
    rec(0,[full],[])
    return max_dimension,counts,[qs[j] for j in witness]


def main():
    rows=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    assert rows['schema']=='ternary_betweenness_trees_v1'
    assert [(x['n'],x['depth']) for x in rows['entries']]==[(3,1),(4,3),(5,5),(6,7),(7,10),(8,13)]
    for x in rows['entries']:verify_one(x)
    for n,expected in [(3,1),(4,2),(5,4),(6,6)]:
        observed,counts,witness=vc(n)
        assert observed==expected,(n,observed,expected)
        print('VC_OK',n,'dimension',observed,'tested_supports',counts,'witness_queries',witness)
    print('BETWEENNESS_CERTIFICATE_AND_STATIC_CHECKS_PASS')
if __name__=='__main__':main()
