"""Independent direct enumeration for finite radical-square-zero quiver algebra unit-order profiles.
Uses the arrow-basis multiplication, not the closed-form torsion or Potts expansion for enumeration.
Python 3 standard library only. Run: python torsion_tutte_checker.py
"""
from collections import Counter
from itertools import product
from math import gcd


def field(q):
    assert q in (2, 3, 4, 5)
    if q == 4:
        def add(a,b): return a ^ b
        def mul(a,b):
            z=0
            for i in range(2):
                if (b>>i)&1: z ^= a << i
            for i in (2,):
                if z & (1<<i): z ^= 0b111<<(i-2)
            return z
        return add,mul,2
    return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q, q


def potts_count(q,n,edges,d):
    return sum(q**sum(c[i]!=c[j] for i,j in edges if i!=j)
               for c in product(range(d), repeat=n))


def enumerate_orders(q,n,edges):
    add,mul,p=field(q)
    k=len(edges)
    one=(tuple([1]*n), tuple([0]*k))
    def multiply(x,y):
        a,u=x; b,v=y
        return (tuple(mul(a[i],b[i]) for i in range(n)),
                tuple(add(mul(a[i],v[t]),mul(u[t],b[j]))
                      for t,(i,j) in enumerate(edges)))
    orders=Counter()
    allnz=list(range(1,q))
    for diag in product(allnz,repeat=n):
        for rad in product(range(q),repeat=k):
            u=(diag,rad)
            z=one
            for e in range(1,p*(q-1)+1):
                z=multiply(z,u)
                if z==one:
                    orders[e]+=1
                    break
            else: raise AssertionError((q,n,edges,u))
    return orders


def formula_orders(q,n,edges):
    from math import lcm
    _,_,p=field(q)
    all_order=Counter()
    loop_count=sum(i==j for i,j in edges)
    for s in range(1,q):
        if (q-1)%s: continue
        D=[d for d in range(1,s+1) if s%d==0]
        def mobius(z):
            r=1; d=2
            while d*d<=z:
                if z%d==0:
                    z//=d
                    if z%d==0:return 0
                    r=-r
                while z%d==0: z//=d
                d+=1
            return -r if z>1 else r
        values=[]
        for d in D:
            T=potts_count(q,n,edges,d)
            values.append((mobius(s//d),T,d**n*q**len(edges)))
        all_order[s]=sum(mu*t for mu,t,_ in values)
        all_order[p*s]=sum(mu*(pdt-t) for mu,t,pdt in values)
    return +all_order


def check():
    shapes=[(1,[]),(1,[(0,0)]),(2,[(0,1)]),(2,[(1,0)]),
            (2,[(0,1),(0,1)]),(2,[(0,1),(1,0)]),
            (2,[(0,0),(0,1)]),
            (3,[(0,1),(1,2)]),(3,[(0,1),(0,2)]),
            (3,[(0,1),(1,2),(2,0)]),
            (3,[(0,1),(0,2),(1,2)]),
            (3,[(0,1),(0,1),(1,2)])]
    successes=0
    for q in (2,3,4,5):
        for n,edges in shapes:
            actual=enumerate_orders(q,n,edges)
            predicted=formula_orders(q,n,edges)
            assert actual==predicted,(q,n,edges,actual,predicted)
            assert sum(actual.values())==(q-1)**n*q**len(edges)
            successes+=1
    q,n,edges=3,5,[(i,(i+1)%5) for i in range(5)]
    actual=enumerate_orders(q,n,edges)
    assert actual==formula_orders(q,n,edges)
    assert actual=={1:1,2:991,3:242,6:6542}
    successes+=1
    q,n,edges=3,3,[(0,1),(1,2)]
    assert enumerate_orders(q,n,edges)=={1:1,2:31,3:8,6:32}
    print('ALL_DIRECT_UNIT_ORDER_CASES_PASSED',successes)

if __name__=='__main__':check()
