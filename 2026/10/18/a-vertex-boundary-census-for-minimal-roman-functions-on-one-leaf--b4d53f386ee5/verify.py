#!/usr/bin/env python3
"""Independent checks of the minimal Roman census for cycle one-leaf coronas."""
from itertools import product
from collections import Counter
from math import comb


def neighbors(n):
    adj = [set() for _ in range(2*n)]
    for i in range(n):
        j = (i+1) % n
        for a,b in ((i,j),(i,n+i)):
            adj[a].add(b)
            adj[b].add(a)
    return tuple(tuple(sorted(x)) for x in adj)


def rdf(f, adj):
    return all(f[v] != 0 or any(f[u] == 2 for u in adj[v]) for v in range(len(f)))


def independently_minimal(f, adj):
    if not rdf(f, adj): return False
    for i, x in enumerate(f):
        if x > 0:
            for y in range(x):
                lowered = list(f)
                lowered[i] = y
                if rdf(lowered, adj): return False
    return True


def cyclic_word_valid(w):
    n = len(w)
    for i, x in enumerate(w):
        left_is_a = w[(i-1) % n] == 'A'
        right_is_a = w[(i+1) % n] == 'A'
        if x == 'C' and not (left_is_a or right_is_a): return False
        if x in 'BD' and (left_is_a or right_is_a): return False
    return True


def word_to_labeling(w):
    table = {'A':(2,0),'B':(1,1),'C':(0,1),'D':(0,2)}
    return tuple(table[x][0] for x in w)+tuple(table[x][1] for x in w)


def polynomial_n(n):
    # A-vertex gaps: H(u,z)=1+zu+z^2u^2/(1-2z^2u)
    # For k selected A positions, coefficient [u^(n-k)] H^k, with n/k rotational factor.
    ans = Counter({2*n:2**n})
    for k in range(1,n+1):
        # Exact polynomial dynamic programming over k gaps; key (total gap length, weight).
        states={(0,0):1}
        for _ in range(k):
            new={}
            for (used,weight),mult in states.items():
                for ell in range(n-k-used+1):
                    if ell==0: wt, ways=0,1
                    elif ell==1: wt, ways=1,1
                    else: wt, ways=2*ell-2,2**(ell-2)
                    key=(used+ell,weight+wt)
                    new[key]=new.get(key,0)+mult*ways
            states=new
        for (ell,weight),mult in states.items():
            if ell==n-k:
                assert (n*mult)%k==0
                ans[weight+2*k]+=n*mult//k
    return +ans


def poly_add(*polys):
    c=Counter()
    for p in polys:c.update(p)
    return +c


def poly_shift_mul(p, coef, step):
    return Counter({x+step:coef*y for x,y in p.items()})


def recurrence_counts(n_max):
    # 1-3z²t+(2z⁴-z³)t²+(2z⁵-z⁴)t³
    pol={1:Counter({2:3}),2:Counter({3:2,4:5}),3:Counter({4:3,5:3,6:9})}
    for n in range(4,n_max+1):
        pol[n]=poly_add(poly_shift_mul(pol[n-1],3,2),
                        poly_shift_mul(pol[n-2],1,3),
                        poly_shift_mul(pol[n-2],-2,4),
                        poly_shift_mul(pol[n-3],1,4),
                        poly_shift_mul(pol[n-3],-2,5))
        assert min(pol[n].values())>=0
    return pol


def corona_neighbors(n, base_edges):
    adj=[set() for _ in range(2*n)]
    for i,j in base_edges:
        adj[i].add(j);adj[j].add(i)
    for i in range(n):
        adj[i].add(n+i);adj[n+i].add(i)
    return tuple(tuple(sorted(x)) for x in adj)


def boundary_polynomial(n, base_edges):
    adj=[set() for _ in range(n)]
    for i,j in base_edges:
        adj[i].add(j);adj[j].add(i)
    c=Counter()
    for mask in range(1<<n):
        selected={i for i in range(n) if mask>>i&1}
        boundary=set()
        for i in selected:boundary|=adj[i]
        boundary-=selected
        outside=n-len(selected)-len(boundary)
        c[2*n-len(boundary)]+=2**outside
    return c


def check_general_corona():
    cases=0;trials=0
    for n in range(1,5):
        pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
        for mask in range(1<<len(pairs)):
            edges=[edge for i,edge in enumerate(pairs) if mask>>i&1]
            adj=corona_neighbors(n,edges)
            actual=Counter()
            for f in product(range(3),repeat=2*n):
                trials+=1
                if independently_minimal(f,adj):actual[sum(f)]+=1
            want=boundary_polynomial(n,edges)
            assert actual==want,(n,edges,actual,want)
            cases+=1
    print('GENERAL_CORONA_OK base_graphs=',cases,'labelings=',trials)


def check():
    check_general_corona()
    rec=recurrence_counts(24)
    # Independently check all 3^(2n) labelings for cycles of orders 3 through 6.
    brute_total=0
    for n in range(3,7):
        adj=neighbors(n)
        census=Counter()
        for f in product(range(3), repeat=2*n):
            brute_total+=1
            if independently_minimal(f,adj):
                census[sum(f)]+=1
        want=polynomial_n(n)
        assert census==want==rec[n], (n,census,want,rec[n])
        print('BRUTE_OK',n,sum(census.values()),dict(sorted(census.items())))
    # Independently check four-letter local characterization and the same coefficients.
    checked_words=0
    for n in range(3,10):
        c=Counter()
        for w in product('ABCD',repeat=n):
            checked_words+=1
            if cyclic_word_valid(w):
                c[sum(word_to_labeling(w))]+=1
                assert independently_minimal(word_to_labeling(w),neighbors(n))
        assert c==rec[n], (n,c,rec[n])
    # Independently verify the proved minimum-weight multiplicity profile.
    for n in range(3,25):
        degree=(4*n+2)//3
        q,r=divmod(n,3)
        opt=(3 if r==0 else n*(n+17)//6 if r==1 else n)
        assert (n % 3 != 1 or (n*(n+17)) % 6 == 0)
        assert min(rec[n]) == degree, (n,min(rec[n]),degree)
        assert rec[n][degree] == opt, (n,rec[n][degree],opt)
    # Verify the closed Pell/Lucas formula without numerical approximations:
    # Q_n=(1+sqrt 2)^n+(1-sqrt 2)^n, Q_0=2,Q_1=2,Q_n=2Q_{n-1}+Q_{n-2}.
    a,b=2,2
    for n in range(1,25):
        a,b=b,2*b+a
        assert sum(rec[n].values())==1+a, (n,rec[n],a)
    print('VERIFICATION_OK brute_labelings=',brute_total,
          'cyclic_words=',checked_words,'recurrence_orders=',24)

if __name__=='__main__':check()
