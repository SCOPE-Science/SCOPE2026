#!/usr/bin/env python3
"""Standalone finite cross-checks for height-two tree distance-power identities.
Standard library only; finite tests support but do not prove the parameter theorem.
"""
import math
import random


def matrices(m, k, p):
    a, b, c = 2**p, 3**p, 4**p
    P = ((2*m-(m-1)*a, m*(a+1)-(m-1)*b-1),
         (m*(a+1)-(m-1)*b-1, 2*m*a-(m-1)*c-a*(1-1/k)))
    R = ((a, b-1), (b-1, c-a+a/k))
    H = ((2-a, a+1-b), (a+1-b, 2*a-c))
    return P, R, H


def det(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]


def form(M, u, v):
    return M[0][0]*u*u+2*M[0][1]*u*v+M[1][1]*v*v


def exponent(m, k):
    lo = 1.0
    hi = math.log2(2*m/(m-1)) - 1e-8
    assert det(matrices(m,k,lo)[0]) > 0
    assert det(matrices(m,k,hi)[0]) < 0
    for _ in range(66):
        mid = (lo+hi)/2
        if det(matrices(m,k,mid)[0]) > 0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def distances(m, k):
    verts = [('o',-1,-1)] + [('h',i,-1) for i in range(m)] + [('l',i,j) for i in range(m) for j in range(k)]
    parent = {v: None if v[0]=='o' else verts[0] if v[0]=='h' else ('h',v[1],-1) for v in verts}
    def path(v):
        out=[]
        while v is not None:
            out.append(v)
            v=parent[v]
        return out
    paths=[path(v) for v in verts]
    return [[min(a.index(z)+b.index(z) for z in a if z in b) for b in paths] for a in paths]


def assert_close(x,y,scale=1):
    assert abs(x-y)<2e-9*max(1,abs(x),abs(y),scale), (x,y)


def verify():
    checks=0
    for m in range(2,7):
        for k in range(2,7):
            D=distances(m,k)
            n=1+m*(k+1)
            for p in [1.0,1.09,1.31,1.57,1.86]:
                P,R,H=matrices(m,k,p)
                for i in range(2):
                    for j in range(2):
                        assert_close(P[i][j],R[i][j]+m*H[i][j]);checks+=1
                if p>1:
                    assert (-H[0][0])>0 and det(H)>0
                    checks+=1
                for it in range(4):
                    rg=random.Random((m*100+k)*1000+int(p*100)*10+it)
                    w=[0]+[rg.uniform(-2,2) for _ in range(n-1)]
                    w[0]=-sum(w[1:])
                    y=w[1:1+m]
                    leaf=w[1+m:]
                    Z_i=[sum(leaf[i*k:(i+1)*k]) for i in range(m)]
                    Y,Z=sum(y),sum(Z_i)
                    direct=sum(w[i]*w[j]*(D[i][j]**p) for i in range(n) for j in range(n))
                    predicted=-form(P,Y,Z)/m
                    predicted-=sum(form(R,y[i]-Y/m,Z_i[i]-Z/m) for i in range(m))
                    predicted-=(2**p)*sum((leaf[i*k+j]-Z_i[i]/k)**2 for i in range(m) for j in range(k))
                    assert_close(direct,predicted);checks+=1
            r=exponent(m,k)
            assert 1<r<math.log2(2*m/(m-1))
            assert abs(det(matrices(m,k,r)[0]))<4e-11
            assert matrices(m,k,r)[0][0][0]>0
            assert det(matrices(m,k,r)[1])>0
            if m>2: assert r<exponent(m-1,k)
            if k>2: assert r<exponent(m,k-1)
            checks+=6
    assert_close(exponent(2,2),1.5271730882799717);checks+=1
    L2,L3=math.log(2),math.log(3)
    Delta=8*L2**2-(2*L2-3*L3)**2
    assert Delta>0
    def gamma(m):return (10*m-8)*L2-(6*m-6)*L3
    def c_k(k):
        T=20*L2-12*L3+4*L2/k
        return (T-math.sqrt(T*T-16*Delta/k))/(2*Delta)
    for m in [2,3,5]:
        r=exponent(m,1000)
        assert abs(r-1-2/(1000*gamma(m)))<1e-5
        checks+=1
    for k in [2,3,5]:
        r=exponent(1000,k)
        assert abs(r-1-c_k(k)/1000)<1e-5
        checks+=1
    print(f'VERIFY_OK assertions={checks} m=2..6 k=2..6 exact_decomposition_and_asymptotic_checks')

if __name__=='__main__':verify()
