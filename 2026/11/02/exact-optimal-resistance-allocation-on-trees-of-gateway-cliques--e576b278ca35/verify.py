#!/usr/bin/env python3
"""Matrix and constrained-optimization checks of the gateway-clique-tree resistance formula."""
import numpy as np
from scipy.optimize import minimize


def construct(sizes, tree_edges, budget=1.0):
    n=sum(sizes)
    starts=np.cumsum([0]+list(sizes))[:-1]
    graph_edges=[]
    groups=[]
    for i,p in enumerate(sizes):
        base=int(starts[i]); gw=base
        for j in range(1,p):
            graph_edges.append((gw,base+j));groups.append(('spoke',i))
        for j in range(1,p):
            for k in range(j+1,p):
                graph_edges.append((base+j,base+k));groups.append(('internal',i))
    for idx,(i,j) in enumerate(tree_edges):
        graph_edges.append((int(starts[i]),int(starts[j])));groups.append(('bridge',idx))
    # compute cut sizes using tree traversal
    cut_sizes=[]
    for i,j in tree_edges:
        adj={v:[] for v in range(len(sizes))}
        for u,v in tree_edges:
            if {u,v}!={i,j}:adj[u].append(v);adj[v].append(u)
        reached={i};todo=[i]
        for u in todo:
            for v in adj[u]:
                if v not in reached:reached.add(v);todo.append(v)
        cut_sizes.append(sum(sizes[u] for u in reached))
    R=n
    sigma=sum(np.sqrt(p*(n-p+1)/2)+(p-2)*np.sqrt(n/2) for p in sizes)
    sigma+=sum(np.sqrt(s*(n-s)) for s in cut_sizes)
    ratio=budget/sigma
    opt={}
    for i,p in enumerate(sizes):
        b=ratio*np.sqrt(2*(n-p+1)/p)
        lam=ratio*np.sqrt(2*n)
        a=(lam-b)/(p-1)
        opt[('spoke',i)]=b
        opt[('internal',i)]=a
    for i,s in enumerate(cut_sizes):opt[('bridge',i)]=ratio*np.sqrt(s*(n-s))
    weights=np.array([opt[g] for g in groups])
    assert min(weights)>0 and abs(sum(weights)-budget)<1e-10
    incidence=np.zeros((n,len(graph_edges)))
    for k,(i,j) in enumerate(graph_edges):incidence[i,k]=1;incidence[j,k]=-1
    # force matrix to be SPD for any positive weights including optimizer
    red=incidence[:-1]
    def total_resistance(w):
        # grounded inverse Kf=N*tr(L^+) by identity using inverse reduced grounded Laplacian
        G=(red*w)@red.T
        T=np.linalg.inv(G)
        return n*np.trace(T)-np.sum(T)
    at=total_resistance(weights)
    expected=sigma**2/budget
    assert abs(at-expected)<max(1e-7,abs(expected)*1e-10),(sizes,at,expected)
    return weights,expected,total_resistance,graph_edges,groups,sigma

def run():
    cases=[([2,3],[(0,1)]),([2,4,3],[(0,1),(1,2)]),([3,3,3],[(0,1),(1,2)]),([2,2,3,4],[(0,1),(1,2),(1,3)]),([5,2,3,2],[(0,1),(0,2),(2,3)])]
    allchecks=0
    for sizes,tree in cases:
        w,exp,f,es,groups,S=construct(sizes,tree)
        # random independent, positive perturbations around optimizer, normalized budget
        rg=np.random.default_rng(100+sum(sizes))
        for _ in range(50):
            variation=np.exp(rg.normal(scale=.35,size=len(w)))
            guess=w*variation;guess/=sum(guess)
            got=f(guess)
            assert got>=exp-1e-7,(sizes,got,exp)
            allchecks+=1
        # independently optimize all edges on small graphs
        if len(w)<20:
            bounds=[(1e-7,1.0)]*len(w)
            sol=minimize(f,np.full(len(w),1/len(w)),bounds=bounds,constraints=[{'type':'eq','fun':lambda x: np.sum(x)-1}], method='SLSQP', options={'maxiter':400,'ftol':1e-11})
            assert sol.success,(sizes,sol.message)
            assert abs(f(sol.x)-exp)<1e-7,(sizes,f(sol.x),exp)
        print('sizes',sizes,'bridge_tree',tree,'edges',len(w),'R*',round(exp,12),'checks passed')
    print('PASS: 5 direct matrix certificates, 250 asymmetric feasible perturbations, 5 unrestricted SLSQP comparison checks')

if __name__=='__main__':run()
