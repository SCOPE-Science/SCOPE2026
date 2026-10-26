"""Direct finite checks for free-submodule intersection types over length-two rings.
Canonical residue bases and explicit ring-linear combinations provide an independent count.
"""
from itertools import combinations, product
from math import prod
from collections import Counter

def gauss(n,k,q):
    if k<0 or k>n: return 0
    num=prod(q**(n-j)-1 for j in range(k))
    den=prod(q**(k-j)-1 for j in range(k))
    return num//den

def rank_matrices(m,n,r,q):
    if r<0 or r>min(m,n): return 0
    return gauss(m,r,q)*gauss(n,r,q)*prod(q**r-q**j for j in range(r))

def expected(n,k,l,q):
    ans=Counter()
    for d in range(max(0,k+l-n),min(k,l)+1):
        c=n-k-l+d
        count_L=gauss(k,d,q)*gauss(n-k,l-d,q)*q**((k-d)*(l-d))
        for b in range(min(d,c)+1):
            a=d-b
            ans[a,b]+=count_L*q**(l*(n-l)-d*c)*rank_matrices(d,c,b,q)
    return ans

def rrefs(n,l,q):
    for piv in combinations(range(n),l):
        choices=[(i,j) for i in range(l) for j in range(piv[i]+1,n) if j not in piv]
        for vals in product(range(q),repeat=len(choices)):
            rows=[[0]*n for i in range(l)]
            for i,j in enumerate(piv): rows[i][j]=1
            for (i,j),v in zip(choices,vals): rows[i][j]=v
            yield rows,piv

def brute(n,k,l,q):
    assert q in (2,3,5)
    result=Counter(); total=0
    for basis,piv in rrefs(n,l,q):
        nonpiv=[j for j in range(n) if j not in piv]
        for vals in product(range(q),repeat=l*(n-l)):
            phi=[[0]*n for _ in range(l)]
            for i in range(l):
                for t,j in enumerate(nonpiv): phi[i][j]=vals[i*(n-l)+t]
            # Generate submodule from R-linear combinations
            intersection=set()
            for lower in product(range(q),repeat=l):
                base=tuple(sum(lower[i]*basis[i][j] for i in range(l))%q for j in range(n))
                if any(base[j] for j in range(k,n)): continue
                tail0=tuple(sum(lower[i]*phi[i][j] for i in range(l))%q for j in range(n))
                for upper in product(range(q),repeat=l):
                    tail=tuple((tail0[j]+sum(upper[i]*basis[i][j] for i in range(l)))%q for j in range(n))
                    if any(tail[j] for j in range(k,n)): continue
                    intersection.add((base,tail))
            assert intersection
            bases={base for base,tail in intersection}
            a=0;v=len(bases)
            while v>1:
                assert v%q==0;(v,a)=(v//q,a+1)
            b=0;v=len(intersection)//(q**(2*a))
            assert len(intersection)%(q**(2*a))==0
            while v>1:
                assert v%q==0;(v,b)=(v//q,b+1)
            result[a,b]+=1; total+=1
    assert total == q**(l*(n-l))*gauss(n,l,q), (total,n,k,l,q)
    return result

def check(n,k,l,q):
    direct=brute(n,k,l,q)
    predicted=expected(n,k,l,q)
    assert direct==predicted,(n,k,l,q,direct,predicted)
    print('OK', (n,k,l,q), 'submodules',sum(direct.values()),'types',sorted(direct.items()))

if __name__=='__main__':
    for params in [(2,1,1,2),(3,1,1,2),(3,1,2,2),(3,2,2,2),(4,2,2,2),(4,1,2,2),(2,1,1,3),(3,1,1,3),(3,1,2,3),(3,2,2,3)]:
        check(*params)
    for q in (2,3,4,5,7):
      for n in range(1,10):
       for k in range(n+1):
        for l in range(n+1):
         assert sum(expected(n,k,l,q).values())==q**(l*(n-l))*gauss(n,l,q)
    print('VERIFY_OK')

def brute_z4(n,k,l):
    result=Counter();total=0;q=2
    for basis,piv in rrefs(n,l,2):
        nonpiv=[j for j in range(n) if j not in piv]
        for vals in product(range(q),repeat=l*(n-l)):
            lifts=[[int(x) for x in row] for row in basis]
            for i in range(l):
                for t,j in enumerate(nonpiv): lifts[i][j]+=2*vals[i*(n-l)+t]
            intersection=set()
            for scalars in product(range(4),repeat=l):
                vec=tuple(sum(scalars[i]*lifts[i][j] for i in range(l))%4 for j in range(n))
                if all(vec[j]==0 for j in range(k,n)):
                    intersection.add(vec)
            bases={tuple(x%2 for x in v) for v in intersection}
            a=0;z=len(bases)
            while z>1:
                assert z%2==0;z//=2;a+=1
            b=0;z=len(intersection)//(4**a)
            assert len(intersection)%(4**a)==0
            while z>1:
                assert z%2==0;z//=2;b+=1
            result[a,b]+=1;total+=1
    assert total==2**(l*(n-l))*gauss(n,l,2)
    return result

if __name__=='__main__':
    for n,k,l in [(2,1,1),(3,1,1),(3,1,2),(3,2,2),(4,1,2),(4,2,2)]:
        obs=brute_z4(n,k,l)
        assert obs==expected(n,k,l,2),(n,k,l,obs,expected(n,k,l,2))
        print('Z4_OK',(n,k,l),sum(obs.values()),sorted(obs.items()))
    print('ALL_CHECKS_OK')
