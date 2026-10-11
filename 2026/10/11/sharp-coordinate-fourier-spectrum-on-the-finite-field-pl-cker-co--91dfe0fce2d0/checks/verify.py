#!/usr/bin/env python3
"""Independent exact arithmetic and direct finite-field Fourier Gram checks."""
from fractions import Fraction
from math import comb, sqrt
from itertools import product
import cmath


def parameters(q,m):
    assert q>=2 and m>=4
    W=q**(2*m)-(q+1)*q**m+q**3
    A=q**(2*m-2)-(q+1)*q**m+q**3
    B=q**(2*m-4)-(q+1)*q**m+q**3
    a,b=Fraction(A,W),Fraction(B,W)
    E=comb(m,2)
    C=1-a
    R=1+(q-2)*a+(q-1)*((m-4)*a-(m-3)*b)
    D=1-q*a+(q-1)*b
    E0=1+(q-2)*a+(q-1)*(2*(m-2)*a+comb(m-2,2)*b)
    h=sqrt(E*(q-1))*float(a)
    Lp=(1+float(E0)+sqrt((1-float(E0))**2+4*h*h))/2
    Lm=(1+float(E0)-sqrt((1-float(E0))**2+4*h*h))/2
    n=W//(q*(q*q-1))
    assert W%(q*(q*q-1))==0
    return n,a,b,C,R,D,E0,Lm,Lp


def gf_ops(q):
    if q in (2,3,5):
        def add(x,y): return (x+y)%q
        def mult(x,y): return (x*y)%q
        def char(x): return cmath.exp(2j*cmath.pi*x/q)
        return add,mult,char
    assert q==4
    def add(x,y): return x^y
    def mult(x,y):
        v=0
        for i in range(2):
            for j in range(2):
                if ((x>>i)&1) and ((y>>j)&1): v ^= (1<<(i+j))
        if (v>>3)&1: v ^= 0b1110  # safety, never triggered for degree<=2
        if (v>>2)&1: v ^= 0b111
        return v
    def char(x): return -1+0j if x in (2,3) else 1+0j
    return add,mult,char


def direct_gram(q,m):
    add,mul,chi=gf_ops(q)
    edges=[(i,j) for i in range(m) for j in range(i+1,m)]
    vecs=list(product(range(q),repeat=m))
    X=set()
    for u in vecs:
        for v in vecs:
            co=[]
            for i,j in edges:
                co.append(add(mul(u[i],v[j]), (q-mul(u[j],v[i]))%q if q != 4 else mul(u[j],v[i])))
            X.add(tuple(co))
    n,a,b,C,R,D,E0,Lm,Lp=parameters(q,m)
    assert len(X)==n,(q,m,len(X),n)
    columns=[(None,None)]+[(k,t) for k in range(len(edges)) for t in range(1,q)]
    F=[[1+0j for _ in columns] for _ in range(n)]
    for z,x in enumerate(X):
        for k,t in enumerate(columns[1:],1):
            F[z][k]=chi(mul(t[1],x[t[0]]))
    dim=len(columns)
    G=[[0j]*dim for _ in range(dim)]
    max_err=0.
    for i in range(dim):
        for j in range(i,dim):
            val=sum(row[i].conjugate()*row[j] for row in F)/n
            G[i][j]=val;G[j][i]=val.conjugate()
            if i==j: want=1
            elif i==0: want=a
            else:
                e1=columns[i][0];e2=columns[j][0]
                want=b if set(edges[e1]).isdisjoint(edges[e2]) else a
            max_err=max(max_err,abs(val-complex(want)))
    assert max_err <3e-11,(q,m,max_err)
    def residual(x,lam):
        return max(abs(sum(G[i][j]*x[j] for j in range(dim))-complex(lam)*x[i])
                   for i in range(dim))
    # Every edge's within-block character contrast is an eigenvector of C.
    if q>2:
        x=[0j]*dim;x[1]=1;x[2]=-1
        assert residual(x,C)<3e-11,(q,m,'contrast')
    # Johnson incidence: a vertex-balanced edge vector belongs to R-mode.
    x=[0j]*dim
    for e,(i,j) in enumerate(edges):
        w=(i==0)+(j==0)-(i==1)-(j==1)
        for t in range(1,q): x[1+e*(q-1)+(t-1)]=w
    assert residual(x,R)<3e-11,(q,m,'incidence')
    # Four-cycle edge vectors belong to the degree-two Johnson D-mode.
    weights={(0,1):1,(2,3):1,(0,2):-1,(1,3):-1}
    x=[0j]*dim
    for e,ij in enumerate(edges):
        w=weights.get(ij,0)
        for t in range(1,q): x[1+e*(q-1)+(t-1)]=w
    assert residual(x,D)<3e-11,(q,m,'cycle')
    # Constant and uniform coefficient mode form the advertised 2x2 block.
    uni=[0j]+[1/sqrt((q-1)*len(edges))]*(dim-1)
    assert abs(sum(G[0][j]*uni[j] for j in range(dim))-sqrt((q-1)*len(edges))*float(a))<3e-11
    assert abs(sum(G[1][j]*uni[j] for j in range(dim))-float(E0)*uni[1]-float(a)*uni[0])<3e-11
    for eigen in (Lm,Lp):
        # normalized vectors not needed, use nonzero eigenvector in span.
        h=sqrt((q-1)*len(edges))*float(a)
        vec=[complex(h)]+[complex((eigen-1)*u) for u in uni[1:]]
        assert residual(vec,eigen)<3e-10,(q,m,'two-d eigen')
    err=max_err
    return n,err


def global_checks():
    # Exact integer test of the least-mode crossover; 36 prime-power values, 3,642 (q,m) pairs.
    cases=0
    for q in (2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,53,59,61,64,67,71,73,79,81,83,89,97,101):
        cutoff=10 if q==2 else (4*q+3 if q in (3,4) else 4*q+4)
        for m in sorted(set(range(4,100))|set(range(cutoff-3,cutoff+4))|{4*q+7,4*q+30}):
            if m<4: continue
            W=q**(2*m)-(q+1)*q**m+q**3
            A=q**(2*m-2)-(q+1)*q**m+q**3
            B=q**(2*m-4)-(q+1)*q**m+q**3
            S=4*(q*A-(q-1)*B)-m*(A-(q-1)*B)
            assert (S<0)==(m>=cutoff),(q,m,S,cutoff)
            assert S!=0
            assert A>0 and A>B
            assert 1-q*Fraction(A,W)+(q-1)*Fraction(B,W)>0
            cases+=1
    checked=[]
    for q,m in ((2,4),(2,5),(2,6),(2,7),(3,4),(3,5),(4,4),(5,4)):
        n,err=direct_gram(q,m)
        checked.append([q,m,n])
    print('VERIFY_OK independent_direct_full_fourier_gram_cases=',len(checked),'cases=',checked,'max_error_lt=3e-11','exact_sign_tests=',cases)

if __name__=='__main__':
    global_checks()
