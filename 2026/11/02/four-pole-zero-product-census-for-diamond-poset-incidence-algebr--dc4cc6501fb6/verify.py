#!/usr/bin/env python3
"""Independent finite-field left-multiplication rank census for diamond incidence algebras."""
from itertools import product


def operations(q):
    if q == 4:
        # F4 = F2[t]/(t*t+t+1), packed binary coefficients.
        def add(a,b): return a^b
        def mul(a,b):
            z=0
            for i in range(2):
                for j in range(2):
                    if (a>>i)&(b>>j)&1: z^=1<<(i+j)
            if z&4: z^=7
            return z
    else:
        def add(a,b): return (a+b)%q
        def mul(a,b): return (a*b)%q
    inverse={a:next(b for b in range(1,q) if mul(a,b)==1) for a in range(1,q)}
    return add,mul,inverse


def rank(rows,q,add,mul,inv):
    rows=[row[:] for row in rows]
    if not rows:return 0
    n=len(rows[0]);r=0
    for j in range(n):
        p=next((i for i in range(r,len(rows)) if rows[i][j]),None)
        if p is None:continue
        rows[r],rows[p]=rows[p],rows[r]
        v=inv[rows[r][j]]
        rows[r]=[mul(v,x) for x in rows[r]]
        for i in range(r+1,len(rows)):
            if rows[i][j]:
                a=rows[i][j]
                rows[i]=[add(x,mul(a,y)) for x,y in zip(rows[i],rows[r])]
        r+=1
        if r==len(rows):break
    return r


def predict(m,q):
    u=q**3*(3*q-2)
    v=q**3*(2*q-1)
    w=q**2*(q*q+q-1)
    z=q**2*(2*q-1)
    return q**3*(u**m+(q-1)*v**m)+2*q*q*(q-1)*w**m+q*(q-1)**2*z**m


def compute(m,q):
    vertices=m+2
    intervals=[(i,j) for i in range(vertices) for j in range(i,vertices) if i==j or i==0 or j==vertices-1]
    assert len(intervals)==3*m+3
    pos={pair:i for i,pair in enumerate(intervals)}
    prod=[[(pos[(u[0],v[1])] if u[1]==v[0] else None) for v in intervals] for u in intervals]
    add,mul,inv=operations(q)
    count=0;N=len(intervals)
    for a in product(range(q),repeat=N):
        # For fixed a, [a * e_j]_j is a linear map; count kernel by rank.
        M=[[0]*N for _ in range(N)]
        for i,x in enumerate(a):
            if x:
                for j,output in enumerate(prod[i]):
                    if output is not None:M[output][j]=add(M[output][j],x)
        count+=q**(N-rank(M,q,add,mul,inv))
    return count


def run():
    cases=[(m,q) for q,M in [(2,4),(3,2),(4,1),(5,1),(7,1)] for m in range(M+1)]
    # q=4 extension field, not integer residue arithmetic.
    for m,q in cases:
        a=compute(m,q);b=predict(m,q)
        assert a==b,(m,q,a,b)
        print(f'm={m} q={q} count={a} PASS')
    print(f'DIAMOND_INCIDENCE_ZERO_PRODUCT_CENSUS_OK {len(cases)}')

if __name__=='__main__':run()
