"""Reproducible exact and numerical checks of the two-edge cyclic-shift theorem.

Requires Python 3, SymPy and NumPy. Run: python verify.py
The tests corroborate the algebra; the all-size assertions require the proof.
"""
import sympy as sp
import numpy as np

x, a, b, z = sp.symbols("x a b z")
q = {-1: sp.Integer(0), 0: sp.Integer(1), 1: x}
for m in range(2, 13):
    q[m] = sp.expand(x * q[m-1] - q[m-2])

exact = 0
for n in range(4, 11):
    for k in range(1, n//2 + 1):
        M = sp.zeros(n)
        for j in range(n):
            v = a if j == 0 else b if j == k else sp.Integer(1)
            M[j, (j+1) % n] = v
            M[(j+1) % n, j] = v
        target = (q[n] - (a*a + b*b - 1) * q[n-2] - 2*a*b
                  + (a*a-1)*(b*b-1)*q[k-2]*q[n-k-2])
        assert sp.Poly(sp.expand(M.charpoly(x).as_expr()-target), x, a, b).is_zero
        exact += 1
    for k in range(1, n//2):
        assert sp.expand(q[k-1]*q[n-k-3] - q[k-2]*q[n-k-2] - q[n-2*k-2]) == 0
        exact += 1

# Check the phase-dependent polynomial identity for selected exact parameter values.
phase_exact = 0
for n in range(4, 9):
    for k in range(1, n//2+1):
        for aa, bb in [(sp.Rational(3,2), sp.Rational(1,2)), (sp.Rational(2,3), sp.Rational(4,5))]:
            M = sp.zeros(n)
            for j in range(n):
                v = aa if j==0 else bb if j==k else sp.Integer(1)
                if j < n-1:
                    M[j,j+1] = M[j+1,j] = v
                else:
                    M[n-1,0] = v*z
                    M[0,n-1] = v/z
            target = (q[n] - (aa*aa+bb*bb-1)*q[n-2]
                      + (aa*aa-1)*(bb*bb-1)*q[k-2]*q[n-k-2]
                      - aa*bb*(z + 1/z))
            assert sp.cancel(M.charpoly(x).as_expr() - target) == 0
            phase_exact += 1

# Harmonic support-function comparison for multiple parameter and phase choices.
numeric = 0
for n in range(4, 13):
    for aa, bb in [(2., 3.), (.5, .6), (2., .3), (.4, 4.), (.8, 1.3), (1.1, 1.2)]:
        sgn = np.sign((aa*aa-1)*(bb*bb-1))
        for k in range(1, n//2):
            for theta in np.linspace(0, 2*np.pi, 49):
                top=[]
                for pos in (k, k+1):
                    S=np.zeros((n,n),dtype=complex)
                    for j in range(n):
                        S[j,(j+1)%n] = aa if j==0 else bb if j==pos else 1.
                    H=np.exp(1j*theta)*S + np.exp(-1j*theta)*S.conj().T
                    top.append(np.linalg.eigvalsh(H)[-1])
                assert sgn*(top[0]-top[1]) > -1.e-9
                numeric += 1
print(f"PASSED: {exact} exact zero-flux identities; {phase_exact} exact flux identities; {numeric} numerical support comparisons")
