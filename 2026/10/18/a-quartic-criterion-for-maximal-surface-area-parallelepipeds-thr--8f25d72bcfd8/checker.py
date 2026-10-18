"""Exact and numerical checks for the three-dimensional barycentric diagonal criterion.

Run with Python 3, SymPy and NumPy: python checker.py
The mathematical proof, rather than the numerical tests, handles all inputs.
"""
import sympy as sp
import numpy as np

p, q, r, b, c, d = sp.symbols('p q r b c d', real=True)
C = sp.Matrix([[p, r, b], [r, q, c], [b, c, d]])
y = sp.Matrix([0, 0, 1])
s = sp.trace(C)
m = (y.T*C*y)[0]
k = (y.T*C*C*y)[0]
F = sp.expand(9*m*m + 2*s*m - 12*k + 2*sp.trace(C*C) - s*s)
assert sp.expand(F - ((p-q)**2 + 4*r**2 - 8*(b**2+c**2))) == 0

# The axisymmetric formula holds for every aspect ratio and every direction.
a, h, t = sp.symbols('a h t', real=True)
Cax = sp.diag(a, a, h)
# y is a unit vector with third-coordinate square t.
yax = sp.Matrix([sp.sqrt(1-t), 0, sp.sqrt(t)])
ms = (yax.T*Cax*yax)[0]
qs = (yax.T*Cax*Cax*yax)[0]
Fax = sp.factor(9*ms**2 + 2*sp.trace(Cax)*ms-12*qs
                +2*sp.trace(Cax*Cax)-sp.trace(Cax)**2)
assert sp.simplify(Fax-(a-h)**2*(t-1)*(9*t-1)) == 0

# Non-principal axis: an explicit rational/radical exact orthogonal basis.
U = sp.Matrix([[1/sp.sqrt(6),1/sp.sqrt(6),2/sp.sqrt(6)],
               [-1/sp.sqrt(2),1/sp.sqrt(2),0],
               [1/sp.sqrt(3),1/sp.sqrt(3),-1/sp.sqrt(3)]])
y0 = sp.Matrix([2*sp.sqrt(2)/3,0,sp.Rational(1,3)])
Cx = sp.diag(1,1,2)
assert sp.simplify(U.T*U-sp.eye(3)) == sp.zeros(3)
assert sp.simplify(U.T*y0-sp.ones(3,1)/sp.sqrt(3)) == sp.zeros(3,1)
assert all(sp.simplify(z-sp.Rational(4,3))==0
           for z in (U.T*Cx*U).diagonal())
Ax = sp.diag(1, 1, sp.Rational(1,2))
Ax_half = sp.diag(1, 1, 1/sp.sqrt(2))
edge = Ax_half*U*(2/sp.sqrt(3))
for eps1 in (-1, 1):
    for eps2 in (-1, 1):
        for eps3 in (-1, 1):
            vertex = edge*sp.Matrix([eps1, eps2, eps3])/2
            assert sp.simplify((vertex.T*Cx*vertex)[0]-1) == 0
surf = 0
for i,j in ((0,1),(0,2),(1,2)):
    cross = edge[:,i].cross(edge[:,j])
    surf += 2*sp.sqrt(sp.simplify(cross.dot(cross)))
assert sp.simplify(surf-8/sp.sqrt(3)*sp.sqrt(Ax.det())*sp.sqrt(sp.trace(Cx))) == 0

# For general symmetric positive matrices satisfying F=0, reconstruct
# by the 3-theta harmonic formula and check in floating point.
rng = np.random.default_rng(2026)
max_orth = max_diag = max_bary = 0.0
for it in range(300):
    # Work in coordinates y=e3, create arbitrary b and choose D norm accordingly.
    pp, qq, rr, bb, cc = rng.normal(size=5)
    base = np.hypot(bb, cc)
    phase = rng.uniform(-np.pi,np.pi)
    dd1, dd2 = np.sqrt(2)*base*np.cos(phase), np.sqrt(2)*base*np.sin(phase)
    T = np.array([[3+dd1, rr, bb], [rr,3-dd1,cc],[bb,cc,3.]])
    # enforce the trace-free transverse part: cross entry rr must match dd2.
    T[0,1] = T[1,0] = dd2
    T += (1+np.linalg.norm(T,2))*np.eye(3)
    beta, delta = bb+1j*cc, dd1+1j*dd2
    theta = np.angle(-np.sqrt(2)*beta/np.conj(delta))/3 if abs(delta)>1e-12 else 0.0
    th = theta+2*np.pi*np.arange(3)/3
    W = np.stack([np.sqrt(2/3)*np.cos(th),np.sqrt(2/3)*np.sin(th),
                  np.ones(3)/np.sqrt(3)])
    max_orth = max(max_orth,float(np.max(abs(W.T@W-np.eye(3)))))
    max_bary = max(max_bary,float(np.max(abs(W[-1]-1/np.sqrt(3)))))
    max_diag = max(max_diag,float(np.max(abs(np.diag(W.T@T@W)-np.trace(T)/3))))
assert max_orth < 3e-14 and max_diag < 3e-13 and max_bary < 3e-14
print('Exact symbolic identities: PASS')
print('Exact axisymmetric latitude law: PASS')
print('Explicit non-axial basis: PASS')
print('300 numerical 3-harmonic reconstructions: PASS')
print('max orthogonality, diagonal, barycentric errors:',max_orth,max_diag,max_bary)
