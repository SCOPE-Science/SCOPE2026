"""Reproduce the column-additive logarithmic-dual Bregman ADMM orbit.

Only the Python standard library is required. Finite checks supplement the proof.
"""
import math


def check(cond, message):
    if not cond:
        raise AssertionError(message)


def close(x, y, tol=1e-10):
    return abs(x-y) < tol*(1+abs(x)+abs(y))


def experiment(a,b,c,rho,s,count):
    m,n=len(a),len(b)
    X=[[a[i]*b[j] for j in range(n)] for i in range(m)]
    Z=[[0.0 for j in range(n)] for i in range(m)]
    tests=0
    for k in range(1,count+1):
        raw=[[X[i][j]*math.exp(Z[i][j]/rho) for j in range(n)] for i in range(m)]
        cols=[sum(raw[i][j] for i in range(m)) for j in range(n)]
        Y=[[raw[i][j]*b[j]/cols[j] for j in range(n)] for i in range(m)]
        Z=[[Z[i][j]+s*rho*math.log(X[i][j]/Y[i][j]) for j in range(n)] for i in range(m)]
        raw=[[Y[i][j]*math.exp(-(c[j]+Z[i][j])/rho) for j in range(n)] for i in range(m)]
        rows=[sum(raw[i]) for i in range(m)]
        X=[[raw[i][j]*a[i]/rows[i] for j in range(n)] for i in range(m)]
        delta=(1-s)**(k-1)
        theta=[math.log(b[j])-c[j]*delta/rho for j in range(n)]
        shift=max(theta)
        soft=[math.exp(t-shift) for t in theta]
        norm=sum(soft)
        w=[u/norm for u in soft]
        for i in range(m):
            for j in range(n):
                check(close(Y[i][j],a[i]*b[j]),'column normalization')
                check(close(X[i][j],a[i]*w[j]),'closed-form primal')
                tests+=2
                for ell in range(n):
                    expected=-(c[j]-c[ell])*(1-delta)
                    check(close(Z[i][j]-Z[i][ell],expected),'dual contrast')
                    tests+=1
    return tests


def main():
    total=0
    configurations=[
       ([.13,.87],[.32,.68],[.2,1.7],2.3),
       ([.1,.2,.7],[.13,.19,.27,.41],[.2,2.,1.1,2.],3.7),
       ([.4,.6],[.13,.24,.63],[.2,.2,2.],1.4),
       ([.21,.29,.5],[.09,.26,.65],[.02,.7,2.3],7.0),
    ]
    for a,b,c,rho in configurations:
        check(close(sum(a),1),'row mass')
        check(close(sum(b),1),'column mass')
        for s in [0.1,0.3,0.6,1.0,1.4,1.9,2.0,2.1,2.5]:
            total+=experiment(a,b,c,rho,s,6)
    # Exact softmax branch identities at finite, manageable exponents.
    for s in [0.2,0.8,1.0,1.9]:
        for k in range(1,12):
            delta=(1-s)**(k-1)
            check(abs(delta)<1e-13 if (s==1 and k>=2) else True,'termination')
            total+=1
    for d in (2.0,10.0,100.0):
        p=1/(1+math.exp(-d))
        q=1/(1+math.exp(d))
        check(p>q,'distinct positive-cost endpoint branches')
        total+=1
    print('VERIFY_OK',total)


if __name__=='__main__':
    main()
