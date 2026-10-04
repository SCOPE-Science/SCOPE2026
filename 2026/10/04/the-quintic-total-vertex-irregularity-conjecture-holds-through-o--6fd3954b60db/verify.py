#!/usr/bin/env python3
import json
from itertools import combinations
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def pairs_and_index(n):
    pairs=[]; idx={}
    for i in range(n):
        for j in range(i+1,n):
            idx[(i,j)]=len(pairs); pairs.append((i,j))
    return pairs,idx


def erdos_gallai(seq):
    seq=sorted(seq, reverse=True)
    if sum(seq)%2: return False
    pref=0
    for k in range(1,len(seq)+1):
        pref += seq[k-1]
        if pref > k*(k-1)+sum(min(x,k) for x in seq[k:]):
            return False
    return True


def good_subgraph_and_labeling(G,H,n,pairs,inc):
    # d=5, s=3, r=2. The Shan--Zhong interval construction applies
    # when every H-degree class has size <=2, with at most one class of size 3.
    deg=[(H & inc[v]).bit_count() for v in range(n)]
    classes=[[v for v in range(n) if deg[v]==i] for i in range(6)]
    sizes=[len(c) for c in classes]
    if any(x>3 for x in sizes) or sum(x==3 for x in sizes)>1:
        return False
    exceptional=next((i for i,x in enumerate(sizes) if x==3), 6)
    vlabel=[None]*n
    for i,C in enumerate(classes):
        for ell,v in enumerate(C):
            vlabel[v]=1+ell+(1 if i>exceptional else 0)
            if not 1 <= vlabel[v] <= 3:
                return False
    weights=[]
    for v in range(n):
        edge_sum=0
        for k,(a,b) in enumerate(pairs):
            if a==v or b==v:
                edge_sum += 3 if ((H>>k)&1) else 1
        weights.append(edge_sum+vlabel[v])
    return len(set(weights))==n


def enumerate_and_check(n, cert_name, expected_count):
    data=json.loads((ROOT/cert_name).read_text())
    masks=data['masks']
    cdeg=n-1-5
    pairs,idx=pairs_and_index(n)
    allmask=(1<<len(pairs))-1
    inc=[]
    for v in range(n):
        m=0
        for k,(a,b) in enumerate(pairs):
            if a==v or b==v: m |= 1<<k
        inc.append(m)
    fixed=list(range(1,cdeg+1))
    C0=0
    for j in fixed: C0 |= 1<<idx[(0,j)]
    # residual degrees of complement after fixing N_C(0)={1,...,cdeg}
    deg=[0]+[cdeg-1]*cdeg+[cdeg]*(n-1-cdeg)
    count=0
    def rec(vdeg, Cmask):
        nonlocal count
        try:
            v=next(i for i in range(1,n) if vdeg[i]>0)
        except StopIteration:
            G=allmask ^ Cmask
            count += 1
            for F in masks:
                H=G & int(F)
                if good_subgraph_and_labeling(G,H,n,pairs,inc):
                    return
            raise AssertionError(f'no certificate for n={n}, completion #{count}, Gmask={G}')
        d=vdeg[v]
        cand=[u for u in range(v+1,n) if vdeg[u]>0]
        if len(cand)<d: return
        vdeg[v]=0
        for nbrs in combinations(cand,d):
            m=Cmask; ok=True
            for u in nbrs:
                vdeg[u]-=1; m |= 1<<idx[(v,u)]
                if vdeg[u]<0: ok=False
            if ok and erdos_gallai([vdeg[i] for i in range(v+1,n)]):
                rec(vdeg,m)
            for u in nbrs: vdeg[u]+=1
        vdeg[v]=d
    rec(deg,C0)
    assert count==expected_count,(n,count,expected_count)
    return count,len(masks)


def check_k6():
    n=6; pairs,idx=pairs_and_index(n)
    # all edges are present. High-edge mask 111 in lexicographic pair order;
    # vertex labels are 2,2,1,2,1,1.
    H=111; labels=[2,2,1,2,1,1]
    inc=[]
    for v in range(n):
        m=0
        for k,(a,b) in enumerate(pairs):
            if a==v or b==v:m|=1<<k
        inc.append(m)
    weights=[]
    for v in range(n):
        weights.append(5 + (H&inc[v]).bit_count() + labels[v])
    assert weights==[11,10,8,9,7,6]
    assert len(set(weights))==6
    return weights

if __name__=='__main__':
    w6=check_k6()
    c8,m8=enumerate_and_check(8,'cert8.json',167)
    c10,m10=enumerate_and_check(10,'cert10.json',527481)
    print('ALL CHECKS PASSED')
    print(f'K6 weights={w6}')
    print(f'n=8 fixed-neighborhood complement completions={c8}; certificate_masks={m8}')
    print(f'n=10 fixed-neighborhood complement completions={c10}; certificate_masks={m10}')
    print('Every simple 5-regular graph on at most 10 vertices is covered by relabeling.')
