#!/usr/bin/env python3
"""Exact-rational reproducibility checks for matching-augmented biclique Hodge norms.

The unrestricted theorem is proved algebraically in RESULT.md; the checks below
compare its formulas with independent grounded-Laplacian reconstructions.
"""
from fractions import Fraction as F
import sympy as sp


def analytic(m, n, t):
    """Exact claims for m>=4,n>=2,0<=t<=m//2."""
    m, n, t = int(m), int(n), int(t)
    assert m >= 4 and n >= 2 and 0 <= t <= m // 2
    m0, n0 = F(m), F(n)
    q0 = 3 - 2 / m0 - 2 / n0 + 2 / (m0 * n0)
    p0 = 4 * (1 - 1 / m0) * (1 - 1 / n0)
    if m <= n + 2:
        dq = -(n0 - 2) / (n0 * (n0 + 2))
        dp = -(n0 - 4) / (n0 * (n0 + 2))
    else:
        dq = (m0 * n0 - 2 * n0*n0 - 2*n0 + 4) / (m0*n0*(n0+2))
        dp = (m0 - 2*n0 + 2) / (m0*n0)
    if t == 0:
        return q0, p0
    if 2*t < m:
        return q0 + max(F(0), dq), p0 + max(F(0), dp)
    return q0 + dq, p0 + dp


def make_edges(m, n, t):
    return [(2*i,2*i+1) for i in range(t)] + [(i,m+j) for i in range(m) for j in range(n)]


def grounded_columns(m, n, t):
    """Independent pure-rational grounded Laplacian solve for every edge column."""
    N=m+n
    edges=make_edges(m,n,t)
    L=[[0]*N for _ in range(N)]
    for u,v in edges:
        L[u][u]+=1; L[v][v]+=1
        L[u][v]-=1; L[v][u]-=1
    grounded=[list(map(F,row[:-1])) for row in L[:-1]]
    out=[]
    for u,v in edges:
        M=[row+[F((i==u)-(i==v))] for i,row in enumerate(grounded)]
        for i in range(N-1):
            if not M[i][i]:
                k=next(k for k in range(i+1,N-1) if M[k][i]);M[k],M[i]=M[i],M[k]
            z=M[i][i]
            for j in range(i+1,N-1):
                if M[j][i]:
                    y=M[j][i]/z
                    for k in range(i+1,N):
                        M[j][k]-=y*M[i][k]
                    M[j][i]=F(0)
        x=[F(0)]*N
        for i in range(N-2,-1,-1):
            x[i]=(M[i][-1]-sum(M[i][j]*x[j] for j in range(i+1,N-1)))/M[i][i]
        assert all(sum(L[i][j]*x[j] for j in range(N))==F((i==u)-(i==v)) for i in range(N))
        q=sum(abs(x[a]-x[b]) for a,b in edges)
        diag=x[u]-x[v]
        assert 0<diag<1
        out.append((q,q+1-2*diag))
    return max(q for q,p in out),max(p for q,p in out),len(edges)


def symbolic_identities():
    m,n=sp.symbols('m n',positive=True)
    # Potentials of the paired-left -> right cross-edge dipole, up to constants.
    cL=1/(m*(m+n));cR=-1/(n*(m+n))
    V_a=cL+(sp.Rational(1,2)-1/m)/n+1/(2*(n+2))
    V_b=cL+(sp.Rational(1,2)-1/m)/n-1/(2*(n+2))
    V_c=cL-1/(m*n)
    W_1=cR-(1-1/n)/m
    W_0=cR+1/(m*n)
    aw=V_a-W_1; ao=V_a-W_0; bw=V_b-W_1
    bo=V_b-W_0; cw=V_c-W_1; co=V_c-W_0; match=V_a-V_b
    should={
      aw:(m*n+m+n*n+n-2)/(m*n*(n+2)),
      ao:(m*n+m-n-2)/(m*n*(n+2)),
      bw:(m+n*n+n-2)/(m*n*(n+2)),
      bo:(m-n-2)/(m*n*(n+2)),
      cw:(n-1)/(m*n),
      co:-1/(m*n),
      match:1/(n+2)
    }
    for actual,formula in should.items():assert sp.cancel(actual-formula)==0
    q0=3-2/m-2/n+2/(m*n);p0=4*(1-1/m)*(1-1/n)
    for sign in (1,-1):
        qp=sp.factor(aw+(n-1)*ao+bw+sign*(n-1)*bo+(m-2)*cw-(m-2)*(n-1)*co+match)
        pp=sp.factor(qp+1-2*aw)
        if sign == -1:
            dq=-(n-2)/(n*(n+2));dp=-(n-4)/(n*(n+2))
            assert sp.cancel(qp-2*(n+1)/(n+2)-(m-2)*(n-1)/(m*n))==0
            assert sp.cancel(pp-3*n/(n+2)-(n-1)*(m*n+4*m-4*n-8)/(m*n*(n+2)))==0
        else:
            dq=(m*n-2*n*n-2*n+4)/(m*n*(n+2))
            dp=(m-2*n+2)/(m*n)
            assert sp.cancel(qp-2*(n+1)/(n+2)-(n-1)*(m*n+4*m-4*n-8)/(m*n*(n+2)))==0
            assert sp.cancel(pp-3*n/(n+2)-(n-1)*(m*n+6*m-6*n-12)/(m*n*(n+2)))==0
        assert sp.cancel(qp-q0-dq)==0
        assert sp.cancel(pp-p0-dp)==0
    assert sp.cancel((- (n-2)/(n*(n+2))) - ((m*n-2*n*n-2*n+4)/(m*n*(n+2))).subs(m,n+2))==0
    assert sp.cancel((- (n-4)/(n*(n+2))) - ((m-2*n+2)/(m*n)).subs(m,n+2))==0
    # Unpaired cross dipole has no matching-edge currents.
    V_u=cL+(1-1/m)/n;V_o=cL-1/(m*n)
    assert sp.cancel(V_u-W_1-(m+n-1)/(m*n))==0
    assert sp.cancel(V_u-W_0-(m-1)/(m*n))==0
    assert sp.cancel(V_o-W_1-(n-1)/(m*n))==0
    assert sp.cancel(V_o-W_0+1/(m*n))==0


def main():
    symbolic_identities()
    test_count=0; columns=0
    for m in (4,5,6,7,8,9,10,12):
        for n in range(2,11):
            for t in range(0,m//2+1):
                q,p,ec=grounded_columns(m,n,t)
                expected=analytic(m,n,t)
                assert(q,p)==expected,(m,n,t,(q,p),expected)
                test_count+=1;columns+=ec
    # Sharp collective saturation: a final matching edge decreases both norms.
    assert analytic(4,7,0)==analytic(4,7,1)
    assert analytic(4,7,2)[0]<analytic(4,7,1)[0]
    assert analytic(4,7,2)[1]<analytic(4,7,1)[1]
    print(f'MATCHING_SATURATION_HODGE_EXACT_OK graphs={test_count} checked_edge_columns={columns} symbolic_identities=PASS')

if __name__=='__main__':main()
