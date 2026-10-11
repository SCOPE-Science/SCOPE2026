"""Exact rational zonotope determinant and directional-phase checks."""
from fractions import Fraction as F
from itertools import combinations, permutations, product

PERMS = list(permutations(range(4)))
SIGNS = [(-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) for p in PERMS]

def det4(cols):
    return sum(sign * cols[0][p[0]] * cols[1][p[1]] * cols[2][p[2]] * cols[3][p[3]]
               for p, sign in zip(PERMS, SIGNS))

def volume(cols):
    return sum(abs(det4(t)) for t in combinations(cols, 4))

e1=(F(1),F(0),F(0),F(0)); e2=(F(0),F(1),F(0),F(0)); e3=(F(0),F(0),F(1),F(0)); e4=(F(0),F(0),F(0),F(1))
sub=lambda x,y:tuple(a-b for a,b in zip(x,y))
G=[e1,e2,e3,sub(e2,e4),sub(e3,e4)]
w=sub(e1,e4); z=sub(e2,e3)

def volumes(a,b):
    h=(F(1),-a,-b,F(0))
    return tuple(volume(G + [h] + extra) for extra in ([],[w],[z],[w,z]))

def asserted(a,b):
    q=a+b; X=abs(1-a)+abs(1-b); Z=abs(1-q)
    return (8+3*q,17+6*q+X+Z,16+5*q,35+9*q+X+3*Z)

def defect(a,b):
    q=a+b; X=abs(1-a)+abs(1-b); Z=abs(1-q)
    return 8-4*q-3*q*q-(8+2*q)*X+(8+4*q)*Z

def chamber_defect(a,b):
    q=a+b
    if a<=1 and b<=1 and q<=1: return -q*(5*q+4)
    if a<=1 and b<=1 and q>=1: return 3*q*q+4*q-16
    if a>=1 and b>=1: return 16-4*q-q*q
    return q*q-(8+2*q)*abs(a-b)

assert volumes(F(1),F(1)) == (14,30,26,56)
assert volumes(F(0),F(0)) == (8,20,16,40)
grid=[F(0),F(1,7),F(1,3),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(2),F(5,2),F(3),F(5)]
for a,b in product(grid, repeat=2):
    actual=volumes(a,b)
    expected=asserted(a,b)
    assert actual==expected,(a,b,actual,expected)
    d=actual[0]*actual[3]-actual[1]*actual[2]
    assert d==defect(a,b)==chamber_defect(a,b),(a,b,d,defect(a,b),chamber_defect(a,b))
print(f'VERIFY_OK {len(grid)**2} exact rational full determinant cases, including all chamber boundaries')
