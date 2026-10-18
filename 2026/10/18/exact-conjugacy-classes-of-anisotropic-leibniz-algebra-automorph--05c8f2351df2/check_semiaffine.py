#!/usr/bin/env python3
"""Exact enumeration of affine-semilinear conjugacy classes over F_(q^2).

Runs independently of the closed-form proof and uses only Python's standard library.
Test fields: q=3,5,7 and q=9 (the latter constructed as F3[u]/(u^2+1)).
"""
from collections import Counter


def base_field(q):
    if q in (3, 5, 7):
        return (lambda a,b:(a+b)%q), (lambda a,b:(a*b)%q), (lambda a:(-a)%q), 1
    if q == 9:
        # Integers 0..8 encode a+bu, with a,b in F3 and u^2=-1.
        def add(x,y):
            return ((x%3+y%3)%3)+3*((x//3+y//3)%3)
        def mul(x,y):
            a,b=x%3,x//3; c,d=y%3,y//3
            return ((a*c-b*d)%3)+3*((a*d+b*c)%3)
        def neg(x):return ((-x%3)%3)+3*((-(x//3))%3)
        return add,mul,neg,1
    raise ValueError(q)


def build_quadratic_extension(q):
    addk,mulk,negk,one=base_field(q)
    z=0
    squares={mulk(x,x) for x in range(1,q)}
    d=next(x for x in range(1,q) if x not in squares)
    Q=q*q
    K=range(Q)
    def add(x,y):
        a,b=x%q,x//q;c,e=y%q,y//q
        return addk(a,c)+q*addk(b,e)
    def mul(x,y):
        a,b=x%q,x//q;c,e=y%q,y//q
        return addk(mulk(a,c),mulk(d,mulk(b,e)))+q*addk(mulk(a,e),mulk(b,c))
    def neg(x):return negk(x%q)+q*negk(x//q)
    A=[[add(x,y) for y in K] for x in K]
    M=[[mul(x,y) for y in K] for x in K]
    F=[x%q+q*negk(x//q) for x in K]  # q-power Frobenius
    Inv=[0]*Q
    for x in range(1,Q):
        Inv[x]=next(y for y in range(1,Q) if M[x][y]==1)
    assert all(M[x][F[x]] in range(1,q) for x in range(1,Q))
    assert all(M[F[x]][F[y]]==F[M[x][y]] for x in K for y in K)
    return d,A,M,F,Inv,neg


def test_similitudes(q):
    # Independent exhaustive check of the two-dimensional bilinear similitude group.
    add,mul,neg,_=base_field(q)
    d,_,_,_,_,_=build_quadratic_extension(q)
    def sub(x,y):return add(x,neg(y))
    def B(x,y):return sub(mul(x[0],y[0]),mul(d,mul(x[1],y[1])))
    similitudes=set()
    for a in range(q):
        for b in range(q):
            for c in range(q):
                for e in range(q):
                    x=(a,c);y=(b,e)
                    mu=B(x,x)
                    if mu and B(x,y)==0 and B(y,y)==mul(neg(d),mu):
                        similitudes.add((a,b,c,e))
    semilinear=set()
    for a in range(q):
        for b in range(q):
            if not (a or b):continue
            db=mul(d,b)
            semilinear.add((a,db,b,a))
            semilinear.add((a,neg(db),b,neg(a)))
    assert similitudes==semilinear,(q, len(similitudes),len(semilinear))
    assert len(similitudes)==2*(q*q-1)
    return len(similitudes)


def run_case(q):
    d,A,M,F,Inv,neg=build_quadratic_extension(q)
    Q=q*q
    G=[(a,b,e) for a in range(1,Q) for b in range(Q) for e in (0,1)]
    ident=(1,0,0)

    def product(g,h):
        a,b,e=g;c,f,t=h
        if e:c,f=F[c],F[f]
        return (M[a][c],A[b][M[a][f]],e^t)
    def inverse(g):
        a,b,e=g;c=Inv[a]
        if e:c,b=F[c],F[b]
        return (c,neg(M[c][b]),e)

    classes=Counter()
    unseen=set(G)
    involution_count=0
    while unseen:
        g=next(iter(unseen))
        orb={product(product(h,g),inverse(h)) for h in G}
        assert orb <= unseen, 'Conjugacy orbit overlap'
        unseen.difference_update(orb)
        classes[len(orb)]+=1
    for g in G:
        if g!=ident and product(g,g)==ident:
            involution_count+=1

    predicted=Counter({1:1,Q-1:1})
    predicted[Q]+=q-2
    predicted[2*Q]+=(Q-q)//2
    predicted[Q*(q+1)]+=q-2
    predicted[q*(q+1)]+=1
    predicted[q*(Q-1)]+=1
    assert classes==predicted,(q,classes,predicted)
    assert len(G)==2*Q*(Q-1)
    assert sum(k*v for k,v in classes.items())==len(G)
    assert sum(classes.values())==(Q+3*q)//2
    assert involution_count==2*Q+q
    print('q=',q,'nonsquare=',d,'|G|=',len(G),
          'number_classes=',sum(classes.values()),
          'class_sizes=',sorted(classes.items()),
          'involutions=',involution_count)


if __name__=='__main__':
    for q in (3,5,7,9):
        test_similitudes(q)
        run_case(q)
    print('ALL_EXACT_CHECKS_PASSED')
