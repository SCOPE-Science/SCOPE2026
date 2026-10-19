"""Reproduce checks for minimax effective-resistance diameter on power-priced spider trees.
Dependencies: Python 3, NumPy and SciPy. All data are generated here deterministically.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.optimize import minimize
from fractions import Fraction


def theorem(arms, prices, exponent, budget):
    """Return optimal edge conductances, radial resistances, and diameter."""
    a=float(exponent)
    S=np.array([sum(float(c)**(1/(a+1)) for c in costs) for costs in prices])
    C=S**(a+1)
    j=int(np.argmax(C))
    other=float(C.sum()-C[j])
    if C[j] > other:
        u=float(C[j]**(1/(a+1)))
        v=float(other**(1/(a+1)))
        r=np.full(len(arms),v/(u+v))
        r[j]=u/(u+v)
        cost_min=(u+v)**(a+1)
    else:
        r=np.full(len(arms),0.5)
        cost_min=2**a*float(C.sum())
    diam=(cost_min/budget)**(1/a)
    R=diam*r
    weights=[(S[i]/R[i])*np.array(prices[i],dtype=float)**(-1/(a+1)) for i in range(len(arms))]
    return weights,R,diam,C,cost_min


def direct_laplacian_diameter(weights):
    n=1+sum(len(w) for w in weights)
    lap=np.zeros((n,n)); leaves=[]
    v=1
    for arm in weights:
        parent=0
        for w in arm:
            lap[parent,parent]+=w; lap[v,v]+=w
            lap[parent,v]-=w; lap[v,parent]-=w
            parent=v; v+=1
        leaves.append(parent)
    pinv=np.linalg.pinv(lap,hermitian=True)
    diam=max(pinv[i,i]+pinv[j,j]-2*pinv[i,j] for i in range(n) for j in range(i+1,n))
    return float(diam)


def numerical_normalized(prices,a):
    # Independent convex optimization on arm-resistance variables: no theorem formula.
    C=np.array([sum(float(c)**(1/(a+1)) for c in costs)**(a+1) for costs in prices])
    m=len(prices)
    pairs=[(i,j) for i in range(m) for j in range(i+1,m)]
    A=np.zeros((len(pairs),m))
    for k,(i,j) in enumerate(pairs):A[k,i]=1;A[k,j]=1
    def cost(x):return float(np.sum(C/x**a))
    def jac(x):return -a*C/x**(a+1)
    from scipy.optimize import LinearConstraint
    con=LinearConstraint(A,-np.inf,np.ones(len(pairs)))
    opt=minimize(cost,np.full(m,0.45),jac=jac,bounds=[(1e-7,1.)]*m,
                 constraints=[con],method='SLSQP',
                 options={'ftol':1e-10,'maxiter':2500})
    return opt


def main():
    count=0
    # Exact rational tests at exponent 1 and perfect square prices.
    for raw in [(1,1,1),(9,1,1),(25,1,1),(4,4,1),(9,4,4)]:
        c=list(map(Fraction,raw))
        Cmax=max(c); total=sum(c)
        if 2*Cmax<=total: q=2*total
        else:
            rest=total-Cmax
            q=(math.isqrt(Cmax.numerator)+math.isqrt(rest.numerator))**2 if rest.denominator==1 and math.isqrt(rest.numerator)**2==rest.numerator else None
        w,R,D,C,_=theorem([1]*len(c),[[int(t)] for t in c],1.,7.)
        assert abs(sum(t*float(g[0]) for t,g in zip(c,w))-7.)<1e-12
        assert abs(max(R[i]+R[j] for i in range(len(c)) for j in range(i+1,len(c)))-D)<1e-11
        if q is not None: assert abs(D-float(q)/7)<1e-12
        count+=3
    rng=np.random.default_rng(194002)
    for i in range(80):
        arms=int(rng.integers(3,7))
        lengths=rng.integers(1,4,size=arms)
        prices=[np.exp(rng.uniform(-1.,1.5,int(L))) for L in lengths]
        a=float(rng.choice([0.3,0.6,1.,1.5,2.5]))
        B=float(np.exp(rng.uniform(-1,2)))
        w,R,D,C,cost=theorem(lengths,prices,a,B)
        assert np.isclose(sum(sum(t*float(g)**a for t,g in zip(cc,ww)) for cc,ww in zip(prices,w)),B,rtol=1e-11)
        count+=1
        assert np.isclose(max(R[i]+R[j] for i in range(arms) for j in range(i+1,arms)),D,rtol=1e-12)
        count+=1
        assert np.isclose(direct_laplacian_diameter(w),D,rtol=1e-8,atol=1e-8)
        count+=1
        # Check deterministic random feasible allocations directly on the graph.
        for k in range(12):
            h=[rng.lognormal(0,1,len(ww)) for ww in w]
            expense=sum(sum(c*x**a for c,x in zip(cc,hh)) for cc,hh in zip(prices,h))
            h=[hh*(B/expense)**(1/a) for hh in h]
            observed=max(sum(1/x for x in h[i])+sum(1/x for x in h[j]) for i in range(arms) for j in range(i+1,arms))
            assert observed>=D-1e-9
            count+=1
        if i < 18:
            result=numerical_normalized(prices,a)
            assert result.success or abs(result.fun-cost)/cost < 2e-6, (i, a, [len(x) for x in prices], result.message, result.fun, cost, result.x)
            assert abs(result.fun-cost)/cost < 2e-6,(result.fun,cost)
            count+=2
    # Sharp exponent transition on uniform-length arms (3,2,2).
    acrit=math.log(2)/math.log(1.5)-1.
    assert 0.7<acrit<0.72
    count+=1
    for a in [0.3,acrit,1.,3.]:
        _,R,D,C,_=theorem([3,2,2],[[1]*3,[1]*2,[1]*2],a,1.)
        if a<acrit-1e-8: assert max(R)-min(R)<1e-11
        if a>acrit+1e-8: assert R[0]>R[1] and abs(R[1]-R[2])<1e-12
        count+=1
    print(f'PASS {count} independent structural, numerical, and matrix tests')

if __name__=='__main__':main()
