#!/usr/bin/env python3
"""Standalone finite exact-matrix and bounded-grid checks for a two-round
stochastic consensus theorem on strongly regular graphs.

Python 3.10+ standard library only. The infinite-family optimality argument
is mathematical and is not replaced by these finite checks.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import sqrt, isclose

checks = 0

def ck(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def matrix_from_rule(vertices, rule):
    n = len(vertices)
    return [[int(i != j and rule(vertices[i], vertices[j]))
             for j in range(n)] for i in range(n)]

def cycle(n):
    return matrix_from_rule(list(range(n)), lambda a, b: (a-b)%n in (1,n-1))

def petersen():
    return matrix_from_rule(list(combinations(range(5),2)),
                            lambda a,b: set(a).isdisjoint(b))

def clebsch():
    return matrix_from_rule([x for x in range(32) if x.bit_count()%2==0],
                            lambda a,b:(a^b).bit_count()==4)

def rook(m):
    return matrix_from_rule(list(product(range(m),repeat=2)),
                            lambda a,b:a[0]==b[0] or a[1]==b[1])

def triangular(n):
    return matrix_from_rule(list(combinations(range(n),2)),
                            lambda a,b:len(set(a)&set(b))==1)

def multipartite(count,size):
    return matrix_from_rule([(i,j) for i in range(count) for j in range(size)],
                            lambda a,b:a[0]!=b[0])

def shrikhande():
    generators={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
    return matrix_from_rule(list(product(range(4),repeat=2)),
        lambda a,b:((b[0]-a[0])%4,(b[1]-a[1])%4) in generators)

def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]

def test_graph(title,A):
    n=len(A)
    deg=sum(A[0]); ck(0<deg<n-1, title+' proper regularity')
    for i in range(n):
        ck(A[i][i]==0,title+' no loops')
        ck(sum(A[i])==deg,title+' degree')
        for j in range(n): ck(A[i][j]==A[j][i],title+' symmetry')
    C=mm(A,A)
    adjacent={C[i][j] for i in range(n) for j in range(i+1,n) if A[i][j]}
    distant={C[i][j] for i in range(n) for j in range(i+1,n) if not A[i][j]}
    ck(len(adjacent)==1 and len(distant)==1,title+' strong regularity')
    lam=next(iter(adjacent)); mu=next(iter(distant))
    for i in range(n):
        for j in range(n):
            rhs=(deg-mu if i==j else 0)+(lam-mu)*A[i][j]+mu
            ck(C[i][j]==rhs,title+' quadratic adjacency relation')
    m=mu-lam
    if m>0:
        p=F(1,deg);q=F(1,deg+m);R=F(deg-mu,deg*(deg+m))
    else:
        p=q=F(1,deg)
        positive=(lam-mu+sqrt((lam-mu)**2+4*(deg-mu)))/2
        R=positive**2/deg**2
    ck(F(0)<=p<=F(1,deg) and F(0)<=q<=F(1,deg),title+' allowed gains')
    P=[[int(i==j)*(1-deg*p)+p*A[i][j] for j in range(n)] for i in range(n)]
    Q=[[int(i==j)*(1-deg*q)+q*A[i][j] for j in range(n)] for i in range(n)]
    for X in (P,Q):
        for i in range(n):
            ck(sum(X[i])==1,title+' stochastic row')
            for x in X[i]: ck(x>=0,title+' Markov positivity')
    T=mm(P,Q)
    for i in range(n):
        for j in range(n):
            if m>0:
                expected=F(deg-mu,deg*(deg+m))*(i==j)+F(mu,deg*(deg+m))
                ck(T[i][j]==expected,title+' mean-field identity')
                ck(T[i][j]==(R if i==j else 0)+(1-R)/n,
                   title+' centered mean-field representation')
            else:
                expected=F(deg-mu,deg**2)*(i==j)+F(lam-mu,deg**2)*A[i][j]+F(mu,deg**2)
                ck(T[i][j]==expected,title+' two-step polynomial')
    disc=sqrt((lam-mu)**2+4*(deg-mu))
    rr=(lam-mu+disc)/2;ss=(lam-mu-disc)/2
    aa=deg-rr;bb=deg-ss
    def objective(x,y):
        return max(abs((1-aa*x)*(1-aa*y)),abs((1-bb*x)*(1-bb*y)))
    ck(isclose(objective(float(p),float(q)),float(R),rel_tol=1e-12,abs_tol=1e-12),
       title+' exact spectrum objective')
    for i in range(41):
        for j in range(41):
            x=F(i,40*deg);y=F(j,40*deg)
            ck(objective(float(x),float(y))>=float(R)-1e-11,
               title+' bounded-grid global consistency')
    if m>0:
        stat=(rr-ss)**2/(aa+bb)**2
        ck(float(R)<stat-1e-12,title+' strict two-round improvement')
    else:
        ck(rr+ss>=-1e-12,title+' phase sign')
    return (title,n,deg,lam,mu,str(p),str(q),str(R))

cases=[('five-cycle',cycle(5)),('Petersen',petersen()),
       ('Clebsch',clebsch()),('rook-3',rook(3)),
       ('triangular-7',triangular(7)),('multipartite-3x3',multipartite(3,3)),
       ('Shrikhande',shrikhande()),('four-cycle',cycle(4))]
for title,A in cases:
    print('CASE',*test_graph(title,A))
print('VERIFY_OK',checks,'assertions;',len(cases),'independently constructed graphs')
