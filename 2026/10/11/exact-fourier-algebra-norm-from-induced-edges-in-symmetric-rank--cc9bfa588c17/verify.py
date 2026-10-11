from fractions import Fraction
from itertools import permutations, combinations
from math import sqrt

# Exhaustive exact check for the rank-three action of S4 on 2-subsets.
# Convolution is normalized by |S4|.  All spectral checks below use exact rationals.

def compose(p,q):
    return tuple(p[q[i]] for i in range(4))

def inv(p):
    r=[0]*4
    for i,j in enumerate(p): r[j]=i
    return tuple(r)

def matmul(A,B):
    n=len(A); m=len(B); k=len(B[0])
    return [[sum(A[i][t]*B[t][j] for t in range(m)) for j in range(k)] for i in range(n)]

def transpose(A):
    return [list(row) for row in zip(*A)]

def rank_fraction(A):
    A=[[Fraction(x) for x in row] for row in A]
    m=len(A); n=len(A[0]) if m else 0
    r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def nullity_shift(B,lam):
    n=len(B)
    A=[[Fraction(B[i][j])-(lam if i==j else 0) for j in range(n)] for i in range(n)]
    return n-rank_fraction(A)

def edge_count(J,Omega):
    J=set(J); e=0
    for i,j in combinations(sorted(J),2):
        if len(set(Omega[i]) & set(Omega[j]))==1:
            e+=1
    return e

G=list(permutations(range(4)))
idx={g:i for i,g in enumerate(G)}
Ginv={g:inv(g) for g in G}
Omega=list(combinations(range(4),2))
oi={a:i for i,a in enumerate(Omega)}
alpha=0

def act(g,a):
    x=Omega[a]
    return oi[tuple(sorted((g[x[0]],g[x[1]])))]

checked=0
max_numeric_error=0.0
for mask in range(1<<len(Omega)):
    J={i for i in range(len(Omega)) if (mask>>i)&1}
    r=len(J); e=edge_count(J,Omega)
    # Integer convolution matrix C = |G| L_{1_A}.
    # C[z,x] = 1_A(z x^{-1}).
    C=[]
    for z in G:
        row=[]
        for x in G:
            y=compose(z,Ginv[x])
            row.append(1 if act(y,alpha) in J else 0)
        C.append(row)
    B=matmul(transpose(C),C)

    # Johnson graph J(4,2): v=6,k=4, theta=0 (mult 3), tau=-2 (mult 2).
    qth=Fraction(2*e + 2*r - r*r,2)   # 1_J^T P_theta 1_J
    qta=Fraction(r*r,3)-e              # 1_J^T P_tau 1_J
    assert qth>=0 and qta>=0
    lam0=Fraction((4*r)**2) if r else Fraction(0)
    lamth=Fraction(32)*qth
    lamta=Fraction(48)*qta

    expected={}
    if lam0: expected[lam0]=expected.get(lam0,0)+1
    if lamth: expected[lamth]=expected.get(lamth,0)+3
    if lamta: expected[lamta]=expected.get(lamta,0)+2

    for lam,mult in expected.items():
        got=nullity_shift(B,lam)
        assert got==mult,(mask,lam,mult,got,r,e)
    assert rank_fraction(B)==sum(expected.values()),(mask,r,e,rank_fraction(B),expected)

    nuclear=sum(mult*sqrt(float(lam)) for lam,mult in expected.items())/24.0
    formula=(Fraction(r,6) + sqrt(float(Fraction(3,6)*qth)) + sqrt(float(Fraction(2,6)*qta)))
    max_numeric_error=max(max_numeric_error,abs(nuclear-formula))
    assert abs(nuclear-formula)<1e-12
    checked+=1

print(f"VERIFY_OK exact_convolution_cases={checked} max_numeric_error={max_numeric_error:.3e}")
