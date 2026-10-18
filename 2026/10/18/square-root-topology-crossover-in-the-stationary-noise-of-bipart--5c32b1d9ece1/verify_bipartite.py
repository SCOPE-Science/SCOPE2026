"""Exact-rational stationary finite-chain checks for noisy spin copying on complete bipartite networks.
Run: python verify_bipartite.py. Requires standard-library fractions only."""
from fractions import Fraction as F


def solve(A,b):
    N=len(b)
    A=[list(map(F,row))+[F(b[i])] for i,row in enumerate(A)]
    for k in range(N):
        p=next(j for j in range(k,N) if A[j][k]); A[k],A[p]=A[p],A[k]
        t=A[k][k]
        A[k]=[z/t for z in A[k]]
        for i in range(N):
            if i==k:continue
            t=A[i][k]
            if t:
                A[i]=[A[i][j]-t*A[k][j] for j in range(N+1)]
    return [row[-1] for row in A]


def predicted(m,n,e,clock):
    if clock=='vertex': la=lb=F(1)
    else:la,lb=F(n),F(m)
    z=(la/F(n)+lb/F(m))/(la+lb+4*e-la*F(n-1,n)*lb/(lb+2*e)-lb*F(m-1,m)*la/(la+2*e))
    xx=z*la/(la+2*e); yy=z*lb/(lb+2*e)
    N=m+n
    return (F(N)+m*(m-1)*xx+n*(n-1)*yy+2*m*n*z)/N**2,xx,yy,z


def measured(m,n,e,clock):
    states=[(i,j) for i in range(m+1) for j in range(n+1)]
    idx={x:k for k,x in enumerate(states)}
    N=len(states)
    Q=[[F(0) for _ in range(N)] for _ in range(N)]
    for t,(i,j) in enumerate(states):
        if clock=='vertex':
            upa=(m-i)*(e+F(j,n));downa=i*(e+F(n-j,n))
            upb=(n-j)*(e+F(i,m));downb=j*(e+F(m-i,m))
        else:
            upa=(m-i)*(e+j);downa=i*(e+n-j)
            upb=(n-j)*(e+i);downb=j*(e+m-i)
        for target,rate in [((i+1,j),upa),((i-1,j),downa),((i,j+1),upb),((i,j-1),downb)]:
            if rate:
                assert target in idx
                Q[t][idx[target]]+=rate;Q[t][t]-=rate
    A=[[Q[j][i] for j in range(N)] for i in range(N)]
    A[-1]=[F(1)]*N
    b=[F(0)]*(N-1)+[F(1)]
    pi=solve(A,b)
    assert all(t>0 for t in pi)
    assert sum(pi)==1
    assert all(sum(pi[t]*Q[t][j] for t in range(N))==0 for j in range(N))
    mag=[F(2*(i+j)-m-n,m+n) for i,j in states]
    v=sum(p*x*x for p,x in zip(pi,mag))
    # pair correlations from lumped state moments
    x= sum(p*F((2*i-m)**2-m,m*(m-1)) for p,(i,j) in zip(pi,states)) if m>1 else None
    y= sum(p*F((2*j-n)**2-n,n*(n-1)) for p,(i,j) in zip(pi,states)) if n>1 else None
    z= sum(p*F((2*i-m)*(2*j-n),m*n) for p,(i,j) in zip(pi,states))
    return v,x,y,z


def run():
    cases=0
    for m,n in [(1,1),(1,2),(1,3),(2,2),(2,3),(3,3),(1,4),(3,4),(4,2)]:
        for e in [F(1,5),F(1),F(3,2)]:
            for clk in ['vertex','edge']:
                p=predicted(m,n,e,clk)
                q=measured(m,n,e,clk)
                assert q[0]==p[0],(m,n,e,clk,'variance',p,q)
                assert q[3]==p[3],(m,n,e,clk,'cross',p,q)
                if m>1: assert q[1]==p[1],(m,n,e,clk,'within A')
                if n>1: assert q[2]==p[2],(m,n,e,clk,'within B')
                cases+=1
    print('PASS',cases,'full exact rational lumped CTMC stationary checks')
    for e in [F(1,5),F(1),F(3,2)]:
        for c in [F(1,5),F(1),F(3)]:
            # asymptotic check, not a proof
            n=1000000;m=max(1,int(float(c)*n**.5))
            ve=predicted(m,n,e,'edge')[0]; vv=predicted(m,n,e,'vertex')[0]
            ratio=float(ve/vv)
            target=8*(1+float(e))*float(c)**2
            print('asymptotic sample',e,c,'ratio',round(ratio,6),'target',round(target,6))

if __name__=='__main__':run()
