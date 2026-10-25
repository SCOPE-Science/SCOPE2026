"""Exact checks of conditional path length under root protection in uniform recursive trees."""
from fractions import Fraction as Q
from itertools import product
from math import factorial

checks=0

def eq(a,b,msg):
    global checks
    assert a == b, (msg,a,b)
    checks+=1

def h(n):
    return sum((Q(1,j) for j in range(1,n+1)),Q())

def f(n):
    return sum((Q((-1)**j,factorial(j)) for j in range(n+1)),Q())

def tree_stats(parents):
    n=len(parents)+1
    children=[0]*(n+1)
    depth=[0]*(n+1)
    for j,p in enumerate(parents,start=2):
        children[p]+=1
        depth[j]=depth[p]+1
    root_protected=all(children[j]>0 for j in range(2,n+1) if parents[j-2]==1)
    return sum(depth),root_protected

# Independently enumerate every recursive tree of orders 3-8.
for n in range(3,9):
    paths=list(product(*(range(1,j) for j in range(2,n+1))))
    total=len(paths)
    count=0
    psum=0
    psum_cond=0
    for parent in paths:
        length, protected=tree_stats(parent)
        psum+=length
        if protected:
            count+=1
            psum_cond+=length
    N=n-1
    eq(Q(count,total),f(N),f'probability n={n}')
    eq(Q(psum,total),n*(h(n)-1),f'unconditional P n={n}')
    exact_cond=Q(N)+sum(((h(s)-1)*f(N-s) for s in range(2,N+1)),Q())/f(N)
    eq(Q(psum_cond,count),exact_cond,f'conditional P n={n}')
    delta=exact_cond-n*(h(n)-1)
    alternate=sum(((h(N-j)-1)*(f(j)-f(N)) for j in range(N-1)),Q())/f(N)
    eq(delta,alternate,f'covariance difference identity n={n}')
    assert delta>0
    checks+=1

# Exact coefficient identity and strict sign through N=125.
for N in range(2,126):
    conditional=Q(N)+sum(((h(s)-1)*f(N-s) for s in range(2,N+1)),Q())/f(N)
    delta=conditional-(N+1)*(h(N+1)-1)
    alt=sum(((h(N-j)-1)*(f(j)-f(N)) for j in range(N-1)),Q())/f(N)
    eq(delta,alt,f'exact identity N={N}')
    assert delta>0
    checks+=1

# The limiting shift is H_N - 1 + 1/(2N) with error of quadratic order.
for N in (50,100,150,250):
    # high precision avoids large fractions for big N
    import mpmath as mp
    mp.mp.dps=65
    es=[]
    for k in range(30):
        v=f(k)
        es.append(mp.mpf(v.numerator)/v.denominator)
    fN=mp.e**-1 + mp.mpf(0) # negligible factorial correction for N>50
    bN=mp.harmonic(N)-1
    num=mp.fsum((mp.harmonic(N-j)-1)*(es[j]-mp.e**-1) for j in range(30))
    d=num/fN
    err=d-(bN+1/(2*mp.mpf(N)))
    assert abs(err)*N**2 < 20, (N,err)
    checks+=1

print(f'PASS {checks} exact/sign/asymptotic checks; recursive trees exhaustively enumerated n=3..8')
