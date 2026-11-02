#!/usr/bin/env python3
"""Independent bitboard-generation and exchange adjacency verification."""
import collections
import json
import sys

N=8
MASK=(1<<N)-1

def all_placements():
    out=[]
    def visit(row, cols, diag_down, diag_up, placement):
        if row==N:
            out.append(placement)
            return
        available=MASK & ~(cols | diag_down | diag_up)
        while available:
            bit=available & -available
            available-=bit
            visit(row+1,cols|bit,((diag_down|bit)<<1)&MASK,(diag_up|bit)>>1,
                  placement|(bit<<(N*row)))
    visit(0,0,0,0,0)
    return sorted(out)

def d_batch(x,y):
    diff=x^y
    assert diff.bit_count()%2==0
    return diff.bit_count()//2

def neighborhoods(states,threshold):
    n=len(states)
    a=[set() for _ in states]
    for i in range(n):
        for j in range(i):
            if d_batch(states[i],states[j])<=threshold:
                a[i].add(j);a[j].add(i)
    return a

def comps(a):
    seen=set();sizes=[]
    for start in range(len(a)):
        if start in seen:continue
        todo=[start];seen.add(start)
        for u in todo:
            for v in a[u]:
                if v not in seen:seen.add(v);todo.append(v)
        sizes.append(len(todo))
    return sorted(sizes,reverse=True)

def radius_and_distances(a):
    ecc=[];pairs=collections.Counter()
    for start in range(len(a)):
        depth={start:0};front=[start]
        while front:
            nxt=[]
            for u in front:
                for v in a[u]:
                    if v not in depth:
                        depth[v]=depth[u]+1;nxt.append(v)
            front=nxt
        if len(depth)!=len(a):return None
        ecc.append(max(depth.values()))
        pairs.update({d:sum(1 for j in range(start) if depth[j]==d) for d in set(depth.values()) if d>0})
    return collections.Counter(ecc),pairs

def main():
    board_states=all_placements()
    assert len(board_states)==92
    qs=set()
    for state in board_states:
        p=[]
        for row in range(N):
            field=(state>>(N*row))&MASK
            assert field.bit_count()==1
            p.append(field.bit_length()-1)
        assert sorted(p)==list(range(N))
        assert len(set(i+p[i] for i in range(N)))==N
        assert len(set(i-p[i] for i in range(N)))==N
        qs.add(tuple(p))
    assert len(qs)==92
    C=collections.Counter(d_batch(board_states[i],board_states[j]) for i in range(92) for j in range(i))
    assert C=={2:8,3:32,4:128,5:296,6:824,7:1272,8:1626}
    a4=neighborhoods(board_states,4)
    a5=neighborhoods(board_states,5)
    assert sum(map(len,a4))//2==168
    assert comps(a4)==[84,2,2,2,2]
    assert sum(map(len,a5))//2==464
    assert comps(a5)==[92]
    a_exact5=[set() for _ in board_states]
    for i in range(92):
        for j in range(i):
            if d_batch(board_states[i],board_states[j])==5:
                a_exact5[i].add(j);a_exact5[j].add(i)
    assert sum(map(len,a_exact5))//2==296
    assert comps(a_exact5)==[92]
    exstats=radius_and_distances(a_exact5)
    assert exstats is not None
    assert exstats[0]=={4:68,5:24}
    assert exstats[1]=={1:296,2:1178,3:1968,4:720,5:24}
    stats=radius_and_distances(a5)
    assert stats is not None
    ec,dd=stats
    assert ec=={3:68,4:24}
    assert dd=={1:464,2:2002,3:1704,4:16}
    # Independent validation of the bundled all-pairs certificate.
    if len(sys.argv)>1:
        with open(sys.argv[1],encoding='utf8') as f:cert=json.load(f)
        mapped=[]
        for s in cert['solutions']:
            mapped.append(sum(1<<(N*r+c) for r,c in enumerate(s)))
        assert set(mapped)==set(board_states)
        ma={s:i for i,s in enumerate(board_states)}
        for i,s in enumerate(mapped):
            for threshold,key in ((4,'neighbors_at_most_four'),(5,'neighbors_at_most_five')):
                claimed={ma[mapped[j]] for j in cert[key][i]}
                assert claimed==neighborhoods_ref(board_states,ma[s],threshold)
        assert [len(comp) for comp in cert['components_at_most_four']]==[84,2,2,2,2]
    print('BITBOARD_INDEPENDENT_PASS')
    print('states=92 at_most_four_components=[84,2,2,2,2] at_most_five_connected=1')
    print('at_most_five_edges=464 radius=3 diameter=4 pair_distances='+str(dict(sorted(dd.items()))))
    print('exactly_five_edges=296 connected=1 radius=4 diameter=5')

def neighborhoods_ref(states,i,k):
    return {j for j,s in enumerate(states) if i!=j and d_batch(states[i],s)<=k}
if __name__=='__main__':main()
