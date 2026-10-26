#!/usr/bin/env python3
"""Reproduce finite binary adjacency rank and basin-depth checks for GP(n,2)."""

def graph_rows(n):
    """Two rings of n vertices; rows specify distinct open neighbors."""
    return [((1<<((i-1)%n))^(1<<((i+1)%n))^(1<<(n+i))) for i in range(n)] + [((1<<i)^(1<<(n+((i-2)%n)))^(1<<(n+((i+2)%n)))) for i in range(n)]

def apply_to_cols(rows, columns):
    out=[]
    for col in columns:
        value=0
        for i,row in enumerate(rows):
            if ((row & col).bit_count()&1): value|=1<<i
        out.append(value)
    return out

def gf2_basis(cols):
    b={}
    for y in cols:
        while y:
            p=y.bit_length()-1
            if p not in b:
                b[p]=y
                break
            y^=b[p]
    return b

def in_span(y,b):
    while y:
        p=y.bit_length()-1
        if p not in b: return False
        y^=b[p]
    return True

def mul(cols,x):
    out=0
    while x:
        b=x&-x
        out^=cols[b.bit_length()-1]
        x^=b
    return out

def parameters(n):
    k=n&-n
    r=n//k
    c3=int(r%3==0);c5=int(r%5==0)
    stable=2*n-4*k*(c3+c5)
    depth=max(2*k if c3 else 0,k if c5 else 0)
    return k,c3,c5,stable,depth

def expected_rank(n,t):
    k,c3,c5,stable,_=parameters(n)
    return stable+2*c3*max(2*k-t,0)+4*c5*max(k-t,0)

def expected_depth_cumulative(n,t):
    k,c3,c5,stable,_=parameters(n)
    return 1 << (stable+2*c3*min(t,2*k)+4*c5*min(t,k))

def main():
    checks=0
    for n in range(5,97):
        rows=graph_rows(n)
        current=[1<<i for i in range(2*n)]
        k,c3,c5,stable,T=parameters(n)
        for t in range(max(T,2)+3):
            rank=len(gf2_basis(current))
            assert rank==expected_rank(n,t), ('rank',n,t,rank,expected_rank(n,t))
            checks+=1
            current=apply_to_cols(rows,current)
    print('RANK_CHECKS_OK',checks,'n=5..96')
    total=0
    for n in (5,6):
        rows=graph_rows(n)
        k,c3,c5,stable,T=parameters(n)
        powers=[]
        curr=[1<<i for i in range(2*n)]
        for t in range(T+1):
            powers.append(curr)
            curr=apply_to_cols(rows,curr)
        eventual_basis=gf2_basis(powers[T])
        assert len(eventual_basis)==stable
        observed=[0]*(T+1)
        for x in range(1<<(2*n)):
            for t in range(T+1):
                if in_span(mul(powers[t],x),eventual_basis):
                    observed[t]+=1
            total+=1
        expected=[expected_depth_cumulative(n,t) for t in range(T+1)]
        assert observed==expected,('depth',n,observed,expected)
        print('EXHAUSTIVE_DEPTH_OK',n,observed)
    print('GP_PARITY_VERIFICATION_OK','states=',total)

if __name__=='__main__':main()
