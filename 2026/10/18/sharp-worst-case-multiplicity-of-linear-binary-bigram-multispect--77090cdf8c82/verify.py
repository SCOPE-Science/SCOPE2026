"""Independent finite checks for maximum binary bigram-spectrum multiplicity."""
from itertools import product
from collections import Counter
from math import comb

def observed(n):
    counts = Counter()
    for word in product((0, 1), repeat=n):
        profile = tuple(sum(word[i]==a and word[i+1]==b for i in range(n-1))
                        for a,b in ((0,0),(0,1),(1,0),(1,1)))
        counts[profile] += 1
    m=max(counts.values())
    return m,{prof for prof,c in counts.items() if c==m}

def formula(n):
    if n==2: return 1
    if n==3: return 2
    m,r=divmod(n,4)
    if r==0:return (4*m-1)*comb(2*m-2,m-1)*comb(2*m-1,m-1)//m
    if r==1:return 4*comb(2*m-1,m-1)**2
    if r==2:return (4*m+1)*comb(2*m-1,m-1)*comb(2*m,m-1)//m
    return (4*m+2)*comb(2*m,m)**2//(m+1)

def profile_formula(n):
    res=Counter()
    for t in range(n):
        k=t+1
        for p in range(n):
            q=n-1-2*k-p
            if q>=0:
                b=comb(p+k-1,k-1)*comb(q+k-1,k-1)*(n-1)//k
                res[(p,k,k,q)]=b
            q=n-2-2*t-p
            if q>=0:
                v=comb(p+t,t)*comb(q+t,t)
                res[(p,t+1,t,q)]=v
                res[(p,t,t+1,q)]=v
    res[(n-1,0,0,0)]=1
    res[(0,0,0,n-1)]=1
    return res

for n in range(2,17):
    empirical, profiles=observed(n)
    assert empirical==formula(n), (n,empirical,formula(n))
    all_profiles=profile_formula(n)
    predicted=max(all_profiles.values())
    assert predicted==empirical
    assert {p for p,v in all_profiles.items() if v==empirical}==profiles
    if n>=8:
        m,r=divmod(n,4)
        assert len(profiles)==[2,1,4,1][r],(n,len(profiles))
        assert all(p[1]==p[2]>=1 for p in profiles)
    print(n,empirical,len(profiles))
print('ALL_BIGRAM_MAX_CHECKS_PASSED')
