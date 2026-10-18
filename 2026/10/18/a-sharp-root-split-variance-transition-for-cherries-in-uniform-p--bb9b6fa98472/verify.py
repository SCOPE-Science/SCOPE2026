"""Exact independent finite-tree enumeration and algebra checks for cherry-count root-split variance."""
from collections import defaultdict
from fractions import Fraction as F
from math import comb


def v(m):
    if m <= 3:
        return F(0)
    return F(m*(m-1)*(m-2)*(m-3), 2*(2*m-3)**2*(2*m-5))


def split_var(n,k):
    return v(k)+v(n-k)


def poly_shift(coeff,a):
    out=[0]*len(coeff)
    for i,c in enumerate(coeff):
        for j in range(i+1):
            out[j]+=c*comb(i,j)*a**(i-j)
    return out

P=[-270,393,-164,16]
Q=[405,-1935,3675,-3517,1746,-408,32]
assert poly_shift(P,8)==[570,841,220,16]
assert poly_shift(Q,7)==[60262,256932,196182,64971,10986,936,32]
assert [sum(c*k**i for i,c in enumerate(P)) for k in range(3,8)]==[-135,-298,-405,-360,-67]
assert [sum(c*k**i for i,c in enumerate(Q)) for k in range(3,7)]==[-1674,-13367,-40770,-55377]

# Enumerate every rooted, nonplane, leaf-labeled binary phylogeny by a root-split recurrence.
# n=1: single leaf; n=2: unique cherry. Every n>=3 root split is not a cherry.
N={1:{0:1},2:{1:1}}
for n in range(3,21):
    acc=defaultdict(int)
    for k in range(1,n):
        for c1,count1 in N[k].items():
            for c2,count2 in N[n-k].items():
                acc[c1+c2]+=comb(n,k)*count1*count2
    assert all(x%2==0 for x in acc.values())
    N[n]={c:x//2 for c,x in acc.items()}
    total=sum(N[n].values())
    doublefac=1
    for d in range(1,2*n-2,2):doublefac*=d
    assert total==doublefac,(n,total,doublefac)
    mean=sum(F(c*cnt,total) for c,cnt in N[n].items())
    var=sum(F(c*c*cnt,total) for c,cnt in N[n].items())-mean**2
    expect_mean=F(n*(n-1),2*(2*n-3))
    assert (mean,var)==(expect_mean,v(n)),(n,mean,var,expect_mean,v(n))
    for k in range(1,n//2+1):
        d=defaultdict(int)
        for a,aa in N[k].items():
            for b,bb in N[n-k].items():
                d[a+b]+=aa*bb
        den=sum(d.values())
        mu=sum(F(c*cnt,den) for c,cnt in d.items())
        cv=sum(F(c*c*cnt,den) for c,cnt in d.items())-mu**2
        assert cv==split_var(n,k),(n,k,cv,split_var(n,k))

for n in range(6,201):
    f=[split_var(n,k) for k in range(1,n//2+1)]
    assert f.index(min(f))+1 == 3,('min',n)
    expected_max=1 if n<=14 else n//2
    assert f.index(max(f))+1 == expected_max,('max',n)
    assert f.count(min(f))==1 and f.count(max(f))==1
    if n%2==0:
        m=n//2
        Pval=sum(c*m**i for i,c in enumerate(P))
        diff=F((m-2)*(m-1)**2*Pval,(2*m-5)*(2*m-3)**2*(4*m-7)*(4*m-5)**2)
    else:
        m=(n-1)//2
        Qval=sum(c*m**i for i,c in enumerate(Q))
        diff=F(2*m*(m-1)*Qval,(2*m-5)*(2*m-3)**2*(2*m-1)**2*(4*m-5)*(4*m-3)**2)
    assert diff == split_var(n,n//2)-split_var(n,1),('factor',n)

# Another exact identity: the conditional variance changes at n=14/15.
assert split_var(14,1)>split_var(14,7)
assert split_var(15,7)>split_var(15,1)
print('PASS: exact rooted-labeled tree recurrences and conditional laws n<=20; structural extrema and parity identities n<=200; polynomial sign certificates.')
