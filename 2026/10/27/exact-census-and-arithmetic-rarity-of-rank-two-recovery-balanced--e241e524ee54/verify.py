#!/usr/bin/env python3
"""Independent finite checks for recovery balance in rank-two linear codes.
The source and output contain only mathematical reproducibility information.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial, exp, log, pi


def count_balanced_codes(q,n):
    gl=(q*q-1)*(q*q-q)
    total=0
    terms=[]
    for r in range(2,min(q+1,n)+1):
        if n%r: continue
        a=n//r
        term=comb(q+1,r)*factorial(n)//factorial(a)**r * (q-1)**n
        terms.append((r,term))
        total+=term
    assert total%gl==0,(q,n,terms,total,gl)
    return total//gl


def projective_class(v,q):
    x,y=v
    if x%q:
        return (1,(y*pow(x,-1,q))%q)
    if y%q:return (0,1)
    return None


def composition(n,r):
    if r==1:
        yield (n,)
        return
    for a in range(n+1):
        for rem in composition(n-a,r-1):
            yield (a,)+rem


def distribution_time(a,i):
    n=sum(a)
    inds=[]
    for j,count in enumerate(a):inds += [j]*count
    assert a[i]>0 and len(set(inds))>=2
    # Directly apply exact subset-spanning identity, without the Poisson representation.
    alpha=[]
    for s in range(1,n):
        c=0
        for ss in combinations(range(n),s):
            kinds={inds[j] for j in ss}
            if i in kinds or len(kinds)>=2:c+=1
        alpha.append(c)
    return n*sum((Fraction(1,j) for j in range(1,n+1)),Fraction(0))-sum((Fraction(alpha[s-1],comb(n-1,s)) for s in range(1,n)),Fraction(0))


def poisson_time(a,i):
    n=sum(a)
    assert a[i]>0
    pos=[j for j,c in enumerate(a) if c>0]
    r=len(pos)
    assert r>=2
    return n*sum((Fraction(1,n-a[j]) for j in pos if j!=i),Fraction(0))-(r-2)


def exhaustive_profiles():
    counts=[]
    for q,maxn in [(2,8),(3,6)]:
        checked=0
        for n in range(2,maxn+1):
            for a in composition(n,q+1):
                if sum(x>0 for x in a)<2:continue
                for i,c in enumerate(a):
                    if c==0:continue
                    p=poisson_time(a,i)
                    d=distribution_time(a,i)
                    assert p==d,(q,n,a,i,p,d)
                    checked+=1
                # Identical times exactly when positive class sizes are identical.
                v=[poisson_time(a,i) for i,c in enumerate(a) if c>0]
                assert (len(set(v))==1)==(len({c for c in a if c>0})==1)
        counts.append((q,checked))
    return counts


def enumerate_matrices():
    out=[]
    for q,maxn in [(2,7),(3,5),(5,4)]:
        vectors=list(product(range(q),repeat=2))
        gl=(q*q-1)*(q*q-q)
        for n in range(2,maxn+1):
            good=0;all_rank2=0;nondeg=0
            for cols in product(vectors,repeat=n):
                counts={projective_class(v,q):0 for v in cols}
                for v in cols: counts[projective_class(v,q)]+=1
                nr=sum(x>0 for j,x in counts.items() if j is not None)
                if nr<2:continue
                all_rank2+=1
                if None in counts:continue
                nondeg+=1
                if len({v for v in counts.values() if v>0})==1:good+=1
            predicted=count_balanced_codes(q,n)
            assert good==predicted*gl,(q,n,good,predicted,gl)
            assert all_rank2==(q**n-1)*(q**n-q),(q,n,all_rank2)
            assert nondeg==(q*q-1)**n-(q+1)*(q-1)**n,(q,n,nondeg)
            out.append((q,n,all_rank2//gl,nondeg//gl,predicted))
    return out


def asymptotic_sanity():
    out=[]
    for q in (2,3,4):
        for n in (60,84,120):
            rs=[r for r in range(2,min(q+1,n)+1) if n%r==0]
            r=max(rs)
            exact=sum(comb(q+1,j)*factorial(n)//factorial(n//j)**j for j in rs)/((q+1)**n-(q+1))
            asym=comb(q+1,r)*r**(r/2)*exp(-((r-1)/2)*log(2*pi*n)+n*log(r/(q+1)))
            rel=exact/asym
            assert abs(rel-1)<0.08,(q,n,rel)
            out.append((q,n,r,round(rel,7)))
    return out


if __name__=='__main__':
    print('direct_subset_profile_checks:',exhaustive_profiles())
    print('code_counts_(q,n,all,nondeg,balance):')
    for x in enumerate_matrices():print(x)
    print('asymptotic_exact_to_leading_ratios:',asymptotic_sanity())
    print('RANK2_BALANCE_VERIFY_OK')
