#!/usr/bin/env python3
"""Standalone finite tests for higher-independence homology of double-star trees.
Exhaustively enumerate induced-component faces and mod-2 boundaries.
Cross-check automorphism traces via signed fixed simplices.
"""
from itertools import combinations, permutations, product
from math import comb

def pop(m): return m.bit_count()

def make_faces(a,b,r):
    t=a+b; N=t+2; u=t; v=t+1
    nbr=[0]*N
    for x in range(a):nbr[x]|=1<<u;nbr[u]|=1<<x
    for x in range(a,t):nbr[x]|=1<<v;nbr[v]|=1<<x
    nbr[u]|=1<<v;nbr[v]|=1<<u
    out={0:None}
    for mask in range(1,1<<N):
        unseen=mask; good=True
        while unseen:
            start=unseen&-unseen; comp=start
            while True:
                tmp=comp; vicinity=0
                while tmp:
                    bit=tmp&-tmp;tmp-=bit;vicinity|=nbr[bit.bit_length()-1]
                new=comp|(vicinity&mask)
                if new==comp:break
                comp=new
            if pop(comp)>r:good=False;break
            unseen &= ~comp
        if good:out[mask]=None
    F={}
    for mask in out:F.setdefault(pop(mask)-1,[]).append(mask)
    return F

def rank2(F,d):
    rows={m:i for i,m in enumerate(F.get(d-1,[]))}
    piv={}
    for mask in F.get(d,[]):
        z=0;s=mask
        while s:
            bit=s&-s;s-=bit;z ^= (1<<rows[mask^bit])
        while z:
            j=z.bit_length()-1
            if j in piv:z^=piv[j]
            else:piv[j]=z;break
    return len(piv)

def b2(F):
    ranks={d:rank2(F,d) for d in F if d>=0}
    return {d:len(F[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in F if d>=0}

def leaf_det_char(p,k):
    t=len(p);seen=set();coeff=[1]
    for x in range(t):
        if x in seen:continue
        cur=x;ln=0
        while cur not in seen:seen.add(cur);ln+=1;cur=p[cur]
        new=coeff+[0]*ln
        for i,x in enumerate(coeff):new[i+ln]+=(-1)**(ln+1)*x
        coeff=new
    # Divide by (1+z), since permutation module = augmentation + trivial
    quo=[];prev=0
    for c in coeff:
        v=c-prev;quo.append(v);prev=v
    assert quo[-1]==0
    return quo[k] if k<len(quo) else 0

def Lefschetz(F,p):
    total=0;N=len(p)
    for d,ms in F.items():
        for mask in ms:
            verts=[i for i in range(N) if mask>>i&1]
            if {p[i] for i in verts}!=set(verts):continue
            seq=[p[i] for i in verts]
            inv=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
            total+=(-1)**(len(verts)-1+inv)
    return total

def check(a,b,r):
    F=make_faces(a,b,r);betti=b2(F);need=comb(a+b-1,r-2) if r-2<=a+b-1 else 0
    assert betti.get(r-1,0)==need,(a,b,r,betti,need)
    assert all(v==0 for d,v in betti.items() if d!=r-1),(a,b,r,betti)
    t=a+b;u=t;v=t+1
    for pa in permutations(range(a)):
      for pb in permutations(range(a,t)):
        lp=list(pa)+list(pb);p=lp+[u,v]
        want=leaf_det_char(lp,r-2)
        actual=(-1)**(r-1)*Lefschetz(F,p)
        assert want==actual,('within',a,b,r,lp,actual,want)
        if a==b:
            swaps=[*range(a,t),*range(a),v,u]
            q=[swaps[p[i]] for i in range(t+2)]
            lpq=q[:t];want=-leaf_det_char(lpq,r-2)
            actual=(-1)**(r-1)*Lefschetz(F,q)
            assert want==actual,('swap',a,b,r,lpq,actual,want)
    return len(F),sum(map(len,F.values()))

if __name__=='__main__':
    total=0
    for a,b in product(range(1,4),repeat=2):
      for r in range(2,a+b+3):
        check(a,b,r);total+=1
    print(f'DOUBLE_STAR_HIGHER_INDEPENDENCE_CHECKS_PASSED {total} cases; homology and all branch automorphisms')
