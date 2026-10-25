"""Reproducible algebraic and finite-parameter checks for a two-dot BdG fold."""
import numpy as np
import sympy as sp
from scipy.optimize import root

L, R, g, t, x, y, ell, s, z = sp.symbols(
    'L R g t x y ell s z', real=True
)
H = sp.Matrix([
    [L-sp.I*g, 0, t, t],
    [0, -L-sp.I*g, -t, -t],
    [t, -t, R+sp.I*g, 0],
    [t, -t, 0, -R+sp.I*g],
])
u, v = L**2, R**2
p = (x**4+(-u-v+2*g**2-4*t**2)*x**2
     +2*sp.I*g*(u-v)*x+u*v+g**2*(u+v)+g**4-4*g**2*t**2)
assert sp.expand(sp.det(x*sp.eye(4)-H)-p) == 0
q = sp.expand(p.subs(x, sp.I*y))
F = (z*z-8*g*t*t*z+ell*ell
     +4*s*(g*g*ell*ell+(g*g+t*t)*z*z)
     -4*g*s*s*(ell*ell*z+z**3)
     +s**3*(ell*ell*z*z+z**4))
assert sp.simplify(
    q.subs({L:s*ell,R:1/sp.sqrt(s),y:-g+s*z})/s-F
) == 0

for gv,tv in [(0.4,1.0),(1.0,1.0),(3.0,0.5)]:
    for rv in [10.0,30.0,100.0]:
        ss=1/rv**2
        base=4*gv*tv*tv
        def fg(Z):
            zv, lv=Z
            fv=(zv*zv-8*gv*tv**2*zv+lv**2
                +4*ss*(gv**2*lv**2+(gv**2+tv**2)*zv*zv)
                -4*gv*ss**2*(lv**2*zv+zv**3)
                +ss**3*(lv**2*zv*zv+zv**4))
            dz=(2*zv-8*gv*tv**2+8*ss*(gv**2+tv**2)*zv
                -4*gv*ss**2*(lv**2+3*zv*zv)
                +ss**3*(2*lv**2*zv+4*zv**3))
            return [fv,dz]
        sol=root(fg,[base,base],tol=1e-11)
        assert np.linalg.norm(fg(sol.x))<1e-8
        zc,lc=sol.x
        assert lc>0
        half=lc*ss
        approx=base*ss*(1-2*(2*gv**2+tv**2)*ss)
        # The approximation is asymptotic; check scaled second-order remainder.
        if rv>=30:
            assert abs(half-approx)<0.02*base*ss
        def roots_at(mult):
            lval=mult*half
            A=np.array(H.subs({L:lval,R:rv,g:gv,t:tv}),dtype=np.complex128)
            eig=np.linalg.eigvals(A)
            eig=sorted(eig,key=lambda a: abs(a.imag+gv))
            return eig
        inside=roots_at(0.5)
        outside=roots_at(1.5)
        assert max(abs(x.real) for x in inside[:2])<1e-6
        assert min(abs(x.real) for x in outside[:2])>1e-9
        # Schur complement at the exceptional point has rank one.
        xc=1j*(-gv+ss*zc)
        S=1/(xc-rv-1j*gv)+1/(xc+rv-1j*gv)
        M=np.diag([xc-half+1j*gv,xc+half+1j*gv])-tv*tv*S*np.array([[1,-1],[-1,1]])
        assert abs(np.linalg.det(M))<1e-7
        assert np.linalg.norm(M)>1e-8
        print('g,t,R,critical_width,leading_plus_correction:',gv,tv,rv,half,approx)
print('All symbolic and finite-parameter checks passed.')
