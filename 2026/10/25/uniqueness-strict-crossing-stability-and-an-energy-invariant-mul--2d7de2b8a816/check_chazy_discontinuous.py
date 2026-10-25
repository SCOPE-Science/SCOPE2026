"""Exact symbolic consistency checks for the crossing generalized Chazy system.

Run: python check_chazy_discontinuous.py
Requires: sympy >= 1.10.
Finite symbolic tests check algebraic identities, not global cycle existence.
"""
import sympy as sp

x, y, z, a = sp.symbols('x y z a', real=True)
e1 = sp.Matrix([1, 0, 0]); e3 = sp.Matrix([0, 0, 1]); I = sp.eye(3)
count = 0
for sign in (-1, 1):
    # In sector sign*x>0, |x|=sign*x.
    H = x*z - y**2/2 + sign*x**2*y
    F = sp.Matrix([y, z, -sign*x*z-2*sign*y**2])
    assert sp.simplify(sp.Matrix([sp.diff(H,w) for w in (x,y,z)]).dot(F)) == 0
    count += 1
    assert sp.simplify(sum(sp.diff(F[i], (x,y,z)[i]) for i in range(3)) + sign*x) == 0
    count += 1
    Da = sp.diag(a,a*a,a*a*a)
    assert sp.expand(H.subs({x:a*x,y:a*a*y,z:a*a*a*z})-a**4*H) == 0
    count += 1
    assert all(sp.expand(F[i].subs({x:a*x,y:a*a*y,z:a*a*a*z}) - a**(i+2)*F[i])==0 for i in range(3))
    count += 1
    assert H.subs(x,0) == -y**2/2
    count += 1
# Crossing from x<0 to x>0 requires y>0; reverse requires y<0.
Fplus = sp.Matrix([y,z,-2*y**2]); Fminus=sp.Matrix([y,z,2*y**2])
for Fbefore,Fafter in ((Fminus,Fplus),(Fplus,Fminus)):
    S = I + (Fafter-Fbefore)*e1.T / y
    assert sp.simplify(S.det()-1)==0
    count += 1
    assert sp.simplify(S*Fbefore-Fafter)==sp.zeros(3,1)
    count += 1
    # H_x=z,H_y=-y,H_z=0 at the crossing; both gradients preserved.
    g=sp.Matrix([z,-y,0])
    assert sp.simplify(g.T*S-g.T)==sp.zeros(1,3)
    count += 1
    assert sp.simplify((Fafter-Fbefore)[0])==0
    count += 1
print(f'PASS: {count} exact algebraic identity checks')
