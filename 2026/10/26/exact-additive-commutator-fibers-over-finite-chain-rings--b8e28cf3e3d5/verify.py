#!/usr/bin/env python3
"""Exact small-ring checks for the additive 2-by-2 commutator fiber law."""
from itertools import product

def val(a,p,m):
    if a==0:return m
    for i in range(m):
        if a%p:return i
        a//=p
    return m

def ring(p,m,kind):
    Q=p**m
    add=[[0]*Q for _ in range(Q)]
    mul=[[0]*Q for _ in range(Q)]
    if kind=='integer':
        for a in range(Q):
            for b in range(Q):
                add[a][b]=(a+b)%Q
                mul[a][b]=(a*b)%Q
    else:
        digits=[tuple((a//p**i)%p for i in range(m)) for a in range(Q)]
        for a in range(Q):
            for b in range(Q):
                ad=digits[a];bd=digits[b]
                add[a][b]=sum(((ad[i]+bd[i])%p)*p**i for i in range(m))
                mul[a][b]=sum((sum(ad[j]*bd[i-j] for j in range(i+1))%p)*p**i for i in range(m))
    return Q,add,mul

def f_nonzero(q,m,s):
    return (q+1)*(q**(3*m+s-1)-q**(3*m-2))

def zero_count(q,m):
    def primitive(k):
        return (q**(3*k)-q**(3*(k-1)))*(q**(2*k)-q**(2*(k-1)))//(q**k-q**(k-1))
    return q**(6*(m//2))+sum(q**(6*v)*primitive(m-2*v) for v in range((m+1)//2))

def test(p,m,kind):
    Q,add,mul=ring(p,m,kind)
    neg=[next(k for k in range(Q) if add[k][a]==0) for a in range(Q)]
    triples=list(product(range(Q),repeat=3))
    ct={}
    for u in triples:
        for v in triples:
            z=(add[mul[u[1]][v[2]]][neg[mul[u[2]][v[1]]]],
               add[mul[u[2]][v[0]]][neg[mul[u[0]][v[2]]]],
               add[mul[u[0]][v[1]]][neg[mul[u[1]][v[0]]]])
            ct[z]=ct.get(z,0)+1
    assert sum(ct.values())==Q**6
    assert len(ct)==Q**3
    for h in triples:
        s=min(val(x,p,m) for x in h)
        predicted=zero_count(p,m) if s==m else f_nonzero(p,m,s)
        assert ct.get(h,0)==predicted,(p,m,kind,h,ct.get(h,0),predicted)
    print('PASS',p,m,kind,'targets',len(triples),'zero_cross',ct[(0,0,0)],'zero_matrix',Q**2*ct[(0,0,0)])

if __name__=='__main__':
    for p,m in [(2,1),(3,1),(2,2),(3,2),(2,3)]:
        for kind in ['integer','polynomial']:
            test(p,m,kind)
    print('VERIFY_OK_COMMUTATOR_FIBERS_CHAIN_RINGS')
