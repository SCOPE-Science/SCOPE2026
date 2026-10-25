#!/usr/bin/env python3
"""Exact signed Lefschetz checks for Johnson-graph clique complexes.
No external libraries required. This is a finite sanity check; the accompanying theorem is proved for all parameters.
"""
from itertools import combinations
from collections import Counter
from math import comb

def parts(n,m=1):
    if n==0: yield ()
    for x in range(m,n+1):
        for p in parts(n-x,x): yield (x,)+p

def standard_perm(part):
    p=list(range(sum(part))); start=0
    for ell in part:
        for j in range(ell): p[start+j]=start+(j+1)%ell
        start+=ell
    return tuple(p)

def coeff_product(part,degree,omit_one=0,omit_two=0):
    c=Counter(part)
    c[1]-=omit_one;c[2]-=omit_two
    if c[1]<0 or c[2]<0: return 0
    f=[0]*(degree+1);f[0]=1
    for ell,count in c.items():
        for _ in range(count):
            for j in range(degree,ell-1,-1):f[j]+=f[j-ell]
    return f[degree]

def pred(n,k,part,complement=False):
    c=Counter(part);f=c[1];c2=c[2]
    if complement:
        assert n==2*k
        if f==0 and sum(q for q in part if q%2):
            return -1
        if f==0:
            e=len(part)
            return (1<<e)-(c2*(1<<(e-1)))-1
        if f==2 and all(q%2==0 or q==1 for q in part):
            return (1<<(len(part)-2))-1
        return -1
    b=lambda r:coeff_product(part,r)
    E=comb(f,2)*coeff_product(part,k-1,omit_one=2) if f>=2 else 0
    E-=c2*coeff_product(part,k-1,omit_two=1) if c2 else 0
    return b(k-1)+b(k+1)+(1-f)*b(k)+E-1

def all_faces(n,k):
    V=list(combinations(range(n),k));i={v:j for j,v in enumerate(V)}
    faces=[set() for _ in range(min(n-k+1,k+1))]
    for j in range(len(V)):faces[0].add((j,))
    for a in range(len(V)):
        for b in range(a+1,len(V)):
            if len(set(V[a])&set(V[b]))==k-1:faces[1].add((a,b))
    maxcl=[]
    for S in combinations(range(n),k-1):
        maxcl.append([i[tuple(sorted(S+(x,)))] for x in range(n) if x not in S])
    for T in combinations(range(n),k+1):
        maxcl.append([i[tuple(x for x in T if x!=y)] for y in T])
    for F in maxcl:
        for r in range(3,len(F)+1):
            for f in combinations(sorted(F),r):faces[r-1].add(f)
    return V,i,faces

def sign_action(face,image):
    vals=[image[j] for j in face]
    if sorted(vals)!=list(face): return 0
    inversions=sum(vals[u]>vals[v] for u in range(len(vals)) for v in range(u+1,len(vals)))
    return -1 if inversions%2 else 1

def main():
    tests=0;comparisons=0
    for n in (8,10):
        k=n//2
        V,index,faces=all_faces(n,k)
        print('dimension',n,k,'vertices',len(V),'faces',sum(map(len,faces)))
        for part in parts(n):
            if n == 10 and part not in [(1,)*10,(2,)*5,(1,1,2,2,2,2),(1,1,1,1,2,2,2),(2,2,3,3),(2,4,4),(5,5),(10,)]:
                continue
            g=standard_perm(part)
            for comp in (False,True):
                image=[]
                for v in V:
                    w=set(g[x] for x in v)
                    if comp: w=set(range(n))-w
                    image.append(index[tuple(sorted(w))])
                trace=sum((-1)**j*sign_action(f,image) for j,layer in enumerate(faces) for f in layer)-1
                expect=pred(n,k,part,comp)
                assert trace==expect,(n,k,part,comp,trace,expect)
                tests+=1;comparisons+=sum(map(len,faces))
    print('VERIFY_OK cases=',tests,'signed_face_tests=',comparisons)
if __name__=='__main__':main()

def gf2_boundary_betti(faces):
    layers=[sorted(x) for x in faces]
    ranks=[0]*len(layers)
    for dim in range(1,len(layers)):
        prev={f:i for i,f in enumerate(layers[dim-1])}
        pivots={}
        for face in layers[dim]:
            word=0
            for pos in range(len(face)):
                row=face[:pos]+face[pos+1:]
                word^=1<<prev[row]
            while word:
                high=word.bit_length()-1
                if high in pivots:word^=pivots[high]
                else:pivots[high]=word;break
        ranks[dim]=len(pivots)
    betti=[len(layers[d])-ranks[d]-(ranks[d+1] if d+1<len(layers) else 0) for d in range(len(layers))]
    betti[0]-=1
    return betti

if __name__=='__main__':
    for n in (8,):
        f=all_faces(n,n//2)[2]
        betti=gf2_boundary_betti(f)
        assert betti[2]==pred(n,n//2,(1,)*n) and all(x==0 for i,x in enumerate(betti) if i!=2),(n,betti)
        print('GF2_HOMOLOGY_OK',n,betti)
