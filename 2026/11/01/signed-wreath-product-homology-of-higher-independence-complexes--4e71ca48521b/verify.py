#!/usr/bin/env python3
"""Exact finite checks for higher independence complexes of two-level trees.

The all-parameter topology is proved separately; this script tests the
root-link matching, full chain characters and homology in small cases.
"""
from itertools import combinations, permutations, product
from collections import defaultdict, Counter, deque
from math import comb, factorial


def complex_faces(m,s,r):
    n=1+m*(1+s)
    adj=[set() for _ in range(n)]
    for i in range(m):
        u=1+i*(s+1)
        adj[0].add(u);adj[u].add(0)
        for j in range(s):
            v=u+1+j;adj[u].add(v);adj[v].add(u)
    forbidden=[]
    for V in combinations(range(n),r+1):
        S=set(V);seen={V[0]};stack=[V[0]]
        while stack:
            v=stack.pop()
            for w in adj[v]&S:
                if w not in seen:seen.add(w);stack.append(w)
        if len(seen)==r+1:forbidden.append(sum(1<<i for i in V))
    faces=[F for F in range(1<<n) if all(F&T!=T for T in forbidden)]
    return n,faces


def link_matching(m,s,r,faces,n):
    L=set(F for F in faces if not (F&1) and (F|1) in faces)
    pairs={}
    for F in L:
        used={i for i in range(m) if F & (1<<(1+i*(s+1)))}
        assert len(used)<=r-1
        i=next(i for i in range(m) if i not in used)
        v=1+i*(s+1)+1
        G=F ^ (1<<v)
        assert G in L
        lo,hi=sorted((F,G))
        if (F>>v)&1:continue
        assert lo==F and hi==G
        pairs[F]=G
    assert len(pairs)*2==len(L)
    indeg={F:0 for F in L};out=defaultdict(list);inc=0
    for F in L:
        for v in range(n):
            if F>>v&1:
                P=F^(1<<v)
                if P not in L:continue
                if pairs.get(P)==F:src,dst=P,F
                else:src,dst=F,P
                out[src].append(dst);indeg[dst]+=1;inc+=1
    q=deque(F for F in L if not indeg[F]);seen=0
    while q:
        F=q.popleft();seen+=1
        for G in out[F]:
            indeg[G]-=1
            if indeg[G]==0:q.append(G)
    assert seen==len(L),(m,s,r,seen,len(L))
    return len(L),len(pairs),inc


def rank_gf2(faces,n):
    bysize=defaultdict(list)
    for F in faces:bysize[F.bit_count()].append(F)
    ranks={}
    for k in range(2,max(bysize)+1):
        idx={F:i for i,F in enumerate(bysize[k-1])}
        piv={}
        for F in bysize[k]:
            v=0
            for i in range(n):
                if F>>i&1:v^=1<<idx[F^(1<<i)]
            while v:
                j=v.bit_length()-1
                if j in piv:v^=piv[j]
                else:piv[j]=v;break
        ranks[k-1]=len(piv)
    betti={}
    for k in range(1,max(bysize)+1):
        v=len(bysize[k])-ranks.get(k-1,0)-ranks.get(k,0)-(1 if k==1 else 0)
        if v:betti[k-1]=v
    return betti, {k-1:len(v) for k,v in bysize.items() if k}


def char_exterior_aug(p,k):
    s=len(p);seen=set();poly=[1]
    for i in range(s):
        if i in seen:continue
        x=i;j=0
        while x not in seen:seen.add(x);x=p[x];j+=1
        nxt=poly+[0]*j
        for a,c in enumerate(poly):nxt[a+j]-=(-1)**j*c
        poly=nxt
    quotient=[]
    for i in range(k+1):
        quotient.append((poly[i] if i<len(poly) else 0)-(quotient[-1] if quotient else 0))
    return quotient[k]


def character_expected(pi,sigmas,r,s):
    seen=set();out=(-1)**(r*sum(pi[i]>pi[j] for i in range(len(pi)) for j in range(i+1,len(pi))))
    for i in range(len(pi)):
        if i in seen:continue
        C=[];j=i
        while j not in seen:seen.add(j);C.append(j);j=pi[j]
        rho=[]
        for a in range(s):
            b=a
            for j in C:b=sigmas[j][b]
            rho.append(b)
        out*=char_exterior_aug(rho,r-1)
    return out


