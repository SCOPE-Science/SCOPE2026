#!/usr/bin/env python3
"""Exact and numerical tests for the balanced-double-star hitting-time theorem."""
import math
import random
from fractions import Fraction
import numpy as np


def optimum(m, P, Q, R, B):
    assert m>=2 and min(P,Q,R,B)>0
    N=2*m+2
    H=max(P,Q); L=min(P,Q)
    S=math.sqrt(m*L)+math.sqrt(R*(m+1))
    threshold=(N-1)*(math.sqrt(L)+math.sqrt(R*(m+1)/m))**2
    if H <= (N-1)*L:
        W=math.sqrt(m*N*(H+L))+math.sqrt(R*(m+1))
        x=y=W/B*math.sqrt(m*(H+L)/N)
        z=W/B*math.sqrt(R/(m+1))
        T=W**2/B
        regime='equal'
    elif H < threshold:
        W=math.sqrt(m*H*(N-1))+math.sqrt(m*L)+math.sqrt(R*(m+1))
        x=W/B*math.sqrt(m*H/(N-1))
        y=W/B*math.sqrt(m*L)
        z=W/B*math.sqrt(R/(m+1))
        T=W**2/B
        regime='cross'
    else:
        C=m*H+S**2
        x=C/B
        y=x*math.sqrt(m*L)/S
        z=x*math.sqrt(R/(m+1))/S
        T=N*x
        regime='mixed'
    if P>=Q:
        return 1/x,1/y,1/z,T,regime
    return 1/y,1/x,1/z,T,regime


def objective(m,a,b,c):
    n=2*m+2
    x,y,z=1/a,1/b,1/c
    return max(n*x,n*y,x+(n-1)*y+(m+1)*z,(n-1)*x+y+(m+1)*z)


def edges(m):
    # vertices: first hub 0, second hub 1, left leaves 2,...,m+1; right leaves m+2,...,2m+1
    return [(0,k) for k in range(2,m+2)]+[(1,k) for k in range(m+2,2*m+2)]+[(0,1)]


def hit_ctmc_exact(m,wa,wb,wc):
    import sympy as s
    n=2*m+2; ed=edges(m)
    rates=[s.Rational(wa)]*m+[s.Rational(wb)]*m+[s.Rational(wc)]
    L=s.zeros(n)
    for (u,v),w in zip(ed,rates):
        L[u,u]+=w;L[v,v]+=w;L[u,v]-=w;L[v,u]-=w
    out=[]
    for target in range(n):
        inds=[i for i in range(n) if i!=target]
        ht=L.extract(inds,inds).inv()*s.ones(n-1,1)
        out.extend(list(ht))
    return max(out)


def graph_objective(m,rates):
    # formula on tree: per oriented edge, source-side component cardinality divided by the edge rate
    import collections
    n=2*m+2; ed=edges(m)
    adj=[[] for _ in range(n)]
    for j,(u,v) in enumerate(ed):
        adj[u].append((v,j));adj[v].append((u,j))
    def ht(i,t):
        parent={i:None}; stack=[i]
        while stack:
            u=stack.pop()
            for v,j in adj[u]:
                if v not in parent:
                    parent[v]=(u,j);stack.append(v)
        path=[];v=t
        while v!=i:
            u,j=parent[v];path.append((u,v,j));v=u
        ans=0
        for u,v,j in path:
            # count component of source i after edge removed: because oriented path i->t, it is side with u
            seen={u}; todo=[u]
            while todo:
                cur=todo.pop()
                for w,k in adj[cur]:
                    if k==j or w in seen:continue
                    seen.add(w);todo.append(w)
            ans+=len(seen)/rates[j]
        return ans
    return max(ht(i,j) for i in range(n) for j in range(n) if i!=j)


def check_dual(m, P, Q, R, B):
    N=2*m+2; H=max(P,Q); L=min(P,Q)
    S=math.sqrt(m*L)+math.sqrt(R*(m+1))
    H1=(N-1)*L
    H2=(N-1)*S*S/m
    if H<=H1:
        theta=(N*H/(H+L)-1)/(N-2)
        alpha=1+(N-2)*theta
        beta=N-1-(N-2)*theta
        gamma=m+1
    elif H<=H2:
        alpha,beta,gamma=N-1,1,m+1
    else:
        tau=(m*H-(N-1)*S*S)/(m*H+S*S)
        alpha,beta,gamma=N-1+tau,1-tau,(m+1)*(1-tau)
    assert min(alpha,beta,gamma)>0
    lower=(math.sqrt(m*H*alpha)+math.sqrt(m*L*beta)+math.sqrt(R*gamma))**2/B
    got=optimum(m,P,Q,R,B)[3]
    assert abs(lower/got-1)<2e-11,(m,P,Q,R,B,lower,got)
    return True


def trial_numeric(m,P,Q,R,B):
    a,b,c,T,_=optimum(m,P,Q,R,B)
    assert abs((m*P*a+m*Q*b+R*c)/B-1)<1e-11
    assert abs(objective(m,a,b,c)/T-1)<1e-11
    # full unrestriced optimization in reciprocal variables
    n=2*m+2; ed=edges(m)
    prices=np.array([P]*m+[Q]*m+[R],float)
    def loss(logw):
        ww=np.exp(logw); return graph_objective(m,ww)
    def constr(logw):
        return B-np.dot(prices,np.exp(logw))
    # classwise candidate plus perturbations; note objective is nonsmooth
    start=np.log(np.array([a]*m+[b]*m+[c]))
    for _ in range(12):
        perturb=np.exp(np.random.normal(0,0.8,2*m+1)); w=np.exp(start)*perturb
        w*=B/(prices@w)
        val=graph_objective(m,w)
        assert val >= T*(1-2e-10), (m,P,Q,R,B,T,val)
    return True


def main():
    random.seed(3601);np.random.seed(3601)
    exact=0; cases=0; boundaries=0
    for m in range(2,5):
        for aa,bb,cc in [(1,1,1),(2,3,5),(7,2,4),(3,11,2)]:
            h=hit_ctmc_exact(m,aa,bb,cc)
            formula=objective(m,aa,bb,cc)
            assert h==Fraction(formula).limit_denominator(10**6), (m,aa,bb,cc,h,formula)
            exact+=1
    for m in range(2,8):
        for _ in range(120):
            P=math.exp(random.uniform(-4,6));Q=math.exp(random.uniform(-4,4))
            R=math.exp(random.uniform(-5,5));B=math.exp(random.uniform(-3,4))
            trial_numeric(m,P,Q,R,B);check_dual(m,P,Q,R,B);cases+=1
        for R in (0.1,1,3,30):
            Q=1;N=2*m+2
            H1=(N-1)*Q
            H2=(N-1)*(math.sqrt(Q)+math.sqrt(R*(m+1)/m))**2
            for H in (H1,H2):
                low=optimum(m,H*(1-1e-10),Q,R,1)
                high=optimum(m,H*(1+1e-10),Q,R,1)
                assert abs(low[3]/high[3]-1)<3e-9
                boundaries+=1
    print(f'PASS: {exact} exact rational CTMC systems, {cases} randomized full-edge comparisons and dual certificates, {boundaries} phase-boundary continuity tests')

if __name__=='__main__': main()
