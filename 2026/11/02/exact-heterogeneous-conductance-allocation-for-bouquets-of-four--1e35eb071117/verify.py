"""Standalone exact and numerical checks for the four-cycle bouquet design formula.
Requires Python 3 and SymPy. Run: python verify.py
"""
from math import sqrt
import random
import sympy as sp


def quartic(e, p, q, t):
    return (e+2)*p*t**4 + 2*(e+2)*p*t**3 + ((3*e+8)*p-(5*e+6)*q)*t*t - 6*e*q*t - 3*e*q


def shape_cost(e, p, q, t):
    return (p*t+q)*((e+2)*t*t + 6*e*t+3*e+8*t)/(t*(t+1))


def positive_root(e, p, q):
    lo, hi = 0., 1.
    while quartic(e,p,q,hi) <= 0:
        hi *= 2.
    for _ in range(160):
        mid = (lo+hi)/2
        if quartic(e,p,q,mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def optimal(k, budget, prices):
    e=3*k-2
    items=[]
    for p,q in prices:
        t=positive_root(e,p,q)
        c=shape_cost(e,p,q,t)
        items.append((p,q,t,c))
    z=sum(sqrt(c) for _,_,_,c in items)
    result=[]
    for p,q,t,c in items:
        b=budget*sqrt(c)/z
        spoke=b/(2*(p+q/t))
        distal=spoke/t
        result.append((spoke,distal,b,t))
    return result,z*z/budget


def laplacian(k, edge_pairs):
    n=3*k+1
    mat=sp.zeros(n,n)
    for a,b,w in edge_pairs:
        mat[a,a]+=w;mat[b,b]+=w
        mat[a,b]-=w;mat[b,a]-=w
    return mat


def make_edges(rates):
    edges=[]
    for j,(u,v) in enumerate(rates):
        a,b,c=3*j+1,3*j+2,3*j+3
        edges += [(0,a,u),(a,b,v),(b,c,v),(c,0,u)]
    return edges


def actual_kirchhoff(k, rates):
    L=laplacian(k,make_edges(rates))
    inv=L[1:,1:].inv()
    n=L.rows
    # Kirchhoff index = n * tr(L^+) = n*tr(L_ground^-1) - 1^T L_ground^-1 1.
    ones=sp.ones(n-1,1)
    return sp.factor(n*sp.trace(inv)-(ones.T*inv*ones)[0])


def formula_kirchhoff(k, rates):
    e=3*k-2
    total=sp.S(0)
    for u,v in rates:
        x,y=1/u,1/v
        total+=sp.factor(y*(4*x+y)/(x+y)+e*(x*(x+2*y)/(x+y)+(x+y)/2))
    return sp.factor(total)


def execute():
    checks=0
    rng=random.Random(1264)
    t,e,p,q=sp.symbols('t e p q',positive=True)
    F=(p*t+q)*((e+2)*t*t+6*e*t+3*e+8*t)/(t*(t+1))
    assert sp.simplify(sp.diff(F,t)-quartic(e,p,q,t)/(t*t*(t+1)**2))==0;checks+=1
    assert sp.simplify(quartic(e,p,p,t)-p*(t+1)**2*((e+2)*t*t-3*e))==0;checks+=1
    # A ratio derivative with nonnegative positive coefficients proves strict monotonicity.
    den=(5*e+6)*t*t+6*e*t+3*e
    # Correct positive shape numerator is (e+2)t4+2(e+2)t3+(3e+8)t2.
    num=(e+2)*t**4+2*(e+2)*t**3+(3*e+8)*t*t
    der=sp.Poly(sp.expand(sp.diff(num,t)*den-num*sp.diff(den,t)),t)
    assert all(all(c>=0 for c in sp.Poly(co,e).all_coeffs()) for co in der.all_coeffs()); checks+=1
    for k in range(1,5):
        for _ in range(13):
            rates=[(sp.Rational(rng.randint(1,8),rng.randint(1,9)),sp.Rational(rng.randint(1,8),rng.randint(1,9))) for j in range(k)]
            assert actual_kirchhoff(k,rates)==formula_kirchhoff(k,rates)
            checks+=1
    for k in range(2,6):
        for _ in range(21):
            prices=[(rng.randint(1,12)/rng.randint(1,8),rng.randint(1,12)/rng.randint(1,8)) for j in range(k)]
            B=rng.randint(1,18)
            res,mn=optimal(k,B,prices)
            assert all(u>0 and v>0 and b>0 and t>0 for u,v,b,t in res);checks+=1
            assert abs(sum(b for _,_,b,_ in res)-B)<1e-10;checks+=1
            assert abs(sum(2*prices[j][0]*res[j][0]+2*prices[j][1]*res[j][1] for j in range(k))-B)<1e-9;checks+=1
            assert abs(float(formula_kirchhoff(k,[(u,v) for u,v,_,_ in res]))/mn-1)<2e-12;checks+=1
            e=3*k-2
            for j,(u,v,b,t) in enumerate(res):
                p,q=prices[j]
                assert abs(quartic(e,p,q,t))<=1e-8*(1+abs((e+2)*p*t**4));checks+=1
                assert abs(t-u/v)<1e-12;checks+=1
    # A numerical stress-test of the unreduced edge set: perturb all edges and compare
    # first-order cost residual at the symmetric optimum, using full matrix inverses.
    import numpy as np
    for k in range(2,5):
        prices=[(1.0+j,2.0/(j+1)) for j in range(k)]
        rates, best=optimal(k,17.0,prices)
        edges=make_edges([(u,v) for u,v,_,_ in rates])
        orig=np.array([float(w) for _,_,w in edges])
        ep=np.array([prices[j][0] if edge_idx in (0,3) else prices[j][1] for j in range(k) for edge_idx in range(4)])
        assert abs(float(actual_kirchhoff(k,[(sp.Float(u),sp.Float(v)) for u,v,_,_ in rates]))-best)<2e-8;checks+=1
        for _ in range(16):
            direction=np.array([rng.uniform(-1,1) for i in range(len(orig))])
            direction-=direction.dot(ep)/(ep.dot(ep))*ep
            h=1e-5
            vals=[]
            for sg in (-1,1):
                trial=orig+sg*h*direction
                ratesfull=[(a,b,sp.Float(w)) for (a,b,_),w in zip(edges,trial)]
                L=laplacian(k,ratesfull)
                inv=L[1:,1:].inv()
                n=3*k+1
                ones=sp.ones(n-1,1)
                vals.append(float(n*sp.trace(inv)-(ones.T*inv*ones)[0]))
            assert abs(vals[1]-vals[0])<1e-6;checks+=1
            assert (vals[0]+vals[1])*0.5>=best-1e-7;checks+=1
    print('PASS:',checks,'exact and numerical assertion groups')


if __name__=='__main__':
    execute()
