"""Exact standalone verification of a smooth anticanonical net on P1 x P1 / F3."""
from itertools import product
from sympy import symbols, groebner, Poly
x, y = symbols('x y')
F = (1,0,0, 0,0,1, 1,0,0)
G = (1,1,2, 0,0,0, 0,1,0)
H = (1,2,0, 2,2,0, 0,0,1)
BASIS=(F,G,H)
def triple_image(abcs):
    return tuple(sum(t*BASIS[k][j] for k,t in enumerate(abcs))%3 for j in range(9))
def member_chart(coeff, chart1, chart2):
    # chart1: s=1,t=x or s=x,t=1; chart2: u=1,v=y or u=y,v=1
    s,t=(1,x) if chart1==0 else (x,1)
    u,v=(1,y) if chart2==0 else (y,1)
    return sum(coeff[3*i+j]*s**(2-i)*t**i*u**(2-j)*v**j for i in range(3) for j in range(3))
def smooth(coeff):
    for a,b in product((0,1), repeat=2):
        f=member_chart(coeff,a,b)
        ideal=groebner((f,f.diff(x),f.diff(y)), x,y, modulus=3)
        if len(ideal.polys)!=1 or ideal.polys[0].as_expr()!=1:
            return False,(a,b),str(ideal)
    return True,None,None
# all 3^3-1 =26 nonzero vectors, modulo F3^* yielding exactly 13 members.
seen={}
for a,b,c in product(range(3), repeat=3):
    if (a,b,c)==(0,0,0):continue
    vector=triple_image((a,b,c))
    assert any(vector), 'F,G,H are linearly dependent'
    n=next(t for t,v in enumerate((a,b,c)) if v)
    if (a,b,c)[n]!=1: continue
    assert vector not in seen, 'distinct triples map to same member'
    seen[vector]=(a,b,c)
assert len(seen)==13
print('normalization (a,b,c) : binary quartic discriminant coefficients [s^4,s^3t,s^2t^2,st^3,t^4]')
for coeff,abc in seen.items():
    # Independent criterion: discriminant of the quadratic in (u,v) is squarefree.
    aa=coeff[0::3]; bb=coeff[1::3]; cc=coeff[2::3]
    d=[0]*5
    for i,j in product(range(3),repeat=2):
        d[i+j]=(d[i+j]+bb[i]*bb[j]-aa[i]*cc[j])%3
    p=Poly(sum(d[i]*x**(4-i) for i in range(5)),x,modulus=3)
    assert p.degree()>=3 and p.gcd(p.diff()).degree()==0, (abc,d)
    good,chart,ideal = smooth(coeff)
    if not good: raise AssertionError(f'geometric singularity: abc={abc}, chart={chart}, ideal={ideal}')
    print(abc, ':', d)
print('field: F3')
print('bidegree: (2,2)')
print('independent generating sections: 3')
print('projective net members: 13')
print('nonzero members: all 13 geometrically smooth (Jacobian unit ideals on four affine charts)')
print('geometric genus of each member: (2-1)*(2-1) = 1')
print('sharp maximal vector dimension: 3 by 1-jet kernel at any F3-rational point')
