#!/usr/bin/env python3
"""Exact-rational direct enumeration of row/column-sampled gradient updates.

This program checks consequences of the proved formulas. Its finite tests are
not a substitute for the algebraic argument in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def sylvester(order):
    H = [[1]]
    while len(H) < order:
        H = [row + row for row in H] + [row + [-v for v in row] for row in H]
    assert len(H) == order
    return H


def dot(u, v):
    return sum((a*b for a,b in zip(u,v)), F(0))


def norm2(u):
    return dot(u,u)


def matvec(A, e):
    return [dot(row,e) for row in A]


def verify_case(m, scales, e, eta):
    n = len(scales)
    H = sylvester(m)
    A = [[F(H[i][j])*scales[j] for j in range(n)] for i in range(m)]
    assert all(sum(A[i][j]*A[i][k] for i in range(m)) == (m*scales[j]**2 if j==k else 0)
               for j in range(n) for k in range(n))
    r = matvec(A,e)
    total_e = F(0)
    total_r = F(0)
    for i,j in product(range(m),range(n)):
        ep = list(e)
        ep[j] -= eta * A[i][j] * r[i]
        total_e += norm2(ep)
        total_r += norm2(matvec(A,ep))
    total_e /= m*n
    total_r /= m*n
    lambdas = [m*s*s for s in scales]
    s2 = sum(lambdas, F(0))
    s4 = sum((a*a for a in lambdas), F(0))
    rhs_e = norm2(e) - eta * (2-eta*s2/m)*norm2(r)/(m*n)
    rhs_r = norm2(r) - eta*(2*sum(lambdas[j]**2*e[j]**2 for j in range(n))
                           -eta*s4*norm2(r)/m)/(m*n)
    assert total_e == rhs_e, (m,scales,e,eta,total_e,rhs_e)
    assert total_r == rhs_r, (m,scales,e,eta,total_r,rhs_r)
    return 1


def main():
    count=0
    for m,n in ((2,2),(4,2),(4,3),(4,4),(8,3),(8,8)):
        for base in (1,2,3):
            scales = [F((j+1)*base+(j%2),j+base+1) for j in range(n)]
            for shift in (-2,-1,0,1,2):
                e = [F((j+1)*shift+(-1)**j,j+2) for j in range(n)]
                for eta in (F(1,10),F(1,3),F(3,2),F(5,1)):
                    count+=verify_case(m, scales, e, eta)
    # Two-mode exact example: A=Hadamard(2)*diag(2,1), e=(0,1), eta=1/5.
    m=2; scales=[F(2),F(1)]; e=[F(0),F(1)]; eta=F(1,5)
    verify_case(m,scales,e,eta)
    A=[[F(2),F(1)],[F(2),F(-1)]]
    vals=[]
    for i,j in product(range(2),range(2)):
        ep=list(e); ep[j]-=eta*A[i][j]*matvec(A,e)[i]
        vals.append((norm2(ep),norm2(matvec(A,ep))))
    assert sum((a for a,b in vals),F(0))/4==F(9,10)
    assert (sum((b for a,b in vals),F(0))/4)/norm2(matvec(A,e)) == F(57,50)
    # Compare the two-mode second-moment recursion with exact enumeration
    # of all sample paths of length 3, then check a long contrast limit.
    for scale in (F(1),F(2),F(3)):
        rho=scale*scale
        a=1-rho/(rho+1)+rho*rho/(2*(rho+1)**2)
        b=rho/(2*(rho+1)**2)
        d=1-F(1)/(rho+1)+F(1)/(2*(rho+1)**2)
        u,v=F(0),F(1)
        states=[(F(1),[F(0),F(1)])]
        mat=[[scale,F(1)],[scale,-F(1)]]
        eta=F(1)/(rho+1)
        for k in range(1,4):
            u,v=a*u+b*v,b*u+d*v
            next_states=[]
            for probability,error in states:
                residual=matvec(mat,error)
                for i,j in product(range(2),range(2)):
                    ep=error.copy(); ep[j]-=eta*mat[i][j]*residual[i]
                    next_states.append((probability/F(4),ep))
            states=next_states
            actual_u=sum((p*e[0]**2 for p,e in states),F(0))
            actual_v=sum((p*e[1]**2 for p,e in states),F(0))
            assert (u,v)==(actual_u,actual_v),(rho,k,u,v,actual_u,actual_v)
            count+=1
    rho=10**6
    s=rho+1
    a=1-rho/s+rho*rho/(2*s*s)
    c=rho*rho/(2*s*s)
    d=1-1/s+1/(2*s*s)
    q=1/(2*s*s)
    v=0.0
    y=1.0
    for k in range(1000):
        v,y=a*v+c*y,q*v+d*y
    assert 1.997 < v+y < 2.0,(v,y)
    print(f'PASS {count+1} exact-rational enumerations, plus the near-doubling asymptotic check; example error ratio 9/10, residual ratio 57/50')

if __name__ == '__main__':
    main()
