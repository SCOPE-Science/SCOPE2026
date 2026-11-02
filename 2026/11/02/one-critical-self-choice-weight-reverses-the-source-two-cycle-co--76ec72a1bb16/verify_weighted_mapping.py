"""Independent finite weighted-map enumeration for cycle/zero-indegree covariance."""
from fractions import Fraction
from itertools import product
from math import factorial

def counts(mapping):
    n=len(mapping)
    indeg=[0]*n
    for j in mapping: indeg[j]+=1
    z=sum(v==0 for v in indeg)
    cycle=[0]*(n+1)
    done=set()
    for i in range(n):
        if i in done: continue
        cur=i; trail=[]; pos={}
        while cur not in done and cur not in pos:
            pos[cur]=len(trail); trail.append(cur);cur=mapping[cur]
        if cur in pos: cycle[len(trail)-pos[cur]]+=1
        done.update(trail)
    return z,cycle

def formula(n,w,r):
    a=n-1+w
    q=Fraction(n-1,1)/a*((a-1)/a)**(n-1)
    falling=factorial(n)//factorial(n-r)
    expected=Fraction(falling,r)/a**r
    B=(n-r)*(a/(a-1))**r-n
    return expected*q*B

def exact_test(n,w):
    a=n-1+w
    # sum weights exactly; each ordinary offdiagonal mapping 1, fixed weight w
    Ez=Fraction(0);Ec=[Fraction(0) for _ in range(n+1)];Ezc=[Fraction(0) for _ in range(n+1)];total=Fraction(0)
    for mapping in product(range(n),repeat=n):
        wt=w**sum(mapping[i]==i for i in range(n))
        if wt==0:continue
        z,c=counts(mapping);total+=wt;Ez+=wt*z
        for r in range(2,n+1):
            Ec[r]+=wt*c[r];Ezc[r]+=wt*z*c[r]
    assert total==a**n,(n,w,total,a**n)
    checked=0
    for r in range(2,n+1):
        val=Ezc[r]/total-Ez*Ec[r]/total**2
        expected=formula(n,w,r)
        assert val==expected,(n,w,r,val,expected)
        B=(n-r)*(a/(a-1))**r-n
        assert (val>0)-(val<0)==(B>0)-(B<0)
        if r>=3:assert B<0
        checked+=3
    return checked

if __name__=='__main__':
    checks=0; histories=0
    for n in (3,4,5,6):
        for w in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(2)):
            checks+=exact_test(n,w)
            histories+=n**n
    for n in range(3,400):
        from math import sqrt
        threshold=(sqrt(n*(n-2))-(n-2))/2
        assert 0<threshold<0.5
        for r in range(3,n+1):
            a=n-1+Fraction(7,9)
            B=(n-r)*(a/(a-1))**r-n
            assert B<0
            checks+=1
        checks+=1
    print('EXACT_TEST_PASS checks=',checks,'sample_weighted_map_evaluations=',histories)
