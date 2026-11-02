"""Independent numerical and exact checks for optimal priced-cactus tree entropy.
Run: python cactus_candidate_verify.py (requires numpy and scipy).
"""
from fractions import Fraction as F
from itertools import product
import math
import random
import numpy as np
from scipy.optimize import minimize


def cycle_tau(w):
    return sum(math.prod(w[:i]+w[i+1:]) for i in range(len(w)))

def grounded_tree(edges, w, n):
    lap=[[F(0) for _ in range(n)] for _ in range(n)]
    for (u,v), z in zip(edges,w):
        lap[u][u]+=z; lap[v][v]+=z
        lap[u][v]-=z; lap[v][u]-=z
    a=[row[:-1] for row in lap[:-1]]
    ans=F(1)
    for i in range(n-1):
        j=next(j for j in range(i,n-1) if a[j][i])
        if i!=j:
            a[i],a[j]=a[j],a[i];ans=-ans
        p=a[i][i]; ans*=p
        for k in range(i+1,n-1):
            f=a[k][i]/p
            for c in range(i,n-1):a[k][c]-=f*a[i][c]
    return ans

def graph():
    # C3 at 0, bridge (2,3), C4 at 3, bridge (6,7), C5 at 7.
    cycles=[[(0,1),(1,2),(2,0)],[(3,4),(4,5),(5,6),(6,3)],
            [(7,8),(8,9),(9,10),(10,11),(11,7)]]
    bridges=[(2,3),(6,7)]
    edges=bridges+[e for c in cycles for e in c]
    groups=[[edges.index(e) for e in cyc] for cyc in cycles]
    return edges,groups,bridges,12

def solve_cycle(prices,budget):
    k=len(prices);prices=np.asarray(prices,float)
    dominant=np.flatnonzero(prices>=np.sum(prices)-prices-1e-12)
    if len(dominant):
        w=budget/((k-1)*prices)
        w[int(dominant[0])]=0.0
        # The nonzero prices each spend budget/(k-1).
        return w
    def f(x):
        w=x/prices
        t=cycle_tau(list(w))
        return -math.log(t) if t>0 else 1e30
    def jac(x):
        w=x/prices; inv=1/w; tot=sum(inv)
        return -(inv-inv*inv/tot)/prices
    result=minimize(f,np.ones(k)*budget/k,jac=jac,bounds=[(1e-13,budget)]*k,
                    constraints=[{'type':'eq','fun':lambda x:sum(x)-budget,
                                  'jac':lambda x:np.ones(k)}],
                    method='SLSQP',options={'ftol':1e-13,'maxiter':1200})
    assert result.success, (prices,budget,result.message)
    return result.x/prices


def main():
    # A complete exact 7-vertex worked design, independently checking the claimed determinant.
    eg=[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,6),(6,3)]
    wg=[F(1),F(1),F(0),F(1,4),F(6,7),F(6,7),F(6,7),F(3,14)]
    pg=[F(1),F(1),F(3),F(4),F(1),F(1),F(1),F(2)]
    assert sum(x*y for x,y in zip(pg,wg)) == 6
    assert grounded_tree(eg,wg,7)==F(27,98)
    rng=random.Random(151349)
    edges,groups,bridges,n=graph()
    # Independent Kirchhoff determinants versus block factorization on rational inputs.
    for _ in range(28):
        w=[F(rng.randrange(1,19),rng.randrange(1,15)) for e in edges]
        det=grounded_tree(edges,w,n)
        pred=math.prod(w[edges.index(e)] for e in bridges)
        for g in groups:pred*=cycle_tau([w[i] for i in g])
        assert det==pred
    # Single-cycle price phase and exact closed form, including the threshold.
    for k in range(3,9):
        for tau in (F(1,3),F(1,1),F(k-1,2),F(k-1,1),F(k,1),F(2*k,1)):
            budget=F(7,3)
            if tau>=k-1:
                a=budget/(k-1);b=F(0)
            else:
                a=(k-2)*budget/((k-1)**2-tau)
                b=budget*(k-1-tau)/(tau*((k-1)**2-tau))
            assert (k-1)*a+tau*b==budget
            assert b==0 if tau>=k-1 else b>0
            costs=[float(x) for x in [F(1)]*(k-1)+[tau]]
            v=solve_cycle(costs,float(budget))
            ref=[float(a)]*(k-1)+[float(b)]
            assert max(abs(x-y) for x,y in zip(v,ref))<1e-5,(k,tau,v,ref)
    # Cactus global optimum and KKT/direct determinant against asymmetric designs.
    for rep in range(50):
        prices=np.array([rng.uniform(.3,6) for _ in edges]);budget=rng.uniform(2,20)
        if rep%5==0:
            g=groups[rep%3];j=g[rep%len(g)]
            prices[j]=sum(prices[h] for h in g if h!=j)*rng.choice([1,1.01,1.5,3])
        if rep%5==1:
            g=groups[rep%3];j=g[rep%len(g)]
            prices[j]=sum(prices[h] for h in g if h!=j)*.99
        w=np.zeros(len(edges));base=budget/(n-1)
        for edge in bridges:w[edges.index(edge)]=base/prices[edges.index(edge)]
        for g in groups:
            w[g]=solve_cycle(prices[g],len(g)-1 and (len(g)-1)*base)
            predicted=[i for i in g if prices[i]>=sum(prices[j] for j in g if i!=j)-1e-10]
            assert len(predicted)<=1
            assert [i for i in g if w[i]<1e-10]==predicted
            assert abs(sum(prices[g]*w[g])-(len(g)-1)*base)<2e-6
        assert abs(sum(prices*w)-budget)<2e-6
        for _ in range(18):
            x=np.array([rng.expovariate(1) for _ in edges]);x*=budget/sum(x*prices)
            Lstar=float(grounded_tree(edges,[F.from_float(float(v)) for v in w],n))
            Lx=float(grounded_tree(edges,[F.from_float(float(v)) for v in x],n))
            assert Lstar>=Lx*(1-1e-8),(rep,Lstar,Lx)
    print('VERIFIED: 28 exact 12-vertex determinant factorizations; 36 exact price-law cycles; 50 cactus optima; 900 asymmetric comparisons.')

if __name__=='__main__':main()
