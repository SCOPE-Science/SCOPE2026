"""Exact certificate for Barth's sextic at the ramified prime 5.
Run: python verify.py (requires sympy). No external data files.
The projective chart order is x,y,z,w, with first nonzero coordinate 1.
"""
import itertools
from collections import Counter
import sympy as sp

p = 5
vars4 = sp.symbols('x y z w')
x,y,z,w = vars4
Q = x*x+y*y+z*z-w*w
F = -((x*x+y*y)*(y*y+z*z)*(z*z+x*x)) - 3*Q*Q*w*w
FF = sp.Poly(F, *vars4, modulus=p)
partials = [sp.Poly(sp.diff(F,t),*vars4,modulus=p) for t in vars4]
H = sp.hessian(F,vars4)

def evalpoly(poly, point):
    return int(poly.eval(dict(zip(vars4,point)))) % p

def projective_points(q_values, zero, one):
    for i in range(4):
        for tail in itertools.product(q_values, repeat=3-i):
            yield i, (zero,)*i+(one,)+tail

# Scheme-theoretic exact completeness: the Jacobian ideal on every chart
# contains all three field equations T^5-T. Hence all geometric singular
# points are F5-rational. This is an exact Groebner membership certificate.
for i in range(4):
    var = vars4[i]
    local_vars = [t for j,t in enumerate(vars4) if j != i]
    local_f = sp.Poly(F,var).eval(1)
    ideal = [local_f] + [sp.diff(local_f,t) for t in local_vars]
    basis = sp.groebner(ideal, *local_vars, order='grevlex', modulus=5)
    assert basis.is_zero_dimensional
    assert all(sp.Poly(basis.reduce(t**5-t)[1],*local_vars,modulus=5).is_zero
               for t in local_vars)
    print('JACOBIAN_FIELD_EQUATIONS_CERTIFIED_CHART',i)

nodes=[]
chart_nodes=Counter()
hessian=Counter()
for i,P in projective_points(range(5), 0, 1):
    if evalpoly(FF,P)==0 and all(evalpoly(d,P)==0 for d in partials):
        nodes.append(P);chart_nodes[i]+=1
        im=[j for j in range(4) if j!=i]
        h=sp.Matrix([[int(H[a,b].subs(dict(zip(vars4,P))))%5 for b in im] for a in im])
        d=int(h.det())%5
        assert d!=0, ('not an ordinary double point',P)
        hessian[d]+=1
assert len(nodes)==65
assert [chart_nodes[i] for i in range(4)]==[55,7,3,0]
assert hessian==Counter({4:38,1:27})
print('GEOMETRIC_SINGULAR_SCHEME_REDUCED_SPLIT_65_ORDINARY_NODES_OK')
print('NODE_CHART_COUNTS', [chart_nodes[i] for i in range(4)])
print('HESSIAN_DETERMINANTS',dict(hessian))

# GF(25) = GF(5)[theta] / (theta**2-2). Encode a+b*theta as a+5*b.
E=list(range(25));ZERO=0;ONE=1
A=[[0]*25 for _ in E]
M=[[0]*25 for _ in E]
for u in E:
    a,b=u%5,u//5
    for v in E:
        c,d=v%5,v//5
        A[u][v]=(a+c)%5+5*((b+d)%5)
        M[u][v]=(a*c+2*b*d)%5+5*((a*d+b*c)%5)
N=[(-u%5)+5*(-(u//5)%5) for u in E]
S=lambda u,v:A[u][v]
R=lambda u,v:S(u,N[v])
P=lambda u,v:M[u][v]
Sq=[P(u,u) for u in E]

def F25(v):
    a,b,c,d=[Sq[u] for u in v]
    prod=P(P(S(a,b),S(b,c)),S(c,a))
    t=R(S(S(a,b),c),d)
    return R(N[prod], P(3,P(P(t,t),d)))

def Fsquare(a,b,c,d):
    prod=P(P(S(a,b),S(b,c)),S(c,a))
    t=R(S(S(a,b),c),d)
    return R(N[prod],P(3,P(P(t,t),d)))

cnt=[]
for i in range(4):
    k=0
    for tail in itertools.product(E,repeat=3-i):
        if F25((ZERO,)*i+(ONE,)+tail)==ZERO:
            k+=1
    cnt.append(k)
assert cnt==[1635,13,3,0] and sum(cnt)==1651
print('F25_POINTS_BY_PROJECTIVE_CHART_EXHAUSTIVE',cnt,'SUM',sum(cnt))

# Independent square-value weighted enumeration gives same counts.
fibers=Counter(Sq)
assert len(fibers)==13 and sorted(fibers.values())==[1]+[2]*12
squares=sorted(fibers)
weighted=[]
for i in range(4):
    k=0
    for tail in itertools.product(squares,repeat=3-i):
        point=(ZERO,)*i+(ONE,)+tail
        if Fsquare(*point)==ZERO:
            weight=1
            for sq in tail:weight*=fibers[sq]
            k+=weight
    weighted.append(k)
assert weighted==cnt
print('F25_WEIGHTED_SQUARE_FIBER_CROSSCHECK_OK',weighted)

count5=[]
for i in range(4):
    k=0
    for tail in itertools.product(range(5),repeat=3-i):
        point=(0,)*i+(1,)+tail
        if evalpoly(FF,point)==0:k+=1
    count5.append(k)
assert count5==[75,13,3,0] and sum(count5)==91
print('F5_POINTS_BY_PROJECTIVE_CHART_EXHAUSTIVE',count5,'SUM',sum(count5))

# Minimal resolution replaces each rational node by P1: +q points.
Y5=91+65*5
Y25=1651+65*25
assert (Y5,Y25)==(416,3276)
b2=106
assert Y25==1+25*25+b2*25
trace5=Y5-1-25
assert trace5==390
plus=(b2+trace5//5)//2;minus=b2-plus
assert (plus,minus)==(92,14)
assert (plus-65,minus)==(27,14)
for m in (1,2):
    q=5**m
    assert 1+q*q+(27+14*(-1)**m)*q==[91,1651][m-1]
print('F25_WEIL_BOUND_SATURATED_B2_106_FROBENIUS_PLUS92_MINUS14_OK')
print('ZETA_SINGULAR_SURFACE_PLUS27_MINUS14_OK')
print('VERIFY_OK')
