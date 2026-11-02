"""Supplementary arithmetic and direct-Gram checks for cyclic power-kernel phase ordering.
Python 3 standard library only. No scientific claims beyond the accompanying proof.
"""
import math
import cmath
from fractions import Fraction


def poly_step(P, p, d, k):
    # Numerator of the (k mod d) binomial subsequence at exponent p+1.
    b = p * (d - 1) - k
    Q = [Fraction(0) for _ in range(len(P) + 1)]
    for j, a in enumerate(P):
        Q[j] += Fraction(p+k,p)*a
        Q[j+1] += Fraction(b,p)*a
        if j:
            Q[j] += Fraction(d*j,p)*a
            Q[j+1] -= Fraction(d*j,p)*a
    while len(Q)>1 and Q[-1]==0:
        Q.pop()
    return Q


def numer(p,d,k):
    P=[Fraction(1)]
    for h in range(1,p):
        P=poly_step(P,h,d,k)
    return P


def poly_val(P,z):
    out=0j
    for a in reversed(P):out=out*z+float(a)
    return out


def det(A):
    A=[list(row) for row in A]
    n=len(A); prod=1+0j
    for j in range(n):
        k=max(range(j,n),key=lambda i: abs(A[i][j]))
        if abs(A[k][j])<1e-19:return 0j
        if k!=j:
            A[k],A[j]=A[j],A[k];prod=-prod
        pivot=A[j][j];prod*=pivot
        for h in range(j+1,n):
            mult=A[h][j]/pivot
            for c in range(j+1,n):A[h][c]-=mult*A[j][c]
            A[h][j]=0
    return prod


def gram(p,d,r,s,theta):
    z=[r*cmath.exp(2j*math.pi*j/d) for j in range(d)]
    z += [s*cmath.exp(1j*(theta+2*math.pi*j/d)) for j in range(d)]
    G=[[(1-z[j]*z[k].conjugate())**(-p) for k in range(2*d)] for j in range(2*d)]
    return det(G).real


def blocks(p,d,r,s,theta):
    t=(r*s)**d
    w=t*cmath.exp(-1j*d*theta)
    out=1.0
    for k in range(d):
        P=numer(p,d,k)
        a=d*r**(2*k)*poly_val(P,r**(2*d)).real/(1-r**(2*d))**p
        b=d*s**(2*k)*poly_val(P,s**(2*d)).real/(1-s**(2*d))**p
        c=d*(r*s)**k*poly_val(P,w)/(1-w)**p
        out*=a*b-abs(c)**2
    return out


def run():
    assertions=0
    # Exact arithmetic checks of numerator and denominator recurrence,
    # including all Taylor coefficients through index 18.
    for p in range(2,11):
        for d in range(2,10):
            for k in range(d):
                P=numer(p,d,k)
                assert len(P)-1 == (p*(d-1)-k)//d
                assert all(v>0 for v in P)
                for n in range(19):
                    coeff=sum(((-1)**j)*math.comb(p,j)*math.comb(p+k+d*(n-j)-1,p-1)
                        for j in range(min(n,p)+1))
                    assert Fraction(coeff)==(P[n] if n<len(P) else 0)
                    assertions+=1
    # Direct determinants versus the block product.  Points are
    # kept away from collision to avoid floating-point cancellation.
    for p in (2,3,4,5):
        for d in (2,3,4):
            r,s=0.51,0.79
            vals=[]
            for j in range(5):
                angle=math.pi*j/(4*d)
                a=gram(p,d,r,s,angle); b=blocks(p,d,r,s,angle)
                assert a>0 and b>0
                assert abs(a-b)< 5e-7 * max(a,b)
                vals.append(b)
                assertions+=1
            assert all(vals[i]<vals[i+1] for i in range(4))
            assertions+=1
    # Exact root polynomial examples, including an interior negative root.
    assert numer(3,2,0)==[Fraction(1),Fraction(3)]
    assert numer(4,3,1)==[Fraction(4),Fraction(19),Fraction(4)]
    assertions+=2
    print('PASS:', assertions, 'exact coefficient, block-identity and phase-order checks')

if __name__=='__main__':run()
