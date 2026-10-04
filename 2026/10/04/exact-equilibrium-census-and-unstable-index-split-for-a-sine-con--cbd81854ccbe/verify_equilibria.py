from fractions import Fraction as F
import math

# Exact printed coefficient matrix.
D = [
    [F(4195,1000), F(-4295,1000), F(1295,1000)],
    [F(31,10), F(-32,10), F(-61,10)],
    [F(-7605,1000), F(7605,1000), F(-1905,1000)],
]

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

assert det3(D) == F(-54153,10000)
v = [F(-3065,547), F(-98680,18051), F(365,18051)]
for i in range(3):
    lhs = sum(D[i][j]*v[j] for j in range(3))
    assert lhs == (F(1) if i == 2 else F(0))

# Coordinate ratios and scalar reduction.
assert v[0]/v[1] == F(20229,19736)
assert v[2]/v[1] == F(-73,19736)
eps, sig = F(33,10), F(47,10)
B = -sig * v[1] * eps
assert B == F(231898,2735)

# Classical rational bounds 333/106 < pi < 22/7 imply the lobe cutoff.
pi_lo, pi_hi = F(333,106), F(22,7)
assert 26*pi_hi < B
assert B < 27*pi_lo

# The proof's uniform cosine separation: for every nonzero root, |t|<26*pi.
ratio = (26*pi_hi) / B
assert ratio*ratio < F(15,16)  # hence |cos t| > 1/4
q_gap = eps*sig*F(1,4)
assert q_gap == F(1551,400)

# Exact characteristic-polynomial/Routh thresholds.
q_b = F(-1098441,878875)
q_a3 = F(18051,98680)
assert q_gap > -q_b
assert q_gap > q_a3

# Supplementary numerical root bracketing.
Bf = float(B)
def f(t):
    return t + Bf*math.sin(t)

def bisect(a,b):
    fa,fb=f(a),f(b)
    assert fa*fb < 0
    for _ in range(100):
        m=(a+b)/2
        fm=f(m)
        if fa*fm <= 0:
            b,fb=m,fm
        else:
            a,fa=m,fm
    return (a+b)/2

roots=[]
for k in range(1,14):
    a=(2*k-1)*math.pi
    m=(2*k-0.5)*math.pi
    b=2*k*math.pi
    assert f(a) > 0 and f(m) < 0 and f(b) > 0
    roots.append(bisect(a,m))
    roots.append(bisect(m,b))
assert len(roots) == 26
assert roots[-1] < 26*math.pi < Bf < 27*math.pi

# Routh sign patterns at numerical roots: 13 left + 13 right on t>0.
index2=index1=0
for j,t in enumerate(roots):
    q=float(eps*sig)*math.cos(t)
    third=float(F(878875,25000))*q + float(F(1098441,25000))
    last=float(F(54153,10000)) - float(F(7401,250))*q
    signs=[1.0,0.91,third/0.91,last]
    changes=sum(1 for a,b in zip(signs,signs[1:]) if a*b < 0)
    if changes==2: index2+=1
    elif changes==1: index1+=1
    else: raise AssertionError(changes)
assert (index2,index1)==(13,13)
# Reflection doubles both classes and the origin adds one index-1 equilibrium.
assert 2*index2 == 26
assert 2*index1 + 1 == 27
print("VERIFY_OK")
