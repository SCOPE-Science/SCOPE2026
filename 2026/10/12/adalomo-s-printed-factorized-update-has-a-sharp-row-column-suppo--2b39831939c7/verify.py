import itertools
import math


def energies(G):
    m=len(G); n=len(G[0])
    R=[sum(G[i][j]*G[i][j] for j in range(n)) for i in range(m)]
    C=[sum(G[i][j]*G[i][j] for i in range(m)) for j in range(n)]
    return R,C


def raw_current(G,beta=0.9):
    R,C=energies(G)
    total=sum(R)
    if total==0:
        return [[float('nan') for _ in C] for _ in R]
    V=[[(1-beta)*R[i]*C[j]/total for j in range(len(C))] for i in range(len(R))]
    U=[]
    for i,row in enumerate(G):
        out=[]
        for j,g in enumerate(row):
            v=V[i][j]
            out.append(g/v if v!=0 else float('nan'))
        U.append(out)
    return U


def raw_v1(G,beta=0.9):
    R,C=energies(G)
    V=[[(1-beta)**2*R[i]*C[j] for j in range(len(C))] for i in range(len(R))]
    U=[]
    for i,row in enumerate(G):
        out=[]
        for j,g in enumerate(row):
            v=V[i][j]
            out.append(g/v if v!=0 else float('nan'))
        U.append(out)
    return U


def finite(U):
    return all(math.isfinite(x) for row in U for x in row)


def no_zero_rows_cols(G):
    R,C=energies(G)
    return all(r>0 for r in R) and all(c>0 for c in C)

# Exhaustive 2x3 support classification over {-1,0,1}.
for vals in itertools.product((-1.0,0.0,1.0), repeat=6):
    G=[list(vals[:3]),list(vals[3:])]
    expected=no_zero_rows_cols(G)
    assert finite(raw_current(G)) == expected
    assert finite(raw_v1(G)) == expected

# Strongly convex witness: F(W)=1/2 ||W-B||_F^2.
G=[[0.0,0.0],[1.0,-1.0]]
assert sum(x*x for row in G for x in row)>0
U=raw_current(G)
assert not math.isfinite(U[0][0]) and not math.isfinite(U[0][1])
assert math.isfinite(U[1][0]) and math.isfinite(U[1][1])

# Adafactor-style sqrt(V)+eps is finite on the same zero row when total mass is positive.
beta=0.9
eps=1e-8
R,C=energies(G); total=sum(R)
V=[[(1-beta)*R[i]*C[j]/total for j in range(len(C))] for i in range(len(R))]
U_safe=[[G[i][j]/(math.sqrt(V[i][j])+eps) for j in range(2)] for i in range(2)]
assert finite(U_safe)
assert U_safe[0]==[0.0,0.0]

# Maintained-code style positive squared-gradient floor makes all factor states positive.
eps0=1e-30
Q=[[g*g+eps0 for g in row] for row in G]
row_mean=[sum(row)/len(row) for row in Q]
col_mean=[sum(Q[i][j] for i in range(2))/2 for j in range(2)]
assert all(x>0 for x in row_mean+col_mean)
row_global=sum(row_mean)/len(row_mean)
r_factor=[(x/row_global)**-0.5 for x in row_mean]
c_factor=[x**-0.5 for x in col_mean]
U_code=[[r_factor[i]*c_factor[j]*G[i][j] for j in range(2)] for i in range(2)]
assert finite(U_code)
assert U_code[0]==[0.0,0.0]

print('verification passed')
