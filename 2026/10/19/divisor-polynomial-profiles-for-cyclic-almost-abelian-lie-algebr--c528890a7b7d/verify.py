#!/usr/bin/env python3
"""Independent exhaustive checks for finite-field cyclic almost-abelian Lie algebras.
Uses only the Python standard library. Run: python verify.py.
"""
from collections import Counter
from itertools import product
from math import prod

def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)

def divmodpoly(f, g, q):
    f, g = list(trim(f)), trim(g)
    assert g
    rem = f[:]
    quo = [0] * max(0, len(f) - len(g) + 1)
    while len(rem) >= len(g):
        k = len(rem) - len(g)
        c = rem[-1] * pow(g[-1], -1, q) % q
        quo[k] = c
        for i, x in enumerate(g):
            rem[k+i] = (rem[k+i] - c*x) % q
        rem = list(trim(rem))
    return trim(quo), trim(rem)

def gcdpoly(f, g, q):
    f, g = trim(f), trim(g)
    while g:
        f, g = g, divmodpoly(f, g, q)[1]
    if not f:
        return ()
    c = pow(f[-1], -1, q)
    return trim([x*c % q for x in f])

def polys_of_degree(degree, q):
    for c in product(range(q), repeat=degree):
        yield tuple(c)+(1,)

def divisors(f, q):
    for d in range(len(f)):
        for g in polys_of_degree(d, q):
            if not divmodpoly(f, g, q)[1]:
                yield g

def phi(g, q):
    d = len(g)-1
    return sum(gcdpoly(a, g, q) == (1,) for a in product(range(q), repeat=d))

def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    ans = 1
    for j in range(1, k+1):
        ans = ans * (q**(n-j+1)-1)//(q**j-1)
    return ans

def span_basis(vecs, q):
    """Canonical row-reduced basis with pivot indices increasing."""
    if not vecs:
        return ()
    n = len(vecs[0]); rows = [list(x) for x in vecs if any(x)]
    r = 0
    for c in range(n):
        pick = next((k for k in range(r, len(rows)) if rows[k][c] % q), None)
        if pick is None:
            continue
        rows[r], rows[pick] = rows[pick], rows[r]
        inv = pow(rows[r][c], -1, q)
        rows[r] = [(x*inv)%q for x in rows[r]]
        for k in range(len(rows)):
            if k != r and rows[k][c] % q:
                a = rows[k][c]
                rows[k] = [(v - a*w) % q for v,w in zip(rows[k], rows[r])]
        r += 1
        if r == len(rows):
            break
    return tuple(tuple(row) for row in rows[:r])

def is_in(vec, basis, q):
    return len(span_basis(basis+(tuple(vec),),q)) == len(basis)

def mat_T(v, f, q):
    m=len(f)-1
    return tuple((([0]+list(v[:-1]))[i]-f[i]*v[-1])%q for i in range(m))

def bracket(x, y, f, q):
    xv, yv = x[1:], y[1:]
    a = tuple((x[0]*b-y[0]*c)%q for b,c in zip(yv,xv))
    return (0,)+mat_T(a,f,q)

def all_subspaces(n, q):
    zero = ()
    seen = {zero}
    front = [zero]
    vectors = list(product(range(q), repeat=n))[1:]
    while front:
        later=[]
        for h in front:
            for v in vectors:
                if is_in(v, h, q):
                    continue
                h2=span_basis(h+(v,),q)
                if h2 not in seen:
                    seen.add(h2); later.append(h2)
        front=later
    return seen

def closure_dim(x, y, f, q):
    bas = span_basis((x,y),q)
    while True:
        new=[]
        for v in bas:
            for w in bas:
                z = bracket(v,w,f,q)
                if not is_in(z,bas,q):
                    new.append(z)
        bas2=span_basis(bas+tuple(new),q)
        if len(bas2)==len(bas):
            return len(bas)
        bas=bas2

def check(q, f):
    m=len(f)-1; n=m+1
    e=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    zero=[0]*(m+2)
    D=Counter({len(g)-1: 0 for g in divisors(f,q)})
    F=Counter()
    for g in divisors(f,q):
        d=len(g)-1
        D[d]+=1
        F[d]+=phi(g,q)
    assert sum(F.values()) == q**m
    psub=Counter(); pideal=Counter(); ppairs=Counter()
    for i in range(m+2):
        if 1<=i<=m+1:
            psub[i] += gaussian(m,i-1,q)
            pideal[i] += D[i-1]
        if i<=m:
            psub[i]+=q**i*D[i]
        if i==0:
            pideal[i]+=1
        if i==1 and f[0]==0:
            pideal[i]+=q
    for j in range(m+2):
        if j==0:
            ppairs[j]+=1
        if j==1:
            ppairs[j]+=(q**m-1)*(q+1)
        if j==2:
            ppairs[j]+=(q**m-1)*(q**m-q)
        if j>=1:
            ppairs[j]+=(q*q-1)*q**m*F[j-1]
    assert sum(ppairs.values())==q**(2*n)
    assert sum(psub.values()) == sum(gaussian(m,i,q) for i in range(m+1))+sum(q**i*D[i] for i in range(m+1))
    obs_sub=Counter();obs_ideal=Counter()
    for bas in all_subspaces(n,q):
        codim=n-len(bas)
        goodsub=all(is_in(bracket(x,y,f,q),bas,q) for x in bas for y in bas)
        goodideal=all(is_in(bracket(x,y,f,q),bas,q) for x in bas for y in e)
        if goodsub:
            obs_sub[codim]+=1
        if goodideal:
            obs_ideal[codim]+=1
    assert obs_sub==psub,(q,f,'subalgebra',obs_sub,psub)
    assert obs_ideal==pideal,(q,f,'ideal',obs_ideal,pideal)
    vv=list(product(range(q),repeat=n))
    obs_pairs=Counter(closure_dim(x,y,f,q) for x in vv for y in vv)
    assert obs_pairs==ppairs,(q,f,'pairs',obs_pairs,ppairs)
    print('PASS',q,list(f), 'sub',sorted(obs_sub.items()),'ideal',sorted(obs_ideal.items()),'pairdims',sorted(obs_pairs.items()))

if __name__=='__main__':
    cases=[(2,(0,0,0,0,0,1)),(2,(1,0,1,0,0,1)),(2,(0,0,0,0,1)),(2,(1,0,0,0,1)),(2,(0,1,1,1,1)),(2,(1,1,0,1)),(2,(0,1,1,1)),
           (3,(0,0,1)),(3,(1,0,1)),(3,(0,2,0,1)),(3,(1,2,0,1))]
    for q,f in cases:
        check(q,f)
    print('VERIFY_OK',len(cases),'independent finite-field configurations')
