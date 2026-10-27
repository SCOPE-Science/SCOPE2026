"""Independent exact checks of degree-one / non-induced motif-count covariances.
Only standard library. Run: python verify_degree_one_motifs.py"""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb

def ff(a,r):
    out=1
    for j in range(r):out*=a-j
    return out

def normalized(n,m,k,h,ell):
    """E[L1 X_H]/(E[L1] E[X_H]); defined for h<=m<=U."""
    N=comb(n,2); U=comb(n-1,2)
    assert 2<=k<=n and 1<=h<=m<=U and 0<=ell<=k and h<=U
    A=Fraction(ff(N,h),ff(U,h))
    return A*Fraction((n-k)*(m-h),n*m) + A*Fraction(ell*(U-h+1),n*(n-1)*m)

def expectation_cov(n,m,k,h,ell):
    N=comb(n,2);U=comb(n-1,2)
    if not (h<=m<=U):return None
    q=Fraction((n-1)*comb(U,m-1),comb(N,m))
    Ey=Fraction(ff(n,k)*ff(m,h),ff(N,h))
    return n*q*Ey*(normalized(n,m,k,h,ell)-1)

def brute(n,m,k,edges_H):
    edges=list(combinations(range(n),2)); indices={e:i for i,e in enumerate(edges)}
    patterns=[]
    for phi in permutations(range(n),k):
        mask=0
        for a,b in edges_H:
            e=tuple(sorted((phi[a],phi[b])));mask|=1<<indices[e]
        patterns.append(mask)
    N=len(edges); denominator=comb(N,m); I_sum=X_sum=IX_sum=0
    for ids in combinations(range(N),m):
        mask=0;degree=[0]*n
        for i in ids:
            mask|=1<<i;a,b=edges[i];degree[a]+=1;degree[b]+=1
        I=sum(d==1 for d in degree)
        X=sum(mask & pat == pat for pat in patterns)
        I_sum+=I;X_sum+=X;IX_sum+=I*X
    return Fraction(IX_sum,denominator)-Fraction(I_sum*X_sum,denominator**2)

motifs=[('edge',2,[(0,1)]),('path3',3,[(0,1),(1,2)]),('triangle',3,[(0,1),(1,2),(0,2)]),('path4',4,[(0,1),(1,2),(2,3)]),('star4',4,[(0,1),(0,2),(0,3)]),('matching2',4,[(0,1),(2,3)]),('cycle4',4,[(0,1),(1,2),(2,3),(0,3)])]
checks=0
for n in [4,5,6]:
    N=comb(n,2)
    ms=range(N+1) if n<=5 else [1,2,3,4,5,6]
    for name,k,E in motifs:
        if k>n:continue
        deg=[0]*k
        for a,b in E:deg[a]+=1;deg[b]+=1
        assert all(deg)
        ell=sum(x==1 for x in deg)
        for m in ms:
            if not (len(E)<=m<=comb(n-1,2)):continue
            actual=brute(n,m,k,E)
            wanted=expectation_cov(n,m,k,len(E),ell)
            assert actual==wanted,(n,m,name,actual,wanted)
            checks+=1
print('PASS',checks,'exact full graph enumerations')
n=12;m=10;k=6;h=5
for name,ell in [('six-vertex path',2),('six-vertex star',5)]:
    r=normalized(n,m,k,h,ell)
    cov=expectation_cov(n,m,k,h,ell)
    print(name,'ratio',str(r),'cov',str(cov),'sign','+' if cov>0 else '-')

# Crossings: strict at most one when h,m in admissible range, since ratio affine in 1/m.
# Check exhaustive rational sign-change property over modest full parameter grid.
monotone_cases=0
for n in range(5,17):
 U=comb(n-1,2)
 for k in range(2,min(n,7)+1):
  for h in range(k-1,min(comb(k,2),U)+1):
   for ell in range(0,k+1):
    if h<1:continue
    values=[normalized(n,m,k,h,ell)-1 for m in range(h,U+1)]
    differences=[values[j+1]-values[j] for j in range(len(values)-1)]
    assert all(d>=0 for d in differences) or all(d<=0 for d in differences)
    monotone_cases+=1
print('PASS',monotone_cases,'algebraic monotone-grid cases')
