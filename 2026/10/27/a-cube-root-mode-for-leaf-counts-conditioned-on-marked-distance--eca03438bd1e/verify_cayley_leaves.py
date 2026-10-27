"""Exact finite checks for conditional leaf counts in Cayley trees.
Usage: python verify_cayley_leaves.py
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial


def decode_prufer(n, code):
    deg=[1]*n
    for v in code: deg[v]+=1
    adj=[set() for _ in range(n)]
    for v in code:
        leaf=next(i for i,d in enumerate(deg) if d==1)
        adj[leaf].add(v);adj[v].add(leaf)
        deg[leaf]-=1;deg[v]-=1
    a,b=[i for i,d in enumerate(deg) if d==1]
    adj[a].add(b);adj[b].add(a)
    return adj


def distance(adj):
    curr={0}; seen={0}
    for depth in range(1,len(adj)):
        curr={v for u in curr for v in adj[u] if v not in seen}
        if 1 in curr: return depth
        seen.update(curr)
    raise AssertionError('disconnected')


def predicted(n,k):
    r=k+1
    q=Fraction(n-1,n)
    return (n-r+Fraction(2*(r-1),r))*q**(n-r-1)


def main():
    checks=0;trees=0
    for n in range(2,9):
        nd=Counter(); ls=Counter(); endpoints=Counter(); outside=Counter()
        for code in product(range(n),repeat=n-2):
            adj=decode_prufer(n,code);trees+=1
            k=distance(adj)
            leaf_count=sum(len(a)==1 for a in adj)
            nd[k]+=1;ls[k]+=leaf_count
            endpoints[k]+=int(len(adj[0])==1)+int(len(adj[1])==1)
            outside[k]+=leaf_count-(int(len(adj[0])==1)+int(len(adj[1])==1))
        assert sum(nd.values())==n**(n-2)
        for k in range(1,n):
            r=k+1;q=Fraction(n-1,n)
            want_p=Fraction((k+1)*factorial(n-2)//factorial(n-k-1),n**k)
            assert Fraction(nd[k],n**(n-2))==want_p,(n,k,'distance')
            assert Fraction(ls[k],nd[k])==predicted(n,k),(n,k,'total',ls[k],nd[k])
            assert Fraction(endpoints[k],nd[k])==2*Fraction(r-1,r)*q**(n-r-1)
            assert Fraction(outside[k],nd[k])==(n-r)*q**(n-r-1)
            checks+=4
            if k+1<n:
                diff=predicted(n,k+1)-predicted(n,k)
                discriminant=2*(n-1)-r*r*(r-1)
                assert (diff>0)-(diff<0)==(discriminant>0)-(discriminant<0)
                checks+=1
        print(f'n={n} trees={n**(n-2)} profile='+str([predicted(n,k) for k in range(1,n)]))
    # Prove/verify algebraic expression for adjacent difference without floating point.
    for n in range(3,351):
        q=Fraction(n-1,n)
        for r in range(2,n):
            left=predicted(n,r)-predicted(n,r-1)
            right=q**(n-r-2)*Fraction(2*(n-1)-r*r*(r-1),n*r*(r+1))
            assert left==right,(n,r,'difference')
            checks+=1
    print('VERIFY_OK',checks,'exact assertions,',trees,'enumerated labeled trees')

if __name__=='__main__':main()