def induced_map(pi,sigmas,m,s):
    n=1+m*(s+1);mapping=list(range(n))
    for i in range(m):
        u=1+i*(s+1);v=1+pi[i]*(s+1)
        mapping[u]=v
        for j in range(s):mapping[u+j+1]=v+sigmas[i][j]+1
    assert sorted(mapping)==list(range(n))
    return mapping


def char_actual(faces,n,mapping,m,r):
    total=0
    for F in faces:
        xs=[j for j in range(n) if F>>j&1]
        ys=[mapping[j] for j in xs]
        if sum(1<<j for j in ys)!=F:continue
        inv=sum(ys[i]>ys[j] for i in range(len(ys)) for j in range(i+1,len(ys)))
        total+=(-1)**(len(xs)+inv)
    return (-1)**(r*m)*total


def verify(m,s,r,all_group=True):
    n,faces=complex_faces(m,s,r)
    L,pairs,inc=link_matching(m,s,r,faces,n)
    betti,fs=rank_gf2(faces,n)
    exp={r*m-1:comb(s-1,r-1)**m}
    exp={k:v for k,v in exp.items() if v}
    assert betti==exp,(betti,exp)
    checks=0
    perms_s=list(permutations(range(s)))
    for pi in permutations(range(m)):
        for sigmas in product(perms_s,repeat=m):
            if not all_group and checks>25:break
            got=char_actual(faces,n,induced_map(pi,sigmas,m,s),m,r)
            want=character_expected(pi,sigmas,r,s)
            assert got==want,(m,s,r,pi,sigmas,got,want)
            checks+=1
        if not all_group and checks>25:break
    print(f'VERIFY_OK r={r} branches={m} leaves_per_branch={s} vertices={n} faces={len(faces)} face_vector={fs} link_faces={L} link_matching_pairs={pairs} link_Hasse_incidences={inc} link_acyclic=True reduced_GF2_betti={betti} character_elements_checked={checks}')

if __name__=='__main__':
    verify(3,3,3,True)
    verify(3,4,3,False)
    print('ALL_VERIFY_OK')

# Unequal branches check: independent enumeration of the complete induced-subgraph rule.
def verify_unequal(sizes=(3,3,4),r=3):
    m=len(sizes)
    n=1+m+sum(sizes)
    adj=[set() for _ in range(n)]
    centers=list(range(1,m+1)); leaves=[]; cursor=m+1
    for i,s in enumerate(sizes):
        u=centers[i];adj[0].add(u);adj[u].add(0)
        branch=list(range(cursor,cursor+s)); cursor+=s;leaves.append(branch)
        for v in branch:adj[u].add(v);adj[v].add(u)
    assert cursor==n
    faces=[]
    for F in range(1<<n):
        selected={v for v in range(n) if F>>v&1}; remaining=set(selected);ok=True
        while remaining:
            a=remaining.pop(); comp={a};queue=[a]
            while queue:
                x=queue.pop()
                for y in adj[x]&selected:
                    if y not in comp:comp.add(y);remaining.discard(y);queue.append(y)
            if len(comp)>r:ok=False;break
        if ok:faces.append(F)
    L={F for F in faces if not F&1 and F|1 in faces}
    pairs={}
    for F in L:
        used={i for i,u in enumerate(centers) if F>>u&1}
        assert len(used)<=r-1
        v=leaves[next(i for i in range(m) if i not in used)][0]
        assert F^(1<<v) in L
        if not F>>v&1:pairs[F]=F|(1<<v)
    assert 2*len(pairs)==len(L)
    indeg={F:0 for F in L};out=defaultdict(list)
    for F in L:
        for v in range(n):
            if F>>v&1:
                P=F^(1<<v)
                if P not in L:continue
                src,dst=(P,F) if pairs.get(P)==F else (F,P)
                out[src].append(dst);indeg[dst]+=1
    queue=deque(x for x in L if indeg[x]==0);visited=0
    while queue:
        a=queue.popleft();visited+=1
        for b in out[a]:
            indeg[b]-=1
            if indeg[b]==0:queue.append(b)
    assert visited==len(L)
    B=1
    for s in sizes:B*=comb(s-1,r-1)
    betti,_=rank_gf2(faces,n)
    assert betti==({m*r-1:B} if B else {})
    print(f'VERIFY_UNEQUAL_OK threshold={r} branches={sizes} faces={len(faces)} link_faces={len(L)} link_acyclic=True reduced_GF2_betti={betti}')

if __name__=='__main__':
    verify_unequal()
