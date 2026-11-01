#!/usr/bin/env python3
"""Finite independent cellular checks for complete-graph Hom complexes.
Only mathematical data and reproducibility; no network access needed.
"""
from itertools import permutations, product
from collections import defaultdict
from math import comb, factorial


def cycles(p):
    unseen=set(range(len(p))); out=[]
    while unseen:
        i=min(unseen); cy=[]; j=i
        while j in unseen:
            unseen.remove(j); cy.append(j); j=p[j]
        out.append(tuple(cy))
    return out


def parity(p):
    return (-1)**(len(p)-len(cycles(p)))


def formula(m,n,s,p):
    src=[len(c) for c in cycles(s)]
    tgt=[len(c) for c in cycles(p)]
    v=0
    for mask in range(1<<len(src)):
        active=[src[i] for i in range(len(src)) if mask>>i&1]
        q=1
        for L in tgt:
            q*=1-sum(a for a in active if L%a==0)
        v+=(-1)**(len(src)-len(active))*q
    return ((-1)**m)*parity(s)*v


def cell_list(m,n):
    C=defaultdict(list)
    for x in product(range(m+1),repeat=n):
        if set(range(1,m+1)).issubset(x):
            C[sum(t>0 for t in x)-m].append(x)
    return dict(C)


def transform(x,s,p):
    r=[0]*len(x)
    for c,i in enumerate(x):
        r[p[c]]=s[i-1]+1 if i else 0
    return tuple(r)


def fixed_signed_cell_sum(m,n,s,p,C):
    acc=0
    for d,cl in C.items():
        for x in cl:
            if transform(x,s,p)!=x:
                continue
            selected=[i for i,t in enumerate(x) if t]
            # parity of action on used color coordinates
            perm=[selected.index(p[i]) for i in selected]
            acc+=(-1)**d * parity(perm)*parity(s)
    return acc


def boundaries(m,n,C):
    bydim={d:{x:i for i,x in enumerate(rows)} for d,rows in C.items()}
    result={}
    for d in sorted(C):
        if d==0: continue
        B=[]
        for x in C[d]:
            col={}; pre=0
            for i in range(1,m+1):
                elements=[j for j,a in enumerate(x) if a==i]
                if len(elements)>1:
                    for index,j in enumerate(elements):
                        y=list(x);y[j]=0
                        row=bydim[d-1][tuple(y)]
                        col[row]=(-1)**(pre+index)
                pre+=len(elements)-1
            B.append(col)
        result[d]=B
    return result


def rank_mod(columns,p=1000003):
    piv={}
    for col in columns:
        v={k:(a%p) for k,a in col.items() if a%p}
        while v:
            idx=min(v)
            if idx not in piv:
                fac=pow(v[idx],-1,p)
                piv[idx]={k:a*fac%p for k,a in v.items()}
                break
            q=v.pop(idx)
            for k,a in piv[idx].items():
                if k==idx: continue
                b=(v.get(k,0)-q*a)%p
                if b: v[k]=b
                else: v.pop(k,None)
    return len(piv)


def check_case(m,n):
    C=cell_list(m,n)
    bd=boundaries(m,n,C)
    # Every cellular boundary composition must vanish exactly over the integers.
    for d in bd:
        if d<2: continue
        for upper in bd[d]:
            accum=defaultdict(int)
            for middle,coef in upper.items():
                for lower,c in bd[d-1][middle].items():
                    accum[lower]+=coef*c
            assert all(v==0 for v in accum.values()), (m,n,d,accum)
    rr={d:rank_mod(B) for d,B in bd.items()}
    betti={d:len(C[d])-rr.get(d,0)-rr.get(d+1,0) for d in C}
    beta=betti.get(n-m,0)
    pred=(-1)**(n-m)*(formula(m,n,tuple(range(m)),tuple(range(n)))-1)
    assert betti.get(0)==1 and beta==pred
    assert all(v==0 for d,v in betti.items() if d not in (0,n-m))
    # Distinct actions including nontrivial simultaneous source & target permutations.
    group=0
    for s in permutations(range(m)):
        for p in permutations(range(n)):
            got=fixed_signed_cell_sum(m,n,s,p,C)
            want=formula(m,n,s,p)
            assert got==want,(m,n,s,p,got,want)
            group+=1
    print(f'CASE m={m} n={n}; cells={tuple(len(C[i]) for i in sorted(C))}; ranks={rr}; betti={betti}; actions={group} OK')


def subgroup_checks():
    for m,n in [(2,4),(3,4),(3,5),(4,5),(3,6),(4,6)]:
        si=tuple(range(m))
        vals=[(parity(p),(-1)**(n-m)*(formula(m,n,si,p)-1)) for p in permutations(range(n))]
        assert sum(v for sg,v in vals)%factorial(n)==0
        assert sum(sg*v for sg,v in vals)%factorial(n)==0
        triv=sum(v for sg,v in vals)//factorial(n)
        sgn=sum(sg*v for sg,v in vals)//factorial(n)
        assert triv==0,(m,n,triv)
        assert sgn==comb(n-2,m-2),(m,n,sgn)
        print(f'QUOTIENT m={m} n={n}; full-invariants={triv}; alternating-invariants={triv+sgn} OK')

if __name__=='__main__':
    for c in ((2,4),(3,4),(3,5),(4,5)):
        check_case(*c)
    subgroup_checks()
    print('HOM_COMPLETE_GRAPH_EQUIVARIANT_CHARACTER_OK')
