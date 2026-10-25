"""Exact-rational reproducibility checks for the three-block Birkhoff face.

All calculations use only the Python standard library. Finite checks are
supplementary to the arbitrary-integer algebraic proof in RESULT.md.
"""
from fractions import Fraction as F

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def edges(m):
    result = []
    for r in range(3):
        for k in range(m):
            left = r*m+k
            for l in range(m):
                result.append((left,r*m+l,'internal'))
            result.append((left,((r+1)%3)*m+k,'connector'))
    return result

def table(m):
    """Closed-form unit-dipole potential, gauge potential(left 0,0)=0."""
    d=3*m*(m+1)*(m+2)
    aa0=[F(0),F(-3*m*(m+1),d)]
    aa1=[F(-(5*m+1)*(m+1),d)]*2
    aa2=[F(-(4*m-1)*(m+1),d)]*2
    cc0=[F(-(3*m*m+m-1),d)]*2
    cc1=[F(-m*(8*m+7),d),F(-m*(5*m+4),d)]
    cc2=[F(-(2*m+1)**2,d)]*2
    aa=[aa0,aa1,aa2];cc=[cc0,cc1,cc2]
    a=[aa[r][0 if k==0 else 1] for r in range(3) for k in range(m)]
    c=[cc[r][0 if k==0 else 1] for r in range(3) for k in range(m)]
    return a+c

def elimination(M,rhs):
    n=len(rhs)
    A=[list(M[i])+[rhs[i]] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if A[i][j]),None)
        check(pivot is not None,'singular reduced graph Laplacian')
        A[j],A[pivot]=A[pivot],A[j]
        v=A[j][j]
        for q in range(j,n+1):A[j][q]/=v
        for i in range(j+1,n):
            if not A[i][j]:continue
            v=A[i][j]
            for q in range(j,n+1):A[i][q]-=v*A[j][q]
    x=[F(0)]*n
    for i in range(n-1,-1,-1):
        x[i]=A[i][n]-sum((A[i][j]*x[j] for j in range(i+1,n)),F(0))
    return x

def direct_potentials(m):
    n=3*m
    E=edges(m)
    L=[[F(0) for _ in range(2*n)] for _ in range(2*n)]
    for i,j,_ in E:
        j+=n
        L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
    # Dipole at connector (left(0,0), right(1,0)), with gauge left(0,0)=0.
    b=[F(0)]*(2*n);b[0]=1;b[n+m]=-1
    reduced=[[L[i][j] for j in range(1,2*n)] for i in range(1,2*n)]
    return [F(0)]+elimination(reduced,b[1:])

def row(m,phi):
    n=3*m
    E=edges(m)
    e=next(j for j,(i,k,kind) in enumerate(E) if i==0 and k==m and kind=='connector')
    vals=[]
    for f,(i,j,_) in enumerate(E):
        vals.append(F(f==e)-(phi[i]-phi[n+j]))
    return E,e,vals

def do_checks():
    for m in range(2,21):
        n=3*m;phi=table(m);E,e,vals=row(m,phi)
        check(len(E)==3*m*(m+1),'support size')
        check(phi[0]==0,'gauge')
        degL=[0]*n;degR=[0]*n
        b=[F(0)]*(2*n);b[0]=1;b[n+m]=-1
        Lphi=[F(0)]*(2*n)
        for i,j,kind in E:
            degL[i]+=1;degR[j]+=1
            Lphi[i]+=phi[i]-phi[n+j]
            Lphi[n+j]+=phi[n+j]-phi[i]
        for i in range(n):
            check(degL[i]==m+1 and degR[i]==m+1,'bistochastic support degree')
        for i in range(2*n):check(Lphi[i]==b[i],'closed-form Kirchhoff equations')
        # A kernel column of the orthogonal cycle-space projection.
        for i in range(n):
            check(sum((v for (a,bb,_),v in zip(E,vals) if a==i),F(0))==0,'zero row divergence')
            check(sum((v for (a,bb,_),v in zip(E,vals) if bb==i),F(0))==0,'zero col divergence')
        norm=sum(map(abs,vals),F(0))
        value=F(2*(3*m*m+m-1),(m+1)*(m+2))
        check(norm==value,'sharp connector row absolute mass')
        check(vals[e]==F(3*m*m+m-1,3*(m+1)*(m+2)),'diagonal projection entry')
        full=F(4*(n-1)**2,n*n)
        check((norm>full)==(m>=4),'first transition within this family')
        # Grouping of 3 internal/connector blocks into two mass classes.
        for rr in range(3):
            ins=sum((abs(vals[t]) for t,v in enumerate(E) if v[2]=='internal' and v[0]//m==rr),F(0))
            con=sum((abs(vals[t]) for t,v in enumerate(E) if v[2]=='connector' and v[0]//m==rr),F(0))
            expected_a=F(5*m*m-2,3*(m+1)*(m+2))
            expected_b=F(m,3*(m+1))
            # Internal blocks 0 and 1 have A; block 2 has B.
            check(ins==(expected_a if rr<2 else expected_b),'internal group mass')
            # Connector block 0 has A; blocks 1 and 2 have B.
            check(con==(expected_a if rr==0 else expected_b),'connector group mass')
    for m in range(2,7):
        exact=direct_potentials(m)
        claimed=table(m)
        for j in range(6*m):check(exact[j]==claimed[j],'independent reduced-Laplacian solve')
        E,e,v=row(m,exact)
        check(sum(abs(t) for t in v)==F(2*(3*m*m+m-1),(m+1)*(m+2)),'independent row norm')
    # Positive-coefficient polynomial, equivalent to strict advantage for all m>=4.
    for m in range(4,45):
        t=m-4
        p=9*t**4+111*t**3+457*t*t+650*t+84
        orig=9*m**4-33*m**3-11*m*m+18*m-4
        check(p==orig and p>0,'integer polynomial identity')
    print('EXACT_CHECKS_OK',CHECKS)

if __name__=='__main__': do_checks()
