"""Exact-arithmetic certificate checks for three-row minimax sampling.
Run: python VERIFY.py. Requires only the Python standard library.
These finite tests support, but do not replace, the general proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

ZERO, ONE = F(0), F(1)


def det(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))


def inverse(M):
    d=det(M)
    assert d
    I=[]
    for i in range(3):
        row=[]
        for j in range(3):
            inds_i=[k for k in range(3) if k!=j]
            inds_j=[k for k in range(3) if k!=i]
            minor=M[inds_i[0]][inds_j[0]]*M[inds_i[1]][inds_j[1]]-M[inds_i[0]][inds_j[1]]*M[inds_i[1]][inds_j[0]]
            row.append((-1 if (i+j)%2 else 1)*minor/d)
        I.append(row)
    return I


def psd(M):
    for i in range(3):
        if M[i][i]<0:return False
    for i,j in [(0,1),(0,2),(1,2)]:
        if M[i][i]*M[j][j]-M[i][j]*M[j][i]<0:return False
    return det(M)>=0


def pd(M):
    return M[0][0]>0 and M[0][0]*M[1][1]-M[0][1]*M[1][0]>0 and det(M)>0


def closed_sampler(C):
    edges={(0,1):abs(C[0][1]),(0,2):abs(C[0][2]),(1,2):abs(C[1][2])}
    prod=C[0][1]*C[0][2]*C[1][2]
    q=[ZERO]*3
    if prod>=0:
        regime='balanced'
        for (i,j),a in edges.items():q[i]+=a;q[j]+=a
    else:
        a,b,c=edges[(0,1)],edges[(0,2)],edges[(1,2)]
        side=[1/a,1/b,1/c]
        if 2*max(side)<sum(side):
            regime='frustrated-interior'
            q=[a*b/c,a*c/b,b*c/a]
        else:
            regime='frustrated-cut'
            (j,k),weak=min(edges.items(),key=lambda pair:pair[1])
            i=3-j-k
            q[i]=edges[tuple(sorted((i,j)))]+edges[tuple(sorted((i,k)))]
            q[j]=edges[tuple(sorted((i,j)))]-weak
            q[k]=edges[tuple(sorted((i,k)))]-weak
    w=[C[i][i]+q[i] for i in range(3)]
    tau=sum(w)
    p=[x/tau for x in w]
    L=ONE/tau
    S=[[q[i] if i==j else -C[i][j] for j in range(3)] for i in range(3)]
    assert all(x>0 for x in p)
    assert sum(p)==1
    assert all(x>=0 for x in q)
    assert psd(S)
    assert det(S)==0
    return p,L,regime,S


checks=0
counts={}

# Exhaustive rational correlation triples on a symmetric grid.
vals=[F(k,5) for k in range(-4,5)]
for a,b,c in product(vals,repeat=3):
    G=[[ONE,a,b],[a,ONE,c],[b,c,ONE]]
    if not pd(G):continue
    C=inverse(G)
    p,L,regime,S=closed_sampler(C)
    counts[regime]=counts.get(regime,0)+1
    # The displayed transition is a constructive primal certificate.
    D=[[p[i]-(L*C[i][i]) if i==j else -L*C[i][j] for j in range(3)] for i in range(3)]
    assert psd(D) and det(D)==0
    checks+=1

# Exact two-branch corollary, including both endpoints of the kink.
for k in range(-49,100):
    t=F(k,100)
    G=[[ONE,F(1,2),F(1,2)],[F(1,2),ONE,t],[F(1,2),t,ONE]]
    assert pd(G)
    p,L,regime,S=closed_sampler(inverse(G))
    if t<=F(2,5):
        ex=[(t+2)/(t+5),F(3,1)/(2*(t+5)),F(3,1)/(2*(t+5))]
        eL=(2*t+1)/(2*(t+5))
    else:
        denom=6*t-2*t*t-1
        ex=[2*t*(1-t)/denom,(4*t-1)/(2*denom),(4*t-1)/(2*denom)]
        eL=(1-t)*(4*t-1)/(2*denom)
    assert p==ex and L==eL
    checks+=1

# Finite randomized independent objective crosscheck: at the candidate optimum
# no alternative probability has a *strictly* PD improvement certificate.
rng=Random(240631)
for k in range(320):
    a,b,c=(F(rng.randrange(-9,10),10) for _ in range(3))
    G=[[ONE,a,b],[a,ONE,c],[b,c,ONE]]
    if not pd(G):continue
    C=inverse(G)
    p,L,mode,S=closed_sampler(C)
    for j in range(30):
        i=rng.randrange(1,100)
        h=rng.randrange(1,101-i)
        trial=[F(i,101),F(h,101),F(101-i-h,101)]
        T=[[trial[x]-L*C[x][x] if x==y else -L*C[x][y] for y in range(3)] for x in range(3)]
        assert not pd(T)
        checks+=1

assert counts['balanced']>0 and counts['frustrated-interior']>0 and counts['frustrated-cut']>0
print('PASS',checks,'exact checks; exhaustive grid case counts:',counts)
