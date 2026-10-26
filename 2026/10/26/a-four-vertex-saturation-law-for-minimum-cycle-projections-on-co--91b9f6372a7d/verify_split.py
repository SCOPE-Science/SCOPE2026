"""Independent exact-rational checks for cycle projections on complete split graphs.

Run: python3 split_cycle_verify.py
Uses only Python's standard library. All edges have unit length.
"""
from fractions import Fraction as F


def solve(A,b):
    n=len(b)
    M=[[F(A[i][j]) for j in range(n)]+[F(b[i])] for i in range(n)]
    for j in range(n):
        p=next(i for i in range(j,n) if M[i][j])
        M[j],M[p]=M[p],M[j]
        x=M[j][j]
        M[j]=[z/x for z in M[j]]
        for i in range(n):
            if i!=j and M[i][j]:
                z=M[i][j]
                M[i]=[M[i][k]-z*M[j][k] for k in range(n+1)]
    return [row[-1] for row in M]


def graph(r,s):
    edges=[(i,j) for i in range(r) for j in range(i+1,r)]
    edges += [(i,r+j) for i in range(r) for j in range(s)]
    n=r+s
    L=[[0]*n for i in range(n)]
    for i,j in edges:
        L[i][i]+=1; L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
    return edges,L


def candidate_t(r,s):
    if s>=4:return -F(s,r)
    return F(s*(r-4)*(s-1), r*(6*s+(r-1)*(4-s)))


def predicted(r,s):
    if s>=4:return F(3*(r-1),r)
    n=r+s
    t=candidate_t(r,s)
    return F(3)-F(6,n)+6*t/n


def direct(r,s,check_idempotence=False):
    edges,L=graph(r,s)
    n=r+s;m=len(edges); t=candidate_t(r,s)
    cols=[];types=[]
    for k,(tail,head) in enumerate(edges):
        d=[F(0)]*n;d[tail]+=1;d[head]-=1
        phi=solve([row[:-1] for row in L[:-1]],d[:-1])+[F(0)]
        u=[phi[i]-sum(phi[:r],F(0))/r for i in range(r)]
        column=[]
        for f,(i,j) in enumerate(edges):
            q=phi[i]-phi[j]
            z=u[i]-u[j] if j<r else -F(r,s)*u[i]
            column.append(F(k==f)-q+t*z)
        assert all(sum((F(int(v==i)-int(w==i))*column[f] for f,(v,w) in enumerate(edges)),F(0))==0 for i in range(n))
        cols.append(column)
        types.append('AA' if head<r else 'AB')
    norms=[sum(map(abs,c),F(0)) for c in cols]
    assert max(norms)==predicted(r,s), (r,s,'actual',max(norms),'predicted',predicted(r,s))
    assert len(set(norms[:r*(r-1)//2]))<=1
    assert len(set(norms[r*(r-1)//2:]))<=1
    if check_idempotence:
        for k in range(m):
            for i in range(m):
                y=sum((cols[j][i]*cols[k][j] for j in range(m)),F(0))
                assert y==cols[k][i],(r,s,'idempotence',i,k)
    return m,m*m if check_idempotence else 0


def main():
    cases=columns=idempotence=0
    for r in range(2,9):
        for s in range(1,9):
            m, checks=direct(r,s,check_idempotence=(r<=4 and s<=4))
            cases+=1;columns+=m;idempotence+=checks
    print('PASS exact rational split-graph cases:',cases)
    print('PASS exact projection columns:',columns)
    print('PASS full idempotence entries:',idempotence)
    for r,s in [(2,1),(2,2),(3,2),(4,3),(5,3),(7,4),(3,8)]:
        print('r=%d s=%d t=%s lambda=%s'%(r,s,candidate_t(r,s),predicted(r,s)))


if __name__=='__main__':main()
