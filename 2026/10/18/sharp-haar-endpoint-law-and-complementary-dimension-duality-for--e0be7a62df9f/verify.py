#!/usr/bin/env python3
"""Check exact identities and geometric local formula for cross-polytope shadow tails.
Requires only the Python standard library. Numerical experiments are not proofs.
"""
from math import comb, gamma, lgamma, log, pi, exp, sqrt
from random import Random


def log_multigamma(x, k):
    return k*(k-1)*log(pi)/4 + sum(lgamma(x-j/2) for j in range(k))


def leading(n, k):
    q = n-k
    m = k*q
    return exp(log(comb(n,k)) + (m/2)*log(2)
           + log_multigamma(n/2,k)-log_multigamma(k/2,k)
           -lgamma(m/2+1))


def correction(n,k):
    q=n-k
    m=k*q
    return m*(k-2)*(q-2)/(4*(m+2))


def raw_gram(A):
    # Matrix A holds q rows of length two; Gram equals I + A^t A.
    return (1+sum(a*a for a,b in A),
            sum(a*b for a,b in A),
            1+sum(b*b for a,b in A))


def invsqrt2(a,b,c):
    root_det = sqrt(a*c-b*b)
    scalar=sqrt(a+c+2*root_det)
    A,B,C=a+root_det,b,c+root_det
    det=A*C-B*B
    return ((scalar*C/det,-scalar*B/det),
            (-scalar*B/det,scalar*A/det))


def hull_area(points):
    p=sorted(set(points))
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    low=[]
    for x in p:
        while len(low)>=2 and cross(low[-2],low[-1],x)<=0: low.pop()
        low.append(x)
    up=[]
    for x in reversed(p):
        while len(up)>=2 and cross(up[-2],up[-1],x)<=0: up.pop()
        up.append(x)
    poly=low[:-1]+up[:-1]
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]
                 -poly[(i+1)%len(poly)][0]*poly[i][1]
                 for i in range(len(poly))))/2


def check_local_shadow():
    rng=Random(20261017)
    ntests=0
    for q in range(1,8):
        for _ in range(200):
            T=[[rng.uniform(-0.08,0.08),rng.uniform(-0.08,0.08)] for __ in range(q)]
            assert all(sum(abs(x) for x in row)<1 for row in T)
            a,b,c=raw_gram(T)
            M=invsqrt2(a,b,c)
            # Projection images of the ambient coordinate basis, in plane coordinates.
            source=[(1,0),(0,1)]+[tuple(row) for row in T]
            pts=[]
            for x,y in source:
                px=(M[0][0]*x+M[0][1]*y, M[1][0]*x+M[1][1]*y)
                pts.extend([px,(-px[0],-px[1])])
            true_area=hull_area(pts)
            predicted=2/sqrt(a*c-b*b)
            assert abs(true_area-predicted)<2e-12, (q,true_area,predicted)
            ntests+=1
    return ntests


def check_beta_moments():
    # Haar-Stiefel coordinate determinant moments via the beta product.
    tests=0
    for n in range(2,13):
        for k in range(1,n):
            q=n-k
            for s in [1,2,3]:
                val=1.
                for i in range(1,k+1):
                    aa=(k-i+1)/2
                    bb=q/2
                    for j in range(s):val*=(aa+j)/(aa+bb+j)
                # E |det(top block)|^{2}=1 / binomial(n,k)
                if s==1:assert abs(val-1/comb(n,k))<1e-12,(n,k,val)
                tests+=1
    return tests


def check_expansion_algebra():
    count=0
    for n in range(2,16):
        for k in range(1,n):
            q=n-k;m=k*q
            assert abs(leading(n,k)-leading(n,q))<1e-6
            assert abs(correction(n,k)-correction(n,q))<1e-14
            if k==2 or q==2:
                assert abs(leading(n,k)-comb(n,2))<1e-6
                assert correction(n,k)==0
            # Wick fourth moment gives (n+1)/(m+2) for the sphere.
            a=(n+1)/(m+2)
            coeff=(m/4)*(1+2*a-4*n/(m+2))
            assert abs(coeff-correction(n,k))<1e-13,(n,k,coeff)
            count+=1
    assert abs(leading(2,1)-4*sqrt(2)/pi)<1e-13
    assert abs(correction(2,1)-1/12)<1e-13
    assert abs(leading(3,1)-3)<1e-13
    assert abs(leading(3,2)-3)<1e-13
    assert abs(leading(4,2)-6)<1e-13
    return count


def check_beta_monte_carlo():
    # For n=4,k=2, the exact single-coordinate-endpoint tail is eps**2.
    rng=Random(2818)
    eps=.3
    trials=130000
    exceed=0
    for _ in range(trials):
        D2=rng.betavariate(1.,1.)*rng.betavariate(.5,1.)
        exceed+=(D2>=(1-eps)**2)
    p=exceed/trials
    assert abs(p-eps**2)<.004,(p,eps**2)
    return (trials,p)


if __name__=='__main__':
    c=check_local_shadow()
    m=check_beta_moments()
    t=check_expansion_algebra()
    trials,p=check_beta_monte_carlo()
    print('VERIFY_OK',f'local_hulls={c}',f'beta_moments={m}',
          f'asymptotic_identities={t}',f'seeded_mc_n={trials}',f'seeded_mc_p={p:.8f}')
