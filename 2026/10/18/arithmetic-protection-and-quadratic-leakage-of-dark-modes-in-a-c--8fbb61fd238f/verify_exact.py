"""Small-size exact characteristic-polynomial checks, independent of the resolvent argument.
Requires SymPy. Run: python verify_exact.py.
"""
import sympy as sp


def check(m, s):
    z, eps = sp.symbols('z eps')
    size = 2*m+1
    H = sp.zeros(size)
    for j in range(size-1):
        H[j,j+1] = H[j+1,j] = 1
    H[m,m] = -sp.I  # gamma=2, with -i gamma/2
    H[s-1,s-1] = eps
    poly = (z*sp.eye(size)-H).det(method='berkowitz')
    for k in range(1,m+1):
        Ek = 2*sp.cos(sp.pi*k/(m+1))
        at0 = {z:Ek, eps:0}
        d1=sp.diff(poly,z).subs(at0)
        assert sp.simplify(d1) != 0
        a1=sp.simplify(-sp.diff(poly,eps).subs(at0)/d1)
        a2=sp.simplify(-(
           sp.Rational(1,2)*sp.diff(poly,z,2).subs(at0)*a1**2
           +sp.diff(poly,z,eps).subs(at0)*a1
           +sp.Rational(1,2)*sp.diff(poly,eps,2).subs(at0))/d1)
        theta=sp.pi*k/(m+1)
        predicted=sp.simplify(-sp.sin(s*theta)**4/(4*(m+1)*sp.sin(theta)**2))
        assert sp.simplify(sp.im(a2)-predicted)==0,(m,s,k,sp.im(a2),predicted)
        predicted_a1=sp.simplify(sp.sin(s*theta)**2/(m+1))
        assert sp.simplify(a1-predicted_a1)==0,(m,s,k,a1,predicted_a1)


if __name__=='__main__':
    for m,s in [(1,1),(2,1),(3,1),(3,2)]:
        check(m,s)
    print('EXACT_VERIFY_OK: characteristic-polynomial coefficients for 4 finite chains')
