#!/usr/bin/env python3
"""Direct finite-field enumeration for linear-leading square-zero principal ideals.
Only Python 3 standard library is required. No symbolic algebra packages.
"""
from itertools import product

def plus(a,b,q):
    return (a^b) if q==4 else (a+b)%q

def times(a,b,q):
    if q!=4:return (a*b)%q
    z=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1:z ^= 1<<(i+j)
    if z&4:z^=0b111   # x^2=x+1
    return z

def reciprocal(a,q):
    assert a!=0
    return next(x for x in range(1,q) if times(x,a,q)==1)

def mul(f,g,d,q):
    N=1<<d;out=[0]*N
    for i,a in enumerate(f):
        if not a:continue
        for j,b in enumerate(g):
            if b and i&j==0:out[i|j]=plus(out[i|j],times(a,b,q),q)
    return tuple(out)

def canonical_basis(rows,q):
    m=[list(a) for a in rows if any(a)];r=0
    for c in range(len(rows[0])):
        j=next((s for s in range(r,len(m)) if m[s][c]),None)
        if j is None:continue
        m[r],m[j]=m[j],m[r]
        inv=reciprocal(m[r][c],q)
        m[r]=[times(z,inv,q) for z in m[r]]
        for s in range(len(m)):
            if s==r or not m[s][c]:continue
            v=m[s][c]
            m[s]=[plus(z,times(v,w,q),q) if q==4 else (z-v*w)%q for z,w in zip(m[s],m[r])]
        r+=1
        if r==len(m):break
    return tuple(tuple(a) for a in m[:r]),r

def brute(d,q):
    N=1<<d
    id_basis=[tuple(int(j==i) for j in range(N)) for i in range(N)]
    ideals=set(); eligible=0;squarezero=0
    for tail in product(range(q),repeat=N-1):
        f=(0,)+tail
        if not any(f[1<<j] for j in range(d)):continue
        eligible+=1
        if any(mul(f,f,d,q)):continue
        squarezero+=1
        rows=[mul(f,b,d,q) for b in id_basis]
        basis,r=canonical_basis(rows,q)
        assert r==N//2,(d,q,f,r)
        ideals.add(basis)
    expected=(q**d-1)*q**(N//2-d)//(q-1) if q%2==0 else d
    assert len(ideals)==expected,(d,q,len(ideals),expected)
    return d,q,eligible,squarezero,len(ideals)

def main():
    cases=[(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2)]
    for case in cases:
        d,q,n,c,i=brute(*case)
        print(f'd={d} q={q} nonzero_linear_generators={n} squarezero_generators={c} distinct_ideals={i}')
    print('EXACT_SELFANNIHILATOR_IDEALS_OK',len(cases),'direct exhaustive enumerations')
if __name__=='__main__':main()
