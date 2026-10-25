#!/usr/bin/env python3
"""Exact finite-field tests of Mayer path homology on parallel directed paths.

No outside packages. Primitive Nth roots are represented in prime fields p=1 (mod N).
The complex-char-zero theorem uses a separate general proof; finite-field tests are checks.
"""
from itertools import product
from math import gcd


def isprime(p):
    if p < 2: return False
    for d in range(2, int(p ** 0.5) + 1):
        if p % d == 0: return False
    return True


def primitive_root_mod_prime(p):
    factors = [q for q in range(2,p) if (p-1)%q==0 and isprime(q)]
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in factors): return g
    raise AssertionError('root not found')


def root(N):
    p=10001
    while (p-1)%N or not isprime(p): p+=1
    xi=pow(primitive_root_mod_prime(p),(p-1)//N,p)
    assert pow(xi,N,p)==1 and all(pow(xi,k,p)!=1 for k in range(1,N))
    return p,xi


def rr(A,p):
    A=[[(a%p) for a in row] for row in A]
    if not A: return 0,[],[]
    nc=len(A[0]); r=0; piv=[]
    for j in range(nc):
        k=next((i for i in range(r,len(A)) if A[i][j]),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]
        inv=pow(A[r][j],-1,p)
        A[r]=[(u*inv)%p for u in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][j]:
                fac=A[i][j]
                A[i]=[(x-fac*y)%p for x,y in zip(A[i],A[r])]
        piv.append(j);r+=1
        if r==len(A): break
    return r,piv,A


def kernel(A,p,nc):
    if not A: return [[int(i==j) for i in range(nc)] for j in range(nc)]
    rank,piv,R=rr(A,p)
    return [[(1 if i==j else (-R[piv.index(i)][j] if i in piv else 0))%p for i in range(nc)] for j in range(nc) if j not in piv]


def mul(A,B,p):
    if not A: return []
    if not B: return [[] for _ in A]
    return [[sum(x*y for x,y in zip(row,col))%p for col in zip(*B)] for row in A]


def graph(lengths):
    src,dst=0,1; nex=2; E=[]; arms=[]
    for ell in lengths:
        path=[src]+list(range(nex,nex+ell-1))+[dst]
        nex+=ell-1
        E += list(zip(path[:-1],path[1:]))
        arms.append(path)
    return nex,E,arms


def paths(arms,k):
    return [tuple(a[i:i+k+1]) for a in arms for i in range(len(a)-k)]


def predicted(lengths,N,deg,q):
    E=sum(lengths); r=len(lengths); V=2+E-r; a=sum(L==2 for L in lengths)
    period=2*N if N%2 else (N if N%4==0 else N//2)
    delta=int(all((L-lengths[0])%period==0 for L in lengths))
    if deg==0:
        if q==N-1:return delta
        if q==N-2:return V-(a-1 if a else 0)
        return V
    if deg==1:
        if q==1:return r-2+delta
        return E-(max(0,a-1) if q==N-1 else 0)
    if deg==2:return max(0,a-1) if q>=3 else 0
    return 0


def check_one(lengths,N,p,xi):
    V,edges,arms=graph(lengths); E=len(edges)
    edge_idx={e:i for i,e in enumerate(edges)}
    D1=[[0]*E for _ in range(V)]
    for j,(a,b) in enumerate(edges):D1[a][j]=xi;D1[b][j]=1
    r1=rr(D1,p)[0]
    A2=paths(arms,2); all_pairs={}
    for path in A2:
        for pair in (path[1:],(path[0],path[2]),path[:2]):
            if pair not in edge_idx: all_pairs.setdefault(pair,len(all_pairs))
    Bad=[[0]*len(A2) for _ in all_pairs]
    for col,(a,b,c) in enumerate(A2):
        for pair,coeff in [((b,c),1),((a,c),xi),((a,b),xi*xi%p)]:
            if pair not in edge_idx:Bad[all_pairs[pair]][col]=(Bad[all_pairs[pair]][col]+coeff)%p
    K2=kernel(Bad,p,len(A2)); d2dim=len(K2)
    # Full allowed differential of Omega_2, using a computed kernel of nonallowed faces.
    D2all=[[0]*len(A2) for _ in edges]
    for col,(a,b,c) in enumerate(A2):
        for pair,coeff in [((b,c),1),((a,c),xi),((a,b),xi*xi%p)]:
            if pair in edge_idx:D2all[edge_idx[pair]][col]=(D2all[edge_idx[pair]][col]+coeff)%p
    D2=mul(D2all,[list(x) for x in zip(*K2)] if K2 else [[] for _ in A2],p)
    D20=mul(D1,D2,p)
    r2=rr(D2,p)[0];r20=rr(D20,p)[0]
    a=sum(x==2 for x in lengths)
    assert d2dim==max(0,a-1),(lengths,N,'Omega2',d2dim,a)
    assert r2==r20==d2dim,(lengths,N,'D2 rank',r2,r20,d2dim)
    # Verify higher Omega_n vanish: any allowed n-path gives a unique bad face.
    for n in range(3,max(lengths)+1):
        An=paths(arms,n)
        if not An:continue
        faces={}
        for seq in An:
            for j in range(n+1):
                face=seq[:j]+seq[j+1:]
                if face not in paths(arms,n-1): faces.setdefault(face,len(faces))
        M=[[0]*len(An) for _ in faces]
        for col,seq in enumerate(An):
            for j in range(n+1):
                face=seq[:j]+seq[j+1:]
                if face in faces:M[faces[face]][col]=(M[faces[face]][col]+pow(xi,j,p))%p
        assert rr(M,p)[0]==len(An),(lengths,N,'Omega high',n)
    # Independently calculate every N,q Betti number using ranks of d1,d2,d^2.
    for q in range(1,N):
        for n in range(4):
            dims=[V,E,d2dim,0]
            if n==0: z=V
            elif n==1:z=E-r1 if q==1 else E
            elif n==2:z=0 if q in (1,2) else d2dim
            else:z=0
            src=n+N-q
            if src>2:b=0
            elif src==2:b=r20 if N-q==2 else r2 if N-q==1 else 0
            elif src==1:b=r1 if N-q==1 else 0
            else:b=0
            found=z-b; expect=predicted(lengths,N,n,q)
            assert found==expect,(lengths,N,n,q,found,expect,z,b)
    return len(A2),max(lengths),E,V


def main():
    total=0; two=0; high=0; em=0
    for N in (3,4,5,6,7,8,10,12):
        p,xi=root(N)
        for r in (2,3,4):
            for lengths in product((2,3,4,5),repeat=r):
                d2,m,E,V=check_one(lengths,N,p,xi)
                total+=1;two+=d2;high+=m;em+=E
        print('N',N,'prime',p,'primitive_root',xi,'cases',total)
    print('EXACT_MODULAR_CHECK_OK', 'configurations',total,'allowed_two_paths',two,'max_degree_total',high,'edges_total',em)

if __name__=='__main__': main()
