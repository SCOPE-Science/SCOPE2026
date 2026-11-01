#!/usr/bin/env python3
"""Independent finite checks of centered furtherness persistent homology on nonempty subset posets.
All calculations here use a direct simplicial boundary-matrix reduction, separate
from the proof's filtered change of basis. Standard library only.
"""
from itertools import combinations
from collections import Counter
from math import comb

def face_time(mask, S):
    a = (mask & S).bit_count()
    b = mask.bit_count() - a
    return (1 << a) * ((1 << b) - 1)

def direct_barcode(n, S, p):
    cells = sorted(range(1, 1 << n), key=lambda m: (face_time(m,S), m.bit_count(), m))
    idx = {m:i for i,m in enumerate(cells)}
    columns=[]; lowest={}; pairs=[]; essential=[]
    for j,m in enumerate(cells):
        verts=[i for i in range(n) if (m >> i)&1]
        col = {}
        if len(verts)>1:
            for sign,i in enumerate(verts):
                lower=m^(1<<i)
                col[idx[lower]]= (-1 if sign%2 else 1)%p
        while col:
            pivot=max(col)
            if pivot not in lowest:break
            k=lowest[pivot]
            den=columns[k][pivot]
            fac=col[pivot]*pow(den,-1,p)%p
            for row,c in columns[k].items():
                v=(col.get(row,0)-fac*c)%p
                if v:col[row]=v
                else:col.pop(row,None)
        columns.append(col)
        if col:
            lowest[max(col)]=j
            birth=cells[max(col)]
            if face_time(birth,S)<face_time(m,S):
                pairs.append(((birth.bit_count()-1),face_time(birth,S),face_time(m,S)))
    births=set(lowest)
    for j,m in enumerate(cells):
        if not columns[j] and j not in births:
            essential.append((m.bit_count()-1,face_time(m,S)))
    return Counter(pairs),Counter(essential)

def predicted(n,S):
    v=next(i for i in range(n) if S&(1<<i))
    wanted=Counter()
    for m in range(1,1<<n):
        if m&(1<<v): continue
        t=face_time(m,S)
        if t>0:wanted[(m.bit_count()-1,t,2*t)]+=1
    return wanted

def check_triangular(n,S):
    v=next(i for i in range(n) if S&(1<<i))
    for m in range(1,1<<n):
        if m&(1<<v):continue
        t=face_time(m,S)
        assert face_time(m|(1<<v),S)==2*t if t else face_time(m|(1<<v),S)==0
        for i in range(n):
            if m & (1<<i):
                face=m^(1<<i)
                if face:
                    assert face_time(face|(1<<v),S)<=t
    return True


def actual_order_barcodes(n, S, p=2):
    """Compute persistence directly on the order complex, not its unsusbdivided face complex."""
    from itertools import combinations
    elements=list(range(1,1<<n))
    # Enumerate strict subset chains recursively.
    chains=[]
    def extend(chain, last):
        chains.append(chain)
        for sup in elements:
            if (sup & last)==last and sup!=last:
                extend(chain+(sup,),sup)
    for m in elements:extend((m,),m)
    chains.sort(key=lambda ch:(face_time(ch[-1], S),len(ch),ch))
    idx={ch:j for j,ch in enumerate(chains)}
    columns=[]; lowest={}; bars=Counter(); ess=Counter()
    for j,ch in enumerate(chains):
        col={}
        if len(ch)>1:
            for i in range(len(ch)):
                k=idx[ch[:i]+ch[i+1:]]
                col[k]=(-1 if i%2 else 1)%p
        while col:
            pivot=max(col)
            if pivot not in lowest:break
            k=lowest[pivot]
            factor=col[pivot]*pow(columns[k][pivot],-1,p)%p
            for row,c in columns[k].items():
                vv=(col.get(row,0)-factor*c)%p
                if vv:col[row]=vv
                else:col.pop(row,None)
        columns.append(col)
        if col:
            pivot=max(col);lowest[pivot]=j
            bt=face_time(chains[pivot][-1],S)
            dt=face_time(ch[-1],S)
            if bt<dt:bars[(len(chains[pivot])-1,bt,dt)]+=1
    births=set(lowest)
    for j,ch in enumerate(chains):
        if not columns[j] and j not in births:
            ess[(len(ch)-1,face_time(ch[-1],S))]+=1
    return bars,ess,len(chains)

def main():
    num_cases=0; comparisons=0; cell_count=0; total_positive=0
    for n in range(2,9):
        for s in range(1,n+1):
            S=(1<<s)-1
            check_triangular(n,S)
            expected=predicted(n,S)
            closed=Counter()
            for a in range(s):
                for b in range(1,n-s+1):
                    t=(1<<a)*((1<<b)-1)
                    closed[(a+b-1,t,2*t)]+=comb(s-1,a)*comb(n-s,b)
            assert expected==closed,(n,s,'closed formula mismatch',expected,closed)
            for p in (2,3,5):
                got,essential=direct_barcode(n,S,p)
                assert got==expected,(n,s,p,'barcode mismatch',got-expected,expected-got)
                assert essential==Counter({(0,0):1}), (n,s,p,'essential mismatch',essential)
                comparisons+=1
            num_cases+=1;cell_count+=(1<<n)-1; total_positive+=sum(expected.values())
    order_chains=0; order_cases=0
    for n in range(2,6):
        for s in range(1,n+1):
            S=(1<<s)-1
            bars,ess,count=actual_order_barcodes(n,S,2)
            assert bars==predicted(n,S),(n,s,'order-complex bars',bars,predicted(n,S))
            assert ess==Counter({(0,0):1}),(n,s,'order-complex essential',ess)
            order_cases+=1;order_chains+=count
    print(f'ORDER_COMPLEX_OK cases={order_cases} chains={order_chains}')
    print(f'VERIFY_OK n2..8 cases={num_cases} direct_field_reductions={comparisons} simplices_examined={cell_count} positive_bars={total_positive} boundary_primes=(2,3,5)')

if __name__=='__main__':main()
