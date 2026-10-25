#!/usr/bin/env python3
"""Independent three-round finite group signatures and four-variable boundary.
The infinite reduction is proved in the accompanying mathematical text.
"""
from collections import defaultdict

def group(n,minus):
    assert n >= 1
    N = 2**(2*n+1)
    def cocycle(v,w):
        r=0
        for i in range(n):
            a=(v>>(2*i))&1; b=(v>>(2*i+1))&1
            c=(w>>(2*i))&1; d=(w>>(2*i+1))&1
            r ^= a&d
            if minus and i==0: r ^= (a&c)^(b&d)
        return r
    table=[]
    for x in range(N):
        row=[]
        for y in range(N):
            row.append(((x//2^y//2)*2)+((x&1)^(y&1)^cocycle(x//2,y//2)))
        table.append(tuple(row))
    return tuple(table)

def atom(T,x,y,z):
    a=(x,y,z)
    return (tuple(v==0 for v in a),tuple(a[i]==a[j] for i,j in ((0,1),(0,2),(1,2))),tuple(T[a[i]][a[j]]==a[k] for i in range(3) for j in range(3) for k in range(3)))

def rank3(T):
    N=len(T)
    pairtypes={}
    for x in range(N):
        for y in range(N):
            pairtypes[(x,y)]=frozenset(atom(T,x,y,z) for z in range(N))
    pointed={x:frozenset(pairtypes[x,y] for y in range(N)) for x in range(N)}
    return frozenset(pointed.values()),pairtypes,pointed

def q4_boundary(T):
    # A Klein four whose three nonidentity elements all lack square roots.
    N=len(T);sq={T[x][x] for x in range(N)}
    for x in range(1,N):
        if T[x][x]!=0 or x in sq:continue
        for y in range(1,N):
            if y==x or T[y][y]!=0 or y in sq:continue
            z=T[x][y]
            if z not in (0,x,y) and T[z][z]==0 and z not in sq:return True
    return False

def xtype(T,x):
    if x==0:return 'identity'
    if x==1:return 'central_involution'
    return 'noncentral_involution' if T[x][x]==0 else 'order_four'

def main():
    sigs={}
    for n in (1,2):
        for minus in (False,True):
            T=group(n,minus)
            s,p,pointed=rank3(T)
            sigs[n,minus]=s
            labels={}
            for x,typ in pointed.items():labels.setdefault(xtype(T,x),set()).add(typ)
            assert all(len(v)==1 for v in labels.values())
            print(f'GROUP_OK degree={n} sign={"minus" if minus else "plus"} size={len(T)} pointed_types={len(s)}')
            if n==2:
                counts={k:len(next(iter(v))) for k,v in labels.items()}
                assert counts=={'identity':4,'central_involution':4,'order_four':8,'noncentral_involution':7},counts
                print('STABLE_PAIR_PROFILE_SIZES_OK identity=4 central=4 noncentral_involution=7 order_four=8')
                assert q4_boundary(T)==(not minus)
                print(f'RANK_FOUR_ARF_WITNESS_OK sign={"minus" if minus else "plus"} truth={not minus}')
    assert sigs[2,False]==sigs[2,True]
    assert len({sigs[k] for k in sigs})==3
    print('THREE_THEORIES_FOR_TESTED_GROUPS_OK')
    print('VERIFY_SYMBOLIC_OK')

if __name__=='__main__':main()
