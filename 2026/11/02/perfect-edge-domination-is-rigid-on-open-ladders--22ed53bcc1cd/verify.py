#!/usr/bin/env python3
"""Independent direct edge-subset test and finite transition certificate."""
from collections import defaultdict
from math import comb

def edge_list(n):
    vertices=[(row,j) for j in range(n) for row in range(2)]
    E=[((0,j),(1,j)) for j in range(n)]
    E += [((row,j),(row,j+1)) for j in range(n-1) for row in range(2)]
    return E

def brute(n):
    E=edge_list(n)
    nei=[sum(1<<j for j,f in enumerate(E) if j!=i and len(set(e)&set(f))>0) for i,e in enumerate(E)]
    counts=defaultdict(int)
    for mask in range(1<<len(E)):
        if all((mask>>i)&1 or (mask&nei[i]).bit_count()==1 for i in range(len(E))):
            counts[mask.bit_count()]+=1
    return dict(sorted(counts.items()))

def good(p,c,t,final=False):
    C=c&1; a=(c>>1)&1; b=(c>>2)&1
    pa=(p>>1)&1;pb=(p>>2)&1
    ta=(t>>1)&1;tb=(t>>2)&1;T=t&1
    if not C and pa+pb+a+b != 1:return False
    if not final:
        if not a and pa+C+T+ta!=1:return False
        if not b and pb+C+T+tb!=1:return False
    return True

def automaton():
    states=[(p,c) for p in range(8) for c in range(8)]
    E={st:[(st[1],n) for n in range(8) if good(st[0],st[1],n)] for st in states}
    start={(0,c) for c in range(8)}
    end={(p,c) for p in range(8) for c in (0,1) if good(p,c,0,final=True)}
    def closure(seed,adj):
        seen=set(seed);todo=list(seed)
        for x in todo:
            for y in adj[x]:
                if y not in seen:seen.add(y);todo.append(y)
        return seen
    backwards={x:[] for x in states}
    for x,ys in E.items():
        for y in ys:backwards[y].append(x)
    relevant=closure(start,E)&closure(end,backwards)
    expected={
      (0,1):[], (0,2):[(2,1),(2,3)],(0,3):[(3,0)],
      (0,4):[(4,1),(4,5)],(0,5):[(5,0)],
      (0,7):[(7,1),(7,7)], (2,1):[],(2,3):[(3,0)],
      (3,0):[(0,4)],(4,1):[],(4,5):[(5,0)],
      (5,0):[(0,2)],(7,1):[],(7,7):[(7,1),(7,7)]}
    assert relevant==set(expected), (relevant^set(expected))
    for st, successors in expected.items():assert sorted(x for x in E[st] if x in relevant)==sorted(successors)
    assert start&relevant=={(0,1),(0,2),(0,3),(0,4),(0,5),(0,7)}
    assert end&relevant=={(0,1),(2,1),(3,0),(4,1),(5,0),(7,1)}
    return E,start,end,relevant

def dp(n):
    E,start,end,_=automaton()
    ways={(0,c):{c.bit_count():1} for c in range(8) if n>=2}
    for _ in range(1,n):
        nxt=defaultdict(lambda:defaultdict(int))
        for st,poly in ways.items():
            for y in E[st]:
                for exponent,coefficient in poly.items():nxt[y][exponent+y[1].bit_count()]+=coefficient
        ways=nxt
    out=defaultdict(int)
    for st,poly in ways.items():
        if st in end:
            for e,c in poly.items():out[e]+=c
    return dict(sorted(out.items()))

def formula(n):
    return {n:2+(2 if n%3==2 else 0), 3*n-2:1}

if __name__=='__main__':
    automaton()
    checks=0
    for n in range(2,8):
        assert brute(n)==formula(n)==dp(n),(n,brute(n),dp(n));checks+=1
    for n in range(8,161):assert dp(n)==formula(n),n
    print('VERIFY_OK direct_ladder_lengths=2..7 checked_edge_subsets='+str(sum(2**(3*n-2) for n in range(2,8)))+' finite_relevant_states='+str(len(automaton()[3]))+' transfer_lengths=2..160')
