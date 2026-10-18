#!/usr/bin/env python3
"""Finite integral cellular-chain and fundamental-group checks for a multipath complex."""
from itertools import combinations
from collections import Counter
from pathlib import Path

ARCS = [(i, 3+j) for i in range(3) for j in range(3)] + [(3+j, i) for j in range(3) for i in range(3)]
BASE = Path(__file__).resolve().parent

def valid(inds):
    indeg = [0]*6; outdeg=[0]*6; nxt={}
    for ix in inds:
        u,v=ARCS[ix]; indeg[v]+=1; outdeg[u]+=1
        if indeg[v]>1 or outdeg[u]>1:return False
        nxt[u]=v
    for u in nxt:
        x=u;seen=set()
        while x in nxt:
            if x in seen:return False
            seen.add(x);x=nxt[x]
    return True

def faces():
    groups={k:[] for k in range(1,6)}
    for k in range(1,6):
        groups[k]=sorted(sum(1<<a for a in inds) for inds in combinations(range(18),k) if valid(inds))
    return groups

def build_boundary(F):
    return {k:{f:{f^(1<<a):(-1)**j for j,a in enumerate(i for i in range(18) if f>>i&1)} for f in F[k]} for k in range(2,6)}

def check_chain(M):
    for k in range(3,6):
        for col,lower in M[k].items():
            composition={}
            for mid,c in lower.items():
                for row,d in M[k-1][mid].items():
                    composition[row]=composition.get(row,0)+c*d
            assert all(v==0 for v in composition.values()),(k,col,composition)

def markowitz(C,M):
    best=None
    for k in range(2,6):
        rows={}
        for col,vec in M[k].items():
            for row,val in vec.items():rows.setdefault(row,[]).append((col,val))
        for row,inc in rows.items():
            for col,v in inc:
                if abs(v)!=1:continue
                score=((len(inc)-1)*(len(M[k][col])-1),len(inc)+len(M[k][col]),k,row,col)
                if best is None or score < best[0]:best=(score,k,row,col,v,rows)
    return best

def cancel(C,M,k,row,col,v,rows):
    assert abs(v)==1 and row in C[k-1] and col in C[k]
    pivot=M[k][col]
    for other,entry in rows[row]:
        if other==col:continue
        coeff=entry//v
        target=M[k][other]
        for lower,a in pivot.items():
            nv=target.get(lower,0)-coeff*a
            if nv:target[lower]=nv
            else:target.pop(lower,None)
    del M[k][col]
    for other,_ in rows[row]:
        if other!=col:M[k][other].pop(row,None)
    C[k].remove(col);C[k-1].remove(row)
    if k<5:
        for _,target in M[k+1].items():target.pop(col,None)
    if k>2:del M[k-1][row]

def fundamental_group(F):
    edges=F[2]; triangles=F[3]
    parent=list(range(18))
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    tree=set()
    for mask in edges:
        i,j=[x for x in range(18) if mask>>x&1]
        a,b=root(i),root(j)
        if a!=b:parent[a]=b;tree.add(mask)
    assert len(tree)==17
    dead=set(tree); rounds=[]
    while True:
        batch=set()
        for t in triangles:
            bits=[a for a in range(18) if t>>a&1]
            edges_of_t={(1<<bits[i])|(1<<bits[j]) for i,j in ((0,1),(0,2),(1,2))}
            unknown=edges_of_t-dead
            if len(unknown)==1:batch.update(unknown)
        batch-=dead
        if not batch:break
        dead.update(batch);rounds.append(len(batch))
    assert len(dead)==len(edges)==108 and rounds==[46,7,12,19,7]
    return len(tree),rounds

def main():
    F=faces(); counts=[1]+[len(F[k]) for k in range(1,6)]
    assert counts==[1,18,108,264,252,72],counts
    tree,rounds=fundamental_group(F)
    C={k:set(F[k]) for k in F};M=build_boundary(F)
    check_chain(M)
    written=[];pivot_counts=Counter()
    while True:
        best=markowitz(C,M)
        if best is None:break
        _,k,row,col,v,rows=best
        written.append((k,row,col,v));pivot_counts[k]+=1
        cancel(C,M,k,row,col,v,rows)
    check_chain(M)
    assert len(written)==341 and dict(pivot_counts)=={2:17,3:91,4:173,5:60}
    rem={k:len(C[k]) for k in range(1,6)}
    assert rem=={1:1,2:0,3:0,4:19,5:12},rem
    assert all(not vec for d in M.values() for vec in d.values())
    output='degree,lower_mask,upper_mask,pivot\n'+''.join(f'{k},{row},{col},{v}\n' for k,row,col,v in written)
    cert=BASE/'certificates'/'unit_pivots.csv'
    assert cert.read_text(encoding='utf8')==output,'The explicit 341-unit-pivot certificate differs.'
    print('arc_count:',len(ARCS))
    print('face_counts_including_empty:',counts)
    print('euler_characteristic:',sum((-1)**(k-1)*len(F[k]) for k in range(1,6)))
    print('fundamental_group_tree_edges:',tree)
    print('fundamental_group_triangle_kill_rounds:',rounds)
    print('unit_pivot_counts_by_degree:',dict(sorted(pivot_counts.items())))
    print('remaining_free_groups_Ck_face_size:',rem)
    print('all_remaining_boundary_matrices_zero:',True)
    print('integral_reduced_homology: H3=Z^19 H4=Z^12 all others zero')
    print('certificate_recomputed_and_matched:',True)

if __name__=='__main__':main()
