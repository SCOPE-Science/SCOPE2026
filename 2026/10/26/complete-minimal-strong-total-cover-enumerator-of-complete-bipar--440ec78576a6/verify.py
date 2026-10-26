"""Independent enumeration of inclusionwise-minimal strong total covers of complete bipartite graphs."""
from itertools import product
from math import comb
from collections import Counter

def formula(m,n):
    pol=Counter()
    for a in range(1,m+1):
        for b in range(1,n+1):
            pol[m+n-a-b+a*b]+=comb(m,a)*comb(n,b)
    d=1+sum(comb(n,b)*(m**b-m) for b in range(1,n+1))+sum(comb(m,a)*(n**a-n) for a in range(1,m+1))
    pol[m+n]+=d
    return +pol

def direct(m,n):
    N=m+n+m*n
    edges=[(i,m+j) for i in range(m) for j in range(n)]
    cond=[1<<v | sum(1<<(m+n+k) for k,e in enumerate(edges) if v in e) for v in range(m+n)]
    cond += [(1<<u)|(1<<v)|(1<<(m+n+k)) for k,(u,v) in enumerate(edges)]
    out=Counter()
    for mask in range(1<<N):
        if not all(mask&x for x in cond):continue
        if all(any((mask^(1<<j))&x==0 for x in cond) for j in range(N) if mask>>j&1):
            out[mask.bit_count()]+=1
    return +out

if __name__=='__main__':
    c=0
    for m,n in [(1,1),(1,2),(2,2),(2,3),(2,4),(3,3),(3,4)]:
        f,d=formula(m,n),direct(m,n)
        print(m,n,'formula',sorted(f.items()),'direct',sorted(d.items()))
        assert f==d
        c+=1
    print('VERIFY_OK',c,'complete_bipartite_cases')
