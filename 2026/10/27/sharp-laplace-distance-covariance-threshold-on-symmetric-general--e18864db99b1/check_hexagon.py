#!/usr/bin/env python3
"""Algebraic checks for the distance kernel on equal-order generalized hexagons.
Requires Python 3 and SymPy. The paper contains the independent universal proof.
"""
import sympy as S

def main():
    q, x, t = S.symbols('q x t', positive=True)
    P = [S.Integer(1), x, x*x-(q+1)]
    for i in range(3, 6):
        P.append(S.expand(x*P[-1]-q*P[-2]))
    P.append(S.cancel((x*P[-1]-q*P[-2])/(q+1)))
    assert len(P)==7
    # The recurrence requires b_0=q+1, b_i=q (i>=1),
    # c_i=1 (1<=i<=5), c_6=q+1.
    assert S.expand(x*P[1]-P[2]-(q+1))==0
    for i in range(2, 5):
        assert S.expand(x*P[i]-P[i+1]-q*P[i-1])==0
    assert S.simplify(x*P[5]-(q+1)*P[6]-q*P[4])==0
    u = S.sqrt(q)*t
    table = {
       q+1: (1+t)*(1+q*t)*(1-q*t+q*q*t*t)*(1+q*t+q*q*t*t),
       -q-1: (1-t)*(1-q*t)*(1+q*q*t*t+q**4*t**4),
       S.Integer(0): (1-t*t)*(1-q*t*t+q*q*t**4),
       S.sqrt(q): (1-t*t)*(1+u)*(1-u**3),
       -S.sqrt(q): (1-t*t)*(1-u)*(1+u**3),
       S.sqrt(3*q): (1-t*t)*(1+u*u)*(1+u*u+S.sqrt(3)*u),
       -S.sqrt(3*q): (1-t*t)*(1+u*u)*(1+u*u-S.sqrt(3)*u)
    }
    for eigen, predicted in table.items():
        actual=sum(z.subs(x,eigen)*t**i for i,z in enumerate(P))
        difference=S.simplify(S.expand(actual-predicted))
        assert difference==0,(eigen,difference)
    # The top distance polynomial determines the graph diameter.
    for Q in (2,3,4,5,7,9):
        k=Q+1
        v=2*(Q+1)*(1+Q*Q+Q**4)
        kvals=[S.Integer(Q+1), -S.Integer(Q+1),0, S.sqrt(Q),-S.sqrt(Q),S.sqrt(3*Q),-S.sqrt(3*Q)]
        assert len({str(z) for z in kvals})==7
        for eig in kvals:
            assert S.simplify(sum(z.subs({q:Q,x:eig}) for z in P)-(v if eig==k else 0))==0
            t0=S.Rational(1,Q)
            ev=S.simplify(sum(z.subs({q:Q,x:eig})*t0**i for i,z in enumerate(P)))
            assert ev >= 0, (Q,eig,ev)
            assert (ev==0)==(eig==-k), (Q,eig,ev)
    print('PASS: recurrence, seven symbolic spectral factorizations, integer-q endpoint checks')
if __name__=='__main__':
    main()
