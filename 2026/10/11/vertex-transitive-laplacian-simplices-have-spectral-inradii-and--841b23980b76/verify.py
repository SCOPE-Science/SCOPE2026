#!/usr/bin/env python3
import sympy as sp

def laplacian_from_edges(n, edges):
    A=sp.zeros(n)
    for u,v in edges:
        A[u,v]=A[v,u]=1
    deg=[sum(int(A[i,j]) for j in range(n)) for i in range(n)]
    L=sp.diag(*deg)-A
    return L,deg

def complete_edges(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def cycle_edges(n):
    return [(i,(i+1)%n) for i in range(n)]

def cube3_edges():
    out=[]
    for x in range(8):
        for b in (1,2,4):
            y=x^b
            if x<y:
                out.append((x,y))
    return out

def petersen_edges():
    outer=[(i,(i+1)%5) for i in range(5)]
    inner=[(5+i,5+((i+2)%5)) for i in range(5)]
    spokes=[(i,5+i) for i in range(5)]
    # de-duplicate undirected inner edges
    return sorted({tuple(sorted(e)) for e in outer+inner+spokes})

graphs=[
    ("K5",5,complete_edges(5)),
    ("C6",6,cycle_edges(6)),
    ("Q3",8,cube3_edges()),
    ("Petersen",10,petersen_edges()),
]

for name,n,edges in graphs:
    L,deg=laplacian_from_edges(n,edges)
    assert L.rank()==n-1
    assert L*sp.ones(n,1)==sp.zeros(n,1)
    assert len(set(deg))==1
    k=deg[0]

    J=sp.ones(n,n)
    Lp=(L+sp.Rational(1,n)*J).inv()-sp.Rational(1,n)*J
    assert L*Lp==sp.eye(n)-sp.Rational(1,n)*J
    assert Lp*L==sp.eye(n)-sp.Rational(1,n)*J
    assert Lp*sp.ones(n,1)==sp.zeros(n,1)

    # All vertex norms and centroid.
    verts=[L[:,i] for i in range(n)]
    assert sum(verts, sp.zeros(n,1))==sp.zeros(n,1)
    norm2=[sp.expand((v.T*v)[0]) for v in verts]
    assert set(norm2)=={k*(k+1)}

    # Barycentric facet formula: lambda_i(v_j)=delta_ij.
    for i in range(n):
        ni=Lp[:,i]
        for j in range(n):
            lam=sp.Rational(1,n)+(ni.T*verts[j])[0]
            assert sp.simplify(lam-(1 if i==j else 0))==0

    colnorm2=[sp.simplify((Lp[:,i].T*Lp[:,i])[0]) for i in range(n)]
    assert len(set(colnorm2))==1
    q=colnorm2[0]

    # Spectral/Frobenius trace identity.
    evals=[]
    for val,mult in L.eigenvals().items():
        evals += [sp.simplify(val)]*mult
    nonzero=[x for x in evals if x!=0]
    S=sp.simplify(sum(1/(x*x) for x in nonzero))
    assert sp.simplify(n*q-S)==0

    r2=sp.simplify(1/(n*S))
    assert sp.simplify(r2-1/(n*n*q))==0
    R2=k*(k+1)

    print(name, "n=",n, "k=",k, "R2=",R2, "r2=",r2)

print("VERIFY_OK vertex-transitive-Laplacian-simplex exact=yes")
