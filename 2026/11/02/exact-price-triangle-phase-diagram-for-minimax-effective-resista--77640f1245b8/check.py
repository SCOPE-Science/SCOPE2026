"""Reproducible numerical and exact tests for priced resistance-diameter design on double stars.

Requires Python 3 and numpy; scipy is used only for the optional independent optimizer tests.
The tests corroborate, but do not replace, the analytic proof.
"""
from fractions import Fraction
from math import sqrt, isclose
import random
import numpy as np


def closed_form(p, q, a, b, c, budget):
    assert p >= 2 and q >= 2 and min(a, b, c, budget) > 0
    A, D, C = p*a, q*b, c
    U, V, W = sqrt(A), sqrt(D), sqrt(C)
    if U > V + W:
        x, y, z = 0.5, V/(2*(V+W)), W/(2*(V+W))
        branch = 'left_cap'
    elif V > U + W:
        x, y, z = U/(2*(U+W)), 0.5, W/(2*(U+W))
        branch = 'right_cap'
    else:
        s = U+V+W
        x, y, z = U/s, V/s, W/s
        branch = 'triangle'
    F = A/x + D/y + C/z
    return np.r_[np.repeat(budget/(F*x), p), np.repeat(budget/(F*y), q), budget/(F*z)], F/budget, branch, (x,y,z), F


def graph(p,q):
    # Vertex 0 is left hub, vertex 1 right hub.
    edges=[(0,2+i) for i in range(p)]+[(1,2+p+j) for j in range(q)]+[(0,1)]
    return edges,p+q+2


def numeric_effective_resistance_diameter(p,q,weights):
    edges,n=graph(p,q)
    L=np.zeros((n,n))
    for (i,j),w in zip(edges,weights):
        L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
    # Invert nonsingular grounded Laplacian instead of using the unique tree-path formula.
    H=np.linalg.inv(L[1:,1:])
    rmax=0.
    for i in range(n):
        for j in range(i+1,n):
            def ix(k): return k if k < 1 else k-1
            if i == 1:
                R=H[ix(j),ix(j)]
            elif j == 1:
                R=H[ix(i),ix(i)]
            else:
                ii=ix(i); jj=ix(j)
                R=H[ii,ii]+H[jj,jj]-2*H[ii,jj]
            rmax=max(rmax,R)
    return rmax


def path_diameter(p,q,weights):
    u=1/weights[:p]
    v=1/weights[p:p+q]
    bridge=1/weights[-1]
    return max(sum(sorted(u)[-2:]), sum(sorted(v)[-2:]),max(u)+max(v)+bridge)


def check_exact_rational_examples():
    # The normalized resistances and the objective are rational when cost square roots are integral.
    cases=[(9,4,Fraction(1),Fraction(1),Fraction(1)),
           (16,4,Fraction(1),Fraction(1),Fraction(1)),
           (4,16,Fraction(1),Fraction(1),Fraction(1)),
           (4,4,Fraction(1),Fraction(1),Fraction(36)),
           (4,4,Fraction(9),Fraction(1),Fraction(1))]
    for p,q,a,b,c in cases:
        A, D, C=p*a,q*b,c
        def sqt(v):
            import math
            s=math.isqrt(v.numerator);t=math.isqrt(v.denominator)
            assert s*s==v.numerator and t*t==v.denominator
            return Fraction(s,t)
        U,V,W=map(sqt,(A,D,C))
        if U>V+W:
            x,y,z=Fraction(1,2), V/(2*(V+W)), W/(2*(V+W))
        elif V>U+W:
            x,y,z=U/(2*(U+W)),Fraction(1,2),W/(2*(U+W))
        else:
            x,y,z=U/(U+V+W),V/(U+V+W),W/(U+V+W)
        F=A/x+D/y+C/z
        assert max(2*x,2*y,x+y+z)==1
        assert F>0
        assert (A/x+D/y+C/z)==F
    return len(cases)


