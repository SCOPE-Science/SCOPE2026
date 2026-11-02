"""Independent exact checks of quadratic Jacobian syzygies and sampled linear syzygy ranks.
Finite cases corroborate the uniform argument in RESULT.md.
Requires sympy.
"""
import sympy as S
x,y,z=S.symbols('x y z')
coords=[x,y,z]
forms={'coordinate_x':x,'coordinate_y':y,'coordinate_z':z,'through_one':y+z,'generic':x+2*y+3*z,'both_x_y':x+y}
for k in range(2,8):
    f=x**k*y**k+z**(2*k)
    for label,L in forms.items():
        F=S.expand(L*f)
        a,b,c=[S.expand(S.diff(L,q)) for q in coords]
        D=S.expand(a*x-b*y)
        degree=2*k+1
        syz=[S.expand(degree*L*q*sign - D*q) for q,sign in ((x,1),(y,-1),(z,0))]
        assert S.expand(sum(q*S.diff(F,v) for q,v in zip(syz,coords)))==0,(k,label)
        # Exact linear-syzygy nullity via coefficient matrix.
        vec=[S.expand(coord*S.diff(F,variable)) for variable in coords for coord in coords]
        monomials=list(S.polys.monomials.itermonomials(coords,degree))
        monomials=[m for m in monomials if S.total_degree(m)==degree]
        matrix=S.Matrix([[S.Poly(p,x,y,z).coeff_monomial(m) for p in vec] for m in monomials])
        nullity=9-matrix.rank()
        assert (nullity>0)==(label.startswith('coordinate')), (k,label,nullity)
        assert nullity==1 if label.startswith('coordinate') else nullity==0
    print(f'k={k} six syzygies and linear ranks verified')
print('SYZYGY_AND_LINEAR_RANK_CHECKS_OK')
