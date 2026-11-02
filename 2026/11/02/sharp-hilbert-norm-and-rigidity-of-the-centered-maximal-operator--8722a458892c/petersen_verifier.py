"""Standalone exact certificate for the centered graph-ball maximal L2 norm on KG(5,2).
Run: python3 petersen_verifier.py. Only Python standard library needed.
"""
from itertools import combinations, permutations
from hashlib import sha256

PAIRS = tuple(combinations(range(5), 2))
N = len(PAIRS)
POW3 = tuple(3**i for i in range(N))
NEIGHBORS = tuple(tuple(j for j, q in enumerate(PAIRS)
                       if not (set(p) & set(q))) for p in PAIRS)
assert all(len(v) == 3 for v in NEIGHBORS)

# Every ground-set permutation induces a Petersen-graph automorphism.
AUT = []
for perm in permutations(range(5)):
    m = tuple(PAIRS.index(tuple(sorted((perm[p[0]], perm[p[1]])))) for p in PAIRS)
    assert all(set(m[j] for j in NEIGHBORS[i]) == set(NEIGHBORS[m[i]]) for i in range(N))
    AUT.append(m)
assert len(set(AUT)) == 120

def digits(code):
    out = []
    for _ in range(N):
        out.append(code % 3)
        code //= 3
    return tuple(out)

def relabel(col, automorphism):
    # Color at vertex i moves to automorphism(i).
    code = 0
    for i in range(N):
        code += col[i] * POW3[automorphism[i]]
    return code

def ball_matrix(col):
    b = [[0]*N for _ in range(N)]
    for i, c in enumerate(col):
        if c == 0:
            b[i][i] = 20
        elif c == 1:
            b[i][i] = 5
            for j in NEIGHBORS[i]:
                b[i][j] = 5
        else:
            b[i] = [2]*N
    return b

