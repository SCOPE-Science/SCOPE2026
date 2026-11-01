"""Numerical and combinatorial checks for the circle Rips onset theorem."""
from itertools import combinations
from math import comb
import numpy as np
from numpy.polynomial.legendre import leggauss
from numpy.polynomial.chebyshev import Chebyshev


def graph_edges(positions, radius):
    n=len(positions)
    return {(i,j) for i in range(n) for j in range(i+1,n)
            if min(abs(positions[i]-positions[j]),1-abs(positions[i]-positions[j])) <= radius+1e-12}

def cycle_edges(n):
    return {(min(i,(i+1)%n),max(i,(i+1)%n)) for i in range(n)}

def is_chordal_component(edges,n):
    # Verify absence of induced cycles of length >=4 by brute force on all subsets.
    adj={i:set() for i in range(n)}
    for i,j in edges:adj[i].add(j);adj[j].add(i)
    for m in range(4,n+1):
        for subset in combinations(range(n),m):
            deg=[len(adj[i].intersection(subset)) for i in subset]
            if all(d==2 for d in deg):
                seen={subset[0]};stack=[subset[0]]
                while stack:
                    i=stack.pop()
                    for j in adj[i].intersection(subset):
                        if j not in seen:seen.add(j);stack.append(j)
                if len(seen)==m:return False
    return True


def test_exact_topology():
    rng=np.random.default_rng(15129)
    checked=0
    for n in range(4,9):
        for case in range(160):
            r=(1+rng.uniform(0.0005,0.999)/(n-1))/n
            if case%2:
                gaps=r-rng.dirichlet(np.ones(n))*(n*r-1)
            else:
                gaps=rng.dirichlet(np.ones(n))
            assert abs(sum(gaps)-1)<1e-10
            pos=np.cumsum([0]+gaps.tolist())[:-1]
            edges=graph_edges(pos,r)
            if max(gaps)<=r:
                assert edges==cycle_edges(n),(n,r,gaps,edges)
            else:
                assert is_chordal_component(edges,n),(n,r,gaps,edges)
            checked+=1
    return checked


def trig_coeff(n,k,eps,nt=32768):
    t=(np.arange(nt)+.5)/nt
    p=np.ones(nt)
    for j in range(n):p*=1+eps*np.cos(2*np.pi*k*(t+j/n))
    return p.mean()


def conditional_integral(n,h,eps,k=1,points=12,theta_points=128):
    if n>5: raise ValueError('quadrature reserved for n <= 5')
    nodes,basew=leggauss(points)
    nodes=(nodes+1)*.5
    basew=basew*.5
    theta=(np.arange(theta_points)+.5)/theta_points
    out=0.
    # weighted stick breaking quadrature for Dirichlet(1,...,1)
    for idx in np.ndindex(*([points]*(n-1))):
        v=np.zeros(n)
        left=1.;wt=1.
        for j,ii in enumerate(idx):
            x=nodes[ii];dim=n-1-j
            wt*=basew[ii]*dim*(1-x)**(dim-1)
            v[j]=left*x;left*=1-x
        v[-1]=left
        c=np.cumsum(v)
        p=np.ones_like(theta)
        for j in range(n):
            offset=j/n+h*(j/n-(c[j-1] if j else 0.))
            p*=1+eps*np.cos(2*np.pi*k*(theta+offset))
        out+=wt*p.mean()
    return out


def second_coefficient(n,eps,k=1,nt=32768):
    t=(np.arange(nt)+.5)/nt
    arr=[];fst=[];snd=[]
    for j in range(n):
        a=2*np.pi*k*(t+j/n)
        arr.append(1+eps*np.cos(a))
        fst.append(-eps*2*np.pi*k*np.sin(a))
        snd.append(-eps*(2*np.pi*k)**2*np.cos(a))
    out=np.zeros(nt)
    for j in range(1,n):
        for ell in range(1,n):
            cov=min(j,ell)*(n-max(j,ell))/(n*n*(n+1))
            p=np.ones(nt)
            for i in range(n):
                if i==j==ell:p*=snd[i]
                elif i==j or i==ell:p*=fst[i]
                else:p*=arr[i]
            out+=0.5*cov*p
    return out.mean()


def run():
    num=test_exact_topology()
    print('TOPOLOGY_OK',num)
    for n in range(4,10):
        for k in [1,2,n,n+1]:
            e=.47;v=trig_coeff(n,k,e)
            # Resonance occurs exactly when the frequency is divisible by n.
            assert (v<1-1e-6 if k%n else v>1+1e-6),(n,k,v)
            if np.gcd(n,k)==1:
                formula=2**(1-n)*e**n*Chebyshev.basis(n)(1/e)
                assert abs(v-formula)<1e-10,(n,k,v,formula)
    print('FOURIER_OK',24)
    for n in [4,5]:
        e=.4;k=1
        C=trig_coeff(n,k,e)
        D=second_coefficient(n,e,k)
        data=[]
        for h in [.12,.07,.035]:
            direct=conditional_integral(n,h,e,k,points=(14 if n==4 else 9),theta_points=128)
            residue=(direct-C-D*h*h)/h**3
            assert abs(residue)<20,(n,h,direct,C,D,residue)
            data.append((h,round(direct,10),round(C+D*h*h,10),round(residue,7)))
        print('SECOND_ORDER_OK',n,round(C,9),round(D,9),data)
    print('VERIFY_OK')

if __name__=='__main__':run()
