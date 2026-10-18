#!/usr/bin/env python3
"""Independent finite checks for commuting nuclei on root-star upset lattices.

Run: python3 verify.py
Uses only Python's standard library.  Finite checks are not the proof for all n.
"""
from itertools import product
from math import comb


def upsets(n):
    leaves = ((1 << (n+1)) - 1) ^ 1
    return tuple((u << 1) for u in range(1 << n)) + ((1 << (n+1)) - 1,)


def nucleus(s, u, n):
    # Pointwise definition using the star partial order, independent of
    # the explicit classification formulas.
    ans = 0
    for x in range(n+1):
        eligible = range(n+1) if x == 0 else (x,)
        if all(((s >> y)&1) == 0 or ((u >> y)&1) for y in eligible):
            ans |= 1 << x
    return ans


def all_nuclei(n):
    U = upsets(n)
    return {s:tuple(nucleus(s,u,n) for u in U) for s in range(1<<(n+1))}


def classify_pair(s,t,n):
    a,b=s&1,t&1
    A,B=s>>1,t>>1
    return a==b or (a==0 and (A&B)==A) or (b==0 and (B&A)==B)


def check_nuclei(n):
    U=upsets(n)
    i={u:k for k,u in enumerate(U)}
    fs=all_nuclei(n)
    assert len(set(fs.values())) == (1<<(n+1))
    for s,f in fs.items():
        for k,u in enumerate(U):
            assert (u & ~f[k]) == 0
            assert f[i[f[k]]] == f[k]
            for l,v in enumerate(U):
                assert f[i[u&v]] == (f[k]&f[l])
        for t,g in fs.items():
            equal = all(f[i[g[k]]] == g[i[f[k]]] for k in range(len(U)))
            assert equal == classify_pair(s,t,n),(n,s,t)
    count=sum(classify_pair(s,t,n) for s in fs for t in fs)
    assert count == 2*4**n+2*3**n,(n,count)
    return count


def exhaustive_operators(n):
    U=upsets(n)
    i={u:k for k,u in enumerate(U)}
    good=[]
    for choice in product(U, repeat=len(U)):
        if any((u&~choice[k]) for k,u in enumerate(U)):
            continue
        if any(choice[i[choice[k]]]!=choice[k] for k in range(len(U))):
            continue
        if any(choice[i[u&v]]!=(choice[k]&choice[l]) for k,u in enumerate(U)
               for l,v in enumerate(U)):
            continue
        good.append(tuple(choice))
    assert set(good) == set(all_nuclei(n).values())
    return len(good)


def maximal_cliques(n):
    size = 1 << (n+1)
    vertices = set(range(size))
    edges = {s:{t for t in vertices if t!=s and classify_pair(s,t,n)}
             for s in vertices}
    output=[]
    def bk(R,P,X):
        if not P and not X:
            output.append(frozenset(R)); return
        pivot = max(P|X, key=lambda u: len(P & edges[u])) if (P|X) else None
        for v in list(P - (edges[pivot] if pivot is not None else set())):
            bk(R|{v}, P&edges[v], X&edges[v])
            P.remove(v); X.add(v)
    bk(set(), set(vertices), set())
    expected=[]
    for I in range(1<<n):
        F0={A<<1 for A in range(1<<n) if (A&I)==A}
        F1={(B<<1)|1 for B in range(1<<n) if (B&I)==I}
        F=frozenset(F0|F1)
        assert len(F)==2**I.bit_count()+2**(n-I.bit_count())
        expected.append(F)
    assert set(output)==set(expected), (n,len(output),len(expected))
    return len(output)


def ordered_tuples(n,k):
    fs=range(1<<(n+1))
    actual=sum(all(classify_pair(tup[i],tup[j],n)
                   for i in range(k) for j in range(i+1,k))
               for tup in product(fs,repeat=k))
    predicted=sum(comb(k,r)*(2**r+2**(k-r)-1)**n for r in range(k+1))
    assert actual==predicted,(n,k,actual,predicted)
    return actual


def main():
    assert exhaustive_operators(1)==4
    assert exhaustive_operators(2)==8
    print('EXHAUSTIVE_NUCLEUS_AXIOMS_OK n=1,2')
    for n in range(1,5):
        count=check_nuclei(n)
        countmax=maximal_cliques(n)
        print(f'NUCLEI_AND_COMMUTATION_OK n={n} count={count} maximal_families={countmax}')
    for n in range(1,4):
        for k in range(0,4):
            print('TUPLE_OK',n,k,ordered_tuples(n,k))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
