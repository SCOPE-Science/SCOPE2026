"""Exact-integer Bernstein certificate for an eighth-moment inequality.

Requires Python 3 only. All arithmetic in the certificate is integral.
"""
from math import factorial

EXPS = [(i, j, 8-i-j) for i in range(9) for j in range(9-i)]
INDEX = {e: k for k, e in enumerate(EXPS)}
ONE = {(0, 0, 0): 1}

def add(dest, source, factor=1):
    for e, v in source.items():
        dest[e] = dest.get(e, 0) + factor*v
    return dest

def multiply(p, q):
    r = {}
    for (i,j,k), v in p.items():
        for (a,b,c), w in q.items():
            e = (i+a,j+b,k+c)
            r[e] = r.get(e, 0) + v*w
    return r

def power(p, n):
    ans = ONE
    for _ in range(n):
        ans = multiply(ans, p)
    return ans

def multinomial(n, i, j, k):
    return factorial(n)//(factorial(i)*factorial(j)*factorial(k))

# The normalized eighth moment of a+b*z+c*z^3 is the sum of
# squares of the coefficients of (a+b*z+c*z^3)^4.
COEFFS = {}
for i in range(5):
    for j in range(5-i):
        k = 4-i-j
        d = j+3*k
        COEFFS.setdefault(d, {})[(i,j,k)] = multinomial(4,i,j,k)
M = {}
for p in COEFFS.values():
    add(M, multiply(p,p))
NORM4 = {}
for i in range(5):
    for j in range(5-i):
        k = 4-i-j
        NORM4[(2*i,2*j,2*k)] = multinomial(4,i,j,k)

upper_num, denom = 9221771, 1000000
F = {}
add(F, NORM4, upper_num)
add(F, M, -denom)

A = {(1,0,0):1}
B = {(0,1,0):1}
C = {(0,0,1):1}
def L(a,b,c):
    p={}
    add(p,A,a); add(p,B,b); add(p,C,c)
    return p

# Each row is (twice) the barycentric coordinates of a child's
# vertices. Substitution multiplies the restricted degree-eight
# polynomial by 2^8, so no fractions enter the certificate.
FORMS = [
    (L(2,1,1), B, C),
    (A, L(1,2,1), C),
    (A, B, L(1,1,2)),
    (L(1,0,1), L(1,1,0), L(0,1,1)),
]
TRANSFORMS=[]
for a,b,c in FORMS:
    TRANSFORMS.append([
        [(INDEX[e], v) for e,v in multiply(
            multiply(power(a,i), power(b,j)),power(c,k)).items() if v]
        for (i,j,k) in EXPS
    ])

def transform(coef, T):
    out=[0]*len(EXPS)
    for v,col in zip(coef,T):
        if v:
            for index,weight in col:
                out[index]+=v*weight
    return out

# A homogeneous polynomial with only nonnegative coefficients is
# nonnegative on nonnegative barycentric coordinates. Four-way
# subdivision exhausts the entire standard simplex.
stack=[([F.get(e,0) for e in EXPS], 0)]
nodes=leaves=maxdepth=0
while stack:
    coeff,depth = stack.pop()
    nodes+=1
    if all(v>=0 for v in coeff):
        leaves+=1
        continue
    if depth >= 15:
        raise AssertionError('certificate subdivision exceeded depth 15')
    for T in TRANSFORMS:
        stack.append((transform(coeff,T),depth+1))
    maxdepth=max(maxdepth,depth+1)
assert (nodes,leaves,maxdepth)==(81,61,13), (nodes,leaves,maxdepth)

# A concrete positive trinomial gives a strict rational lower bound.
a,b,c=576602,605492,548552
value=sum(v*(a**e[0])*(b**e[1])*(c**e[2]) for e,v in M.items())
energy=(a*a+b*b+c*c)
assert 1000000*value > 9221770*(energy**4)
assert 1000000*value < 9221771*(energy**4)
print('PASS: exact nonnegative Bernstein coefficients on 61 leaves')
print('PASS: 81 visited nodes, maximum subdivision depth 13')
print('PASS: strict rational lower bound 9.221770')
print('PASS: universal upper bound 9.221771')
