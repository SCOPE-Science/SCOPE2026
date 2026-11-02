"""Exact sparse-quadratic support and reaction witness checks.
Run: python3 verify.py
Requires: sympy.
"""
from itertools import combinations
from sympy import symbols, Poly, Matrix, factor, expand, diff, solve, simplify

x,y,u,v=symbols('x y u v')
a,b,c=symbols('a b c')
monoms=[1,x,y,x*x,x*y,y*y]
labels=['1','x','y','x^2','xy','y^2']
q=a*(x-1)**2+b*(x-1)*(y-1)+c*(y-1)**2
coef=[Poly(expand(q),x,y).coeff_monomial(m) for m in monoms]
A=Matrix([[1,1,1,1,1,1],[0,1,0,2,1,0],[0,0,1,0,1,2]])
assert all(A[:,list(S)].rank()==3 for S in combinations(range(6),4))
print('FOUR_SUPPORT_AFFINE_RANK_PASS 15')

count=0
for absent in combinations(range(6),2):
    equations=[coef[j] for j in absent]
    null=Matrix([[eq.diff(t) for t in (a,b,c)] for eq in equations]).nullspace()
    assert len(null)==1, (absent,null)
    aa,bb,cc=null[0]
    form=factor((aa*u*u+bb*u*v+cc*v*v))
    # The unique vanishing polynomial factors into real homogeneous linear factors.
    poly=Poly(form,u,v)
    disc=simplify(bb**2-4*aa*cc)
    assert disc>=0, (absent, form, disc)
    polyxy=expand((aa*(x-1)**2+bb*(x-1)*(y-1)+cc*(y-1)**2))
    assert all(Poly(polyxy,x,y).coeff_monomial(monoms[j])==0 for j in absent)
    count+=1
    print('MISSING',labels[absent[0]],labels[absent[1]],'QUADRATIC',str(form),'DISCRIMINANT',disc)
print('ALL_15_SPARSE_CASES_REAL_LINEAR_FACTOR_PASS',count)

# An exact five-reaction model of Yeung--Erban (2026), evaluated directly.
F=Matrix([x*x-2*x*y+y*y, 1-2*y+y*y])
assert simplify(F[0]-(x-y)**2)==0
assert simplify(F[1]-(y-1)**2)==0
assert F.subs({x:1,y:1})==Matrix([0,0])
assert F.jacobian((x,y)).subs({x:1,y:1})==Matrix([[0,0],[0,0]])
assert set(Poly(F[0],x,y).monoms()+Poly(F[1],x,y).monoms()) == {(2,0),(1,1),(0,2),(0,1),(0,0)}
assert solve(list(F),(x,y))==[(1,1)]
print('FIVE_REACTION_ISOLATED_ZERO_JACOBIAN_SHARPNESS_PASS')

# Products and reactants encoded by their molecularity pairs (X,Y).
channels=[((0,0),(0,1),1),((0,1),(0,0),2),((2,0),(3,0),1),((1,1),(0,1),2),((0,2),(1,3),1)]
F_reaction=Matrix([0,0])
for source,target,rate in channels:
    mon=x**source[0]*y**source[1]
    F_reaction+=Matrix([rate*(target[i]-source[i])*mon for i in range(2)])
assert simplify(F_reaction-F)==Matrix([0,0])
print('MASS_ACTION_FIVE_REACTION_IDENTITIES_PASS')
