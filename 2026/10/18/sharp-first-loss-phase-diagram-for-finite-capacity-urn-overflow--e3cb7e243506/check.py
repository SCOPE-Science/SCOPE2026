"""Exact finite arithmetic cross-checks for a capped occupancy theorem.
The infinite parameter classification is proved analytically in RESULT.md.
"""
from collections import defaultdict

def pmf_count(n,r,m):
    states={(0,)*n:1}
    for _ in range(m):
        nxt=defaultdict(int)
        for bins,multiplicity in states.items():
            for i in range(n):
                b=list(bins)
                b[i]=min(r,b[i]+1)
                nxt[tuple(b)]+=multiplicity
        states=nxt
    ans=defaultdict(int)
    for bins,multiplicity in states.items():
        ans[m-sum(bins)]+=multiplicity
    assert sum(ans.values())==n**m
    return ans

def predicted(n,r):
    a=(r+2)*(n-1)
    N=n**(r+1)
    return {0:n*(N-a-1),1:n*a,2:n}

for n in range(2,7):
    for r in range(2,7):
        assert pmf_count(n,r,r+2)==predicted(n,r)
        a=(r+2)*(n-1);N=n**(r+1)
        lc=(N<=a*a+a+1)
        sharp_lc=(r==2 and n<=14) or (r==3 and n<=3) or (r==4 and n==2)
        assert lc==sharp_lc
        ulc=((a+2)**2>=4*N)
        assert ulc==(r==2 and n==2)
assert pmf_count(2,2,5)=={1:20,2:10,3:2}
for n in range(2,151):
    for r in range(2,41):
        a=(r+2)*(n-1);N=n**(r+1)
        assert (N<=a*a+a+1)==((r==2 and n<=14) or (r==3 and n<=3) or (r==4 and n==2))
        assert (((a+2)**2>=4*N)==(n==r==2))
print('PASS: exact occupancy enumeration, 5x5 finite boundary tests, 5811 symbolic-integer sign instances, exceptional horizon')
