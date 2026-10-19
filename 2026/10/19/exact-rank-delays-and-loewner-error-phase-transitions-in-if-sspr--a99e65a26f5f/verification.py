"""Exact-arithmetic checks for integrating-factor Gramian quadrature.
Run with Python 3.10 or newer; no third-party modules required.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial, comb

CHECKS = 0

def check(condition, label):
    global CHECKS
    assert condition, label
    CHECKS += 1


def zero(d):
    return [[F(0) for _ in range(d)] for _ in range(d)]


def add(A, B):
    return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]


def scale(c,A):
    return [[c*a for a in row] for row in A]


def vec(d,t):
    return [t**(d-1-i)/factorial(d-1-i) for i in range(d)]


def outer(v):
    return [[a*b for b in v] for a in v]


def weights(q,N):
    if q == 1:
        return [F(1,2) if j in (0,N) else F(1) for j in range(N+1)]
    if q == 2:
        return [F(1,6) if j in (0,2*N) else F(2,3) if j%2 else F(1,3)
                for j in range(2*N+1)]
    raise ValueError(q)


def quad(d,q,N,h):
    Q=zero(d)
    for j,a in enumerate(weights(q,N)):
        Q=add(Q,scale(h*a,outer(vec(d,F(j)*h/q))))
    return Q


def exact(d,T):
    return [[T**(p+r+1) / (F(factorial(p)*factorial(r)*(p+r+1)))
            for r in range(d-1,-1,-1)] for p in range(d-1,-1,-1)]


def det(A):
    n=len(A)
    B=[list(row) for row in A]
    z=F(1)
    for k in range(n):
        i=next((i for i in range(k,n) if B[i][k]),None)
        if i is None:return F(0)
        if i!=k:
            B[k],B[i]=B[i],B[k]
            z=-z
        p=B[k][k]
        z*=p
        for i in range(k+1,n):
            if not B[i][k]:continue
            a=B[i][k]/p
            for j in range(k+1,n):
                B[i][j]-=a*B[k][j]
            B[i][k]=F(0)
    return z


def rank(A):
    B=[list(row) for row in A]
    m=len(B);n=len(B[0]) if B else 0
    piv=0
    for col in range(n):
        s=next((i for i in range(piv,m) if B[i][col]),None)
        if s is None:continue
        B[s],B[piv]=B[piv],B[s]
        div=B[piv][col]
        for j in range(col,n):B[piv][j]/=div
        for i in range(piv+1,m):
            fact=B[i][col]
            for j in range(col,n):B[i][j]-=fact*B[piv][j]
        piv+=1
        if piv==m:break
    return piv


def cb_formula(d,q,N,h):
    w=weights(q,N)
    out=F(0)
    factor=F(h**(d*d),q**(d*(d-1))*
             __import__('math').prod(factorial(j)**2 for j in range(d)))
    for inds in combinations(range(q*N+1),d):
        prod=__import__('math').prod(w[i] for i in inds)
        vd=__import__('math').prod((j-i)**2 for i,j in combinations(inds,2))
        out+=prod*vd
    return factor*out


def check_stage_formula(d,q,N,h):
    # The transformed derivative is exp(-tJ)bb^Texp(-tJ^T).
    W=zero(d)
    for k in range(N):
        a=outer(vec(d,-k*h)); b=outer(vec(d,-(k+1)*h))
        z=add(W,scale(h,a))
        z2=add(z,scale(h,b))
        if q==1:
            W=add(scale(F(1,2),W),scale(F(1,2),z2))
        else:
            mid=add(scale(F(3,4),W),scale(F(1,4),z2))
            z3=add(mid,scale(h,outer(vec(d,-(F(k)+F(1,2))*h))))
            W=add(scale(F(1,3),W),scale(F(2,3),z3))
    # exp(TJ) exp(-tJ)b = exp((T-t)J)b
    Y=zero(d);T=N*h
    w=weights(q,N)
    for j,a in enumerate(w):
        Y=add(Y,scale(h*a,outer(vec(d,T-F(j)*h/q))))
    check(Y==quad(d,q,N,h),('reverse symmetry',d,q,N))
    # Factor W into individual rank-one nodes by the same stage algebra.
    Wdirect=zero(d)
    for j,a in enumerate(w):Wdirect=add(Wdirect,scale(h*a,outer(vec(d,-F(j)*h/q))))
    check(W==Wdirect,('published SSP stages',d,q,N))


def main():
    for q in (1,2):
        for d in range(1,8):
            for N in range(1,5):
                h=F(2,3)
                Q=quad(d,q,N,h)
                check(rank(Q)==min(d,q*N+1),('rank',q,d,N))
                check(det(Q)==cb_formula(d,q,N,h),('det',q,d,N))
                check_stage_formula(d,q,N,h)
                D=add(Q,scale(-1,exact(d,N*h)))
                if q==1:
                    if d==1:check(D==zero(d),('trap exact',d,N))
                    elif d==2:
                        check(D[0][0]==N*h**3/6 and D[1][1]==0 and D[0][1]==0,
                              ('trap psd',d,N))
                    else:
                        # entries for powers 0 and 2 (indices d-1 and d-3).
                        i,j=d-1,d-3
                        check(D[i][i]==0 and D[i][j]==N*h**3/12,
                              ('trap indefinite',d,N))
                else:
                    if d<=2:check(D==zero(d),('Simpson exact',d,N))
                    elif d==3:
                        check(D[0][0]==N*h**5/480 and all(D[i][j]==0 for i in range(d)
                                                     for j in range(d) if (i,j)!=(0,0)),
                              ('Simpson psd',d,N))
                    else:
                        # powers 1 and 3 (indices d-2 and d-4).
                        i,j=d-2,d-4
                        check(D[i][i]==0 and D[i][j]==N*h**5/720,
                              ('Simpson indefinite',d,N))
        # Minimal-step determinant identities.
        for d in range(2,8):
            if q==1:
                N=d-1
                x=F(1,4)*F(2,3)**(d*d)
            elif d%2:
                N=(d-1)//2
                x=F(2)**(N-2-d*(d-1))*F(3)**(-(2*N+1))*F(2,3)**(d*d)
            else:continue
            check(det(quad(d,q,N,F(2,3)))==x,('minimal determinant',q,d,N))
    print('PASS',CHECKS,'exact-rational assertion families')

if __name__=='__main__':main()
