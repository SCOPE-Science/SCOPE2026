#!/usr/bin/env python3
"""Exact check of the sparse rank-two Hankel projection degree identities.

For generic moments s0=2, s2=3, s4=5, forms P and S parameterize
unlabeled Prony nodes on the smooth conic s2*S^2=s0*P^2+2*s2*P+s4.
The checker reduces moment recurrences using S^2=Q(P), verifies
polynomial degrees and discriminant-free generic fiber eliminants.
"""
import sympy as sp
P, S, z = sp.symbols('P S z')
s0, s2, s4 = (sp.Integer(2),sp.Integer(3),sp.Integer(5))
Delta=s2*s2-s0*s4
assert Delta != 0
Q=(s0*P**2+2*s2*P+s4)/s2
# Represent f=a(P)+b(P)/S, reducing S^2=Q
# m0=s0, m1=(s2+s0*P)/S, recurrence m_j=S*m_{j-1}-P*m_{j-2}.
vals=[(s0,sp.Integer(0)), (sp.Integer(0),s2+s0*P)]
for j in range(2,22):
    a_prev,b_prev=vals[j-1]
    a_prev2,b_prev2=vals[j-2]
    # S(a+b/S)=a*S+b=a*Q/S+b
    aj=sp.expand(b_prev-P*a_prev2)
    bj=sp.expand(a_prev*Q-P*b_prev2)
    vals.append((aj,bj))
assert vals[2] == (s2,0)
assert vals[4] == (s4,0)
expected=[4,8,8,12,12,16]
for n in range(6,22):
    m=n-1; a,b=vals[m]
    if m%2 == 0:
        assert b==0,(m,b)
        e=int(sp.degree(a,P)); deg=2*e
        assert e==m-4,(m,e)
        if m>=6: assert sp.LC(sp.Poly(a,P))!=0
        eliminant=sp.Poly(a-z,P)
        assert eliminant.degree()==m-4
    else:
        assert a==0,(m,a)
        e=int(sp.degree(b,P)); deg=2*e
        assert e==m-3,(m,e)
        eliminant=sp.Poly(sp.together(b*b-z*z*Q),P)
        assert eliminant.degree()==2*(m-3)
        assert sp.gcd(sp.Poly(b,P),sp.Poly(Q,P)).degree()==0
    if n in range(7,13):assert deg==expected[n-7], (n,deg)
    print('n',n,'coordinate_degree',deg,'finite_eliminant_degree',eliminant.degree())
print('VERIFY_OK')
