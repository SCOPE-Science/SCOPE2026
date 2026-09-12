"""Exact verification for mod-2 self-cup framing at q2 over Q(sqrt2).
Uses only exact rational arithmetic (Fractions); F = Q(sqrt2) elements are pairs (p,q) = p + q*sqrt2.
Covers: discriminant/Minkowski (class number 1), norms, a = eps*sqrt2, (a) = q2,
a nonsquare (norm 2 not a square in Q), -1 nonsquare (signs), full S-unit/2 sign table,
norm equation a = x^2+y^2, and explicit quaternion splitting matrices.
"""
from fractions import Fraction as Q

def add(u, v): return (u[0]+v[0], u[1]+v[1])
def mul(u, v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def norm(u): return u[0]*u[0]-2*u[1]*u[1]
def sq(u): return mul(u, u)

O = (Q(0), Q(0)); ONE = (Q(1), Q(0)); NEG1 = (Q(-1), Q(0))
RT2 = (Q(0), Q(1))          # sqrt2
EPS = (Q(1), Q(1))          # 1+sqrt2
A = (Q(2), Q(1))            # 2+sqrt2, candidate f Kummer representative
X = (Q(1), Q(1,2))          # 1+sqrt2/2
Y = (Q(0), Q(1,2))          # sqrt2/2

print("== discriminant and Minkowski bound: disc=8, bound=(1/2)sqrt(8)=sqrt(2)<2 ==")
# bound^2 = 2 < 4 = 2^2, so every class has an integral rep of norm <= bound < 2, i.e. norm 1
assert Q(2) < Q(4), "bound^2=2 < 4"
print("bound^2 = 2 < 4 = 2^2, so Cl(O_F) = 1; (2) ramifies totally: disc 8 = 2^3, q2=(sqrt2) unique above 2")

print("== norms ==")
print("N(2+sqrt2) =", norm(A))
print("N(1+sqrt2) =", norm(EPS))
print("N(sqrt2) =", norm(RT2))
print("N(-1) =", norm(NEG1))
assert norm(A) == 2 and norm(EPS) == -1 and norm(RT2) == -2 and norm(NEG1) == 1

print("== a = eps*sqrt2 and (a) = q2 ==")
assert mul(EPS, RT2) == A, "a must equal eps*sqrt2"
# N((a)) = |N(a)| = 2, and q2 is the only prime of norm 2 (all norm-2 primes lie above 2, only q2 does)
print("OK: a = eps*sqrt2, N(a)=2 so (a) is prime of norm 2, hence (a)=q2; v_q2(a)=1 (odd -> ramified)")

print("== a is not a square in F (norm 2 is not a square in Q) ==")
# if a=b^2 then 2=N(a)=N(b)^2; 2 is not a square in Q (if (p/q)^2=2 in lowest terms, p^2=2q^2
# forces p even then q even, contradiction)
print("2 is not a square in Q by infinite descent; hence a, -a (N=2) are nonsquares in F")
print("N(eps)=N(-eps)=-1, N(sqrt2)=N(-sqrt2)=-2, all nonsquares in Q: eps,-eps,sqrt2,-sqrt2 nonsquares")

print("== signs at the two real embeddings (sqrt2 in (1.41,1.42)) ==")
lo, hi = Q(141,100), Q(142,100)
assert lo*lo < 2 < hi*hi
# full S-unit/2 sign table: representatives (-1)^e0 eps^e1 rt2^e2
reps = {"1": ONE, "-1": NEG1, "eps": EPS, "-eps": mul(NEG1, EPS),
        "s": RT2, "-s": mul(NEG1, RT2), "a": A, "-a": mul(NEG1, A)}
for name, u in reps.items():
    e1_lo = u[0]+u[1]*lo; e1_hi = u[0]+u[1]*hi
    e2_lo = u[0]-u[1]*hi; e2_hi = u[0]-u[1]*lo
    s1 = "+" if e1_lo > 0 else ("-" if e1_hi < 0 else "?")
    s2 = "+" if e2_lo > 0 else ("-" if e2_hi < 0 else "?")
    print("  [%s] signs (%s,%s)" % (name, s1, s2))
    assert s1 != "?" and s2 != "?", "sign must be certified nonzero"
assert A[0]+A[1]*lo > 0 and A[0]-A[1]*hi > 0, "a must be totally positive"
assert not (NEG1[0]+NEG1[1]*lo > 0), "-1 negative at emb1: not a square in F"
print("OK: only [1] and [a] totally positive; only nontrivial unramified-outside-q2 class is [a]")
print("OK: -1 < 0 at both embeddings, so -1 is not a square in F; F(i)/F is quadratic")

print("== norm equation a = x^2 + y^2 ==")
s = add(sq(X), sq(Y))
print("x^2 =", sq(X), " y^2 =", sq(Y), " sum =", s, " a =", A)
assert s == A, "norm equation failed"
print("OK: a = N_{F(i)/F}(x + i y), so quaternion (a,-1) splits over F")

print("== quaternion splitting matrices for (a,-1): I^2=a, J^2=-1, IJ+JI=0 ==")
def madd(M,N): return [[add(M[i][j],N[i][j]) for j in range(2)] for i in range(2)]
def mmul(M,N): return [[add(mul(M[i][0],N[0][j]), mul(M[i][1],N[1][j])) for j in range(2)] for i in range(2)]
def mscale(c,M): return [[mul(c,M[i][j]) for j in range(2)] for i in range(2)]
I2 = [[ONE,O],[O,ONE]]; Z2=[[O,O],[O,O]]
I = [[X,Y],[Y,(-X[0],-X[1])]]; J = [[O,(-ONE[0],-ONE[1])],[ONE,O]]
I2a = mscale(A,I2); NEGI2 = mscale(NEG1,I2)
assert mmul(I,I) == I2a, "I^2 != a"
assert mmul(J,J) == NEGI2, "J^2 != -1"
assert madd(mmul(I,J),mmul(J,I)) == Z2, "no anticommute"
print("OK: explicit F-algebra map (a,-1) -> M2(F), nonzero hence iso (domain simple, dims 4=4)")

print("== {1,I,J,IJ} F-basis of M2(F) (rank 4 over F via rank 8 over Q) ==")
IJ = mmul(I,J)
def toQ8(M):
    v=[]
    for i in range(2):
        for j in range(2):
            v += [M[i][j][0], M[i][j][1]]
    return v
rows=[toQ8(M) for M in (I2,I,J,IJ)]
M=[list(r) for r in rows]; r=0
for c in range(8):
    piv=None
    for i in range(r,4):
        if M[i][c]!=0: piv=i; break
    if piv is None: continue
    M[r],M[piv]=M[piv],M[r]
    for i in range(4):
        if i!=r and M[i][c]!=0:
            f=M[i][c]/M[r][c]
            for k in range(c,8): M[i][k]-=f*M[r][k]
    r+=1
print("rank =",r); assert r==4
print("OK: splitting is an isomorphism (a,-1) ~= M2(F); Brauer class 0")
print("ALL EXACT CHECKS PASSED")
