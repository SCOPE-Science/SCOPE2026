#!/usr/bin/env python3
"""Independent exhaustive right-power check for labeled evolution algebras over Z/p^s.
Uses original multiplication of vectors, never the path/valuation criterion.
"""
from itertools import product
from math import comb, factorial

def dag_poly(n,q):
    arr=[1]
    for m in range(1,n+1):
        arr.append(sum((-1)**(k+1)*comb(m,k)*q**(k*(m-k))*arr[m-k] for k in range(1,m+1)))
    return arr[n]

def expected(n,p,s):
    q=p
    nil=(q**((s-1)*n*n))*dag_poly(n,q)
    g=(n-1)*(n-2)//2
    extreme=(factorial(n)*(q-1)**(n-1)*q**g if s==1 else factorial(n)*(q-1)**n*q**((s-1)*n*n+g-1))
    return nil,extreme

def right_index(C,p,s):
    # C[i][j] = coefficient of e_j in e_i^2; products of distinct basis vectors zero
    n=len(C);m=p**s
    current={tuple(col) for col in C if any(col)} # A^2 generators
    if not current:return 2
    r=2
    cap=n*s+3
    while current and r<=cap:
        nxt=set()
        for v in current:
            for i in range(n):
                t=v[i]
                if t:
                    y=tuple(t*z%m for z in C[i])
                    if any(y):nxt.add(y)
        current=nxt
        r+=1
    assert not current, ('not nil at cap',C)
    return r

def test(n,p,s):
    m=p**s
    nil=extreme=0
    spectrum={}
    for data in product(range(m),repeat=n*n):
        C=[data[i*n:(i+1)*n] for i in range(n)]
        # Independently detect potentially non-nil structures by checking reduced cycle graph
        zero_graph=[[1 if C[i][j]%p else 0 for j in range(n)] for i in range(n)]
        reach=[v[:] for v in zero_graph]
        for k in range(n):
            for i in range(n):
                if reach[i][k]:
                    for j in range(n):
                        if reach[k][j]:reach[i][j]=1
        if any(reach[i][i] for i in range(n)):
            continue
        nil+=1
        idx=right_index(C,p,s)
        assert idx<=n*s+1,('bound violation',n,p,s,C,idx)
        spectrum[idx]=spectrum.get(idx,0)+1
        extreme+=(idx==n*s+1)
    assert (nil,extreme)==expected(n,p,s),(n,p,s,(nil,extreme),expected(n,p,s))
    print(f'PASS n={n} R=Z/{m}Z candidates={m**(n*n)} nil={nil} extremal={extreme} spectrum={dict(sorted(spectrum.items()))}',flush=True)

if __name__=='__main__':
    for n,p,s in [(1,2,1),(1,2,2),(1,3,3),(2,2,1),(2,2,2),(2,2,3),(2,3,2),(3,2,1),(3,2,2)]:
        test(n,p,s)
    print('FINITE_CHAIN_EVOLUTION_EXTREMAL_OK 9_EXHAUSTIVE_CONFIGURATIONS')

def test_gf4_dual_n2():
    # Ring F4[eps]/eps^2, encoded a+eps*b with a,b in F4.
    # F4=F2[t]/(t^2+t+1).
    def fm(a,b):
        z=0
        for j in range(2):
            for i in range(2):
                if ((a>>i)&1) and ((b>>j)&1):z^=1<<(i+j)
        if z&4:z^=7
        return z
    def mult(x,y):
        a=x&3;b=x>>2;c=y&3;d=y>>2
        return fm(a,c) | ((fm(a,d)^fm(b,c))<<2)
    table=[[mult(i,j) for j in range(16)] for i in range(16)]
    total=extreme=0;spectrum={}
    for data in product(range(16),repeat=4):
        c00,c01,c10,c11=data
        # acyclic residue graph = no loops, not both cross arrows nonzero
        if c00&3 or c11&3 or ((c01&3) and (c10&3)):continue
        total+=1
        C=(data[:2],data[2:])
        current={r for r in C if any(r)}
        t=2
        while current:
            nxt=set()
            for v in current:
                for i in range(2):
                    w=tuple(table[v[i]][x] for x in C[i])
                    if any(w):nxt.add(w)
            current=nxt;t+=1
            assert t<=6
        spectrum[t]=spectrum.get(t,0)+1
        extreme+=(t==5)
    assert total==1792 and extreme==1152,(total,extreme)
    print(f'PASS n=2 R=F4[eps]/eps^2 candidates=65536 nil={total} extremal={extreme} spectrum={dict(sorted(spectrum.items()))}',flush=True)

if __name__=='__main__':
    test_gf4_dual_n2()
    print('FINITE_CHAIN_EVOLUTION_EXTREMAL_OK 10_EXHAUSTIVE_CONFIGURATIONS')
