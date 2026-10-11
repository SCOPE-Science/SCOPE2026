"""Symbolic checks for the near-Hopf period theorem of the Brusselator.
Run with: python verify_brusselator.py  (requires SymPy)."""
import sympy as sp

A, mu, w, p = sp.symbols('A mu w p', real=True, nonzero=True)
B = 1 + A**2 + mu
x = A - p
y = B/A + w + p
xdot = A - (B+1)*x + x*x*y
rhs = (mu*p + 2*A*w*p + (A - 1/A - mu/A)*p**2
       - w*p**2 - p**3)
assert sp.simplify(-xdot + A*A*w - rhs) == 0, 'exact scalar reduction'

q, om, tau = sp.symbols('q om tau', real=True)
w1 = sp.cos(tau)
w1p = sp.diff(w1, tau)
w2 = ((A-1/A)/2 + (A-1/A)/6*sp.cos(2*tau)
      + sp.sin(2*tau)/3)
w2p = sp.diff(w2, tau)
# Order 2 equation: A^2(w2''+w2)=2A^2*w1*w1'+(A^3-A)*w1'^2
res2 = A**2*(sp.diff(w2,tau,2)+w2) - (
    2*A**2*w1*w1p + (A**3-A)*w1p**2)
assert sp.trigsimp(sp.expand_trig(res2)) == 0, 'order-two Fourier equations'

# Cubic resonances in the oscillator, with mu=q*rho^2, Omega=A+om*rho^2.
f3 = (q*A*w1p + 2*A**2*(w1*w2p + w2*w1p)
      + 2*(A**3-A)*w1p*w2p - A**2*w1*w1p**2
      - A**3*w1p**3 + 2*A*om*sp.cos(tau))
C = sp.factor(sp.integrate(sp.expand_trig(f3)*sp.cos(tau), (tau,0,2*sp.pi))/sp.pi)
S = sp.factor(sp.integrate(sp.expand_trig(f3)*sp.sin(tau), (tau,0,2*sp.pi))/sp.pi)
assert sp.simplify(C - (4*A**4-7*A**2+24*A*om+4)/12) == 0, 'cos resonance'
assert sp.simplify(S + A*(4*q-A**2-2)/4) == 0, 'sin resonance'
sol = sp.solve([C,S], [q,om],dict=True)[0]
assert sp.simplify(sol[q] - (A*A+2)/4) == 0, 'Hopf-amplitude coefficient'
assert sp.simplify(sol[om] - (-4*A**4+7*A*A-4)/(24*A)) == 0, 'frequency coefficient'
period_coefficient = sp.factor(-sol[om]/(A*sol[q]))
expected = (4*A**4-7*A**2+4)/(6*A**2*(A**2+2))
assert sp.simplify(period_coefficient-expected) == 0, 'period coefficient'
U = sp.symbols('U',real=True)
assert sp.simplify((4*U**2-7*U+4) - (4*(U-sp.Rational(7,8))**2+sp.Rational(15,16))) == 0
print('PASS: exact scalar reduction; harmonic order 2; two cubic resonances;')
print('PASS: nondegenerate Hopf branch; analytic period coefficient; strict positivity.')
print('kappa =',sol[q])
print('nu =',sol[om])
print('relative period derivative =', period_coefficient)
