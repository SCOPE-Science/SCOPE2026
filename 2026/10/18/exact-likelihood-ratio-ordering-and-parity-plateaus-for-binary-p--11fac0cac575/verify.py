"""Exact finite checks for concentration ordering of binary Pólya alternating runs.
The infinite-parameter theorem is proved analytically; these computations are sanity checks.
"""
from fractions import Fraction
from itertools import product
from math import comb


def rising(x, k):
    z = Fraction(1)
    for i in range(k):
        z *= x+i
    return z


def exact_law(n, a):
    den = rising(2*a, n)
    arr = [Fraction(0) for _ in range(n)]
    for word in product((0,1), repeat=n):
        k=sum(word)
        transitions=sum(word[i]!=word[i+1] for i in range(n-1))
        arr[transitions] += rising(a,k)*rising(a,n-k)/den
    assert sum(arr)==1
    return arr


def kernel_count(n, j, t):
    if j==0:
        return int(t==0)
    if t==0:
        return 0
    if t%2:
        m=(t+1)//2
        if m>j: return 0
        return 2*comb(j-1,m-1)*comb(n-j-1,m-1)
    m=t//2
    if m>j or 2*m>=n: return 0
    return (n-2*m)*comb(j-1,m-1)*comb(n-j-1,m-1)//m


def check():
    assertions=0
    a_values=list(map(Fraction, ['1/3','1/2','1','2','5']))
    for n in range(2,10):
        # Pure combinatorial formula agrees with exhaustive word counts.
        counts=[[0]*n for _ in range(n//2+1)]
        for w in product((0,1),repeat=n):
            j=min(sum(w),n-sum(w))
            t=sum(w[i]!=w[i+1] for i in range(n-1))
            counts[j][t]+=1
        for j in range(n//2+1):
            mult=(1 if 2*j==n else 2)
            for t in range(n):
                assert counts[j][t] == mult*kernel_count(n,j,t)
                assertions+=1
        # The fixed-composition kernel is totally positive of order two.
        h=[[Fraction(kernel_count(n,j,t),comb(n,j)) for t in range(n)] for j in range(n//2+1)]
        for j in range(len(h)):
            for jj in range(j+1,len(h)):
                for t in range(n):
                    for tt in range(t+1,n):
                        assert h[j][t]*h[jj][tt]>=h[j][tt]*h[jj][t]
                        assertions+=1
        laws={a:exact_law(n,a) for a in a_values}
        for a in a_values:
            law=laws[a]
            for m in range(1,(n-1)//2+1):
                assert law[2*m]*2*m==law[2*m-1]*(n-2*m)
                assertions+=1
        for ia,a in enumerate(a_values):
            for b in a_values[ia+1:]:
                pa,pb=laws[a],laws[b]
                l=[pb[t]/pa[t] for t in range(n)]
                for t in range(n-1):
                    assert l[t]<=l[t+1]
                    if t%2 == 1:
                        assert l[t]==l[t+1]
                    else:
                        assert l[t]<l[t+1]
                    assertions+=1
                for h0 in range(1,n):
                    assert sum(pb[h0:])>sum(pa[h0:])
                    assertions+=1
    print('PASSED',assertions,'exact-rational and exhaustive finite checks')


if __name__=='__main__':
    check()
