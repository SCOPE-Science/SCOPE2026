import math
import sympy as sp

tau, sig, u, v, lam = sp.symbols('tau sig u v lam', positive=True)
M = sp.Matrix([[1, tau], [-sig, 1-tau*sig]])
Q = sp.Matrix([[sig, tau*sig/2], [tau*sig/2, tau]])
assert sp.simplify(M.T*Q*M-Q) == sp.zeros(2)
assert sp.simplify(Q.det() - tau*sig*(4-tau*sig)/4) == 0
H = sig*u*u + tau*sig*u*v + tau*v*v
assert sp.expand(H.subs(u,-1) - (sig*(1-tau*sig/4) + tau*(v-sig/2)**2)) == 0
assert sp.expand(H.subs(v,-1) - (tau*(1-tau*sig/4) + sig*(u-tau/2)**2)) == 0
assert sp.simplify(M.det()) == 1
assert sp.simplify(sp.trace(M)) == 2-tau*sig
coeffs = M.charpoly().all_coeffs()
assert len(coeffs)==3 and sp.simplify(coeffs[0]-1)==0 and sp.simplify(coeffs[1]-(tau*sig-2))==0 and sp.simplify(coeffs[2]-1)==0

# Representative resonances and projected-orbit checks.
for m in [3,4,5,6,7,10,25]:
    h = 2*math.sin(math.pi/m)
    MM = ((1.0,h),(-h,1.0-h*h))
    # Small interior start. Its invariant is far below the boundary threshold.
    z = [0.01,0.0]
    z0 = z[:]
    cstar = h*(1-h*h/4)
    H0 = h*z[0]*z[0] + h*h*z[0]*z[1] + h*z[1]*z[1]
    assert 0 < H0 < cstar
    for k in range(3*m):
        # Projected PDHG in centered variables.
        raw_u = z[0] + h*z[1]
        assert raw_u > -1
        up = max(raw_u + 1.0, 0.0) - 1.0
        raw_v = z[1] - h*up
        assert raw_v > -1
        vp = max(raw_v + 1.0, 0.0) - 1.0
        z = [up,vp]
        Hk = h*z[0]*z[0] + h*h*z[0]*z[1] + h*z[1]*z[1]
        assert abs(Hk-H0) < 1e-11
        if (k+1) % m == 0:
            assert max(abs(z[0]-z0[0]),abs(z[1]-z0[1])) < 1e-10
print('VERIFY_OK')
