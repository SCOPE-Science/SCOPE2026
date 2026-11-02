#!/usr/bin/env python3
"""Independent exhaustive validation of opposite-color singleton-run association."""
from itertools import combinations
from fractions import Fraction
from math import comb
from collections import Counter, defaultdict

def fall(m,k):
    if k>m: return 0
    z=1
    for j in range(k): z*=m-j
    return z

def exact_formula(a,b):
    n=a+b
    def factmom(k):
        return Fraction(fall(a,k)*fall(b,k),fall(n-1,k)) if k<=min(a,b) else Fraction(0)
    m2,m3,m4=[factmom(k) for k in (2,3,4)]
    return (m4+4*m3+2*m2-m2*m2)/((a-1)*(b-1))

def runs(bits):
    n=len(bits)
    r=sum(bits[j-1]==0 and bits[j]==1 for j in range(n))
    p=sum(bits[j-1]==0 and bits[j]==1 and bits[(j+1)%n]==0 for j in range(n))
    q=sum(bits[j-1]==1 and bits[j]==0 and bits[(j+1)%n]==1 for j in range(n))
    return r,p,q

def examine(a,b):
    n=a+b
    counts=Counter()
    profiles=Counter()
    for one_indices in combinations(range(n),b):
        bits=[0]*n
        for k in one_indices:bits[k]=1
        counts[runs(bits)]+=1
        z_lens=[];o_lens=[]
        for i in range(n):
            if bits[i]!=bits[(i-1)%n]:
                L=1
                while bits[(i+L)%n]==bits[i]: L+=1
                (z_lens if bits[i]==0 else o_lens).append(L)
        z=tuple(sum(v<=t for v in z_lens) for t in range(1,a+1))
        o=tuple(sum(v<=t for v in o_lens) for t in range(1,b+1))
        profiles[(z,o)]+=1
    count=comb(n,a)
    assert sum(counts.values())==count
    assert sum(profiles.values())==count
    for r in range(1,min(a,b)+1):
        sub={(p,q):v for (rr,p,q),v in counts.items() if rr==r}
        total=sum(sub.values())
        target=n*comb(a-1,r-1)*comb(b-1,r-1)//r
        assert total==target,(a,b,r,'R count')
        pm=Counter();qm=Counter()
        for (p,q),v in sub.items():pm[p]+=v;qm[q]+=v
        for p in range(r+1):
            for q in range(r+1):
                assert sub.get((p,q),0)*total==pm[p]*qm[q],(a,b,r,p,q,'conditional independence')
        ep=sum(p*v for p,v in pm.items())
        eq=sum(q*v for q,v in qm.items())
        assert Fraction(ep,total)==Fraction(r*(r-1),b-1)
        assert Fraction(eq,total)==Fraction(r*(r-1),a-1)
    ep=sum(p*v for (_,p,_),v in counts.items());eq=sum(q*v for (_,_,q),v in counts.items())
    epq=sum(p*q*v for (_,p,q),v in counts.items())
    cov=Fraction(epq,count)-Fraction(ep*eq,count*count)
    assert cov==exact_formula(a,b),(a,b,cov,exact_formula(a,b))
    assert cov>0,(a,b,cov)
    # All upper-threshold upper-orthant covariances: positive quadrant dependence.
    for pp in range(1,b+1):
        cp=sum(v for (_,p,_),v in counts.items() if p>=pp)
        for qq in range(1,a+1):
            cq=sum(v for (_,_,q),v in counts.items() if q>=qq)
            cpq=sum(v for (_,p,q),v in counts.items() if p>=pp and q>=qq)
            assert cpq*count>=cp*cq,(a,b,pp,qq,'positive quadrant')
    # Independent exhaustive multithreshold checks: every zero/one cumulative short-run
    # coordinate pair is positively quadrant dependent and strictly positively correlated.
    for t in range(a):
        for u in range(b):
            ez=sum(z[t]*v for (z,o),v in profiles.items())
            eo=sum(o[u]*v for (z,o),v in profiles.items())
            ezo=sum(z[t]*o[u]*v for (z,o),v in profiles.items())
            assert ezo*count>ez*eo,(a,b,t,u,'strict coordinate covariance')
            for j in range(1,min(a,b)+1):
                cz=sum(v for (z,o),v in profiles.items() if z[t]>=j)
                for k in range(1,min(a,b)+1):
                    co=sum(v for (z,o),v in profiles.items() if o[u]>=k)
                    czo=sum(v for (z,o),v in profiles.items() if z[t]>=j and o[u]>=k)
                    assert czo*count>=cz*co,(a,b,t,u,j,k,'profile quadrant')
    return len(counts)

if __name__=='__main__':
    total=0; profiles=0
    for n in range(4,15):
        for a in range(2,n-1):
            b=n-a
            total+=examine(a,b); profiles+=1
    print('PASS:',profiles,'composition profiles,',total,'run-statistic triple categories; independent exhaustive counts and all threshold tests to n=14')
