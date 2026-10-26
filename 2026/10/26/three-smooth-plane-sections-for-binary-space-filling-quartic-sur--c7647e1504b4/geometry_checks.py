"""Exact GF(2) projective Jacobian-ideal and plane-section checks.
Run: python geometry_checks.py. Requires SymPy; no numerical approximations.
"""
import itertools
import sympy as sp
x=sp.symbols('x0:4')
a,b,c,d=x
F=(a**3*(c+d)+a**2*(b**2+b*c+d**2)
   +a*(b**3+b**2*c+c**3+c**2*d+c*d**2)
   +b**3*(c+d)+b*(c**3+c**2*d+c*d**2+d**3)+c**3*d+c*d**3)

def projectively_smooth(form,variables):
    deriv=[sp.diff(form,z) for z in variables]
    for k in range(len(variables)):
        chart=[form.subs(variables[k],1)]+[D.subs(variables[k],1) for D in deriv]
        rest=[z for j,z in enumerate(variables) if j!=k]
        gb=sp.groebner(chart,*rest,modulus=2,order='lex')
        if len(gb.polys)!=1 or gb.polys[0].as_expr()!=1:
            return False
    return True

def form_monomials(n):
    return [m for m in itertools.product(range(5),repeat=n) if sum(m)==4]
def point_eval(m,p):
    return int(all(e==0 or p>>j&1 for j,e in enumerate(m)))
def nullbasis(columns):
    piv={};out=[]
    for j,a in enumerate(columns):
        c=1<<j
        while a:
            k=a.bit_length()-1
            if k not in piv:piv[k]=(a,c);break
            a^=piv[k][0];c^=piv[k][1]
        else:out.append(c)
    return out,len(piv)

def check_plane_filling_lemma():
    y=sp.symbols('y0:3');mons=form_monomials(3);points=range(1,8)
    columns=[sum(point_eval(m,p)<<k for k,p in enumerate(points)) for m in mons]
    basis,rank=nullbasis(columns)
    assert rank==7 and len(basis)==8
    nonsingular_rational=0; nonsingular_geometric=0
    for mask in range(1<<8):
        coeff=0
        for j,v in enumerate(basis):
            if mask>>j&1:coeff^=v
        G=sum((sp.prod(y[k]**m[k] for k in range(3)) for j,m in enumerate(mons) if coeff>>j&1),sp.S.Zero)
        D=[sp.diff(G,z) for z in y]
        rat_smooth=True
        for p in points:
            vals={y[k]:(p>>k)&1 for k in range(3)}
            if not any(int(h.subs(vals))%2 for h in D):
                rat_smooth=False;break
        if rat_smooth:
            nonsingular_rational+=1
            if projectively_smooth(G,y):nonsingular_geometric+=1
    assert nonsingular_rational==24 and nonsingular_geometric==24
    return nonsingular_rational,nonsingular_geometric

assert projectively_smooth(F,x)
print('example_surface_geometrically_smooth',True)
assert all(int(F.subs({x[k]:(p>>k)&1 for k in range(4)}))%2==0 for p in range(1,16))
print('example_contains_all_15_rational_points',True)
D=[sp.diff(F,z) for z in x]
image=[]
for p in range(1,16):
    vals={x[k]:(p>>k)&1 for k in range(4)}
    h=sum((int(e.subs(vals))%2)<<k for k,e in enumerate(D))
    assert h!=0
    image.append(h)
missing=sorted(set(range(1,16))-set(image))
assert len(set(image))==12 and missing==[2,4,10]
print('example_rational_gauss_images',image)
print('example_missing_tangent_plane_masks',missing)
transverse=[]
for h in range(1,16):
    k=(h&-h).bit_length()-1
    ys=[x[j] for j in range(4) if j!=k]
    restriction=F.subs({x[k]:sum((x[j] for j in range(4) if j!=k and (h>>j)&1),sp.S.Zero)})
    if projectively_smooth(restriction,ys):transverse.append(h)
assert transverse==missing
print('exact_smooth_plane_section_masks',transverse)
a,b=check_plane_filling_lemma()
print('plane_filling_quartics_rationally_smooth',a)
print('plane_filling_quartics_geometrically_smooth',b)
