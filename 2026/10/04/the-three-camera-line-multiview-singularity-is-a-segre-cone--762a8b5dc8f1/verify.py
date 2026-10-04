from sympy import symbols, Matrix, expand, simplify
from math import comb

a,b,d,e,g,h = symbols('a b d e g h')
M = Matrix([[0,d,g],[a,0,h],[b,e,0],[1,1,1]])
# maximal minors, deleting rows 0,1,2,3
mins=[]
for r in range(4):
    rows=[i for i in range(4) if i!=r]
    mins.append(expand(M.extract(rows,[0,1,2]).det()))
F4,F3,F2,F1 = mins
assert expand(F1-(a*e*g+b*d*h)) == 0
assert expand(F2-(-a*d+a*g+d*h)) == 0
assert expand(F3-(-b*d+b*g-e*g)) == 0
assert expand(F4-(a*e+b*h-e*h)) == 0

N=Matrix([[-g,d-g],[a-h,-h],[b,e]])
ms=[]
for rs in [(0,1),(0,2),(1,2)]:
    ms.append(expand(N.extract(list(rs),[0,1]).det()))
assert expand(ms[0]-F2)==0
assert expand(ms[1]-F3)==0
assert expand(ms[2]-F4)==0
assert expand(h*F3-g*F4+F1)==0

# Invertibility of the six-coordinate linear change.
n11,n12,n21,n22,n31,n32 = symbols('n11 n12 n21 n22 n31 n32')
subs_inv={g:-n11,d:n12-n11,h:-n22,a:n21-n22,b:n31,e:n32}
entries=[-g,d-g,a-h,-h,b,e]
expected=[n11,n12,n21,n22,n31,n32]
for x,y in zip(entries,expected):
    assert expand(x.subs(subs_inv)-y)==0

# Hilbert function of the Segre coordinate ring and rational-series coefficients.
# (1+2t)/(1-t)^4 has coefficient C(n+3,3)+2*C(n+2,3).
for n in range(12):
    lhs=comb(n+2,2)*(n+1)
    rhs=comb(n+3,3)+(2*comb(n+2,3) if n>=1 else 0)
    assert lhs==rhs

print('VERIFY_OK')
