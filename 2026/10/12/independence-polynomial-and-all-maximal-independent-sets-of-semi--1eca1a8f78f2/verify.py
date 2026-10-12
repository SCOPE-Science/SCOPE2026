#!/usr/bin/env python3
from itertools import combinations
from math import floor, ceil

def graph(a):
    V=[('A',i) for i in range(1,a+1)]+[('B',j) for j in range(a)]
    E=set()
    for x,y in combinations(V,2):
        adj=False
        if x[0]=='A' and y[0]=='B': adj=x[1]+y[1]>=a
        elif x[0]=='B' and y[0]=='A': adj=x[1]+y[1]>=a
        elif x[0]=='B' and y[0]=='B': adj=x[1]+y[1]>=a
        if adj: E.add(frozenset((x,y)))
    return V,E

def independent(S,E):
    return all(frozenset((x,y)) not in E for x,y in combinations(S,2))

def brute_poly(a):
    V,E=graph(a)
    out=[0]*(len(V)+1)
    maximal=[]
    for mask in range(1<<len(V)):
        S={V[i] for i in range(len(V)) if (mask>>i)&1}
        if not independent(S,E): continue
        out[len(S)]+=1
        if all(not independent(S|{v},E) for v in V if v not in S):
            maximal.append(frozenset(S))
    return out,maximal

def predicted_coeffs(a):
    # polynomial arithmetic for (1+x)^n
    c=[0]*(2*a+1)
    from math import comb
    for k in range(a+1): c[k]+=comb(a,k)
    for m in range(a):
        e=a-m-1+min(m,a-m)
        for k in range(e+1): c[k+1]+=comb(e,k)
    return c

def predicted_facets(a):
    F={frozenset(('A',i) for i in range(1,a+1))}
    for m in range(a):
        r=min(m,a-m)
        S={('B',m)}
        S.update(('B',j) for j in range(r))
        S.update(('A',i) for i in range(1,a-m))
        F.add(frozenset(S))
    return F

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def direct_check(p,q,a):
    n=(p**a)*q
    D=[d for d in divisors(n) if 1<d<n]
    V,E=graph(a)
    im={('A',i):p**i for i in range(1,a+1)}
    im.update({('B',j):(p**j)*q for j in range(a)})
    assert sorted(im.values())==sorted(D)
    for x,y in combinations(V,2):
        direct=(im[x]*im[y])%n==0
        abstract=frozenset((x,y)) in E
        assert direct==abstract,(p,q,a,x,y)
    return n,len(D)

for a in range(1,9):
    brute,facets=brute_poly(a)
    pred=predicted_coeffs(a)
    assert brute==pred,(a,brute,pred)
    PF=predicted_facets(a)
    assert set(facets)==PF,(a,len(facets),len(PF))
    alpha=max(k for k,c in enumerate(brute) if c)
    assert alpha==a
    max_count=brute[a]
    assert max_count==a//2+2,(a,max_count)
    sizes=sorted(len(F) for F in facets)
    expected=sorted([a]+[a-m+min(m,a-m) for m in range(a)])
    assert sizes==expected,(a,sizes,expected)
    well=(len(set(sizes))==1)
    assert well==(a<=2)
    indep_dom=min(sizes)
    assert indep_dom==(1 if a==1 else 2)
    print(f'a={a}: polynomial={brute}, facets={len(facets)}, max_sets={max_count}, well_covered={well}, i={indep_dom}')

for p,q,a in [(2,3,1),(2,3,2),(2,5,4),(3,5,5),(5,7,3)]:
    n,v=direct_check(p,q,a)
    print(f'Z/{n}Z direct ideal-product graph OK: vertices={v}')

print('VERIFY_OK')
