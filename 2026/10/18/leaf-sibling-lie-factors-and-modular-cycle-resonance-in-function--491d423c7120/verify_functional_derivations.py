#!/usr/bin/env python3
"""Direct linear-equation and bracket checks for derivations of functional evolution algebras."""
from itertools import product
from collections import defaultdict

def rankmod(a,p):
    a=[[v%p for v in row] for row in a]
    if not a:return 0
    h=0; n=len(a[0])
    for c in range(n):
        pivot=next((i for i in range(h,len(a)) if a[i][c]),None)
        if pivot is None:continue
        a[h],a[pivot]=a[pivot],a[h]
        inv=pow(a[h][c],-1,p)
        a[h]=[(x*inv)%p for x in a[h]]
        for i in range(len(a)):
            if i!=h and a[i][c]:
                w=a[i][c]
                a[i]=[(v-w*u)%p for v,u in zip(a[i],a[h])]
        h+=1
        if h==len(a):break
    return h

def constraints(f,p):
    n=len(f); e=[]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(n):
                row=[0]*(n*n)
                if k==f[j]:row[j*n+i]+=1  # coeff d_{j,i}
                if k==f[i]:row[i*n+j]+=1  # coeff d_{i,j}
                if any(row):e.append(row)
        for k in range(n):
            row=[0]*(n*n)
            row[k*n+f[i]]+=1
            if k==f[i]:row[i*n+i]-=2
            e.append(row)
    return [[v%p for v in row] for row in e]

def pred_basis(f,p):
    n=len(f); image=set(f); leaves=set(range(n))-image
    groups=defaultdict(list)
    for i in leaves:groups[f[i]].append(i)
    mat=[]
    def add(d):mat.append([d[i][j]%p for i in range(n) for j in range(n)])
    for vs in groups.values():
        if p==2:
            for i in vs:
                d=[[0]*n for _ in range(n)];d[i][i]=1;add(d)
        for ia,i in enumerate(vs):
            for j in vs[ia+1:]:
                d=[[0]*n for _ in range(n)];d[i][j]=1;d[j][i]=-1;add(d)
    if p!=2:
        marked=set()
        for seed in range(n):
            if seed in marked:continue
            component=set([seed]); changed=True
            while changed:
                changed=False
                for i in range(n):
                    if (i in component or f[i] in component) and not (i in component and f[i] in component):
                        component.add(i); component.add(f[i]);changed=True
            marked |= component
            cycl=[]; now=seed;seen={}
            while now not in seen:
                seen[now]=len(cycl);cycl.append(now);now=f[now]
            cycl=cycl[seen[now]:];L=len(cycl)
            if (pow(2,L,p)-1)%p:continue
            vals={cycl[0]:1}; queue=[cycl[0]]
            for y in queue:
                for i in component:
                    if f[i]==y and i not in vals:
                        vals[i]=vals[y]*pow(2,-1,p)%p;queue.append(i)
            assert len(vals)==len(component)
            d=[[0]*n for _ in range(n)]
            for i,v in vals.items():d[i][i]=v
            add(d)
    return mat

def matcomm(A,B,n,p):
    C=[0]*(n*n)
    for i in range(n):
        for j in range(n):
            C[i*n+j]=sum(A[i*n+k]*B[k*n+j]-B[i*n+k]*A[k*n+j] for k in range(n))%p
    return C

def run():
    trials=0;liechecks=0
    for p in (2,3,5,7):
        for n in range(1,6):
            fs=product(range(n),repeat=n) if n<=4 else (tuple((3*i+2)%n for i in range(n)),tuple([0]*n),tuple(range(n)))
            for f in fs:
                E=constraints(f,p);B=pred_basis(f,p);rank=rankmod(E,p);brank=rankmod(B,p)
                assert n*n-rank==len(B)==brank,(p,n,f,n*n-rank,len(B),brank)
                for vec in B:
                    assert all(sum(x*y for x,y in zip(row,vec))%p==0 for row in E),(p,n,f,'bad basis')
                if trials%97==0 and len(B)>1:
                    for A in B[:5]:
                        for C in B[:5]:
                            comm=matcomm(A,C,n,p)
                            assert all(sum(x*y for x,y in zip(row,comm))%p==0 for row in E)
                            liechecks+=1
                trials+=1
    print('VERIFY_OK_FUNCTIONAL_DERIVATION_LIE trials=',trials,'bracket_checks=',liechecks)
if __name__=='__main__':run()
