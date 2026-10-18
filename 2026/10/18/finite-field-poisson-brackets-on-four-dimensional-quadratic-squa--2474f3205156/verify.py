#!/usr/bin/env python3
"""Direct finite-field checks for Poisson brackets of a four-dimensional quadratic nilalgebra."""
from itertools import product
from collections import Counter

def det3(a,b,c,p):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]))%p

def dot(a,b,p):return sum(x*y for x,y in zip(a,b))%p

def all_so(p):
    vec=list(product(range(p),repeat=3))
    uu=[v for v in vec if dot(v,v,p)==1]
    ss=[]
    for a in uu:
        for b in uu:
            if dot(a,b,p):continue
            for c in uu:
                if dot(a,c,p) or dot(b,c,p):continue
                if det3(a,b,c,p)==1:ss.append((a,b,c))
    return ss

def submul(a,b,p):return (0,0,0,sum(a[i]*b[i] for i in range(3))%p)
def add(a,b,p):return tuple((x+y)%p for x,y in zip(a,b))
def equal(a,b):return a==b

def brackets(t,w,p):
    T={}
    for i in range(4):
      for j in range(4):
        v=[0]*4
        if i<3 and j<3 and i!=j:
            for k in range(3):
                u=[0]*3; v0=[0]*3
                u[i]=1;v0[j]=1
                e=[0]*3;e[k]=1
                s=det3(u,v0,e,p)
                v[k]=(t*s)%p
                v[3]=(v[3]+w[k]*s)%p
        T[i,j]=tuple(v)
    return T

def br(T,x,y,p):
    out=[0]*4
    for i in range(4):
      for j in range(4):
       if x[i] and y[j]:
        v=T[i,j]
        for k in range(4):out[k]=(out[k]+x[i]*y[j]*v[k])%p
    return tuple(out)

def checks(p):
    basis=[tuple(int(i==j) for i in range(4)) for j in range(4)]
    cnt=0
    for t in range(p):
      for w in product(range(p),repeat=3):
        T=brackets(t,w,p)
        for x,y,z in product(basis, repeat=3):
            lhs=br(T,submul(x,y,p),z,p)
            rhs=add(submul(br(T,x,z,p),y,p),submul(x,br(T,y,z,p),p),p)
            assert lhs==rhs,(p,t,w,'Leibniz')
            jac=add(add(br(T,br(T,x,y,p),z,p),br(T,br(T,y,z,p),x,p),p),br(T,br(T,z,x,p),y,p),p)
            assert jac==(0,0,0,0),(p,t,w,'Jacobi')
        cnt+=1
    # SO3 transitivity independently checked by orbit enumeration
    so=all_so(p)
    vec=list(product(range(p),repeat=3))
    remaining=set(vec);orbits=[]
    while remaining:
        w=next(iter(remaining))
        orb={tuple(sum(so_i[col][row]*w[col] for col in range(3))%p for row in range(3)) for so_i in so}
        assert orb<=remaining
        norms={dot(v,v,p) for v in orb}
        assert len(norms)==1
        orbits.append((len(orb),next(iter(norms)),w==(0,0,0)))
        remaining-=orb
    assert len(orbits)==p+1,(p,orbits)
    assert len(so)==p*(p*p-1),(p,len(so))
    print('CHECK',p,'brackets',cnt,'SO3',len(so),'central_orbits',len(orbits),'poisson_iso_classes',len(orbits)+1,'orbit_data',sorted(orbits),flush=True)

# Linear Leibniz rank for arbitrary skew brackets (24 variables)
def rank_leibniz(p):
    basis=[tuple(int(i==j) for i in range(4)) for j in range(4)]
    pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
    cols=[]
    for i,j in pairs:
      for k in range(4):
       B={(a,b):(0,0,0,0) for a in range(4) for b in range(4)}
       v=[0]*4;v[k]=1;B[i,j]=tuple(v)
       v[k]=p-1;B[j,i]=tuple(v)
       cols.append(B)
    rows=[]
    for a,b,c in product(range(4),repeat=3):
       x,y,z=basis[a],basis[b],basis[c]
       for k in range(4):
         arr=[]
         for T in cols:
          lhs=br(T,submul(x,y,p),z,p)
          rhs=add(submul(br(T,x,z,p),y,p),submul(x,br(T,y,z,p),p),p)
          arr.append((lhs[k]-rhs[k])%p)
         rows.append(arr)
    pivots=[];r=0
    for c in range(len(cols)):
       pivot=next((j for j in range(r,len(rows)) if rows[j][c]),None)
       if pivot is None:continue
       rows[r],rows[pivot]=rows[pivot],rows[r]
       inv=pow(rows[r][c],-1,p)
       rows[r]=[(x*inv)%p for x in rows[r]]
       for j in range(len(rows)):
         if j!=r and rows[j][c]:
           t=rows[j][c];rows[j]=[(rows[j][i]-t*rows[r][i])%p for i in range(len(cols))]
       pivots.append(c);r+=1
    assert r==20,(p,r)
    print('LEIBNIZ_LINEAR_RANK',p,r,'free',len(cols)-r,flush=True)

if __name__=='__main__':
    for p in [3,5,7]:
       rank_leibniz(p)
       checks(p)
    print('VERIFY_OK')
