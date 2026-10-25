"""Finite experimental cross-check for sharp linear Lipschitz midpoint extensions.

Run: python verify_simplex_midpoint.py
Uses NumPy and SciPy only for the independent finite-dimensional LP test.
The theorem for arbitrary simplex dimension is proved analytically elsewhere.
"""
import itertools
import math
import numpy as np
from scipy.optimize import linprog


def analytical(n):
    if n == 3:
        delta = 2*(3*math.sqrt(3)-5)
        L = 8-4*math.sqrt(3)
    else:
        delta = (n-1)/(n*math.sqrt(2)+n-2)
        L = 2*math.sqrt(2)*delta
    a = (1+(n-2)*delta)/n
    b = (1-2*delta)/n
    return L,a,b


def pair_dist(n, p, q):
    # Represent a vertex by one unit atom and a midpoint by two half-atoms;
    # for zero-mass differences the Gram norm is squared Euclidean/sqrt(2).
    v = np.zeros(n)
    for i in p: v[i] += 1/len(p)
    for i in q: v[i] -= 1/len(q)
    return math.sqrt(float(v @ v)/2)


def independent_lp(n):
    mids=list(itertools.combinations(range(n),2))
    locs=[(i,) for i in range(n)]+mids
    m=len(mids)
    xvars=m*n
    rows=[]; rhs=[]
    # Symmetrically normalized indicator boundary data are all extreme points
    # of the equilateral Lipschitz unit ball modulo constants.
    data=[np.array(f,dtype=float) for f in itertools.product((0,1),repeat=n)]
    for i,p in enumerate(locs):
        for j in range(i+1,len(locs)):
            q=locs[j]
            dist=pair_dist(n,p,q)
            for f in data:
                r=np.zeros(xvars+1)
                const=0.
                for sign,ind in ((1,i),(-1,j)):
                    if ind<n:const += sign*f[ind]
                    else:r[(ind-n)*n:(ind-n+1)*n] += sign*f
                r[-1]=-dist
                rows.append(r);rhs.append(-const)
    eq=np.zeros((m,xvars+1)); beq=np.ones(m)
    for t in range(m): eq[t,t*n:(t+1)*n]=1
    c=np.zeros(xvars+1);c[-1]=1
    res=linprog(c,A_ub=np.array(rows),b_ub=np.array(rhs),A_eq=eq,b_eq=beq,bounds=[(None,None)]*xvars+[(1,None)],method='highs')
    if not res.success: raise RuntimeError(res.message)
    return res.fun,len(rows)


def orbit_formula(n):
    L,a,b=analytical(n)
    di=a-b
    incidence=abs(1-a)+abs(a)+(n-2)*abs(b)
    nonincident=(abs(1-b)+2*abs(a)+(n-3)*abs(b))/math.sqrt(3)
    common=2*abs(di)
    disjoint=2*math.sqrt(2)*abs(di) if n>=4 else 0
    norms=[1,incidence,nonincident,common,disjoint]
    assert abs(max(norms)-L)<2e-12, (n,L,norms)
    assert a>=0 and b>=0
    return norms


if __name__=='__main__':
    for n in range(3,11):
        L,a,b=analytical(n)
        norms=orbit_formula(n)
        print(f'n={n}: exact-formula numerical check {L:.12f}; weights a={a:.12f}, b={b:.12f}; orbit max={max(norms):.12f}')
    for n in (3,4,5,6):
        L,_,_=analytical(n)
        lp,number=independent_lp(n)
        print(f'n={n}: full unsymmetrized linear program: {number} inequalities, optimum={lp:.12f}')
        assert abs(lp-L)<2e-8,(n,L,lp)
    print('All checks passed.')
