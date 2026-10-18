"""Exact finite-population checks for uniformly permuted fixed-length blocks.

Standard library only. Computes directly enumerated prefix risks, closed formulas,
and exact sufficient inequalities for the universal sharp variance envelope.
"""
from fractions import Fraction as F
from itertools import permutations


def dot(u, v):
    return sum((a*b for a,b in zip(u,v)), F(0))


def sumvec(vecs, d):
    ans=[F(0)]*d
    for u in vecs:
        ans=[a+b for a,b in zip(ans,u)]
    return ans


def mul(c, v):
    return [c*t for t in v]


def risk_by_enumeration(rows, m):
    K=len(rows); b=len(rows[0]); d=len(rows[0][0]); n=K*b
    mu=mul(F(1,n),sumvec([x for block in rows for x in block],d))
    sq=F(0); cnt=0
    for perm in permutations(range(K)):
        pref=[rows[i][j] for i in perm for j in range(b)][:m]
        error=sumvec([[(x-y)/m for x,y in zip(row,mu)] for row in pref],d)
        sq+=dot(error,error)
        cnt+=1
    return sq/cnt


def closed_risk(rows,m):
    K=len(rows);b=len(rows[0]);d=len(rows[0][0]);n=K*b
    q,r=divmod(m,b)
    mu=mul(F(1,n),sumvec([x for block in rows for x in block],d))
    B=[sumvec([[(z-t) for z,t in zip(row,mu)] for row in block],d) for block in rows]
    C=[sumvec([[(z-t) for z,t in zip(row,mu)] for row in block[:r]],d) for block in rows]
    delta=mul(F(1,K),sumvec(C,d))
    C0=[[a-v for a,v in zip(row,delta)] for row in C]
    variance=F(q*(K-q),K-1)*sum(dot(x,x) for x in B)/K
    variance+=sum(dot(x,x) for x in C0)/K
    variance-=F(2*q,K-1)*sum(dot(x,y) for x,y in zip(B,C0))/K
    return (variance+dot(delta,delta))/(m*m)


def rr_risk(rows,m):
    K=len(rows);b=len(rows[0]);d=len(rows[0][0]);n=K*b
    mu=mul(F(1,n),sumvec([x for block in rows for x in block],d))
    sigma=sum(dot([z-t for z,t in zip(row,mu)],[z-t for z,t in zip(row,mu)]) for block in rows for row in block)/n
    return F(n-m,m*(n-1))*sigma


def check_matrix(K,b,q,r):
    """Check strictness of a rank-two matrix via exact principal minors."""
    d=F(r*(b-r),b)
    A=F(q*(K-q)*b,K-1)+F(r*r,b)-F(2*q*r,K-1)
    T=F((q*b+r)*((K-q)*b-r),b*(K-1))
    B2=d*(F(r*r,b)-F(2*q*r,K-1)+F(q*q*b,(K-1)**2))
    det=(T-A)*(T-d)-B2
    if r:
        assert T-A>0 and det>0,(K,b,q,r,T-A,det)
    else:
        assert T-A==0 and B2==0


def run():
    checks=0
    for K in range(2,15):
        for b in range(2,12):
            for m in range(1,K*b):
                q,r=divmod(m,b)
                check_matrix(K,b,q,r);checks+=1
    for K in range(2,6):
        for b in range(2,6):
            d=3
            for seed in range(3):
                rows=[[[F(((i+2)*(j+3)*(z+1)+seed*7)%23-11, (i+2)*(z+2)) for z in range(d)] for j in range(b)] for i in range(K)]
                for m in range(1,K*b):
                    enumerated=risk_by_enumeration(rows,m)
                    closed=closed_risk(rows,m)
                    rr=rr_risk(rows,m)
                    assert enumerated==closed,(K,b,m,seed,enumerated,closed)
                    assert closed<=F(K*b-1,K-1)*rr,(K,b,m,seed,closed,rr)
                    checks+=2
    for K in range(2,12):
        for b in range(2,12):
            # A block-constant contrast shows attainment at any whole-block prefix.
            rows=[[[F(1 if i==0 else (-1 if i==1 else 0))] for j in range(b)] for i in range(K)]
            for q in range(1,K):
                m=q*b
                lhs=closed_risk(rows,m)
                rhs=rr_risk(rows,m)
                assert lhs==F(K*b-1,K-1)*rhs
                checks+=1
    print('OK',checks,'exact checks')

if __name__=='__main__':run()
