"""Independent exact enumerator for degree-parity versus motif-count covariance.
Run using Python 3 standard library; no files or packages required.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import factorial

TEMPLATES = {
    'edge': (2, ((0,1),)),
    'path3': (3, ((0,1),(1,2))),
    'triangle': (3, ((0,1),(0,2),(1,2))),
    'path4': (4, ((0,1),(1,2),(2,3))),
    'cycle4': (4, ((0,1),(1,2),(2,3),(3,0))),
    'two_edges': (4, ((0,1),(2,3))),
    'complete4': (4, tuple(combinations(range(4),2))),
    'complete5': (5, tuple(combinations(range(5),2))),
}

def edge_masks(n, v, template_edges, edge_index):
    result=set()
    for injective in permutations(range(n), v):
        mask=0
        for a,b in template_edges:
            mask |= 1<<edge_index[tuple(sorted((injective[a], injective[b])))]
        result.add(mask)
    return tuple(sorted(result))

def direct_cov(n,p,patterns,edge_list):
    m=len(edge_list)
    total_odd=F(0); total_motif=F(0); total_joint=F(0)
    for g in range(1<<m):
        k=g.bit_count()
        w=p**k*(1-p)**(m-k)
        degrees=[0]*n
        for idx,(u,v) in enumerate(edge_list):
            if g&(1<<idx):
                degrees[u]+=1; degrees[v]+=1
        odd=sum(d%2 for d in degrees)
        copies=sum((g & pattern)==pattern for pattern in patterns)
        total_odd+=w*odd
        total_motif+=w*copies
        total_joint+=w*odd*copies
    return total_joint-total_odd*total_motif

def formula(n,p,v,template_edges,count):
    d=[0]*v
    for u,w in template_edges:
        d[u]+=1; d[w]+=1
    s=1-2*p
    e=len(template_edges)
    expected=F(count)*p**e
    return -(expected/F(2))*sum(((-1)**di)*s**(n-1-di)-s**(n-1) for di in d)

def run():
    checks=0
    observations=[]
    for n in range(2,6):
        edges=tuple(combinations(range(n),2))
        idx={e:i for i,e in enumerate(edges)}
        for name,(v,Hedges) in TEMPLATES.items():
            if v>n: continue
            patterns=edge_masks(n,v,Hedges,idx)
            for p in (F(1,4), F(2,5), F(1,2), F(3,5), F(3,4)):
                exact=direct_cov(n,p,patterns,edges)
                proposed=formula(n,p,v,Hedges,len(patterns))
                assert exact==proposed,(n,name,str(p),str(exact),str(proposed))
                checks+=1
                d=[0]*v
                for u,w in Hedges:
                    d[u]+=1;d[w]+=1
                if all(x%2==0 for x in d):
                    if p!=F(1,2): assert (exact>0)==(n%2==0 and p>F(1,2))
                    else: assert exact<=0
                    checks+=1
                if all(x%2==1 for x in d):
                    if p!=F(1,2): assert (exact>0)==(n%2==0 or p<F(1,2))
                    else: assert exact>=0
                    checks+=1
            if n==5 and name in ('complete5','triangle','two_edges'):
                observations.append((n,name,len(patterns),str(formula(n,F(1,2),v,Hedges,len(patterns)))))
    # Check derived explicit edge / cycle formulas for all n and representative p.
    for n in range(2,31):
        for p in (F(1,7), F(1,2), F(6,7)):
            edges_n=n*(n-1)//2
            actual=formula(n,p,2,TEMPLATES['edge'][1],edges_n)
            assert actual==n*(n-1)*p*(1-p)*(1-2*p)**(n-2)
            checks+=1
            if n>=3:
                cyc_cnt=n*(n-1)*(n-2)//6
                actual=formula(n,p,3,TEMPLATES['triangle'][1],cyc_cnt)
                assert actual==-n*(n-1)*(n-2)*p**4*(1-p)*(1-2*p)**(n-3)
                checks+=1
    # Derive exact p=1/2 boundary from degree n-1 factors (including K5, K4).
    for n,name in ((4,'complete4'),(5,'complete5')):
        v,Hedges=TEMPLATES[name]
        count=1
        cov=formula(n,F(1,2),v,Hedges,count)
        assert (cov>0 if n==4 else cov<0)
        checks+=1
    print('PASS',checks,'exact-rational identities and sign checks')
    print('Boundary illustrations:',observations)
if __name__=='__main__': run()
