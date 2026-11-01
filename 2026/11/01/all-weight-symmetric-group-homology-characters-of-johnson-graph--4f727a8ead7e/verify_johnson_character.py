#!/usr/bin/env python3
"""Exhaustive small-case checks of Johnson clique-complex character identity.
Run: python3 verify_johnson_character.py  (Python standard library only).
The symbolic proof for all parameters is not replaced by finite tests.
"""
from itertools import combinations
from collections import defaultdict
from math import comb, factorial
from collections import Counter

def partitions(n, high=None):
    if n==0:
        yield ()
    else:
        if high is None: high=n
        for a in range(min(n,high),1-1,-1):
            for p in partitions(n-a,a): yield (a,)+p

def cycle_perm(parts):
    p=[]; t=0
    for size in parts:
        p.extend(list(range(t+1,t+size))+[t]); t+=size
    return p

def parity(xs):
    return -1 if sum(a>b for i,a in enumerate(xs) for b in xs[i+1:])%2 else 1

def data(n,k):
    vertices=list(combinations(range(n),k)); vid={v:i for i,v in enumerate(vertices)}
    facets=[]
    for A in combinations(range(n),k-1):
        A=set(A); facets.append(tuple(sorted(vid[tuple(sorted(A|{b}))] for b in range(n) if b not in A)))
    for B in combinations(range(n),k+1):
        B=set(B); facets.append(tuple(sorted(vid[tuple(sorted(B-{b}))] for b in B)))
    faces=set()
    for facet in facets:
        for z in range(1,len(facet)+1):
            faces.update(combinations(facet,z))
    faces=sorted(faces,key=lambda face:(len(face),face))
    sizes=defaultdict(int)
    for face in faces: sizes[len(face)-1]+=1
    edges=[x for x in faces if len(x)==2]
    flags_left=[(tuple(A),tuple(sorted(set(A)|{b}))) for A in combinations(range(n),k-1) for b in range(n) if b not in A]
    flags_right=[(tuple(U),tuple(sorted(set(U)|{b}))) for U in vertices for b in range(n) if b not in U]
    return vertices,faces,edges,flags_left,flags_right,dict(sizes)

def char_actual(faces,vperm):
    out=0
    for face in faces:
        mapped=[vperm[x] for x in face]
        if set(mapped)==set(face): out+= (-1 if len(face)%2==0 else 1)*parity(mapped)
    return out -1

def char_formula(n,k,vertices,edges,flags_left,flags_right,p):
    f=lambda U:tuple(sorted(p[x] for x in U))
    p_r=lambda r:sum(1 for U in combinations(range(n),r) if f(U)==U)
    eid={U:i for i,U in enumerate(vertices)}
    vperm=[eid[f(U)] for U in vertices]
    e_trace=sum(1 if (vperm[u],vperm[v])==(u,v) else -1 for u,v in edges if {vperm[u],vperm[v]}=={u,v})
    fl=sum(1 for A,U in flags_left if f(A)==A and f(U)==U)
    fr=sum(1 for U,B in flags_right if f(U)==U and f(B)==B)
    return p_r(k)+p_r(k-1)+p_r(k+1)+e_trace-fl-fr-1,vperm

def rank_mod2(columns):
    piv={}
    for col in columns:
        while col:
            p=col.bit_length()-1
            if p not in piv: piv[p]=col;break
            col^=piv[p]
    return len(piv)

def homology_mod2(faces):
    bydim=defaultdict(list)
    for f in faces: bydim[len(f)-1].append(f)
    ranks={}
    for j in sorted(bydim):
        if j==0: ranks[j]=0;continue
        idx={f:i for i,f in enumerate(bydim[j-1])}
        columns=[sum(1<<idx[f[:i]+f[i+1:]] for i in range(len(f))) for f in bydim[j]]
        ranks[j]=rank_mod2(columns)
    return {j:len(b) - ranks.get(j,0) - ranks.get(j+1,0) for j,b in bydim.items()}

def main():
    total=0
    for n,k in ((6,3),(7,3),(8,3),(8,4)):
        verts,faces,edges,fl,fr,sizes=data(n,k)
        expected=comb(n,k)-1 - comb(n,k)*k*(n-k)//2 + comb(n,k-1)*comb(n-k,2) + comb(n,k+1)*comb(k,2)
        av=0; avsign=0
        for part in partitions(n):
            perm=cycle_perm(part)
            predicted,vperm=char_formula(n,k,verts,edges,fl,fr,perm)
            actual=char_actual(faces,vperm)
            assert actual==predicted,(n,k,part,actual,predicted)
            if part==(1,)*n: assert actual==expected,(n,k,actual,expected)
            mult=Counter(part)
            den=1
            for size,num in mult.items(): den*=size**num*factorial(num)
            classsize=factorial(n)//den
            av+=classsize*actual
            avsign+=classsize*actual*((-1)**(n-len(part)))
            total+=1
        assert av==0 and avsign==0,(n,k,av,avsign)
        if n<=8:
            hom=homology_mod2(faces)
            assert hom=={0:1,1:0,2:expected,3:0} or (hom.get(0)==1 and all(v==(expected if j==2 else 0) for j,v in hom.items() if j!=0)),(n,k,hom)
        print('case',n,k,'vertices',len(verts),'simplices',len(faces),'fvector',sizes,'beta2',expected,'classes',sum(1 for _ in partitions(n)))
    print('JOHNSON_ALL_WEIGHT_SYMMETRY_VERIFY_OK',total)
if __name__=='__main__': main()
