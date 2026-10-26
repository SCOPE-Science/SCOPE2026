"""Exact rational checks for a family of symmetric four-coordinate projections.

This checker tests selected rational parameters only. The all-parameter
statement is established by the analytic proof accompanying it.
"""
from fractions import Fraction as F
from itertools import product

def mm(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def check(t):
    B=[[F(1),F(0)],[F(0),F(1)],[F(1),t],[t,F(1)]]
    A=[[(1+t)/(2+t),-t/(2+t),1/(2+t),F(0)],
       [-t/(2+t),(1+t)/(2+t),F(0),1/(2+t)]]
    AB=mm(A,B)
    assert AB==[[F(1),F(0)],[F(0),F(1)]]
    P=mm(B,A)
    expected=2*(1+t)/(2+t)
    rows=[sum(map(abs,row)) for row in P]
    assert rows==[expected]*4, (t,rows)
    # Check the dual certificates for a grid of arbitrary equivariant
    # projections. These examples are not a proof of the global minimum.
    for c,d in product([F(-3,2),F(-1,3),F(0),F(1,4),F(1,1)],repeat=2):
        a=1-c-t*d
        b=-t*c-d
        L1=sum(map(abs,(a,b,c,d)))
        L3=sum(map(abs,(a+t*b,b+t*a,c+t*d,d+t*c)))
        h=t*(c+d)
        assert L1>=1+h and L3>=(1+t)*(1-h)
        assert max(L1,L3)>=expected
    # On the dual polygon the four signed vertices suffice to compute
    # the norm of a linear map into ell_infinity^2.
    q=t/(2+t)
    T=[[F(1),q],[q,F(1)]]
    if t<1:
        a=1/(1+t)
        vertices=[(F(1),F(0)),(F(0),F(1)),(F(1),-F(1)),(a,a)]
    else:
        vertices=[(F(1),F(0)),(F(0),F(1)),(F(1),-F(1))]
    assert max(abs(sum(T[i][j]*v[j] for j in range(2)))
               for i in range(2) for v in vertices)==1
    det=1-q*q
    Inv=[[F(1)/det,-q/det],[-q/det,F(1)/det]]
    def norm(x):
        u,v=x
        return max(abs(u),abs(v),abs(u+t*v),abs(t*u+v))
    inverse_norm=max(norm([sum(Inv[i][j]*v[j] for j in range(2))
                            for i in range(2)])
                     for v in product((-1,1),repeat=2))
    assert inverse_norm==1+t/F(2), (t,inverse_norm)
    assert expected<=inverse_norm
    return rows,inverse_norm

if __name__=='__main__':
    parameters=[F(0),F(1,20),F(1,8),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(7,8),F(1)]
    for t in parameters:
        r, d=check(t)
        print(f't={t} projection={r[0]} distance_upper={d}')
    print(f'PASS: {len(parameters)} exact rational parameter checks, projection identities, dual bounds and distance upper bounds')
