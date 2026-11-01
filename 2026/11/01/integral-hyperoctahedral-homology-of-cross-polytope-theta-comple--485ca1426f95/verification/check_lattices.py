#!/usr/bin/env python3
"""Finite-field invariant-space check for root and weight lattices."""
def modrank(rows,p):
    if not rows:return 0
    a=[[z%p for z in row] for row in rows]; m=len(a); n=len(a[0]); i=0
    for j in range(n):
        piv=next((t for t in range(i,m) if a[t][j]),None)
        if piv is None:continue
        a[i],a[piv]=a[piv],a[i]
        r=pow(a[i][j],-1,p)
        a[i]=[v*r%p for v in a[i]]
        for t in range(m):
            if t!=i and a[t][j]:
                z=a[t][j]
                a[t]=[(v-z*w)%p for v,w in zip(a[t],a[i])]
        i+=1
        if i==m:break
    return i

def invariants(n,p,kind):
    d=n-1; constraints=[]
    for a in range(n-1):
        perm=list(range(n));perm[a],perm[a+1]=perm[a+1],perm[a]
        matrix=[[0]*d for _ in range(d)]
        for j in range(d):
            if kind=='root':
                u=[0]*n;u[j]=1;u[n-1]=-1
                y=[0]*n
                for v,val in enumerate(u):y[perm[v]]=val
                col=y[:d]
            else:
                i=perm[j]
                col=[0]*d
                if i<n-1:col[i]=1
                else:col=[-1]*d
            for i in range(d):matrix[i][j]=col[i]-(1 if i==j else 0)
        constraints.extend(matrix)
    return d-modrank(constraints,p)

for n in range(3,11):
    p=next(p for p in range(2,n+1) if n%p==0 and all(p%j for j in range(2,int(p**0.5)+1)))
    r=invariants(n,p,'root');w=invariants(n,p,'weight')
    assert (r,w)==(1,0),(n,p,r,w)
    print('LATTICE_OK',n,'characteristic',p,'root_invariants',r,'weight_invariants',w)
print('MODULAR_VERIFY_OK')
