"""Independent small-field enumeration of Lie-subalgebra generation pairs.
Run with Python 3 standard library only; decimal is used for the limit checks.
"""
from collections import Counter
from itertools import combinations, product
from math import prod

def gaussian(m,r,q):
    if r<0 or r>m:return 0
    r=min(r,m-r)
    a=prod(q**(m-i)-1 for i in range(r))
    b=prod(q**(i+1)-1 for i in range(r))
    return a//b

def isotropic(m,r,q):
    if r<0 or r>m:return 0
    return prod(q**(2*(m-i))-1 for i in range(r))//prod(q**(i+1)-1 for i in range(r))

def rrefs(d,p):
    for k in range(d+1):
        for piv in combinations(range(d),k):
            coords=[(i,j) for i in range(k) for j in range(piv[i]+1,d) if j not in piv]
            for vals in product(range(p),repeat=len(coords)):
                a=[[0]*d for _ in piv]
                for i,j in enumerate(piv):a[i][j]=1
                for (i,j),v in zip(coords,vals):a[i][j]=v
                yield a

def rank(rows,p):
    if not rows:return 0
    a=[list(row) for row in rows]; d=len(a[0]); k=0
    for col in range(d):
        pos=next((i for i in range(k,len(a)) if a[i][col]%p),None)
        if pos is None:continue
        a[k],a[pos]=a[pos],a[k]
        fac=pow(a[k][col],-1,p)
        a[k]=[(v*fac)%p for v in a[k]]
        for i in range(len(a)):
            if i!=k and a[i][col]%p:
                z=a[i][col]%p
                a[i]=[(x-z*y)%p for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return k

def projection(rows,d):
    return tuple(tuple(row[:d]) for row in rows)

def brute(n,p):
    d=2*n
    hist=Counter(); num_sub=0
    for rows in rrefs(d+1,p):
        central=rank(rows+[[0]*d+[1]],p)==len(rows)
        iso=all(sum((v[2*i]*w[2*i+1]-v[2*i+1]*w[2*i]) for i in range(n))%p==0 for v,w in combinations(rows,2))
        if central or iso:
            hist[projection(rows,d)]+=1
            num_sub+=1
    ps=list(hist.items())
    pairs=sum(c1*c2 for (a,c1) in ps for (b,c2) in ps if rank(a+b,p)==d)
    return num_sub,pairs,len(ps)

def finite_spanning(n,q):
    D=2*n
    N=sum(gaussian(D,r,q) for r in range(D+1))
    T=0
    for r in range(D+1):
        for s in range(D-r,D+1):
            t=r+s-D
            T+=gaussian(D,r,q)*gaussian(r,t,q)*q**((D-r)*(D-s))
    return T,N*N

def limit(q):
    from decimal import Decimal, getcontext
    getcontext().prec=85
    Q=Decimal(q)
    phi=[Decimal(1)]
    for i in range(1,100):
        phi.append(phi[-1]*(1-Q**(-i)))
    theta=sum((Q**(-j*j) for j in range(-20,21)),Decimal(0))
    K=sum((Q**(-j*j-k*k)/phi[j+k]
           for j in range(-15,16) for k in range(-15,16) if j+k>=0),Decimal(0))
    return phi[-1]*K/theta**2

def main():
    for n,q in ((1,2),(1,3),(1,5),(2,2),(2,3)):
        N,G,C=brute(n,q)
        subN=sum(gaussian(2*n,r,q) for r in range(2*n+1))+sum(q**r*isotropic(n,r,q) for r in range(n+1))
        assert N==subN,(n,q,N,subN)
        assert 0<G<N*N
        print('EXHAUSTIVE_PAIR_OK',n,q,'total_subalgebras',N,'generating_pairs',G,'projection_subspaces',C)
    for q in (2,3,5):
        L=limit(q)
        print('THETA_CONSTANT',q,str(L))
        for n in (8,16,32,48):
            top,bot=finite_spanning(n,q)
            v=top/bot
            assert abs(v-float(L))<.16,(n,q,v,float(L))
            print('ASYMPTOTIC_PAIR_OK',q,n,'center_containing_ratio',format(v,'.12f'))
    print('VERIFY_OK 5 exhaustive configurations and 12 asymptotic finite-sum checks')
if __name__=='__main__':main()
