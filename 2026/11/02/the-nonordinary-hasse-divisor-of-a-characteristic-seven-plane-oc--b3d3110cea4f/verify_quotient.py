#!/usr/bin/env python3
"""Independent exact prime-field checks of geometry and quotient Hasse data.

These finite-field checks support, but do not replace, the geometric proof.
All calculations use integer arithmetic modulo seven.
"""
from math import comb
P=7


def curve(x,y,z,lam):
    q=(y*y-2*x*z)%P
    return (y**8-x**7*z-x*z**7-lam*q**4)%P


def grad(x,y,z,lam):
    q=(y*y-2*x*z)%P
    return ((-z**7+lam*z*q**3)%P,
            (y**7-lam*y*q**3)%P,
            (-x**7+lam*x*q**3)%P)


def f_hasse(a):
    # f(t)=t^7+a*t^4+t. Expand f(t)^3 exactly in F_7[t].
    co = [0]*22
    terms = [(7,1),(4,a),(1,1)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                deg=terms[i][0]+terms[j][0]+terms[k][0]
                val=terms[i][1]*terms[j][1]*terms[k][1]
                co[deg]=(co[deg]+val)%P
    return [[co[(i+1)*7-(j+1)] for j in range(3)] for i in range(3)]


def main():
    # Check all F_7-projective representatives (affine and at infinity).
    points=[(x,y,1) for x in range(P) for y in range(P)]
    points.extend((1,y,0) for y in range(P))
    points.append((0,1,0))
    singular_counts={}
    for lam in range(P):
        singular_counts[lam]=sum(curve(*v,lam)==0 and grad(*v,lam)==(0,0,0)
                                 for v in points)
        for x in range(P):
            for y in range(P):
                Q=(y*y-2*x)%P
                eta=(pow(y,7,P)-y)%P
                # Minus sign follows from direct substitution in F_lambda=0.
                if curve(x,y,1,lam)==0:
                    assert (eta*eta-(pow(Q,7,P)+Q-2*lam*pow(Q,4,P)))%P==0
                for b in range(P):
                    yp=(y+b)%P
                    xp=(x+b*y+b*b*pow(2,-1,P))%P
                    assert curve(xp,yp,1,lam)==curve(x,y,1,lam)
                    assert (yp*yp-2*xp-Q)%P==0
                    assert ((pow(yp,7,P)-yp)-eta)%P==0
    assert all(singular_counts[l]==0 for l in range(P) if l not in (1,6))
    assert singular_counts[1]>0 and singular_counts[6]>0
    for lam in range(P):
        a=(-2*lam)%P
        M=f_hasse(a)
        assert M==[[(3*a)%P,0,0],[0,(a**3-a)%P,0],[0,0,(3*a)%P]]
        rank=sum(M[i][i]!=0 for i in range(3))
        expected=0 if lam==0 else (2 if lam in (3,4) else 3)
        assert rank==expected,(lam,rank)
    print('PGL2_7_QUOTIENT_GROUP_ACTION_SMOOTHNESS_AND_HASSE_OK')
    print('Affine F7 non-smooth parameters: '+str([t for t,n in singular_counts.items() if n]))


if __name__ == '__main__':
    main()
