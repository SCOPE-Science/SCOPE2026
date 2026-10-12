#!/usr/bin/env python3
"""Independent checks of the bivariate Italian-domination enumerator on chain graphs.
All counted objects are vertex labelings; two implementations use different representations.
Standard library only: python3 verify_italian_chain_bivariate.py
"""
from itertools import product
from collections import defaultdict, Counter
from math import comb


def local_distribution(m, mode):
    """Counts of ones and twos in an m-vertex class (vertices labeled 0/1/2)."""
    out={}
    for ones in range(m+1):
        for twos in range(m-ones+1):
            zeros=m-ones-twos
            if mode=='positive' and zeros:continue
            if mode=='has_zero' and not zeros:continue
            out[(ones,twos)]=comb(m,ones)*comb(m-ones,twos)
    return out


def shore_boundary(sizes,shore,zero_boundary,opposite_zero_boundary):
    """Enumerate one shore by twin-class local generating products and a saturated two-unit test."""
    p=len(sizes)
    states={(0,0,0):1}  # (number of ones, number of twos, marked weight clipped at 2)
    for t,m in enumerate(sizes,1):
        if shore=='A':
            if zero_boundary==p+1 or t<zero_boundary:mode='positive'
            elif t==zero_boundary:mode='has_zero'
            else:mode='any'
            marked = opposite_zero_boundary>0 and t>=opposite_zero_boundary
        else:
            if zero_boundary==0 or t>zero_boundary:mode='positive'
            elif t==zero_boundary:mode='has_zero'
            else:mode='any'
            marked = opposite_zero_boundary<=p and t<=opposite_zero_boundary
        new=defaultdict(int)
        for (a,b,c),mult in states.items():
            for (x,y),ways in local_distribution(m,mode).items():
                d=min(2,c+((x+2*y) if marked else 0))
                new[(a+x,b+y,d)]+=mult*ways
        states=new
    requires = (shore=='A' and opposite_zero_boundary>0) or (shore=='B' and opposite_zero_boundary<=p)
    out=Counter()
    for (a,b,c),num in states.items():
        if not requires or c==2:out[(a,b)]+=num
    return +out


def predicted_distribution(alpha,beta):
    p=len(alpha)
    total=Counter()
    for i in range(1,p+2):
        for j in range(p+1):
            aa=shore_boundary(alpha,'A',i,j)
            bb=shore_boundary(beta,'B',j,i)
            for (a1,a2),u in aa.items():
                for (b1,b2),v in bb.items():total[(a1+b1,a2+b2)]+=u*v
    return +total


def direct_distribution(alpha,beta):
    p=len(alpha)
    A=[i for i,m in enumerate(alpha,1) for _ in range(m)]
    B=[j for j,m in enumerate(beta,1) for _ in range(m)]
    na=len(A); N=na+len(B)
    # No reference to class-boundary decomposition: test original graph adjacency directly.
    neighbors=[]
    for i in A:neighbors.append(tuple(na+h for h,j in enumerate(B) if j<=i))
    for j in B:neighbors.append(tuple(h for h,i in enumerate(A) if i>=j))
    counts=Counter()
    for labeling in product((0,1,2),repeat=N):
        if all(labeling[v] or sum(labeling[u] for u in neighbors[v])>=2 for v in range(N)):
            counts[(labeling.count(1),labeling.count(2))]+=1
    return +counts


def compositions(n,k):
    if k==1:
        yield (n,)
    else:
        for v in range(1,n-k+2):
            for s in compositions(n-v,k-1):yield (v,)+s


def predicted_weight_three(alpha,beta):
    """Closed minimum-weight coefficient for a proper connected chain graph."""
    assert len(alpha)==len(beta)>=2
    a,b=sum(alpha),sum(beta)
    return (int(a==2)+int(a==3 and alpha[-1]>=2)
            +int(b==2)+int(b==3 and beta[0]>=2)
            +int(a==2 and beta[-1]==1)
            +int(b==2 and alpha[0]==1))


def check_minimum_coefficient(alpha,beta,distribution):
    if len(alpha)<2:return
    low=min(x+2*y for x,y in distribution)
    c3=sum(n for (x,y),n in distribution.items() if x+2*y==3)
    assert c3==predicted_weight_three(alpha,beta),(alpha,beta,c3,predicted_weight_three(alpha,beta))
    assert low==(3 if c3 else 4),(alpha,beta,low,c3)


def main():
    examined=0; profiles=0; nontrivial=0
    for N in range(2,10):
        for p in range(1,N//2+1):
            for a_size in range(p,N-p+1):
                for alpha in compositions(a_size,p):
                    for beta in compositions(N-a_size,p):
                        f=predicted_distribution(alpha,beta)
                        b=direct_distribution(alpha,beta)
                        assert f==b,(alpha,beta, f-b, b-f)
                        check_minimum_coefficient(alpha,beta,f)
                        profiles+=1;examined+=3**N
                        if p>=2:nontrivial+=1
    # Ten-vertex profiles with high twin-class diversity plus a non-tree p=2 example.
    N=10
    for p in (3,4,5):
        for a_size in range(p,N-p+1):
            for alpha in compositions(a_size,p):
                for beta in compositions(N-a_size,p):
                    assert predicted_distribution(alpha,beta)==direct_distribution(alpha,beta),(alpha,beta)
                    check_minimum_coefficient(alpha,beta,predicted_distribution(alpha,beta))
                    profiles+=1;examined+=3**N;nontrivial+=1
    alpha,beta=(1,2,1,1),(2,1,1,1)
    assert predicted_distribution(alpha,beta)==direct_distribution(alpha,beta)
    check_minimum_coefficient(alpha,beta,predicted_distribution(alpha,beta))
    profiles+=1;examined+=3**10;nontrivial+=1
    print('PASS: exact bivariate distributions match independent full graph-label enumeration')
    print('Profiles:',profiles,'including noncomplete chain profiles:',nontrivial)
    print('Total labelings checked:',examined)
    print('PASS: minimum weight is 3 iff the exact six-term weight-three coefficient is nonzero (else 4)')
    for a,b in [((1,),(1,)),((1,1),(1,1)),((1,2),(2,1))]:
        dist=predicted_distribution(a,b)
        univ=Counter()
        for (ones,twos),v in dist.items():univ[ones+2*twos]+=v
        print('Sample',a,b,'weight_coefficients:',sorted(univ.items()),'bivariate_monomials:',len(dist))

if __name__=='__main__':main()
