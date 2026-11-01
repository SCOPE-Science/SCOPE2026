#!/usr/bin/env python3
"""Finite independent tests for the cyclic-layer Mayer-path theorem.

Uses finite fields containing a primitive Nth root of unity. Directly builds
allowed paths and twisted boundaries, computes the missing-face kernel in
degree two, and obtains induced permutation characters from quotient matrices.
These tests corroborate, but do not replace, the all-parameter proof.
"""
from collections import defaultdict
from itertools import product
from random import Random
from math import gcd

P = 241

def prime_divisors(n):
    q=[]; k=2
    while k*k<=n:
        if n%k==0:
            q.append(k)
            while n%k==0:n//=k
        k+=1
    if n>1:q.append(n)
    return q

def root(n):
    for x in range(2,P):
        if pow(x,n,P)==1 and all(pow(x,n//d,P)!=1 for d in prime_divisors(n)):
            return x
    raise ValueError('No primitive root for N=%s' % n)

def rref(rows,nc):
    aa=[[x%P for x in row] for row in rows]
    pivots=[];r=0
    for c in range(nc):
        hit=next((i for i in range(r,len(aa)) if aa[i][c]),None)
        if hit is None:continue
        aa[r],aa[hit]=aa[hit],aa[r]
        inv=pow(aa[r][c],-1,P)
        aa[r]=[(t*inv)%P for t in aa[r]]
        for i in range(len(aa)):
            if i!=r and aa[i][c]:
                a=aa[i][c]
                aa[i]=[(y-a*x)%P for x,y in zip(aa[r],aa[i])]
        pivots.append(c);r+=1
        if r==len(aa):break
    return aa[:r],pivots

def kernel_basis(rows,nc):
    rr, pivots=rref(rows,nc)
    free=[j for j in range(nc) if j not in pivots]
    basis=[]
    for j in free:
        v=[0]*nc;v[j]=1
        for i,c in enumerate(pivots):v[c]=(-rr[i][j])%P
        basis.append(v)
    return basis

def check(n,sizes,N,with_character=False):
    xi=root(N)
    vertices=[(i,j) for i,a in enumerate(sizes) for j in range(a)]
    edges=[(u,v) for u in vertices for v in vertices if v[0]==(u[0]+1)%n]
    triples=[(u,v,w) for (u,v) in edges for w in vertices if w[0]==(v[0]+1)%n]
    vid={x:i for i,x in enumerate(vertices)}
    eid={x:i for i,x in enumerate(edges)}
    mid={pair:i for i,pair in enumerate(sorted({(u,w) for u,v,w in triples}))}
    # Missing face of (u,v,w) is (u,w), with coefficient xi.
    M=[[0]*len(triples) for _ in mid]
    for j,(u,v,w) in enumerate(triples):
        M[mid[(u,w)]][j]=xi
    omega2=kernel_basis(M,len(triples))
    # Restrict exact d_2 to omega_2: d(u,v,w)=(v,w)+xi(u,w)+xi^2(u,v),
    # with shortcut (u,w) absent; omega2 makes its total coefficient zero.
    B=[]
    for vector in omega2:
        r=[0]*len(edges)
        for coef,(u,v,w) in zip(vector,triples):
            if not coef:continue
            r[eid[(v,w)]]+=coef
            r[eid[(u,v)]]+=xi*xi*coef
        B.append([x%P for x in r])
    image,pivot=rref(B,len(edges))
    h1=len(edges)-len(image)
    assert h1==len(vertices),(n,sizes,N,'H1',h1,len(vertices))
    # Independently verify the asserted explicit canonical map: send each
    # vertex x in layer i to the average of all outgoing arcs x -> y.
    phi=[]
    for v in vertices:
        row=[0]*len(edges)
        for j,(u,w) in enumerate(edges):
            if u==v: row[j]=pow(sizes[(v[0]+1)%n],-1,P)
        phi.append(row)
    assert len(rref(image+phi,len(edges))[0])==len(edges),(n,sizes,N,'Phi')
    d1=[[0]*len(edges) for _ in vertices]
    for j,(u,v) in enumerate(edges):
        d1[vid[u]][j]=xi
        d1[vid[v]][j]=1
    h0=len(vertices)-len(rref(d1,len(edges))[0])
    d=2*N//gcd(N+2,2*N)
    assert h0==int(n%d==0),(n,sizes,N,'H0',h0,d)
    if h0:
        weight={v:pow(-xi,v[0],P) for v in vertices}
        assert all((xi*weight[u]+weight[v])%P==0 for u,v in edges)
        for shift in range(n):
            if all(sizes[(i+shift)%n]==sizes[i] for i in range(n)):
                eigen=pow(-xi,shift,P)
                assert all(weight[((v[0]+shift)%n,v[1])]==eigen*weight[v]%P
                           for v in vertices)
    if with_character:
        # Layerwise permutations, plus orientation-preserving cyclic rotations
        # in the equal-layer-size case. Compare character on quotient E / im d2
        # with the permutation character on the vertex set.
        rng=Random(n*1000+N*13+sum(sizes))
        maps=[]
        for rep in range(5):
            local=[]
            for a in sizes:
                perm=list(range(a));rng.shuffle(perm);local.append(perm)
            maps.append({(i,j):(i,local[i][j]) for i,a in enumerate(sizes) for j in range(a)})
        if len(set(sizes))==1:
            for shift in range(1,n):
                maps.append({(i,j):((i+shift)%n,j) for i,a in enumerate(sizes) for j in range(a)})
        for mp in maps:
            edge_perm=[eid[(mp[u],mp[v])] for (u,v) in edges]
            inv=[0]*len(edges)
            for j,k in enumerate(edge_perm):inv[k]=j
            tr_im=sum(b[inv[c]] for b,c in zip(image,pivot))%P
            tr_edge=sum(j==edge_perm[j] for j in range(len(edges)))
            actual=(tr_edge-tr_im)%P
            expected=sum(mp[v]==v for v in vertices)%P
            assert actual==expected,(n,sizes,N,'character',actual,expected)
    return len(vertices),len(edges),len(triples),len(omega2)

def main():
    rng=Random(20261029); cases=[]
    for N in (3,4,5,6,8,10,12):
        for n in range(3,13):
            cases.append((n,(1,)*n,N))
        for n in range(3,7):
            for t in range(7):
                sizes=tuple(rng.randint(1,3) for _ in range(n))
                if sum(sizes)<=14:cases.append((n,sizes,N))
    tot=[0,0,0,0]; chars=0
    for n,sizes,N in cases:
        result=check(n,sizes,N,with_character=(sum(sizes)<=11))
        tot=[x+y for x,y in zip(tot,result)]
        if sum(sizes)<=11:chars+=1
    print('VERIFY_OK cases=%d character_cases=%d vertices=%d arcs=%d two_paths=%d omega2_basis_vectors=%d'%(len(cases),chars,*tot))

if __name__=='__main__':main()