def main():
    rng=random.Random(351927)
    exact=check_exact_rational_examples()
    matrix_checks=0
    strict_feasible_comparisons=0
    regime_counts={'triangle':0,'left_cap':0,'right_cap':0}
    for k in range(225):
        p=rng.randint(2,7);q=rng.randint(2,7)
        a=10**rng.uniform(-1.5,1.5);b=10**rng.uniform(-1.5,1.5)
        c=10**rng.uniform(-1.5,1.5); budget=10**rng.uniform(-1,2)
        weights,val,branch,normal,F=closed_form(p,q,a,b,c,budget)
        regime_counts[branch]+=1
        assert abs(p*a*weights[0]+q*b*weights[p]+c*weights[-1]-budget)<1e-9*budget
        assert abs(path_diameter(p,q,weights)-val)<1e-9*val
        value2=numeric_effective_resistance_diameter(p,q,weights)
        assert abs(value2-val)<5e-9*val,(k,value2,val)
        matrix_checks+=1
        # All nonsymmetric competitors are normalized to their own linear budget.
        for j in range(65):
            raw=np.array([10**rng.uniform(-1.5,1.5) for _ in weights])
            raw*=budget/(a*sum(raw[:p])+b*sum(raw[p:p+q])+c*raw[-1])
            comp=path_diameter(p,q,raw)
            assert comp>=val*(1-5e-10),(k,j,comp,val)
            strict_feasible_comparisons+=1
    # Boundary and phase cases from exact radical identities:
    w,t,b,xyz,F=closed_form(9,4,1,1,1,14)
    assert b=='triangle' and isclose(xyz[0],0.5)
    for p,q,c,expected in [(16,4,1,'left_cap'),(4,16,1,'right_cap'),(9,4,1,'triangle'),(4,4,36,'triangle')]:
        assert closed_form(p,q,1,1,c,p+q+c)[2]==expected
    slsqp_cases=0
    try:
        from scipy.optimize import minimize
        for k in range(54):
            p=rng.randint(2,5);q=rng.randint(2,5)
            a=10**rng.uniform(-1,1);b=10**rng.uniform(-1,1);c=10**rng.uniform(-1,1)
            budget=3.
            w,expected,_,_,_=closed_form(p,q,a,b,c,budget)
            edges,n=graph(p,q)
            n_edges=len(edges)
            paths=[]
            # For any two vertices, locate the unique path via adjacency BFS.
            adj=[[] for _ in range(n)]
            for ei,(u,v) in enumerate(edges):
                adj[u].append((v,ei));adj[v].append((u,ei))
            for src in range(n):
                for dst in range(src+1,n):
                    seen={src};queue=[(src,[])]
                    for node,path in queue:
                        if node==dst:
                            row=np.zeros(n_edges)
                            row[path]=1
                            paths.append(row)
                            break
                        for nb,ei in adj[node]:
                            if nb not in seen:
                                seen.add(nb);queue.append((nb,path+[ei]))
            paths=np.array(paths)
            prices=np.array([a]*p+[b]*q+[c])
            # Independent optimization in the physical reciprocal resistance variables,
            # minimizing the paid conductance for a maximum pair resistance of 1.
            def f(r): return float(np.sum(prices/r))
            def jac(r): return -prices/(r*r)
            initial=np.full(n_edges,0.25)
            res=minimize(f,initial,jac=jac,method='SLSQP',
                constraints=[{'type':'ineq','fun':lambda r: 1-paths@r,
                              'jac':lambda r:-paths}],
                bounds=[(1e-6,1.0)]*n_edges,
                options={'ftol':1e-10,'maxiter':700})
            # A failed optimizer is not evidence of mathematical failure or optimality.
            assert res.success, (k,res.message)
            objective=expected*budget
            assert abs(res.fun-objective)<1e-5*max(1,objective),(k,res.fun,objective)
            slsqp_cases+=1
    except ImportError:
        print('SciPy not installed; independent optimizer cases were not run')
    print('Exact rational branch/boundary cases:',exact)
    print('Independent grounded-Laplacian resistance comparisons:',matrix_checks)
    print('Asymmetric feasible allocation inequalities:',strict_feasible_comparisons)
    print('Independent full-dimensional numerical minimizations:',slsqp_cases)
    print('Regime sample counts:',regime_counts)
    print('All implemented checks passed; infinite-domain proof is analytic.')

if __name__=='__main__':main()
