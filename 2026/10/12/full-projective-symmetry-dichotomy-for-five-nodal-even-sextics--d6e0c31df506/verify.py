"""Exact symbolic checks for five-nodal even plane sextics (characteristic zero examples)."""
import sympy as S
X,Y,Z,s,t=S.symbols('X Y Z s t')
I=S.I

def poly(e):
    f=s**3-t**3+4*s*t+s-t+e*s*(s+t)**2
    F=S.expand(X**6*f.subs({s:Y**2/X**2,t:Z**2/X**2}))
    return S.expand(f),S.expand(F)

for e, expected_hessian in [(0,20),(1,28)]:
    f,F=poly(e)
    assert S.groebner([f,S.diff(f,s),S.diff(f,t)],s,t,order='lex').polys == [S.Poly(s-1,s,t),S.Poly(t+1,s,t)]
    assert S.expand(f.subs({s:1,t:-1}))==0
    H=S.hessian(f,(s,t)).subs({s:1,t:-1})
    assert S.expand(H.det())==expected_hessian, (e,H)
    Q=S.Poly(F.subs(X,1),Y,Z)
    assert F.subs({Y:0,Z:0})==0
    assert S.expand(F.subs({Y:Z})) != 0
    assert S.expand(F.subs({Y:-Z})) != 0
    # All axis points other than the central node are smooth.
    gY=S.factor(F.subs(Y,0));gZ=S.factor(F.subs(Z,0))
    assert gY == -Z**2*(X**4+Z**4)
    assert S.expand(gZ - Y**2*(X**4+(1+e)*Y**4))==0
    # Infinity is smooth: the leading binary sextic is squarefree.
    inf=S.Poly(F.subs({X:0,Y:1}),Z)
    assert S.gcd(inf,inf.diff()).degree()==0
    assert S.expand(F.subs({X:0,Y:1,Z:0}))!=0
    # Klein-four invariance and common five-node configuration.
    for h in (F.subs(Y,-Y),F.subs(Z,-Z)):
        assert S.expand(h-F)==0
    for a in [1,-1]:
        for b in [I,-I]:
            assert S.expand(F.subs({X:1,Y:a,Z:b}))==0
            assert S.expand(S.diff(F,Y).subs({X:1,Y:a,Z:b}))==0
            assert S.expand(S.diff(F,Z).subs({X:1,Y:a,Z:b}))==0
    swapped=S.expand(F.subs({Y:I*Z,Z:-I*Y}, simultaneous=True))
    assert (S.expand(swapped-F)==0)==(e==0)
    print(f'eps={e}: Groebner critical ideal (s-1,t+1); Hessian det {expected_hessian}; no infinity singularities; D8 symmetry {e==0}')

# Coefficient test in universal two-variable form. Here coefficients at s,t are opposite.
a,b,c,d,e,f,g=S.symbols('a b c d e f g')
Q=a*s**3+b*s**2*t+c*s**2+d*s*t**2+e*s*t+f*s+g*t**3+c*t**2-f*t
R=S.expand(Q.subs({s:-t,t:-s}, simultaneous=True)-Q)
assert S.expand(R.subs({g:-a,d:-b}))==0
assert S.Poly(R,s,t).coeff_monomial(s**3)==-g-a
assert S.Poly(R,s,t).coeff_monomial(s**2*t)==-d-b
print('VERIFY_OK: general coefficient criterion and both exact example checks')
