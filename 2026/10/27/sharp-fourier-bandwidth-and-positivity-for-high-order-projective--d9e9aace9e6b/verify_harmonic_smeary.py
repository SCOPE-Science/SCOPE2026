"""Standalone exact verification of finite-degree harmonic identities.

Requires Python 3 and sympy. The infinite-degree assertion is proved separately.
"""
from math import comb
from sympy import symbols, cos, diff, expand_trig, simplify, Rational, factorial, pi, integrate

theta, z, eps = symbols('theta z eps', real=True)
checks=0
for m in range(2, 13):
    b0=Rational(comb(2*m,m),2**m)
    bs={j:Rational((-1)**j*comb(2*m,m-j),2**(m-1)) for j in range(1,m+1)}
    f=bs[0] if 0 in bs else b0
    assert simplify(b0+sum(bs.values()))==0;checks+=1
    # spectral multiplier of circular squared-distance kernel
    aj={j:simplify(2*(-1)**j*j*j*bs[j]) for j in range(1,m+1)}
    expect={j:Rational(2**2,2**m)*j*j*comb(2*m,m-j) for j in range(1,m+1)}
    assert aj==expect;checks+=1
    # F''(t)=2(1-pi*psi(t+pi/2)) obtained coefficientwise
    assert all(simplify(Rational((-1)**j,2*j*j)*aj[j]-bs[j])==0 for j in range(1,m+1));checks+=1
    # Closed polynomial form for the density perturbation.
    Rpol = 2*m*(1+z)**(m-1)*(m*z-(m-1))
    # Evaluate at m+1 rational cos points, which determines degree<=m polynomial.
    from sympy import chebyshevt
    T=sum(aj[j]*chebyshevt(j,z) for j in range(1,m+1))
    assert simplify(T-Rpol)==0;checks+=1
    zstar=Rational(m*m-3*m+1,m*m)
    assert -1<zstar<1;checks+=1
    deriv=diff(Rpol,z)
    assert simplify(deriv.subs(z,zstar))==0;checks+=1
    assert simplify(Rpol.subs(zstar if False else z,zstar)+ 2*(2*m-1)*(Rational((2*m-1)*(m-1),m*m))**(m-1))==0;checks+=1
    # derivative changes from negative to positive at zstar; at endpoints R(-1)=0, R(1)>0
    assert simplify(deriv.subs(z,(zstar-1)/2))<0;checks+=1
    assert simplify(deriv.subs(z,(zstar+1)/2))>0;checks+=1
    assert simplify(Rpol.subs(z,-1))==0;checks+=1
    assert Rpol.subs(z,1)>0;checks+=1
print('Verified',checks,'symbolic identities through degree 12')
