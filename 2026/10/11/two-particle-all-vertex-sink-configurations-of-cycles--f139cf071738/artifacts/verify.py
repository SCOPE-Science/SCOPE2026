#!/usr/bin/env python3
from collections import defaultdict

def rank_mod(rows, ncols, p):
    A=[{j:(v%p) for j,v in r.items() if v%p} for r in rows]
    rank=0
    for col in range(ncols):
        piv=None
        for i in range(rank,len(A)):
            if A[i].get(col,0)%p:
                piv=i; break
        if piv is None: continue
        A[rank],A[piv]=A[piv],A[rank]
        inv=pow(A[rank][col],-1,p)
        A[rank]={j:(v*inv)%p for j,v in A[rank].items() if (v*inv)%p}
        for i in range(len(A)):
            if i==rank: continue
            c=A[i].get(col,0)%p
            if not c: continue
            nr=dict(A[i])
            for j,v in A[rank].items():
                nv=(nr.get(j,0)-c*v)%p
                if nv: nr[j]=nv
                elif j in nr: del nr[j]
            A[i]=nr
        rank+=1
        if rank==len(A): break
    return rank

def build(m):
    # C0: (vertex,vertex); C1: A(edge,vertex), B(vertex,edge);
    # C2: E(edge_i,edge_j), i != j. Indices are modulo m.
    c0=[(i,j) for i in range(m) for j in range(m)]
    c1=[('A',i,j) for i in range(m) for j in range(m)] + [('B',i,j) for i in range(m) for j in range(m)]
    c2=[(i,j) for i in range(m) for j in range(m) if i!=j]
    i0={x:k for k,x in enumerate(c0)}; i1={x:k for k,x in enumerate(c1)}
    d1=[defaultdict(int) for _ in c0] # rows C0 x cols C1, stored rows
    for col,x in enumerate(c1):
        t,i,j=x
        if t=='A':
            d1[i0[((i+1)%m,j)]][col]+=1; d1[i0[(i,j)]][col]-=1
        else:
            d1[i0[(i,(j+1)%m)]][col]+=1; d1[i0[(i,j)]][col]-=1
    d2=[defaultdict(int) for _ in c1] # rows C1 x cols C2
    for col,(i,j) in enumerate(c2):
        # d(e_i x e_j)= (de_i)x e_j - e_i x(de_j)
        d2[i1[('B',(i+1)%m,j)]][col]+=1
        d2[i1[('B',i,j)]][col]-=1
        d2[i1[('A',i,(j+1)%m)]][col]-=1
        d2[i1[('A',i,j)]][col]+=1
    return c0,c1,c2,d1,d2

def check_dd(m,c0,c1,c2,d1,d2):
    # verify d1*d2=0 columnwise using sparse rows transposed on demand
    cols_d1=[defaultdict(int) for _ in c1]
    for r,row in enumerate(d1):
        for c,v in row.items(): cols_d1[c][r]=v
    for col2 in range(len(c2)):
        total=defaultdict(int)
        for r1,row in enumerate(d2):
            coeff=row.get(col2,0)
            if coeff:
                for r0,v in cols_d1[r1].items(): total[r0]+=coeff*v
        if any(total.values()): return False
    return True

def swap_traces(m,c0,c1,c2):
    tr0=sum(1 for i,j in c0 if i==j)
    # A(i,j) <-> B(j,i): no C1 basis cell is fixed.
    tr1=0
    # E(i,j) -> -E(j,i), but i != j, so no C2 basis cell is fixed.
    tr2=0
    return tr0,tr1,tr2

for m in range(3,13):
    c0,c1,c2,d1,d2=build(m)
    assert check_dd(m,c0,c1,c2,d1,d2)
    expected_r1=m*m-1
    expected_r2=m*(m-1)
    ranks=[]
    for p in (2,3,5,7):
        r1=rank_mod(d1,len(c1),p)
        r2=rank_mod(d2,len(c2),p)
        assert (r1,r2)==(expected_r1,expected_r2),(m,p,r1,r2)
        ranks.append((p,r1,r2))
    b0=len(c0)-expected_r1
    b1=len(c1)-expected_r1-expected_r2
    b2=len(c2)-expected_r2
    assert (b0,b1,b2)==(1,m+1,0)
    tr=swap_traces(m,c0,c1,c2)
    L=tr[0]-tr[1]+tr[2]
    trH1=1-L
    plus=(b1+trH1)//2; minus=(b1-trH1)//2
    assert (trH1,plus,minus)==(1-m,1,m)
    print(f"m={m}: cells=({len(c0)},{len(c1)},{len(c2)}), ranks=({expected_r1},{expected_r2}) mod 2,3,5,7, Betti=(1,{m+1},0), chain_trace={tr}, H1_trace={1-m}, eigendims=(+1:{plus},-1:{minus})")
print('VERIFY_OK')
