#!/usr/bin/env python3
"""Exact two-round atomic diagrams of one-dimensional affine finite-field groups.
All calculations use the semidirect-product description and cyclicity of F_q^*;
no sample-based extrapolation is used in deriving a spectrum for an individual q.
"""
from collections import defaultdict

def profile(q,p):
    assert q>=2 and q%p==0
    z=q; k=0
    while z%p==0: z//=p; k+=1
    assert z==1
    m=q-1
    def atom(xe,ye,eq,x2e,y2e,x2y,y2x,xy_e):
        return (int(xe),int(ye),int(eq),int(x2e),int(y2e),int(x2y),int(y2x),int(xy_e))
    types=set()
    # Identity as first element.
    inner={atom(1,1,1,1,1,1,1,1),atom(1,0,0,1,p==2,0,p==2,0)}
    if m%2==0:
        inner.add(atom(1,0,0,1,1,0,1,0))
    if m>2:
        inner.add(atom(1,0,0,1,0,0,0,0))
    types.add(frozenset(inner))
    # First element a nonzero translation.
    inner=set()
    for r in range(p):
        inner.add(atom(0,r==0,r==1,p==2,(2*r)%p==0,r==(2%p),(2*r)%p==1,(r+1)%p==0))
    if q>p:
        inner.add(atom(0,0,0,p==2,p==2,0,0,0))
    for k in range(1,m):
        inner.add(atom(0,0,0,p==2,2*k%m==0,0,0,0))
    types.add(frozenset(inner))
    # First nontranslation affine map is conjugate to (a,0).
    for j in range(1,m):
        x2e=(2*j)%m==0
        inner=set()
        for h in range(m):
            inner.add(atom(0,h==0,h==j,x2e,(2*h)%m==0,h==(2*j)%m,(2*h)%m==j,(j+h)%m==0))
            y2e=((h==0 and p==2) or (m%2==0 and h==m//2))
            inner.add(atom(0,0,0,x2e,y2e,0,0,0))
        types.add(frozenset(inner))
    return frozenset(types)

def primes_up_to(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for d in range(2, int(limit ** 0.5) + 1):
        if sieve[d]:
            for z in range(d*d, limit+1, d): sieve[z] = False
    return [d for d in range(2, limit+1) if sieve[d]]

def prime_powers(limit):
    for p in primes_up_to(limit):
        q=p
        while q<=limit:
            yield int(q),int(p)
            q*=p

if __name__=='__main__':
    P=defaultdict(list)
    for q,p in sorted(prime_powers(101)):
        P[profile(q,p)].append(q)
    print('CLASSES',len(P))
    for i,(_,vals) in enumerate(sorted(P.items(),key=lambda o:min(o[1])),1):
        print(i, vals)

def direct_profile(q,p,mod_poly=None):
    """Independent explicit multiplication calculation, for small prime powers."""
    if mod_poly is None: mod_poly=[0,1]
    f=len(mod_poly)-1
    assert p**f==q and mod_poly[-1]==1
    def vec(z):
        a=[]
        for _ in range(f): a.append(z%p); z//=p
        return a
    def num(v): return sum((int(t)%p)*p**i for i,t in enumerate(v))
    V=[vec(z) for z in range(q)]
    plus=[[num([(V[i][k]+V[j][k])%p for k in range(f)]) for j in range(q)] for i in range(q)]
    prod=[]
    for i in range(q):
        row=[]
        for j in range(q):
            vv=[0]*(2*f-1)
            for a in range(f):
                for b in range(f): vv[a+b]=(vv[a+b]+V[i][a]*V[j][b])%p
            for s in range(2*f-2,f-1,-1):
                d=vv[s]
                for t in range(f): vv[s-f+t]=(vv[s-f+t]-d*mod_poly[t])%p
            row.append(num(vv[:f]))
        prod.append(row)
    elems=[(a,b) for a in range(1,q) for b in range(q)]
    e=(1,0)
    def mul(x,y):
        a,b=x;c,d=y
        return prod[a][c],plus[b][prod[a][d]]
    squares={x:mul(x,x) for x in elems}
    out=set()
    for x in elems:
        rows=set()
        for y in elems:
            rows.add(tuple(int(z) for z in (x==e,y==e,x==y,squares[x]==e,squares[y]==e,squares[x]==y,squares[y]==x,mul(x,y)==e)))
        out.add(frozenset(rows))
    return frozenset(out)

def predicted_class(q,p):
    if p==2:
        f=0; z=q
        while z>1: z//=2; f+=1
        return {1:'A',2:'C'}.get(f, 'F' if f%2 else 'J')
    if p==3:
        f=0; z=q
        while z>1: z//=3; f+=1
        return 'B' if f==1 else 'G' if f==2 else 'M' if f%2 else 'O'
    if q==5: return 'D'
    m=q-1; v=0
    while m%2==0: m//=2; v+=1
    has3=(q-1)%3==0
    if v==1: return 'E' if has3 else 'H'
    if v==2: return 'I' if has3 else 'N'
    return 'L' if has3 else 'K'

if __name__=='__main__':
    representatives={'A':2,'B':3,'C':4,'D':5,'E':7,'F':8,'G':9,'H':11,'I':13,'J':16,'K':17,'L':25,'M':27,'N':29,'O':81}
    rp={q: next(p for z,p in prime_powers(81) if z==q) for q in representatives.values()}
    reference={k:profile(q,rp[q]) for k,q in representatives.items()}
    assert len(set(reference.values()))==15
    print('FIFTEEN_PAIRWISE_DISTINCT_ROOT_SIGNATURES_OK')
    checked=0
    for q,p in prime_powers(401):
        assert profile(q,p)==reference[predicted_class(q,p)],(q,p,predicted_class(q,p))
        checked+=1
    print('ARITHMETIC_PARTITION_CHECK_OK',checked,'prime_power_fields_up_to_401')
    tests=[(2,2,[0,1]),(3,3,[0,1]),(4,2,[1,1,1]),(5,5,[0,1]),(7,7,[0,1]),(8,2,[1,1,0,1]),(9,3,[1,0,1]),(11,11,[0,1]),(13,13,[0,1]),(16,2,[1,1,0,0,1]),(17,17,[0,1]),(19,19,[0,1]),(25,5,[2,0,1]),(27,3,[1,2,0,1]),(29,29,[0,1])]
    for q,p,poly in tests:
        a=profile(q,p); b=direct_profile(q,p,poly)
        assert a==b,(q,len(a-b),len(b-a))
        print('DIRECT_GROUP_MULTIPLICATION_OK',q,len(a))
