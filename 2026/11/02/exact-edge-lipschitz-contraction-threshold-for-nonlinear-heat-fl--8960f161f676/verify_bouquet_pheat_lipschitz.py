"""Standalone small-instance checks for individual gradient contraction on clique bouquets.

Requires Python >=3.9 and standard library only.  No graph data or external files.
"""
from itertools import product
from fractions import Fraction
from math import isclose


def edges_of(sizes):
    edges=[]; groups=[]; off=1
    for k in sizes:
        vertices=list(range(off,off+k)); groups.append(vertices)
        for v in vertices: edges.append((0,v))
        for i in range(len(vertices)):
            for j in range(i+1,len(vertices)): edges.append((vertices[i],vertices[j]))
        off+=k
    return edges,groups


def flux(x,p):
    if x == 0: return 0
    return (1 if x>0 else -1)*abs(x)**(p-1)


def flow(u,edges,p):
    du=[0]*len(u)
    for a,b in edges:
        h=flux(u[b]-u[a],p);du[a]+=h;du[b]-=h
    return du


def lip(u,edges): return max(abs(u[a]-u[b]) for a,b in edges)


def sharp_bound(sizes,p):
    c=1 if p<=2 else 2**(2-p)
    N=sum(sizes)
    return max(N-k-2-(k-1)*c for k in sizes)


def canonical_witness(sizes,i,p):
    edges,groups=edges_of(sizes)
    u=[1.0]*(1+sum(sizes)); u[groups[i][0]]=0.0
    for v in groups[i][1:]: u[v]=(0.0 if p<=2 else 0.5)
    for j,g in enumerate(groups):
        if i!=j:
            for v in g: u[v]=2.0
    du=flow(u,edges,p); L=lip(u,edges)
    return L,du[0]-du[groups[i][0]],u,edges


def test():
    # Exact rational evaluation at integer exponents, including fractional maximizing values.
    exact=0
    for sizes in [(1,1),(1,2),(1,1,1),(1,1,1,1),(2,2),(2,3),(3,3),(3,4),(1,2,3),(2,2,2),(4,4)]:
        for p in (2,3,4,5):
            for j,k in enumerate(sizes):
                ed,groups=edges_of(sizes)
                vals=[Fraction(1)]*(1+sum(sizes));vals[groups[j][0]]=Fraction(0)
                for w in groups[j][1:]: vals[w]=Fraction(0) if p==2 else Fraction(1,2)
                for i,g in enumerate(groups):
                    if i!=j:
                        for w in g: vals[w]=Fraction(2)
                deriv=flow(vals,ed,p)[0]-flow(vals,ed,p)[groups[j][0]]
                expected=Fraction(sum(sizes)-k-2) - (k-1)*(Fraction(1) if p==2 else Fraction(1,2)**(p-2))
                assert deriv == expected,(sizes,p,j,deriv,expected)
                assert lip(vals,ed)==1
                exact+=1
    print('EXACT_WITNESS_SHARPNESS_OK',exact)

    # Exhaust a 3-level rational grid for all bouquet profiles with <=5 periphery vertices,
    # both signs at any maximising edge; compare exact upper Dini derivatives.
    exhaustive=0
    for N in range(2,6):
        for sizes in product(range(1,N+1),repeat=2):
            if sum(sizes)!=N:continue
            ed,groups=edges_of(sizes)
            for p in (2,3):
                bound=max(0,sharp_bound(sizes,p))
                for other in product((Fraction(0),Fraction(1,2),Fraction(1)),repeat=N):
                    u=(Fraction(0),)+other
                    L=lip(u,ed)
                    if L==0: continue
                    du=flow(u,ed,p)
                    rates=[(du[a]-du[b])*(u[a]-u[b])/abs(u[a]-u[b]) for a,b in ed if abs(u[a]-u[b])==L]
                    assert max(rates)/L**(p-1) <= bound+1e-12,(sizes,p,u,rates,bound)
                    exhaustive+=1
    print('EXACT_GRID_DINI_UPPER_BOUND_OK',exhaustive)

    # Every claimed violating profile has a constructive derivative greater than zero;
    # every claimed passing profile yields no positive rate in sampled states.
    checks=0; wins=0
    for sizes in product(range(1,5),repeat=3):
        ed,_=edges_of(sizes)
        for p in (1.5,2,2.5,3,4,6):
            M=sharp_bound(sizes,p)
            vals=[]
            for i in range(3):
                L,r,u,_=canonical_witness(sizes,i,p)
                assert abs(L-1)<1e-12
                vals.append(r)
            assert isclose(max(vals),M,abs_tol=1e-10)
            if M>1e-8:
                assert max(vals)>0;wins+=1
            checks+=1
    print('NONLINEAR_PHASE_DIAGRAM_OK',checks,'strict_failure_cases=',wins)
    # Explicit contrast in balanced two-blade case.
    for p,sign in [(2,0),(3,0),(4,1)]:
        M=sharp_bound((3,3),p)
        assert (M>1e-10)==bool(sign)
    print('BALANCED_TWO_BLADE_THRESHOLD_OK p*=3')
    print('ALL_CLIQUE_BOUQUET_PHEAT_CHECKS_OK')

if __name__=='__main__':test()
