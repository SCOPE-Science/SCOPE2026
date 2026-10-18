"""Finite computational checks of the cell-trace formula for two configurations on equal-arm theta graphs.
Requires Python 3 only; it does not replace the general proof.
"""
from itertools import permutations, combinations
from math import comb

def model(k):
    V = tuple(range(2+2*k))
    E = tuple(edge for i in range(k) for edge in ((0,2+2*i),(2+2*i,3+2*i),(3+2*i,1)))
    C0 = tuple(combinations(V,2))
    C1 = tuple((j,w) for j,(a,b) in enumerate(E) for w in V if w not in (a,b))
    C2 = tuple((i,j) for i,j in combinations(range(len(E)),2) if len(set(E[i]+E[j]))==4)
    return V,E,C0,C1,C2

def action(k,E,per,flip):
    def vmap(w):
        if w<2: return w ^ int(flip)
        i,t=divmod(w-2,2)
        return 2+2*per[i]+(t ^ int(flip))
    ei={frozenset(e):i for i,e in enumerate(E)}
    em=[];sign=[]
    for a,b in E:
        newa,newb=vmap(a),vmap(b)
        idx=ei[frozenset((newa,newb))]
        em.append(idx)
        sign.append(1 if (newa,newb)==E[idx] else -1)
    return vmap,em,sign

def character(k,per,flip):
    V,E,C0,C1,C2=model(k)
    vm,em,sgn=action(k,E,per,flip)
    c0=sum(1 for a,b in C0 if {vm(a),vm(b)}=={a,b})
    c1=sum(sgn[e] for e,w in C1 if em[e]==e and vm(w)==w)
    c2=sum(sgn[i]*sgn[j]*(1 if em[i]<em[j] else -1) for i,j in C2 if {em[i],em[j]}=={i,j})
    f1=sum(per[i]==i for i in range(k))
    f2=sum(i<j and per[i]==j and per[j]==i for i in range(k) for j in range(i+1,k))
    wanted=(-1 if flip else 1)*(comb(f1,2)-f2)
    assert 1-c0+c1-c2==wanted,(k,per,flip,c0,c1,c2,wanted)
    return (c0,c1,c2,wanted)

def rank_mod2(cols,nrows):
    basis={}
    for v in cols:
        while v:
            pivot=v.bit_length()-1
            if pivot in basis:v^=basis[pivot]
            else:
                basis[pivot]=v
                break
    return len(basis)

def homology_check(k):
    V,E,C0,C1,C2=model(k)
    ix0={c:i for i,c in enumerate(C0)}
    ix1={c:i for i,c in enumerate(C1)}
    b1=[];b2=[]
    for e,w in C1:
        a,b=E[e]
        b1.append((1<<ix0[tuple(sorted((a,w)))])^(1<<ix0[tuple(sorted((b,w)))]))
    for i,j in C2:
        a,b=E[i];x,y=E[j]
        col=0
        for row in ((j,a),(j,b),(i,x),(i,y)):col^=1<<ix1[row]
        b2.append(col)
    r1=rank_mod2(b1,len(C0));r2=rank_mod2(b2,len(C1))
    assert r1==len(C0)-1
    assert r2==len(C2)
    assert len(C1)-r1-r2==comb(k,2)
    assert all(sum((col>>i)&1 for i in range(len(C1)) if b1[i]&1)==0 for col in [])
    return(len(C0),len(C1),len(C2),r1,r2)

if __name__=='__main__':
    for k in range(3,7):
        m=homology_check(k)
        if k<=5:
            for p in permutations(range(k)):
                for t in (False,True):character(k,p,t)
        print('k',k,'cells',m[:3],'ranks',m[3:],'H1',comb(k,2),'H2',0,'CHAR_OK', k<=5)
    print('VERIFY_OK_THETA_TWO_PARTICLES')
