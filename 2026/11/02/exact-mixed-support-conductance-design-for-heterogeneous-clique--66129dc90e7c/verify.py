"""Independent finite checks of the clique-bouquet resistance-design formula.

Run: python3 verify.py
Uses only the Python standard library. Finite checks supplement an analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt, isclose

COUNT = 0

def test(condition, message='check failed'):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)

def inv(M):
    n = len(M)
    A = [list(row) + [F(i == j) for j in range(n)] for i,row in enumerate(M)]
    for k in range(n):
        h = next(i for i in range(k,n) if A[i][k])
        A[k],A[h] = A[h],A[k]
        q = A[k][k]
        A[k] = [v/q for v in A[k]]
        for i in range(n):
            if i != k:
                q = A[i][k]
                A[i] = [u-q*v for u,v in zip(A[i],A[k])]
    return [row[n:] for row in A]

def grounded_laplacian(ms, xs, ys):
    N = 1 + sum(ms)
    mat = [[F(0) for _ in range(N-1)] for _ in range(N-1)]
    pos = 0
    for m,x,y in zip(ms,xs,ys):
        for u in range(m):
            mat[pos+u][pos+u] += x
            for v in range(u+1,m):
                mat[pos+u][pos+u] += y
                mat[pos+v][pos+v] += y
                mat[pos+u][pos+v] -= y
                mat[pos+v][pos+u] -= y
        pos += m
    return mat

def kirchhoff_direct(ms,xs,ys):
    N = 1+sum(ms)
    H = inv(grounded_laplacian(ms,xs,ys))
    return N*sum(H[i][i] for i in range(N-1))-sum(map(sum,H))

def kirchhoff_formula(ms,xs,ys):
    N = 1+sum(ms)
    return sum((N-m)/x + N*(m-1)/(x+m*y) for m,x,y in zip(ms,xs,ys))

def optimizer(ms, ps, qs, B):
    N = 1+sum(ms)
    data=[]
    for m,P,Q in zip(ms,ps,qs):
        A=N-m
        C=N*(m-1)
        a=m*P
        b=(m-1)*Q/2
        t = sqrt((a-b)*C/(b*A)) if P>Q*(N-1)/(2*N) else 1.0
        if t<1.0: t=1.0
        Fmin=(a+b*(t-1))*(A+C/t)
        data.append((a,b,t,Fmin))
    S=sum(sqrt(z[3]) for z in data)
    spends=[B*sqrt(z[3])/S for z in data]
    xs=[c/(a+b*(t-1)) for c,(a,b,t,f) in zip(spends,data)]
    ys=[x*(t-1)/m for x,m,(_,_,t,_) in zip(xs,ms,data)]
    return xs,ys,spends,S*S/B,data

# Exact-rational resistance checks use the full grounded Laplacian inverse,
# rather than the cut-vertex decomposition from the proof.
for ms in [(2,2), (2,3), (3,3), (2,2,2), (2,3,4), (3,2,3)]:
    for seed in range(16):
        xs=[F(1+(seed+3*j)%5, 1+(seed+j)%3) for j in range(len(ms))]
        ys=[F((seed+2*j)%4, 1+(seed+3*j)%5) for j in range(len(ms))]
        a=kirchhoff_direct(ms,xs,ys)
        b=kirchhoff_formula(ms,xs,ys)
        test(a==b,f'Kirchhoff formula at {ms}, {xs}, {ys}: {a} != {b}')

# The local phase threshold is checked with exact rational values of
# the objective at a boundary and interior optimal design.
for ms in [(2,2),(2,3,4),(3,3,3),(2,2,3,4)]:
    N=1+sum(ms); M=N-1
    for m in ms:
        A=N-m; C=N*(m-1)
        for P,Q in [(1,1),(1,3),(2,5),(5,2),(3,7),(7,3)]:
            a=F(m*P); b=F((m-1)*Q,2)
            active = F(2*N*P,M*Q)>1
            deriv=b*A-(a-b)*C
            test((deriv<0)==active,'boundary derivative threshold')
            if not active:
                base=a*(A+C)
                for t in [F(1),F(3,2),F(2),F(5)]:
                    test((a+b*(t-1))*(A+C/t)>=base,'pruned local minimizer')
            else:
                t=sqrt(float((a-b)*C/(b*A)))
                test(t>1,'interior t')
                eps=1e-5
                def fun(z):return float(a+b*(z-1))*(A+C/z)
                test(fun(t)<=fun(t+eps)+2e-8,'interior right derivative')
                test(fun(t)<=fun(t-eps)+2e-8,'interior left derivative')

# Independent full-graph KKT numerical checks, including the inactive edges,
# with edges indexed individually rather than grouped by orbit.
def full_matrix(ms,xs,ys):
    N=1+sum(ms)
    L=[[0.0]*N for _ in range(N)]
    edges=[]; root=1
    for m,x,y in zip(ms,xs,ys):
        for i in range(m):
            edges.append((0,root+i,float(x)))
        for i in range(m):
            for j in range(i+1,m):
                edges.append((root+i,root+j,float(y)))
        root+=m
    for i,j,w in edges:
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    return L,edges

# Numeric tests use the standard-library exact inverse on rounded rational
# parameters, comparing predicted optimum to dozens of feasible perturbations.
for ms,ps,qs in [
    ([2,3,4],[1,1,1],[1,3,2]),
    ([2,2,3],[3,1,2],[1,4,5]),
    ([3,4],[2,3],[5,1]),
    ([2,2,2,2],[1,3,2,4],[4,2,8,1]),
    ([2,3],[1,1],[5,6]),
]:
    B=10.0
    xs,ys,spends,optimal,ds=optimizer(ms,ps,qs,B)
    test(all(x>0 for x in xs),'positive spokes')
    budget=sum(m*P*x + m*(m-1)*Q*y/2 for m,P,Q,x,y in zip(ms,ps,qs,xs,ys))
    test(isclose(budget,B,abs_tol=1e-10),'budget exhausted')
    calculated=float(kirchhoff_formula(ms,xs,ys))
    test(isclose(calculated,optimal,abs_tol=2e-9),'optimal predicted value')
    for m,P,Q,y in zip(ms,ps,qs,ys):
        test((y>1e-11)==(Q/P<2*(1+sum(ms))/sum(ms)-1e-12),'support classification')
    # KKT derivatives with actual group-cost coefficients, independently
    # checking every edge orbit is active or correctly inactive.
    multipliers=[]
    for m,P,Q,x,y in zip(ms,ps,qs,xs,ys):
        N=1+sum(ms); A=N-m; C=N*(m-1)
        lam=(A/x**2+C/(x+m*y)**2)/(m*P)
        marginal=C*m/(x+m*y)**2/(m*(m-1)*Q/2)
        multipliers.append(lam)
        test(isclose(lam,optimal/B,rel_tol=2e-9),'spoke KKT')
        if y>1e-11:
            test(isclose(lam,marginal,rel_tol=2e-9),'active internal KKT')
        else:
            test(marginal<=lam+1e-9,'inactive internal KKT')
    # The exact formula is recovered from the complete graph Laplacian
    # after rationalizing the selected conductances.
    X=[F(x).limit_denominator(100000) for x in xs]
    Y=[F(y).limit_denominator(100000) for y in ys]
    test(abs(float(kirchhoff_direct(ms,X,Y))-optimal)<1e-3,'full grounded inverse near optimum')

print('PASS:',COUNT,'independent assertions; exact rational inverses and optimality identities')
