"""Independent finite checks of a barbell-graph Wasserstein semigroup formula.
Requires Python 3, numpy, scipy. The analytic theorem is not inferred from tests.
"""
import math
from collections import deque
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog

def graph(m):
    assert m >= 3
    n = 2*m
    edges = [(i,j) for lo in (0,m) for i in range(lo,lo+m)
             for j in range(i+1,lo+m)] + [(0,m)]
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v); adj[v].append(u)
    distances=np.zeros((n,n),float)
    for u in range(n):
        ds=[None]*n; ds[u]=0; queue=deque([u])
        while queue:
            v=queue.popleft()
            for w in adj[v]:
                if ds[w] is None:
                    ds[w]=ds[v]+1; queue.append(w)
        distances[u]=ds
    Q=np.zeros((n,n),float)
    for u,v in edges: Q[u,v]=Q[v,u]=1.
    np.fill_diagonal(Q,-Q.sum(axis=1))
    return Q,distances,edges

def kr_lp(p,q,D):
    """Primal transport LP: no graph-specific KR norm decomposition is used."""
    n=len(p)
    eq=np.zeros((2*n,n*n),float)
    for i in range(n):
        for j in range(n):
            eq[i,i*n+j]=1
            eq[n+j,i*n+j]=1
    b=np.r_[p/p.sum(),q/q.sum()]*1e5
    ans=linprog(D.ravel(),A_eq=eq,b_eq=b,bounds=(0,None),method='highs',options={"presolve": False})
    assert ans.success,ans.message
    return ans.fun/1e5

def quantities(m,t):
    delta=math.sqrt(m*m+4*m-4)
    lo=(m+2-delta)/2
    hi=(m+2+delta)/2
    aa=(delta+5*m-6)/(2*delta)
    bb=(delta-m+4)/(2*delta)
    en=math.exp(-lo*t); ep=math.exp(-hi*t)
    return (aa*en-(aa-1)*ep, bb*en+(1-bb)*ep, math.exp(-m*t))

def peak(m):
    delta=math.sqrt(m*m+4*m-4)
    lo=4/(m+2+delta)
    hi=(m+2+delta)/2
    aa=(delta+5*m-6)/(2*delta)
    t=math.log((aa-1)*hi/(aa*lo))/delta
    return t,aa*math.exp(-lo*t)-(aa-1)*math.exp(-hi*t)

def run():
    tests=0
    for m in (3,4,5,6,8,10):
        Q,D,edges=graph(m)
        for t in (0.0,0.005,0.03,0.13,0.4,0.8,1.2):
            P=expm(Q*t)
            exact=quantities(m,t)
            pairs=((0,m),(0,1),(1,2))
            for i,pr in enumerate(pairs):
                value=kr_lp(P[pr[0]],P[pr[1]],D)
                assert abs(value-exact[i])<2e-9,(m,t,pr,value,exact)
                tests+=1
            vals=[kr_lp(P[u],P[v],D) for u,v in edges]
            assert abs(max(vals)-exact[0])<2e-9
            tests+=1
            if t>0:
                assert exact[0]>exact[1]>exact[2]
                tests+=1
        tt,pp=peak(m)
        assert tt>0 and pp>1
        assert abs((quantities(m,tt)[0]-pp))<1e-12
        for shift in (-0.5,-0.1,0.1,0.5):
            assert quantities(m,max(0.,tt+shift))[0]<pp+1e-12
            tests+=1
        tests+=2
    for m in (30,60,120,400,1000):
        tt,pp=peak(m)
        assert tt>0 and 1<pp<3
        tests+=2
        if m>=400:
            assert abs((3-pp)*m-8)<.6
            tests+=1
            assert abs((tt*m)-(2*math.log(m)-math.log(3)))<.25
            tests+=1
    print('VERIFICATION_OK',tests,'independent LP/heat/predicted-edge/peak/asymptotic checks')
    for m in (3,4,5,10,20,50,100,1000):
        t,p=peak(m)
        print('m=',m,'t_peak=',format(t,'.12g'),'maximum=',format(p,'.12g'))
if __name__=='__main__':run()
