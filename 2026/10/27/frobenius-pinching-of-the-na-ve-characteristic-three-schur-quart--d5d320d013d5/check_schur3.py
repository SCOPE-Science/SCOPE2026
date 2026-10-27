"""Exact characteristic-three checks for the Schur quartic special fibre.

Uses SymPy for polynomial identities and pure-Python arithmetic for F_3/F_9.
This finite calculation is supplementary; the global statements need the proof.
"""
from itertools import product
import sympy as sp
x,y,z,w,a,b,s,t,L,M = sp.symbols('x y z w a b s t L M')


def zero_mod3(poly, generators):
    p=sp.Poly(sp.expand(poly), *generators)
    return all(int(c) % 3 == 0 for c in p.coeffs())

F=x**4-x*y**3-z**4+z*w**3
assert zero_mod3(F-(x*(x-y)**3-z*(z-w)**3), (x,y,z,w))
assert zero_mod3(sp.diff(F,x)-(x-y)**3,(x,y,z,w))
assert zero_mod3(sp.diff(F,y),(x,y,z,w))
assert zero_mod3(sp.diff(F,z)+(z-w)**3,(x,y,z,w))
assert zero_mod3(sp.diff(F,w),(x,y,z,w))
G=x*a**3-z*b**3
assert zero_mod3(G.subs({x:L*t**3,z:L*s**3,a:M*s,b:M*t}),(s,t,L,M))

# F_9=F_3[u]/(u^2+1), integers encode c+d*u.
def mul9(i,j):
    c,d=i%3,i//3
    e,f=j%3,j//3
    return ((c*e-d*f)%3)+3*((c*f+d*e)%3)

def add9(i,j):
    return (i%3+j%3)%3+3*((i//3+j//3)%3)

def neg9(i):
    return (-i%3)+3*(-(i//3)%3)

def pow9(i,n):
    out=1
    while n:
        if n&1:out=mul9(out,i)
        i=mul9(i,i)
        n//=2
    return out

def P3(q):
    mul=(lambda i,j: i*j%q) if q==3 else mul9
    power=(lambda i,n:pow(i,n,q)) if q==3 else pow9
    seen=set()
    for p in product(range(q),repeat=4):
        if not any(p):continue
        lead=next(v for v in p if v)
        inv=power(lead,q-2)
        norm=tuple(mul(v,inv) for v in p)
        seen.add(norm)
    return seen

def on_surface(point,q):
    x,y,z,w=point
    if q==3:
        return (x**4-x*y**3-z**4+z*w**3)%3==0
    neg=neg9
    A=add9(pow9(x,4),neg(mul9(x,pow9(y,3))))
    B=add9(neg(pow9(z,4)),mul9(z,pow9(w,3)))
    return add9(A,B)==0

for q in (3,9):
    pts=P3(q)
    on={p for p in pts if on_surface(p,q)}
    assert len(pts)==q**3+q**2+q+1
    assert len(on)==(q+1)**2,(q,len(on))
    if q==3:
        line={p for p in on if (p[0]-p[1])%3==0 and (p[2]-p[3])%3==0}
    else:
        line={p for p in on if add9(p[0],neg9(p[1]))==0 and add9(p[2],neg9(p[3]))==0}
    assert len(line)==q+1
    print(f'F_{q}: projective_points={len(pts)}, surface={(q+1)**2}, singular_line={len(line)}')

print('CHECK_OK: polynomial/Jacobian/parametrization identities and F3/F9 counts')
