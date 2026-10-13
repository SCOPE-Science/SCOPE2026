"""Exact rational reconstruction of Laplacian quantum average mixing under joins."""
from fractions import Fraction
import sympy as s


def graph(n,edges):
    A=s.zeros(n)
    for i,j in edges:
        A[i,j]=A[j,i]=1
    return A


def lap(A):
    return s.diag(*[sum(A[i,j] for j in range(A.rows)) for i in range(A.rows)])-A


def join(A,B):
    n,m=A.rows,B.rows
    C=s.zeros(n+m)
    C[:n,:n]=A
    C[n:,n:]=B
    C[:n,n:]=s.ones(n,m)
    C[n:,:n]=s.ones(m,n)
    return C


def projectors(L):
    d={}
    for eig,mult,V in L.eigenvects():
        W=s.Matrix.hstack(*V)
        E=s.simplify(W*(W.T*W).inv()*W.T)
        assert s.simplify(E*E-E)==s.zeros(L.rows)
        d[eig]=E
    assert s.simplify(sum(d.values(),s.zeros(L.rows))-s.eye(L.rows))==s.zeros(L.rows)
    return d


def reduced(A):
    n=A.rows
    P=projectors(lap(A))
    P[s.S.Zero]=P[s.S.Zero]-s.ones(n)/n
    Q=sum((E.multiply_elementwise(E) for E in P.values()),s.zeros(n))
    assert Q*s.ones(n,1)==(1-s.Rational(1,n))*s.ones(n,1)
    return Q,P.get(s.Integer(n),s.zeros(n))


def avg(A):
    P=projectors(lap(A))
    return sum((E.multiply_elementwise(E) for E in P.values()),s.zeros(A.rows))

SAMPLES={
    'O1':graph(1,[]),'O2':graph(2,[]),'O3':graph(3,[]),
    'K2':graph(2,[(0,1)]),
    'P3':graph(3,[(0,1),(1,2)]),
    'K3':graph(3,[(0,1),(0,2),(1,2)]),
    'C4':graph(4,[(0,1),(1,2),(2,3),(3,0)]),
    'K4':graph(4,[(i,j) for i in range(4) for j in range(i+1,4)]),
    'O4':graph(4,[]),
    'S4':graph(4,[(0,1),(0,2),(0,3)]),
}

counter=0
entries=0
null_cases=0
for x,A in SAMPLES.items():
 for y,B in SAMPLES.items():
    n,m=A.rows,B.rows;N=n+m
    actual=avg(join(A,B))
    Qx,Ex=reduced(A);Qy,Ey=reduced(B)
    cX=s.Rational(2*m,n*N)
    cY=s.Rational(2*n,m*N)
    pred=s.diag(Qx+cX*Ex,Qy+cY*Ey)
    j=s.ones(N,1)
    p=s.Matrix([s.Rational(m,n*N)]*n+[s.Rational(n,m*N)]*m)
    pred+=j*j.T/N**2+p*p.T
    assert pred==actual,(x,y,'formula',actual-pred)
    bx=Qx+cX*Ex; by=Qy+cY*Ey
    rank_pred=(bx.rank()+by.rank()) if n>1 and m>1 else (1 if n==m==1 else (1+bx.rank()+by.rank()))
    rank_act=actual.rank()
    assert rank_pred==rank_act,(x,y,'rank',rank_pred,rank_act)
    if rank_act<N: null_cases+=1
    counter+=1; entries+=N*N
print('VERIFY_OK exact_pairs=%d exact_entries=%d singular_cases=%d K4_rank=%d C4_join_O3_rank=%d'%(counter,entries,null_cases,avg(SAMPLES['K4']).rank(),avg(join(SAMPLES['C4'],SAMPLES['O3'])).rank()))
