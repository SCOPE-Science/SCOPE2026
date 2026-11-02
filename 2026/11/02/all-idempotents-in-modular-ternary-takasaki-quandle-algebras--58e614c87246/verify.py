#!/usr/bin/env python3
"""Exact verification of idempotents of elementary ternary Takasaki quandle algebras.

Uses independent direct evaluation of the quandle product and an ordinary
finite group-algebra parametrization. Standard library only, no external data.
"""
from itertools import product
from random import Random


def coeff_field(q):
    if q == 3:
        return lambda a,b:(a+b)%3, lambda a,b:(a*b)%3, 1
    if q == 9:
        def add(a,b):
            return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
        def mul(a,b):
            aa,ab=a%3,a//3; ba,bb=b%3,b//3
            return ((aa*ba+2*ab*bb)%3)+3*((aa*bb+ab*ba)%3)
        return add,mul,1
    raise ValueError(q)


def test(q,d,brute=False,all_params=True):
    addk,mulk,one=coeff_field(q)
    n=3**d
    digits=[tuple((i//(3**j))%3 for j in range(d)) for i in range(n)]
    lookup={u:i for i,u in enumerate(digits)}
    neg=[lookup[tuple((-a)%3 for a in u)] for u in digits]
    summed=[[lookup[tuple((a+b)%3 for a,b in zip(u,v))] for v in digits] for u in digits]
    star=[[neg[summed[i][j]] for j in range(n)] for i in range(n)]
    minus_one=2
    pairs=[]; seen={0}
    for i in range(1,n):
        if i not in seen:
            j=neg[i]; assert i!=j
            pairs.append((i,j));seen.add(i);seen.add(j)
    assert len(pairs)==(n-1)//2

    def add(a,b): return tuple(addk(x,y) for x,y in zip(a,b))
    def negvec(a): return tuple(mulk(minus_one,x) for x in a)
    zero=(0,)*n
    ident=(1,)+(0,)*(n-1)
    def conv(a,b):
        result=[0]*n
        for i,ai in enumerate(a):
            if ai:
                for j,bj in enumerate(b):
                    if bj:
                        k=summed[i][j]
                        result[k]=addk(result[k],mulk(ai,bj))
        return tuple(result)
    def direct_star(a,b):
        result=[0]*n
        for i,ai in enumerate(a):
            if ai:
                for j,bj in enumerate(b):
                    if bj:
                        k=star[i][j]
                        result[k]=addk(result[k],mulk(ai,bj))
        return tuple(result)
    def sig(a): return tuple(a[neg[i]] for i in range(n))
    def param(c):
        w=[0]*n
        for t,(i,j) in enumerate(pairs):
            w[i]=c[t]
            w[j]=mulk(2,c[t])
        w=tuple(w)
        assert sig(w)==negvec(w)
        w2=conv(w,w)
        u=add(add(ident,negvec(w)),negvec(w2))
        assert u[0] is not None
        assert direct_star(u,u)==u
        assert add(u,negvec(sig(u)))==w
        return u
    if all_params:
        cs=product(range(q),repeat=len(pairs))
    else:
        rng=Random(20261028+d+q)
        cs=(tuple(rng.randrange(q) for _ in pairs) for _ in range(100))
    param_set=set(map(param,cs))
    if all_params: assert len(param_set)==q**len(pairs)
    if brute:
        actual=set()
        for a in product(range(q), repeat=n):
            if direct_star(a,a)==a: actual.add(a)
        assert actual==param_set|{zero}, (q,d,len(actual),len(param_set))
        assert len(actual)==1+q**len(pairs)
        print('EXHAUSTIVE',q,d,'tested',q**n,'found',len(actual))
    else:
        print('PARAMETRIC',q,d,'checked',len(param_set),'of',q**len(pairs),'expected nonzero')
    # Algebra-level cross-check on a bounded sample: T(G) under the ordinary-unit group.
    items=list(param_set)[:min(30,len(param_set))]
    for a in items:
        assert conv(a,sig(a))==ident
        assert conv(a,conv(a,a))==ident
        for b in items:
            ab=conv(a,b)
            assert direct_star(a,b)==sig(ab)
            assert direct_star(a,b)==conv(sig(a),sig(b))
            if all_params and len(param_set)<=100:
                assert direct_star(a,b) in param_set
    return len(param_set)

if __name__=='__main__':
    test(3,1,brute=True)
    test(9,1,brute=True)
    test(3,2,brute=True)
    test(9,2,brute=False)
    test(3,3,brute=False,all_params=False)
    print('VERIFY_OK')
