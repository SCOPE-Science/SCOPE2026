"""Exact algebraic and finite-graph checks for weighted-forest connectivity on cacti.
Requires only Python 3 standard library. This finite program checks identities;
the all-graph conclusion follows from the separate analytic block argument.
"""
from fractions import Fraction as F
from itertools import product, combinations

CHECKS = 0

def check(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)

def beta(i, t):
    return ((1 - t)**2, 2*t*(1-t), t*t)[i]

def cyclic(k):
    return {tuple(k[(i+j)%4] for i in range(4)) for j in range(4)}

def dihedral(k):
    return cyclic(k) | cyclic(k[::-1])

def bprod(k, v):
    out = F(1)
    for i, t in zip(k, v):
        out *= beta(i,t)
    return out

def cross_rhs(v):
    sets = ((F(1,8), cyclic((0,1,1,1))),
            (F(1,4), dihedral((0,1,1,2))),
            (F(1,2), cyclic((0,2,1,2))),
            (F(1,4), {(1,1,1,1)}),
            (F(1,8), cyclic((1,1,1,2))))
    return sum((coef*sum((bprod(k,v) for k in orbit), F(0))
                for coef,orbit in sets), F(0))

def shared_LHS(v):
    x,y,z=v;r=x*y*z
    n1=x+y*z-2*r
    n2=z+x*y-2*r
    n12=x*y+x*z+y*z-3*r
    return (1-r)*n12-n1*n2

def noncross_LHS(v):
    a,b,c,d=v;r=a*b*c*d
    n1=a+b*c*d-2*r
    n2=c+a*b*d-2*r
    n12=a*c+a*b*d+b*c*d-3*r
    return (1-r)*n12-n1*n2

def cross_LHS(v):
    a,b,c,d=v;r=a*b*c*d
    n1=a*b+c*d-2*r
    n2=b*c+a*d-2*r
    n12=a*b*c+a*b*d+a*c*d+b*c*d-4*r
    return (1-r)*n12-n1*n2

# Every polynomial in these identities has individual degree at most two.
# A polynomial of individual degree <=2 is determined by 3^d grid values.
grid=(F(0),F(1,2),F(1))
for v in product(grid,repeat=3):
    x,y,z=v
    rhs=y*(1-x)*(1-z)*(x*(1-z)+z*(1-x)+x*z*(1-y))
    check(shared_LHS(v)==rhs,('three-gap identity',v))
for v in product(grid,repeat=4):
    a,b,c,d=v
    rhs=b*d*(1-a)*(1-c)*(a*(1-c)+c*(1-a)+a*c*(1-b*d))
    check(noncross_LHS(v)==rhs,('noncrossing identity',v))
    check(cross_LHS(v)==cross_rhs(v),('crossing Bernstein identity',v))
    check(cross_rhs(v)>=0,('Bernstein positivity',v))

# Independent enumeration: forest probabilities with integer fugacities.
def finite_graph_check(n,edges,lam):
    global CHECKS
    pairs=list(combinations(range(n),2));Z=0
    m=len(edges);single=[0]*len(pairs);joint=[[0]*len(pairs) for _ in pairs]
    count_forests=0
    for mask in range(1<<m):
        par=list(range(n))
        def root(i):
            while par[i]!=i:
                i=par[i]
            return i
        weight=1;valid=True
        for i,(u,v) in enumerate(edges):
            if mask>>i&1:
                ru,rv=root(u),root(v)
                if ru==rv:
                    valid=False;break
                par[ru]=rv
                weight*=lam[i]
        if not valid:continue
        count_forests+=1;Z+=weight
        keys=[int(root(u)==root(v)) for u,v in pairs]
        for i,ki in enumerate(keys):
            if not ki:continue
            single[i]+=weight
            for j,kj in enumerate(keys):
                if kj:joint[i][j]+=weight
    check(Z>0 and count_forests>0,('nonempty partition',edges))
    for i in range(len(pairs)):
        for j in range(len(pairs)):
            check(Z*joint[i][j]>=single[i]*single[j],
                  ('negative covariance',edges,lam,pairs[i],pairs[j]))
    return count_forests

for n in range(3,8):
    edges=[(i,(i+1)%n) for i in range(n)]
    finite_graph_check(n,edges,[1+(3*i+1)%5 for i in range(n)])
# A multi-cycle cactus with three cycles and a bridge.
finite_graph_check(8,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,2),
                      (4,5),(5,6),(6,7),(7,5)],
                   [2,3,5,7,11,13,17,19,23,29])
# A cactus with two cycles sharing a cut vertex.
finite_graph_check(5,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,2)],
                   [1,2,4,3,5,7])
print(f'PASS: {CHECKS} exact rational checks')
