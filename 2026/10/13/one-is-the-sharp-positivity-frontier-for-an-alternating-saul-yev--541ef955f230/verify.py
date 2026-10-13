from fractions import Fraction as F

def coeff(r):
    return r/(1+r), (1-r)/(1+r)

def left(u, r):
    n=len(u)
    beta,gamma=coeff(r)
    v=[F(0)]*n
    for j in range(n):
        prev = v[j-1] if j>0 else F(0)
        right = u[j+1] if j+1<n else F(0)
        v[j]=beta*prev+gamma*u[j]+beta*right
    return v

def right(v, r):
    n=len(v)
    beta,gamma=coeff(r)
    w=[F(0)]*n
    for j in range(n-1,-1,-1):
        leftv = v[j-1] if j>0 else F(0)
        nxt = w[j+1] if j+1<n else F(0)
        w[j]=beta*leftv+gamma*v[j]+beta*nxt
    return w

def pair_matrix(n,r):
    cols=[]
    for k in range(n):
        e=[F(0)]*n
        e[k]=F(1)
        cols.append(right(left(e,r),r))
    return [[cols[j][i] for j in range(n)] for i in range(n)]

def corner_formula(n,r):
    beta,gamma=coeff(r)
    return beta**(n-1)*gamma*(1+gamma)

# One-node exception.
for r in [F(0),F(1,3),F(1),F(2),F(7,2)]:
    P=pair_matrix(1,r)
    _,g=coeff(r)
    assert P == [[g*g]]
    assert P[0][0] >= 0

# Closed corner identity across dimensions and both safe/unsafe values.
for n in range(2,10):
    for r in [F(1,5),F(1),F(6,5),F(2),F(7,3)]:
        P=pair_matrix(n,r)
        assert P[n-1][0] == corner_formula(n,r)

# Representative safe values have no negative entries.
for n in range(1,10):
    for r in [F(0),F(1,7),F(1,2),F(9,10),F(1)]:
        P=pair_matrix(n,r)
        assert min(x for row in P for x in row) >= 0

# Every sampled unsafe value has the certified negative corner for n>=2.
for n in range(2,10):
    for r in [F(11,10),F(3,2),F(2),F(5)]:
        P=pair_matrix(n,r)
        assert P[n-1][0] < 0

# Exact witness.
P=pair_matrix(2,F(2))
assert P[1][0] == F(-4,27)

print("VERIFY_OK")
print("witness_corner", P[1][0])
