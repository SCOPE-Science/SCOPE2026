#!/usr/bin/env python3
"""Standalone exact checks for minimal Roman functions of one-leaf coronas.

Requires only Python 3 standard library. No external data, network, or packages.
"""
from collections import Counter
from itertools import product
from math import sqrt


def base_edges(n, mask):
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    return [e for k,e in enumerate(pairs) if mask & (1 << k)]


def corona_neighbors(n, edges):
    N = [set() for _ in range(2*n)]
    for i,j in list(edges)+[(i,n+i) for i in range(n)]:
        N[i].add(j)
        N[j].add(i)
    return N


def is_rdf(f,N):
    return all(f[i] or any(f[j]==2 for j in N[i]) for i in range(len(f)))


def brute_polynomial(n,edges):
    N=corona_neighbors(n,edges)
    ans=Counter()
    for f in product(range(3),repeat=2*n):
        if not is_rdf(f,N):
            continue
        minimal=True
        for i,x in enumerate(f):
            if x:
                g=list(f)
                g[i]-=1
                if is_rdf(g,N):
                    minimal=False
                    break
        if minimal:
            ans[sum(f)]+=1
    return ans


def formula_polynomial(n,edges):
    out=Counter()
    neigh=[0]*n
    for i,j in edges:
        neigh[i]|=1<<j
        neigh[j]|=1<<i
    for A in range(1<<n):
        nbr=0
        for i in range(n):
            if A>>i&1:
                nbr|=neigh[i]
        outside=nbr&~A
        closed=A|nbr
        b=outside.bit_count()
        u=n-closed.bit_count()
        out[2*n-b]+=1<<u
    return out


def cycle_edges(n):
    return sorted(set((min(i,(i+1)%n),max(i,(i+1)%n)) for i in range(n)))


def polynomial_product(A,B):
    C=Counter()
    for i,a in A.items():
        for j,b in B.items():
            C[i+j]+=a*b
    return +C


def polynomial_trace_cycle(n):
    # Transfer from bit-pair (a,b) to (b,c); triple weights centered at b.
    T=[[Counter() for _ in range(4)] for _ in range(4)]
    for a,b,c in product(range(2),repeat=3):
        weight = {2:1} if b else ({1:1} if a or c else {2:2})
        T[2*a+b][2*b+c] = Counter(weight)
    I=[[Counter({0:1}) if i==j else Counter() for j in range(4)] for i in range(4)]
    def mm(X,Y):
        Z=[[Counter() for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for deg, coeff in polynomial_product(X[i][k],Y[k][j]).items():
                        Z[i][j][deg]+=coeff
        return Z
    for _ in range(n):
        I=mm(I,T)
    out=Counter()
    for i in range(4):
        out.update(I[i][i])
    return +out


def main():
    checked=0
    for n in range(1,5):
        for mask in range(1 << (n*(n-1)//2)):
            edges=base_edges(n,mask)
            a=brute_polynomial(n,edges)
            b=formula_polynomial(n,edges)
            assert a==b,(n,mask,a,b)
            checked+=1
    print('ARBITRARY_BASE_GRAPHS',checked,'PASS')
    for n in range(3,7):
        edges=cycle_edges(n)
        brute=brute_polynomial(n,edges)
        formula=formula_polynomial(n,edges)
        transfer=polynomial_trace_cycle(n)
        assert brute==formula==transfer,(n,brute,formula,transfer)
        print('CYCLE',n,'WEIGHTS',sorted(brute.items()),'PASS')
    counts=[]
    for n in range(3,19):
        p=formula_polynomial(n,cycle_edges(n))
        total=sum(p.values())
        # Pell-Lucas sequence t_n=(1+sqrt2)^n+(1-sqrt2)^n, t0=2,t1=2.
        a,b=2,2
        for _ in range(n):
            a,b=b,2*b+a
        assert total==a+1,(n,total,a+1)
        counts.append(total)
    print('CYCLE_COUNTS_N3_TO18',counts,'PASS')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
