"""Exact verification of indegree-deficiency / directed-cycle covariance identities.
Standard library only; no external datasets.
"""
from itertools import combinations, product, permutations
from fractions import Fraction as F
from math import factorial

def cycles(n):
    out={j:[] for j in range(2,n+1)}
    verts=range(n)
    for ell in range(2,n+1):
        for subset in combinations(verts,ell):
            start=subset[0]
            for rem in permutations(subset[1:]):
                seq=(start,)+rem
                out[ell].append(tuple((seq[i],seq[(i+1)%ell]) for i in range(ell)))
    return out

def test(n,k):
    row_options=[list(combinations((j for j in range(n) if j!=i),k)) for i in range(n)]
    M=1
    for r in row_options: M*=len(r)
    cs=cycles(n)
    Z=0; C={l:0 for l in cs}; ZC={l:0 for l in cs}
    for selected in product(*row_options):
        indeg=[0]*n
        for r in selected:
            for v in r:indeg[v]+=1
        z=sum(x==0 for x in indeg)
        Z+=z
        for ell, clist in cs.items():
            c=sum(all(v in selected[u] for u,v in cyc) for cyc in clist)
            C[ell]+=c
            ZC[ell]+=z*c
    p=F(k,n-1);q=1-p
    Ncycle=lambda ell: F(factorial(n),ell*factorial(n-ell))
    assert F(Z,M)==n*q**(n-1),(n,k,'z')
    for ell in cs:
        assert F(C[ell],M)==Ncycle(ell)*p**ell,(n,k,ell,'cycles')
        cov=F(ZC[ell],M)-F(Z,M)*F(C[ell],M)
        formula=Ncycle(ell)*p**ell*q**(n-1)*(F(n-ell)*(F(n-1,n-2)**ell)-n)
        assert cov==formula,(n,k,ell,cov,formula)
        if 1<=k<=n-2:
            assert (cov>0 if ell==2 else cov<0),(n,k,ell,cov)
    return M,len(cs)

if __name__=='__main__':
    num=0
    for n in range(3,7):
        for k in range(1,n):
            if n>=6 and k>1:continue
            M,ls=test(n,k)
            print('EXACT_ENUMERATION_PASS',n,k,M,ls)
            num+=1
    print('EXACT_ENUMERATION_CASES',num)
    # Independent Bernoulli-arc comparison, independent of row-conditioned counting.
    n=4
    P=F(1,3)
    ce=cycles(n)
    arc=[(i,j) for i in range(n) for j in range(n) if i!=j]
    meanZ=F(0);meanC={l:F(0) for l in ce};cross={l:F(0) for l in ce}
    for mask in range(1<<len(arc)):
        A={arc[i] for i in range(len(arc)) if mask>>i&1}
        prob=P**len(A)*(1-P)**(len(arc)-len(A))
        indeg=[0]*n
        for i,j in A:indeg[j]+=1
        z=sum(x==0 for x in indeg)
        meanZ+=z*prob
        for ell,clist in ce.items():
            c=sum(all(e in A for e in cyc) for cyc in clist)
            meanC[ell]+=prob*c
            cross[ell]+=prob*z*c
    for ell in ce:
        assert cross[ell]-meanZ*meanC[ell]==-F(factorial(n),factorial(n-ell))*P**ell*(1-P)**(n-1)
    print('EXACT_BERNOULLI_ENUMERATION_PASS',n,len(arc),'arcs')
    print('VERIFY_OK')
