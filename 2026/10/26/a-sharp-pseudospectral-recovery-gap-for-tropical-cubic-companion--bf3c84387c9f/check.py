"""Reproduce exact identities and sample singular-value checks for a cubic companion pencil.

Requires Python 3, NumPy, and SymPy.  Run `python check.py`.
"""
import math
import numpy as np
import sympy as sp

e, t = sp.symbols('e t', positive=True)
Q = e + t + e*t*t + e*e*t*t*t
S = sp.Matrix([[1+e*t, 1, e], [1, -e*t, 0], [0, -e, e*t]])
C = sp.Matrix([[e+e*e*t, 1, e], [-1, t, 0], [0, -1, t]])
assert sp.simplify(S - sp.diag(1/e, -1, 1)*C*sp.diag(1, e, e)) == sp.zeros(3,3)
assert sp.factor(S.det() + e*Q) == 0
R = S[:,[0,2]].subs(t,1)
L = S[[1,2],:].subs(t,1)
RG, LG = R.T*R, L*L.T
assert sp.simplify(sp.trace(RG) - (2+2*e+3*e*e)) == 0
assert sp.simplify(RG.det() - e*e*(3+2*e+e*e)) == 0
assert sp.simplify(sp.trace(LG) - (1+3*e*e)) == 0
assert sp.simplify(LG.det() - e*e*(2+e*e)) == 0

phi = (1+math.sqrt(5))/2
for U in (50,100,300,1000,3000,10000):
    E=1.0/U
    X=np.diag([E,-E,E])
    Y=np.array([[1,1,E],[1,0,0],[0,-E,0]],dtype=float)
    A=X+Y
    norm_weight = np.linalg.norm(X,2)+np.linalg.norm(Y,2)
    u,s,vh=np.linalg.svd(A)
    z=vh[-1,:]; w=u[:,-1]
    if z[-1]<0: z=-z
    if w[-1]<0: w=-w
    assert abs(U*s[-1]/norm_weight-1/phi)<.025
    assert abs(abs(z[1])*U-1)<.09
    assert abs(abs(w[0])*U-1)<.09
    muR=np.linalg.svd(A[:,[0,2]], compute_uv=False)[-1]
    muL=np.linalg.svd(A[[1,2],:], compute_uv=False)[-1]
    assert abs(U*muR/norm_weight-math.sqrt(1.5)/phi)<.07
    assert abs(U*muL/norm_weight-math.sqrt(2)/phi)<.07
    for T in (1,2,3):
        actual=np.linalg.svd(Y+T*X, compute_uv=False)[-1]
        target=T/phi
        assert abs(U*actual/(np.linalg.norm(Y,2)+T*E)-target)<.085
print('PASS: companion identity; Gram invariants; scaled singular values; both recovery limits; restricted thresholds')
