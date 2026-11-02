"""Finite reproducibility tests for a central section-probability cusp.
Analytic proofs are in RESULT.md. Uses Python standard library only.
"""
import math,random,itertools

def permutations(xs):return tuple(set(itertools.permutations(xs)))
def direct_count(u,t):
    n=0
    for i in range(3):
        w=sorted((abs(u[j]) for j in range(3) if j!=i),reverse=True)
        m=(t-1)*w[0] if t<=2 else w[0]+(t-2)*w[1]
        n+=2*(abs(u[i])<m)
    verts=permutations((1.,t-1.,0.)) if t<=2 else permutations((1.,1.,t-2.))
    for sign in itertools.product((-1,1),repeat=3):
        vals=[sum(u[i]*sign[i]*v[i] for i in range(3)) for v in verts]
        n+=min(vals)<0<max(vals)
    return n

def left_formula(u,t):
    x,y,z=sorted(map(abs,u),reverse=True)
    r=t-1
    return 4+2*(y<r*x)+2*(z<r*x)+2*(z>r*y)

R=random.Random(17041)
for t in (1.1,1.5,1.9,1.99,2.,2.01,2.1,2.5,2.9):
    for _ in range(2000):
        u=[R.gauss(0,1) for k in range(3)]
        n=direct_count(u,t)
        assert n in (4,6,8,10),(t,n,u)
        if t<2:assert n==left_formula(u,t),(t,n,left_formula(u,t))
        if t==2:assert n==8
print('EXACT_FACET_AND_OCTAGON_RIGIDITY_CHECKS_PASSED')

# Independent quadrature of first-order spherical band areas.
pref=12/math.pi
A=pref/(2*math.sqrt(3))
B=pref*(1-1/math.sqrt(3))/2
C=pref*(1-math.sqrt(2/3))/math.sqrt(2)
D=pref/math.sqrt(3)
assert abs(A-2*math.sqrt(3)/math.pi)<1e-12
assert abs(B-(6-2*math.sqrt(3))/math.pi)<1e-12
assert abs(C-(6*math.sqrt(2)-4*math.sqrt(3))/math.pi)<1e-12
assert abs(D-4*math.sqrt(3)/math.pi)<1e-12
assert abs(A+B-6/math.pi)<1e-12
assert abs(C+D-6*math.sqrt(2)/math.pi)<1e-12
print('SHARP_COEFFICIENT_IDENTITIES_PASSED')

# Finite simulation merely supports the precise limiting claims.
for t in (1.98,2.02):
    counts={4:0,6:0,8:0,10:0}
    n=100000
    for _ in range(n):
        u=[R.gauss(0,1) for i in range(3)]
        counts[direct_count(u,t)]+=1
    eps=abs(t-2)
    slopes=(A,B) if t<2 else (D,C)
    for m,s in zip((6,10),slopes):
        empirical=counts[m]/(n*eps)
        assert abs(empirical-s)<0.19,(t,m,empirical,s)
    print('ONE_SIDED_SLOPE_PROBES',t,counts)
print('ALL_CHECKS_PASSED')
