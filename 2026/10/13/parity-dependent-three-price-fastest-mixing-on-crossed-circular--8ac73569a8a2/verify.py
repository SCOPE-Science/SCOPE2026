#!/usr/bin/env python3
"""Independent finite checks for the weighted two-layer cycle spectral-gap theorem.
Requires Python 3 and NumPy. Finite tests do not prove universal optimality.
"""
import itertools
import math
import random
import numpy as np


def data(n):
    mu = 4.0 * math.sin(math.pi/n)**2
    U = 1.0/mu
    B = 4.0 if n%2 == 0 else 4.0*math.cos(math.pi/(2*n))**2
    d = 4.0-B
    z = (1.0-d*U)/(B-d)
    points = {
        'A': (U,0.5,0.0),
        'C': (0.0,(1.0-d*U)/2.0,U),
        'M1': (z,0.0,U-z),
        'M2': (U-0.25,0.0,0.25),
    }
    if n%2: points['D'] = (0.0,0.0,1.0/d)
    return mu,U,B,d,points


def determinant(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def vertices(U,B,d):
    # Each row states a*a_coefficient + b*b_coefficient + c*c_coefficient >= target.
    inequalities = [((1.,0.,1.),U),((0.,2.,4.),1.),((B,2.,d),1.),
                    ((1.,0.,0.),0.),((0.,1.,0.),0.),((0.,0.,1.),0.)]
    result=[]
    for selection in itertools.combinations(inequalities,3):
        M=[list(item[0]) for item in selection]
        rhs=[item[1] for item in selection]
        det=determinant(M)
        if abs(det)<1e-10:continue
        sol=[]
        for k in range(3):
            T=[row.copy() for row in M]
            for j in range(3):T[j][k]=rhs[j]
            sol.append(determinant(T)/det)
        if all(sum(q*x for q,x in zip(coef,sol)) >= bound-1e-8
               for coef,bound in inequalities):
            if not any(max(abs(x-y) for x,y in zip(sol,v))<1e-7 for v in result):
                result.append(tuple(sol))
    return result


def edges(n):
    edges=[]
    for i in range(n):
        j=(i+1)%n
        for layer in (0,1):edges.append((2*i+layer,2*j+layer,'a'))
        edges.append((2*i,2*i+1,'b'))
        edges.append((2*i,2*j+1,'c'))
        edges.append((2*i+1,2*j,'c'))
    assert len(edges)==5*n
    assert len(set(tuple(sorted((p,q))) for p,q,_ in edges))==5*n
    return edges


def gap(n,w):
    L=np.zeros((2*n,2*n),dtype=float)
    for (i,j,_),v in zip(edges(n),w):
        L[i,i]+=v;L[j,j]+=v;L[i,j]-=v;L[j,i]-=v
    eigen=np.linalg.eigvalsh(L)
    assert abs(eigen[0])<1e-8
    return eigen[1],eigen


def formula_eigen(n,a,b,c):
    vals=[]
    for k in range(n):
        nu=4*math.sin(math.pi*k/n)**2
        vals.extend([nu*(a+c), nu*a+(4-nu)*c+2*b])
    return np.asarray(sorted(vals))


def normalize(n,s,t,point):
    a,b,c=point
    J=2*a+t*b+2*s*c
    return a/(n*J), b/(n*J), c/(n*J), 1/(n*J)


def run():
    rng=random.Random(104729)
    tested_vertices=0; costs=0; spectra=0; asymmetric=0; phase=0
    for n in (5,6,7,8,9,10,11,12,15,16):
        mu,U,B,d,expected=data(n)
        actual=vertices(U,B,d)
        assert len(actual)==len(expected),(n,actual,expected)
        for p in expected.values():
            assert any(max(abs(x-y) for x,y in zip(p,q)) <1e-7 for q in actual),(n,p,actual)
            tested_vertices+=1
        for trial in range(85):
            s=10**rng.uniform(-3,1.5);t=10**rng.uniform(-3,1.5)
            costs_expected=[2*a+t*b+2*s*c for a,b,c in expected.values()]
            costs_actual=[2*a+t*b+2*s*c for a,b,c in actual]
            assert abs(min(costs_expected)-min(costs_actual))<1e-7
            costs+=1
            a,b,c=next(v for v in expected.values()
                       if abs((2*v[0]+t*v[1]+2*s*v[2])-min(costs_expected))<1e-8)
            aa,bb,cc,target=normalize(n,s,t,(a,b,c))
            if trial%7==0:
                weights=[{'a':aa,'b':bb,'c':cc}[typ] for _,_,typ in edges(n)]
                observed,eigs=gap(n,weights)
                assert abs(observed-target)<5e-9,(n,s,t,observed,target)
                assert max(abs(eigs-formula_eigen(n,aa,bb,cc)))<5e-9,(n,s,t)
                spectra+=1
            if trial%2==0:
                raw=[rng.expovariate(1.0) for _ in edges(n)]
                prices={'a':1.,'b':t,'c':s}
                budget=sum(x*prices[typ] for x,(_,_,typ) in zip(raw,edges(n)))
                weights=[x/budget for x in raw]
                observed,_=gap(n,weights)
                assert observed <= target+5e-9,(n,s,t,observed,target)
                asymmetric+=1
        # Confirm strict phase claims on interior price points, excluding all tie surfaces.
        sample_prices=[.01,.08,.2,.5,.9,1.1,1.5,3.0]
        for s in sample_prices:
            for t in sample_prices:
                vals={k:2*v[0]+t*v[1]+2*s*v[2] for k,v in expected.items()}
                lowest=min(vals.values())
                winners={k for k,v in vals.items() if abs(v-lowest)<1e-8}
                if s>1 and abs(t-(s-1))>1e-8:
                    assert winners == ({'A'} if t<s-1 else {'M2'}),(n,s,t,winners)
                if s<1 and n%2==0 and abs(t-(1-s))>1e-8:
                    assert winners == ({'C'} if t<1-s else {'M1'}),(n,s,t,winners)
                if s<1 and n%2:
                    crit=d/B
                    if s<crit-1e-9:
                        T=4*s/d
                        if abs(t-T)>1e-8:
                            assert winners == ({'C'} if t<T else {'D'}),(n,s,t,winners)
                    elif s>crit+1e-9:
                        T=4*(1-s)/(B-d)
                        if abs(t-T)>1e-8:
                            assert winners == ({'C'} if t<T else {'M1'}),(n,s,t,winners)
                phase+=1
    print('VERIFY_OK vertices=%d independent_min_costs=%d full_spectra=%d nonsymmetric_budget_comparisons=%d phase_checks=%d' %
          (tested_vertices,costs,spectra,asymmetric,phase))

if __name__=='__main__':run()
