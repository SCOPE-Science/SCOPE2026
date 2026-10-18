"""Independent full-coefficient search for the extremal proper tritangent bound.

Requires sympy. All computations are over GF(2), including the four-chart
geometric smoothness test via unit Groebner ideals.
"""
from collections import Counter
from itertools import product
from math import comb
import sympy as sp

B = [(i,j) for i in range(4) for j in range(4)]
roots = [(1,0),(0,1),(1,1)]
lines = [(1,0),(0,1),(1,1)]
matrices = [(a,b,c,d) for a,b,c,d in product(range(2),repeat=4) if a*d^b*c]
assert len(matrices) == 6

def mul(p,q):
    r = 0
    for i in range(7):
        for j in range(7-i):
            if (p>>i)&(q>>j)&1:
                r ^= 1<<(i+j)
    return r

def powlinear(a,b,n):
    r = 1
    for _ in range(n):
        r = mul(r,a+2*b)
    return r

substitution = []
for a,b,c,d in matrices:
    substitution.append([mul(powlinear(a,b,3-j),powlinear(c,d,j))<<i for i,j in B])

def squarefree_cubic(g):
    t = sp.Symbol('t')
    p = sp.Poly(sum(((g>>i)&1)*t**i for i in range(4)),t,modulus=2)
    return p.degree()>=2 and sp.gcd(p,p.diff()).degree()==0
sf = {g for g in range(16) if squarefree_cubic(g)}
assert len(sf)==6

def smooth_plane_good(f, row):
    sextic = 0
    for i,b in enumerate(row):
        if (f>>i)&1: sextic ^= b
    if sextic & 0b101010: return False
    cube = sum(((sextic>>(2*i))&1)<<i for i in range(4))
    return cube in sf

def cubic_restriction(f,point,first_fixed):
    value = 0
    for i,j in B:
        if not ((f>>(4*i+j))&1): continue
        if first_fixed:
            if point[0]**(3-i)*point[1]**i: value ^= 1<<j
        else:
            if point[0]**(3-j)*point[1]**j: value ^= 1<<i
    return value

def divide_cubic_by_line_times_square(cub,linear,point):
    for a,b in product(range(2),repeat=2):
        q = mul(linear[0]+2*linear[1],mul(a+2*b,a+2*b))
        if q==cub and (a*point[0]+b*point[1])%2:
            return True
    return False

def tangent_plane_good(f,l,m):
    # l(U,V)=0, m(S,T)=0; their rational roots are unique.
    u = (l[1],l[0]) if l!=(1,1) else (1,1)
    s = (m[1],m[0]) if m!=(1,1) else (1,1)
    return (divide_cubic_by_line_times_square(cubic_restriction(f,u,True),m,s)
            and divide_cubic_by_line_times_square(cubic_restriction(f,s,False),l,u))

def count_tritangents(f):
    a = sum(smooth_plane_good(f,row) for row in substitution)
    b = sum(tangent_plane_good(f,l,m) for l in lines for m in lines)
    return a,b

x,y=sp.symbols('x y')
charts = [[x**(i if e1 else 3-i)*y**(j if e2 else 3-j)
           for i,j in B] for e1,e2 in product(range(2),repeat=2)]
def geometric_smooth(f):
    for basis in charts:
        F = sp.Poly(sum(basis[i] for i in range(16) if (f>>i)&1),x,y,modulus=2)
        G = sp.groebner([F.as_expr(),F.diff(x).as_expr(),F.diff(y).as_expr()],
                       x,y,modulus=2)
        if len(G.polys)!=1 or not G.polys[0].is_one: return False
    return True

if __name__=='__main__':
    candidates = Counter(); actual=[]
    for f in range(1,1<<16):
        a,b=count_tritangents(f)
        if a+b>=3:
            candidates[a+b]+=1
            if geometric_smooth(f): actual.append((f,a,b))
    print('all_equations_with_at_least_3_proper_tritangents:', dict(sorted(candidates.items())))
    print('smooth_equations_with_at_least_3:',len(actual))
    print('smooth_extremal_distribution:',dict(sorted(Counter((a,b) for f,a,b in actual).items())))
    print('least_smooth_extremal_equation_mask:',min(f for f,a,b in actual))
    assert candidates=={3:592,4:150,5:30,6:1}
    assert len(actual)==18 and set((a,b) for f,a,b in actual)=={(1,2)}
    assert min(f for f,a,b in actual)==10723
    print('DIRECT_EXTREMAL_CHECK_PASS')