def gram(b):
    return [[sum(b[k][i]*b[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]

def positive_definite_integer(a):
    """Sylvester's criterion via exact fraction-free elimination.
    At each step the pivot equals the corresponding leading principal minor.
    """
    a = [list(row) for row in a]
    d_prev = 1
    for k in range(N-1):
        pivot = a[k][k]
        if pivot <= 0:
            return False
        for i in range(k+1,N):
            u = a[i][k]
            for j in range(k+1,N):
                v = pivot*a[i][j] - u*a[k][j]
                if v % d_prev:
                    raise AssertionError('fraction-free division failed')
                a[i][j] = v // d_prev
        d_prev = pivot
    return a[-1][-1] > 0

# Strict separator: 741/500 is between second-largest and largest squared norms.
# For B=20 times a radius-selection matrix, test 2964 I - 5 B^T B > 0.
VISITED = bytearray(3**N)
representatives = []
strict_checked = 0
winning_orbit = []
class_counts = []
representative_digest = sha256()
for code in range(3**N):
    if VISITED[code]:
        continue
    col = digits(code)
    images = {relabel(col, automorphism) for automorphism in AUT}
    assert min(images) == code
    for k in images:
        assert not VISITED[k]
        VISITED[k] = 1
    class_counts.append(len(images))
    representatives.append(code)
    representative_digest.update(code.to_bytes(4,'big'))
    T = gram(ball_matrix(col))
    separator = [[(2964 if i==j else 0) - 5*T[i][j]
                  for j in range(N)] for i in range(N)]
    if positive_definite_integer(separator):
        strict_checked += 1
    else:
        winning_orbit.append((code,len(images),col))
assert all(VISITED)
assert len(representatives) == 792
assert sum(class_counts) == 59049
assert strict_checked == 791
assert len(winning_orbit) == 1
assert winning_orbit[0][1] == 20

# Identify exceptional selection combinatorially without numerical eigensolvers.
# There are five choices of a common point and four choices of the omitted pair.
expected = set()
for common in range(5):
    for omitted in range(5):
        if omitted == common:
            continue
        col = [0]*N
        for v,(a,b) in enumerate(PAIRS):
            if common in (a,b):
                col[v] = 2 if omitted in (a,b) else 0
            elif omitted in (a,b):
                col[v] = 1
            else:
                col[v] = 2
        expected.add(sum(c*POW3[i] for i,c in enumerate(col)))
assert len(expected)==20
assert {relabel(winning_orbit[0][2],a) for a in AUT} == expected

# The largest eigenvalue of the exceptional Gram matrix divided by 400
# is the unique root in (1484/1000, 1485/1000) of
# p(z)=200 z^3-355 z^2+87 z-1.
# The strictly positive eigenvector is (H,T,S)=(1,(49z-1)/d,(24z+3)/d)
# on the three pair classes: three high, six intermediate, one low,
# d=200z^2-81z+1. The cubic identity verifies the three row equations.
from fractions import Fraction

def P(z): return 200*z**3-355*z**2+87*z-1
left, right=Fraction(1484,1000), Fraction(1485,1000)
assert P(left)<0<P(right)
# p'(z)=600z^2-710z+87 strictly positive throughout (1.484,1.485).
assert 600*left*left-710*right+87 > 0
# Remainder checking for exact polynomial identities in Z[z] modulo P.
def mod_p(coeff):
    # Low-to-high coefficients, compute remainder after dividing by monic P/200.
    a=[Fraction(v) for v in coeff]
    p=[Fraction(-1,200),Fraction(87,200),Fraction(-355,200),Fraction(1)]
    for d in range(len(a)-1,2,-1):
        t=a[d]
        for j in range(4):a[d-3+j]-=t*p[j]
    return a[:3]
def plus(u,v):
    n=max(len(u),len(v));return [(u[i] if i<len(u) else 0)+(v[i] if i<len(v) else 0) for i in range(n)]
def neg(u):return [-x for x in u]
def mult(u,v):
    a=[0]*(len(u)+len(v)-1)
    for i,x in enumerate(u):
        for j,y in enumerate(v):a[i+j]+=x*y
    return a
z=[0,1]; D=[1,-81,200]; H=D; T=[-1,49]; S=[3,24]
# All H,T,S above share a positive divisor D(z).
# Global mean mu=(3H+6T+S)/10, q=(H+T)/2.
mu_num=plus(plus([3*x for x in H],[6*x for x in T]),S)
q_num=plus(H,T)
# Verify lambda*H = H + (2/5)mu + (1/2)q.
# multiplied by 20: 20*z*H -20*H - 4*mu_num/??
# mu = mu_num / (10D), so (2/5)mu = mu_num/(25D).
# q = q_num / (2D), so (1/2)q=q_num/(4D).
# multiply by 100D: 100 z H -100H -4 mu_num -25 q_num =0.
assert mod_p(plus(plus(plus([100*x for x in mult(z,H)],neg([100*x for x in H])),neg([4*x for x in mu_num])), neg([25*x for x in q_num]))) == [0]*3
# lambda*T = (2/5)mu + (1/4)q; multiply 200D
# 200 z T -8 mu_num -25 q_num =0
assert mod_p(plus(plus([200*x for x in mult(z,T)],neg([8*x for x in mu_num])),neg([25*x for x in q_num]))) == [0]*3
# lambda*S = (2/5)mu; multiply 25D
assert mod_p(plus([25*x for x in mult(z,S)],neg(mu_num))) == [0]*3
# Verify all radii in the winner are uniquely active for the positive input.
# These are rigorous interval estimates; no floating point is involved.
def Df(z): return 200*z*z-81*z+1
dmin,dmax=Df(left),Df(right)
assert dmin>0 and dmin<dmax
Tmin,Tmax=(49*left-1)/dmax,(49*right-1)/dmin
Smin,Smax=(24*left+3)/dmax,(24*right+3)/dmin
assert 0<Smin<Smax<Tmin<Tmax<1
mu_min=(3+6*Tmin+Smin)/10
mu_max=(3+6*Tmax+Smax)/10
# High-pair radius zero beats its radius-one and global choices.
assert 1>max((1+3*Tmax)/4,mu_max)
# The omitted pair takes global radius two.
assert mu_min>max(Smax,(Smax+3*Tmax)/4)
# The three pairs containing omitted ground-element take radius one.
assert (1+Tmin)/2>max(Tmax,mu_max)
# The other three intermediate pairs take radius two.
assert mu_min>max(Tmax,(1+Smax+2*Tmax)/4)

# Strictly positive T=B^TB: four globally-averaging rows in each winner.
assert all(any(row==[2]*N for row in ball_matrix(digits(code))) for code in expected)
# Thus Perron--Frobenius shows the displayed positive eigenvector is unique top ray.
print('CERTIFICATE_OK selections=59049 automorphisms=120 orbits=792 strict=791 winning_orbit_size=20')
print('winning_rep', winning_orbit[0][0], 'representatives_sha256',representative_digest.hexdigest())
