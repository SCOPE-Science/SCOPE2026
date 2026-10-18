"""Independent exact checks for acyclic-set enumerators on complete multipartite graphs."""
from itertools import combinations
from math import comb


def profiles(n, low=1):
    if n == 0:
        yield ()
    else:
        for x in range(low, n+1):
            for remaining in profiles(n-x, x):
                yield (x,) + remaining


def choose(n,k):
    return comb(n,k) if 0<=k<=n else 0


def polynomial(part):
    n=sum(part)
    a=[0]*(n+1)
    a[0]=1
    a[1]=n
    a[2]=comb(n,2)
    for k in range(3,n+1):
        a[k]=sum(choose(x,k)+(n-x)*choose(x,k-1) for x in part)
    while a[-1]==0:
        a.pop()
    return a


def maximal_polynomial(part):
    n=sum(part)
    a=[0]*(n+1)
    s=part.count(1)
    a[2]=comb(s,2)
    for x in part:
        if x>=2:
            a[x+1]+=(n-x)
    return a


def direct_polynomials(part):
    labels=[i for i,x in enumerate(part) for _ in range(x)]
    n=len(labels)
    edges=[(i,j) for i in range(n) for j in range(i+1,n) if labels[i]!=labels[j]]
    adj=[0]*n
    for i,j in edges:
        adj[i]|=1<<j
        adj[j]|=1<<i

    def acyclic(mask):
        parents=list(range(n))
        def root(i):
            while parents[i]!=i:
                i=parents[i]
            return i
        for i,j in edges:
            if (mask>>i)&1 and (mask>>j)&1:
                ii,jj=root(i),root(j)
                if ii==jj:
                    return False
                parents[ii]=jj
        return True

    a=[0]*(n+1)
    maximal=[0]*(n+1)
    forest=[False]*(1<<n)
    for mask in range(1<<n):
        forest[mask]=acyclic(mask)
        if forest[mask]:
            a[mask.bit_count()]+=1
    for mask in range(1<<n):
        if not forest[mask]:
            continue
        if all(not forest[mask | (1<<v)] for v in range(n) if not mask&(1<<v)):
            maximal[mask.bit_count()]+=1
    return a, maximal


def test_direct():
    boards=0
    candidates=0
    for n in range(2,12):
        for part in profiles(n):
            if len(part)<2:
                continue
            boards+=1
            candidates+=1<<n
            actual, actual_m=direct_polynomials(part)
            expected=polynomial(part)
            expected_m=maximal_polynomial(part)
            assert actual[:len(expected)]==expected and not any(actual[len(expected):]), ('polynomial',part,actual,expected)
            assert actual_m==expected_m, ('maximal',part,actual_m,expected_m)
    print('DIRECT_OK profiles=%d subsets=%d'%(boards,candidates))


def test_cutoff():
    profiles_checked=0
    exceptions=[]
    minimum_slack={}
    for n in range(2,17):
        slacks=[]
        for part in profiles(n):
            if len(part)<2:
                continue
            profiles_checked+=1
            a=polynomial(part)
            slack=[a[k]**2-a[k-1]*a[k+1] for k in range(1,len(a)-1)]
            slacks.extend(slack)
            if any(x<0 for x in slack):
                exceptions.append((n,part,slack))
        minimum_slack[n]=min(slacks)
    assert len(exceptions)==1,exceptions
    assert exceptions[0][0]==16 and exceptions[0][1]==(1,)*12+(4,),exceptions
    assert minimum_slack[15]>=0
    assert polynomial(exceptions[0][1])==[1,16,120,76,49,12]
    assert minimum_slack[16]==-104
    print('CUTOFF_OK total_profiles=%d first_order=16 unique_bad=%s slack=-104'% (profiles_checked, exceptions[0][1]))
    print('SMALLER_MIN_SLACK '+repr({n:v for n,v in minimum_slack.items() if n<=15}))


def test_balancing():
    profiles_checked=0
    for n in range(2,17):
        for part in profiles(n):
            if len(part)<2:
                continue
            r=len(part)
            profiles_checked+=1
            # Polynomial dominance holds in *every* coefficient, not just at positive activities.
            balanced=tuple(sorted([n//r]*(r-n%r)+[n//r+1]*(n%r)))
            concentrated=(1,)*(r-1)+(n-r+1,)
            a=polynomial(part)
            low=polynomial(balanced)
            high=polynomial(concentrated)
            for k in range(n+1):
                p=a[k] if k<len(a) else 0
                lo=low[k] if k<len(low) else 0
                hi=high[k] if k<len(high) else 0
                assert lo<=p<=hi,(n,part,k,lo,p,hi)
            if part!=balanced:
                assert any((a[k] if k<len(a) else 0)>(low[k] if k<len(low) else 0) for k in range(3,n+1))
            if part!=concentrated:
                assert any((high[k] if k<len(high) else 0)>(a[k] if k<len(a) else 0) for k in range(3,n+1))
    print('MAJORIZATION_OK profiles=%d'%profiles_checked)


def test_family():
    # K_{4,1,...,1}, s singletons: the cubic log-concavity deficit
    # A_2*A_4-A_3*A_3=(4s^3-43s^2-41s-20)/2 is positive for every s>=12.
    for s in range(1,81):
        a=polynomial((1,)*s+(4,))
        d=a[2]*a[4]-a[3]**2
        form=(4*s**3-43*s**2-41*s-20)//2
        assert 2*d==4*s**3-43*s**2-41*s-20
        if s>=12:
            assert d>0
        else:
            assert d<=0
    print('FAMILY_OK first_singletons=12 tested_to=80')

if __name__=='__main__':
    test_direct()
    test_cutoff()
    test_balancing()
    test_family()
    print('VERIFICATION_OK')
