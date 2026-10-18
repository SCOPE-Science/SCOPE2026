"""Exact checks for local peak/trough covariance in labeled trees.

Pure Python standard library. No network access or external dependencies.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, permutations
from math import factorial, comb

@lru_cache(None)
def adjacent(a,b):
    assert a>=1 and b>=1
    return F(1,a*b)-F(factorial(a-1)*factorial(b-1),factorial(a+b))-F(1,(a+1)*(b+1))

@lru_cache(None)
def distance_two(a,b):
    assert a>=1 and b>=1
    joint=(F(1)-F(1,a+1)-F(1,b+1)+F(factorial(a)*factorial(b),factorial(a+b+1)))/(a*b)
    return joint-F(1,(a+1)*(b+1))

def quenched_cov(edges,n):
    neigh=[set() for _ in range(n)]
    for a,b in edges:
        neigh[a].add(b);neigh[b].add(a)
    deg=[len(x) for x in neigh]
    assert min(deg)>=1
    out=-sum((F(1,(a+1)**2) for a in deg),F(0))
    for v in range(n):
        for w in range(n):
            if v==w: continue
            if w in neigh[v]: out+=adjacent(deg[v],deg[w])
            elif neigh[v]&neigh[w]:out+=distance_two(deg[v],deg[w])
    return out

def brute_cov(edges,n):
    neigh=[set() for _ in range(n)]
    for v,w in edges:neigh[v].add(w);neigh[w].add(v)
    sums=[0,0,0]
    for perm in permutations(range(n)):
        a=sum(all(perm[v]>perm[w] for w in neigh[v]) for v in range(n))
        b=sum(all(perm[v]<perm[w] for w in neigh[v]) for v in range(n))
        sums[0]+=a;sums[1]+=b;sums[2]+=a*b
    m=factorial(n)
    return F(sums[2],m)-F(sums[0]*sums[1],m*m)

def prufer_tree(seq,n):
    d=[1]*n
    for v in seq:d[v]+=1
    edges=[]
    for v in seq:
        u=next(i for i,z in enumerate(d) if z==1)
        edges.append((u,v)); d[u]-=1;d[v]-=1
    u,v=(i for i,z in enumerate(d) if z==1)
    edges.append((u,v))
    return edges

def joint_counts(m,n):
    for i in range(m+1):
        for j in range(m-i+1):
            z=m-i-j
            p=F(factorial(m),factorial(i)*factorial(j)*factorial(z))*F(1,n)**(i+j)*F(n-2,n)**z
            yield i,j,p

def predicted(n):
    assert n>=4
    selfterm=sum((F(comb(n-2,j)*(n-1)**(n-2-j),n**(n-2))*F(1,(2+j)**2) for j in range(n-1)),F(0))
    edge=F(0)
    for i,j,p in joint_counts(n-3,n):
        edge+=p*(adjacent(2+i,1+j)+adjacent(1+i,2+j))/2
    twopath=F(0)
    for i,j,p in joint_counts(n-4,n):
        twopath+=p*(distance_two(2+i,1+j)+distance_two(1+i,2+j)+distance_two(1+i,1+j))/3
    return -n*selfterm+2*(n-1)*edge+F(3*(n-1)*(n-2),n)*twopath

def limit_certificate(K=10):
    """Rational interval for limiting normalized quenched covariance.

    The rational weights 1/(j! E_K), j<=K, are exactly the law
    of Poisson(1) conditional on being <=K. Its tail probability
    delta is at most T=(K+2)/((K+1)*(K+1)!). The TV distance for
    the two-variable product laws is at most 2 delta; with
    |H_1|,|H_2|<=1 and a 1/4 bound on the self term, the difference
    between the full and conditioned expressions is <=21*T.
    """
    E=sum((F(1,factorial(j)) for j in range(K+1)),F(0))
    T=F(K+2,(K+1)*factorial(K+1))
    t=1/E
    u=sum((F(1,factorial(i))*F(1,(2+i)**2) for i in range(K+1)),F(0))
    v=F(0)
    for i in range(K+1):
        for j in range(K+1):
            w=F(1,factorial(i)*factorial(j))
            va=(adjacent(2+i,1+j)+adjacent(1+i,2+j))/2
            vb=(distance_two(2+i,1+j)+distance_two(1+i,2+j)+distance_two(1+i,1+j))/3
            v+=w*(2*va+3*vb)
    estimate=-t*u+t*t*v
    lo,hi=estimate-21*T,estimate+21*T
    assert F(-1,25)<lo<hi<F(-3,100), (lo,hi)
    return lo,hi

def main():
    tests=0
    for n in range(3,7):
        for seq in product(range(n),repeat=n-2):
            edges=prufer_tree(seq,n)
            lhs=quenched_cov(edges,n)
            if n<=5 or (n==6 and len(set(seq))<=2):
                assert lhs==brute_cov(edges,n)
                tests+=1
        if n>=4:
            mean=sum((quenched_cov(prufer_tree(seq,n),n) for seq in product(range(n),repeat=n-2)),F(0))/n**(n-2)
            assert mean==predicted(n), (n,mean,predicted(n))
            tests+=1
    for n in range(4,13):
        path=[(i,i+1) for i in range(n-1)]
        assert quenched_cov(path,n)==F(8*n-37,180)
        tests+=1
    lo,hi=limit_certificate(10)
    tests+=1
    print('PASS:',tests,'exact covariance, enumeration and sign-certificate assertions')
    print('Limiting coefficient certified in (',float(lo),',',float(hi),')')
    print('Examples: n=4 quenched average',predicted(4),'n=5',predicted(5),'n=6',predicted(6))

if __name__=='__main__': main()
