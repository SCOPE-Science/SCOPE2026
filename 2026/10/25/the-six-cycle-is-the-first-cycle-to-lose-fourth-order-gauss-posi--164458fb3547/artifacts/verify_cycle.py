"""Exact symbolic verification of six-cycle fourth-order Gauss endpoint positivity.
Requires SymPy. Run `python verify_cycle.py`. Analytic infinite-n proof is in RESULT.md.
"""
import sympy as S
h=S.symbols('h', positive=True)

def cyc_lap(n):
    L=S.zeros(n)
    for i in range(n):
        j=(i+1)%n
        L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    return L

def update(L,z):
    n=L.rows
    return (12*S.eye(n)+6*z*L+z*z*L*L).inv()*(12*S.eye(n)-6*z*L+z*z*L*L)

L6=cyc_lap(6)
U6=update(L6,h)
D=(h*h+6*h+12)*(3*h*h+6*h+4)*(4*h*h+6*h+3)
Q=5*h**4-12*h**3-102*h**2-144*h-72
exact=[
 (12*h**6+44*h**5+121*h**4+168*h**3+276*h**2+288*h+144)/D,
 -2*h*Q/D,
 2*h*h*(13*h**3+48*h*h+72*h+36)/D,
 2*h**3*(19*h*h+48*h+24)/D
]
for i in range(6):
    for j in range(6):
        d=min((i-j)%6,(j-i)%6)
        assert S.cancel(U6[i,j]-exact[d])==0,(i,j)
    assert S.cancel(sum(U6[i,j] for j in range(6))-1)==0
# C3/C4 from complete multipartite, C5 from the explicit 5-cycle formula.
L5=cyc_lap(5)
U5=update(L5,h)
E=25*h**4+150*h**3+360*h*h+360*h+144
exact5=[(25*h**4+30*h**3+72*h*h+72*h+144)/E,
        72*h*(h+2)/E,
        12*h*h*(5*h+6)/E]
for i in range(5):
    for j in range(5):
        d=min((i-j)%5,(j-i)%5)
        assert S.cancel(U5[i,j]-exact5[d])==0
assert Q.subs(h,6)<0<Q.subs(h,7)
assert [S.sign(c) for c in S.Poly(Q,h).all_coeffs()]==[1,-1,-1,-1,-1]
# Spot check resistance formula, not the proof for all n.
for n in range(6,17):
    L=cyc_lap(n)
    J=S.ones(n,n)/n
    G=(L+J).inv()-J
    assert S.cancel(G[0,1]-S.Rational((n-1)*(n-5),12*n))==0
    assert G[0,1]>0
# Independent exact rational direct inversion at inputs including either side of cutoff.
for val in [S.Rational(1,100),S.Rational(1),S.Rational(6),S.Rational(13,2),S.Rational(7),S.Rational(100)]:
    P=update(L6,val)
    assert all(P[i,j] == exact[min((i-j)%6,(j-i)%6)].subs(h,val) for i in range(6) for j in range(6))
    assert (min(P[i,j] for i in range(6) for j in range(6))>=0)==(val<=S.Rational(6))
print('PASS: C5 and C6 rational orbit formulas; C6 unique threshold sign; 11 cycle Green checks; 216 exact matrix entries')
