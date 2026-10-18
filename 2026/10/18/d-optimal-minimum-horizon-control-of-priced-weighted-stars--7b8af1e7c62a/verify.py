"""Exact finite checks for D-optimal weighted-star finite-horizon control."""
from fractions import Fraction as Q
from math import factorial, prod, sqrt


def det(a):
    a = [list(map(Q, row)) for row in a]
    n = len(a)
    z = Q(1)
    for k in range(n):
        if not a[k][k]:
            t = next((j for j in range(k+1, n) if a[j][k]), None)
            if t is None:
                return Q(0)
            a[t], a[k] = a[k], a[t]
            z = -z
        p = a[k][k]
        z *= p
        for j in range(k+1,n):
            b = a[j][k] / p
            for h in range(k+1,n):
                a[j][h] -= b*a[k][h]
            a[j][k] = 0
    return z


def mult(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def direct(m):
    n=m+1
    w=[Q(i*i+1,1) for i in range(1,m+1)]
    B=sum(w)
    eta=Q(1,2*B)
    L=[[Q(0) for _ in range(n)] for _ in range(n)]
    for i,v in enumerate(w,1):
        L[0][0]+=v;L[i][i]+=v;L[0][i]-=v;L[i][0]-=v
    P=[[(Q(1) if i==j else Q(0))-eta*L[i][j] for j in range(n)] for i in range(n)]
    assert all(sum(row)==1 and all(x>=0 for x in row) for row in P)
    b=[[Q(1) if i==0 else Q(0)] for i in range(n)]
    columns=[]
    for _ in range(n):
        columns.append([v[0] for v in b])
        b=mult(P,b)
    C=[[columns[j][i] for j in range(n)] for i in range(n)]
    G=mult(C,[[C[j][i] for j in range(n)] for i in range(n)])
    d=m*(m+1)//2
    f=prod(w)*prod(w[j]-w[i] for i in range(m) for j in range(i+1,m))
    assert det(C)**2==det(G)==eta**(2*d)*f**2


def poly_mul_x_minus(poly, k):
    out=[0]*(len(poly)+1)
    for i,a in enumerate(poly):
        out[i] -= k*a
        out[i+1] += a
    return out


def laguerre_polys(max_m):
    pp=[[1],[ -2,1]]
    for m in range(2,max_m+1):
        a=poly_mul_x_minus(pp[-1],2*m)
        for i,v in enumerate(pp[-2]):
            a[i]-=m*(m-1)*v
        pp.append(a)
    return pp


def resultant(a,b):
    # Sylvester matrix with descending coefficients.
    m=len(a)-1; n=len(b)-1
    aa=list(reversed(a)); bb=list(reversed(b))
    M=[]
    for i in range(n):M.append([0]*i+aa+[0]*(n-1-i))
    for i in range(m):M.append([0]*i+bb+[0]*(m-1-i))
    return det(M)


def disc_check(m,p):
    if m==1:return
    der=[i*p[i] for i in range(1,len(p))]
    D=(-1)**(m*(m-1)//2)*resultant(p,der)
    formula=prod(j**j*(j+1)**(j-1) for j in range(1,m+1))
    assert D==formula
    assert p[-1]==1 and p[-2]==-m*(m+1)
    assert (-1)**m*p[0]==factorial(m+1)


def two_leaf_cost_check():
    for c1,c2 in [(1,1),(3,1),(8,2),(6,5)]:
        t=(c1+c2+sqrt(c1*c1+c1*c2+c2*c2))/c2
        w1=1/(c1+c2*t);w2=t*w1
        d=3
        lam=d
        lhs1=1/w1+1/(w1-w2)
        lhs2=1/w2+1/(w2-w1)
        assert abs(lhs1-lam*c1)<1e-10 and abs(lhs2-lam*c2)<1e-10
        assert abs(c1*w1+c2*w2-1)<1e-12


def main():
    for m in range(1,7): direct(m)
    for m,p in enumerate(laguerre_polys(7)):
        if m:disc_check(m,p)
    two_leaf_cost_check()
    print('VERIFY_OK exact_star_Gramian_determinants=6 Laguerre_discriminants=6 price_KKT_cases=4')

if __name__=='__main__':main()
