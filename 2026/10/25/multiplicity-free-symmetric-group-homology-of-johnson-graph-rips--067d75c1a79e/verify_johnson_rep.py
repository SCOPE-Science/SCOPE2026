#!/usr/bin/env python3
"""Finite cross-checks for Johnson graph clique-complex characters.
Only standard library; finite calculations corroborate a separate all-parameter proof.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb, factorial


def parity(xs):
    return -1 if sum(xs[i] > xs[j] for i in range(len(xs)) for j in range(i + 1, len(xs))) % 2 else 1


def cycle_partition(p):
    seen=set(); cycles=[]
    for a in range(len(p)):
        if a not in seen:
            cur=a; l=0
            while cur not in seen:
                seen.add(cur); l+=1; cur=p[cur]
            cycles.append(l)
    return tuple(sorted(cycles,reverse=True))


def make_rep(lam):
    p=list(range(sum(lam))); i=0
    for m in lam:
        for j in range(m):p[i+j]=i+(j+1)%m
        i+=m
    return tuple(p)


def parts(n, upper=None):
    if n == 0:
        yield ()
    else:
        for i in range(min(n, upper or n),1-1,-1):
            for rest in parts(n-i,i):
                yield (i,)+rest


def local_wedge(g, sample):
    ss=set(sample); f=sum(g[x]==x for x in ss)
    f2=sum(g[g[x]]==x for x in ss)
    return ((f-1)**2-(f2-1))//2


def character_model(n,k,p,vs,es,star_sets,top_sets):
    gp=lambda v:tuple(sorted(p[x] for x in v))
    # stable vertices (0-chains)
    vert_fix=sum(gp(v)==v for v in vs)
    # signed oriented graph edges (1-chains)
    edge_trace=0
    for a,b in es:
        a1,b1=gp(a),gp(b)
        if a1==a and b1==b: edge_trace+=1
        if a1==b and b1==a: edge_trace-=1
    star_trace=sum(local_wedge(p,tuple(x for x in range(n) if x not in S)) for S in star_sets if gp(S)==S)
    top_trace=sum(local_wedge(p,B) for B in top_sets if gp(B)==B)
    return -1+vert_fix-edge_trace+star_trace+top_trace


def build(n,k):
    vs=list(combinations(range(n),k)); vmap={v:i for i,v in enumerate(vs)}
    edges=[(a,b) for a,b in combinations(vs,2) if len(set(a)&set(b))==k-1]
    stars=list(combinations(range(n),k-1)); tops=list(combinations(range(n),k+1))
    cliques=[]
    for S in stars:
        ss=set(S)
        cliques.append(tuple(sorted(vmap[tuple(sorted(ss|{x}))] for x in range(n) if x not in ss)))
    for B in tops:
        cliques.append(tuple(sorted(vmap[tuple(x for x in B if x!=z)] for z in B)))
    faces={1:set((vmap[a],vmap[b]) for a,b in edges),0:set((i,) for i in range(len(vs)))}
    for cc in cliques:
        for j in range(3,len(cc)+1):
            faces.setdefault(j-1,set()).update(combinations(cc,j))
    ff={d:sorted(vals) for d,vals in faces.items()}
    assert len(ff[2])==sum(comb(len(cc),3) for cc in cliques)
    return vs,edges,stars,tops,ff


def direct_char(n,k,p,vs,ff):
    dic={v:i for i,v in enumerate(vs)}
    perm=[dic[tuple(sorted(p[x] for x in v))] for v in vs]
    tr=-1
    for d,faces in ff.items():
        this=0
        for face in faces:
            mapped=[perm[i] for i in face]
            if sorted(mapped)==list(face):
                this+=parity(mapped)
        tr+=(-1)**d*this
    return tr


def gf2_ranks(ff):
    ranks={0:0}
    for d in range(1,max(ff)+1):
        prev={face:i for i,face in enumerate(ff[d-1])}; pivots={}
        for face in ff[d]:
            b=0
            for j in range(d+1):
                sub=face[:j]+face[j+1:]
                b^=1<<prev[sub]
            while b:
                i=b.bit_length()-1
                if i in pivots:b^=pivots[i]
                else:
                    pivots[i]=b;break
        ranks[d]=len(pivots)
    return ranks


def main():
    cases=[(6,3,True),(7,3,True),(8,4,False)]
    total=0
    for n,k,full in cases:
        vs,edges,stars,tops,faces=build(n,k)
        beta=comb(n,k)-1-len(edges)+comb(n,k-1)*comb(n-k,2)+comb(n,k+1)*comb(k,2)
        if full:
            ranks=gf2_ranks(faces)
            betti={d:len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in faces}
            assert betti.get(2)==beta and all(betti[d]==0 for d in betti if d not in (0,2)),(n,k,betti,beta)
            assert betti[0]==1
        reps=list(permutations(range(n))) if full else [make_rep(la) for la in parts(n)]
        for p in reps:
            mod=character_model(n,k,p,vs,edges,stars,tops)
            direct=direct_char(n,k,p,vs,faces)
            assert mod==direct,(n,k,cycle_partition(p),mod,direct)
            if p==tuple(range(n)):assert mod==beta
            total+=1
        avg=0
        for la in parts(n):
            r=make_rep(la); tr=character_model(n,k,r,vs,edges,stars,tops)
            den=1
            for length,ct in Counter(la).items():den*=length**ct*factorial(ct)
            avg+=tr*factorial(n)//den
        assert avg==0,(n,k,avg)
        print('CASE_OK',n,k,'vertices',len(vs),'edges',len(edges),'faces',sum(map(len,faces.values())),'top_beta',beta,'elements_checked',len(reps),'invariant_sum',avg)
    print('JOHNSON_EQUIVARIANT_CHECKS_OK',total)

if __name__=='__main__':main()
