#!/usr/bin/env python3
"""Independent exhaustive check of Lie ideals for complete-bipartite graph algebras.

Use the graph bracket and canonical reduced-row-echelon enumeration; do not
construct ideals from a classification formula during enumeration.
"""
import itertools
from math import prod


def gaussian(n,r,q):
    if r<0 or r>n:return 0
    return prod(q**(n-i)-1 for i in range(r))//prod(q**(r-i)-1 for i in range(r))


def expected(p,s,q):
    out={}
    for a in range(p+1):
        for b in range(s+1):
            M=(p-a)*(s-b)
            d=p*s-M
            for c in range(min(a,b)+1):
                u=a+b-c
                weight=(gaussian(p,a,q)*gaussian(s,b,q)*gaussian(a,c,q)*gaussian(b,c,q)
                        *prod(q**c-q**i for i in range(c)))
                for e in range(M+1):
                    dim=u+d+e
                    ways=weight*gaussian(M,e,q)*q**(u*(M-e))
                    out[dim]=out.get(dim,0)+ways
    return out


def mul_mod_4(x,y):
    z=0
    for j in range(2):
        if (y>>j)&1:z^=x<<j
    for j in (2,):
        if (z>>j)&1:z^=0b111<<(j-2)
    return z


def field(q):
    if q==4:
        plus=lambda a,b:a^b
        mul=mul_mod_4
    elif q in (2,3,5):
        plus=lambda a,b:(a+b)%q
        mul=lambda a,b:(a*b)%q
    else:raise ValueError(q)
    neg=lambda a:(-a)%q if q!=4 else a
    return plus,mul,neg


def enumerate_rref(n,q):
    for r in range(n+1):
        for piv in itertools.combinations(range(n),r):
            slots=[(i,j) for i in range(r) for j in range(piv[i]+1,n) if j not in piv]
            for vals in itertools.product(range(q),repeat=len(slots)):
                rows=[[0]*n for _ in range(r)]
                for i,v in enumerate(piv):rows[i][v]=1
                for (i,j),v in zip(slots,vals):rows[i][j]=v
                yield piv,rows


def brute(p,s,q):
    n=p+s+p*s
    add,mul,neg=field(q)
    # nonzero original Lie brackets only between A basis and B basis,
    # indexed by a*s+b in the centre.  Evaluating all generators suffices.
    bracket=[[[(0)*1 for _ in range(n)] for j in range(p+s)] for i in range(n)]
    for a in range(p):
        for b in range(s):
            v=[0]*n
            v[p+s+a*s+b]=1
            bracket[a][p+b]=v
            bracket[p+b][a]=[neg(z) for z in v]

    def contains(piv,rows,v):
        v=list(v)
        for i,k in enumerate(piv):
            factor=v[k]
            if factor:
                for j in range(k,n):
                    v[j]=add(v[j],neg(mul(factor,rows[i][j])))
        return not any(v)

    result={};subspaces=0
    for piv,rows in enumerate_rref(n,q):
        subspaces+=1
        valid=True
        for row in rows:
            for j in range(p+s):
                bv=[0]*n
                for i,a in enumerate(row[:p+s]):
                    if a:
                        for k,t in enumerate(bracket[i][j]):
                            if t:bv[k]=add(bv[k],mul(a,t))
                if not contains(piv,rows,bv):
                    valid=False
                    break
            if not valid:break
        if valid:
            result[len(rows)]=result.get(len(rows),0)+1
    return subspaces,result


def main():
    cases=[(1,1,2),(1,1,3),(1,1,4),(1,2,2),(1,2,3),(1,2,4),(2,2,2)]
    for p,s,q in cases:
        total,actual=brute(p,s,q)
        theoretical=expected(p,s,q)
        assert actual==theoretical,(p,s,q,actual,theoretical)
        print(f'K_{{{p},{s}}} F_{q} subspaces={total} ideals={sum(actual.values())} by_dim={dict(sorted(actual.items()))}')
    print('BIPARTITE_GRAPH_LIE_IDEALS_OK 7_EXHAUSTIVE_CONFIGURATIONS')

if __name__=='__main__':main()
