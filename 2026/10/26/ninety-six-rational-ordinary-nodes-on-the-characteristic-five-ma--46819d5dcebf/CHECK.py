"""Independent exact symbolic and prime-field checks for a Maschke-octic fibre.

Requires Python 3 and SymPy.  Runs with: python CHECK.py
These finite computations corroborate, but do not replace, the geometric proof.
"""
from itertools import combinations, product
from sympy import symbols, Poly, prod, hessian, diff

x = symbols('x0:4')
F = sum(t**8 for t in x) + 14*sum(a**4*b**4 for a,b in combinations(x,2)) + 168*prod(a*a for a in x)
G = sum(t**8 for t in x) - sum(a**4*b**4 for a,b in combinations(x,2)) - 2*prod(a*a for a in x)
assert Poly(F-G,*x,modulus=5).is_zero
DF = [Poly(diff(F,t),*x,modulus=5) for t in x]
HH = hessian(F,x)

def fval(poly, q):
    return int(poly.eval(dict(zip(x,q))))%5

def points():
    for q in product(range(5),repeat=4):
        if not any(q): continue
        i = next(i for i,t in enumerate(q) if t)
        if q[i] != 1: continue
        yield q

def prescribed(q):
    nz = [a for a in q if a]
    if len(nz)==3:
        return len({pow(a,4,5) for a in nz}) == 1
    if len(nz)==4:
        a=pow(nz[0],4,5)
        return all(pow(t,4,5)==a for t in nz) and (prod(t*t for t in nz)+a*a)%5==0
    return False

all_pts=list(points())
sing = [q for q in all_pts if fval(Poly(F,*x,modulus=5),q)==0 and all(fval(g,q)==0 for g in DF)]
pred = [q for q in all_pts if prescribed(q)]
zeros= [q for q in all_pts if fval(Poly(F,*x,modulus=5),q)==0]
assert len(all_pts)==156
assert len(sing)==len(pred)==len(zeros)==96 and set(sing)==set(pred)==set(zeros)
assert sum(0 in q for q in sing)==64
assert sum(0 not in q for q in sing)==32

def nodal_test(q):
    i=next(j for j in range(4) if q[j])
    js=[j for j in range(4) if j!=i]
    M=HH.extract(js,js).subs(dict(zip(x,q)))
    return [[int(M[j,k])%5 for k in range(3)] for j in range(3)],int(M.det())%5

q3=(0,1,1,1);q4=(1,1,1,2)
M3,d3=nodal_test(q3)
M4,d4=nodal_test(q4)
assert M3==[[1,0,0],[0,2,4],[0,4,2]] and d3==3
assert M4==[[4,2,1],[2,4,1],[1,1,1]] and d4==3
assert set(q for q in (q3,q4)) <= set(sing)
# The form is invariant under signed-fourth-root scalings with product
# of their squares equal to one, and under coordinate permutations.
mu4=(1,2,3,4)
assert all(pow(t,4,5)==1 for t in mu4)
for z in product(mu4,repeat=4):
    if prod(t*t for t in z)%5 != 1: continue
    assert Poly(F-F.subs(dict(zip(x,[z[i]*x[i] for i in range(4)])),simultaneous=True),*x,modulus=5).is_zero
print('CHECK_OK total_P3_F5=156 S_F5=96 singular_F5=96; support3=64 support4=32')
print('HESSIAN_DETERMINANTS mod5:',d3,d4)
