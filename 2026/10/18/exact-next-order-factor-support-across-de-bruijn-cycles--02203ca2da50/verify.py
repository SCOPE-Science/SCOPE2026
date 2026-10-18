#!/usr/bin/env python3
"""Check the proposed next-window spectrum using graph contractions.
The script reconstructs witness cycles and verifies every cyclic n-window.
"""
from itertools import product

def expected_forbidden(q,n):
    chars=[str(i) for i in range(q)]
    out={a*(n+1) for a in chars}
    if q==2:
        out.update({'0'+'1'*(n-1)+'0','1'+'0'*(n-1)+'1'})
    return out

def graph(q,n):
    verts=[''.join(t) for t in product('0123456789'[:q],repeat=n-1)]
    E=[]
    for v in verts:
        for c in '0123456789'[:q]:
            label=v+c
            E.append((label[:-1],label[1:],label))
    return verts,E

def check_candidate(q,n,w):
    verts,E=graph(q,n)
    e=w[:-1];f=w[1:]
    if e==f:return False
    d={v:[] for v in verts};pairs={}
    shortcut='@'
    for u,v,s in E:
        if s not in (e,f):
            d[u].append((v,s));pairs[s]=(u,v)
    u=e[:-1];z=f[1:]
    d[u].append((z,shortcut))
    # Euler circuit through every edge in the contracted graph (Hierholzer).
    v0=verts[0];stack=[(v0,None)];tour=[]
    while stack:
        v,tag=stack[-1]
        if d[v]:
            nxt,lbl=d[v].pop()
            stack.append((nxt,lbl))
        else:
            v,tag=stack.pop()
            if tag is not None:tour.append(tag)
    tour=tour[::-1]
    if len(tour)!=len(E)-1:return False
    unfolded=[]
    for tag in tour:
        unfolded.extend((e,f) if tag==shortcut else (tag,))
    if len(unfolded)!=q**n or set(unfolded)!={s for _,_,s in E}:raise AssertionError('wrong tour')
    assert all(unfolded[i][1:]==unfolded[(i+1)%len(unfolded)][:-1] for i in range(len(unfolded)))
    seq=''.join(s[-1] for s in unfolded)
    W=lambda width:{''.join(seq[(i+j)%len(seq)] for j in range(width)) for i in range(len(seq))}
    assert W(n)=={s for _,_,s in E}
    assert w in W(n+1)
    return True

def exhaustive_binary(n):
    q=2;V,E=graph(q,n);edges={v:[] for v in V}
    for a,b,s in E:edges[a].append(s)
    e0='0'*n;visited={e0};count=0;union=set()
    def rec(path):
        nonlocal count
        if len(path)==2**n:
            if path[-1][1:]!=e0[:-1]:return
            count+=1
            seq=''.join(s[-1] for s in path)
            union.update(''.join(seq[(i+j)%(2**n)] for j in range(n+1)) for i in range(2**n))
            return
        for e in edges[path[-1][1:]]:
            if e not in visited:
                visited.add(e);rec(path+[e]);visited.remove(e)
    rec([e0])
    return count,union

def main():
    count=0
    for q,hi in [(2,7),(3,4),(4,3)]:
        for n in range(2,hi+1):
            allowed=set(); forbidden=set()
            for tup in product('0123456789'[:q],repeat=n+1):
                w=''.join(tup)
                if check_candidate(q,n,w):allowed.add(w)
                else:forbidden.add(w)
            assert forbidden==expected_forbidden(q,n),(q,n,forbidden)
            print(f'q={q} n={n} tested={q**(n+1)} attainable={len(allowed)} impossible={sorted(forbidden)}')
            count+=q**(n+1)
    for n in range(2,5):
        cycles,union=exhaustive_binary(n)
        assert union==set(''.join(t) for t in product('01',repeat=n+1))-expected_forbidden(2,n)
        print(f'independent exhaustive binary n={n} cycles={cycles} union={len(union)}')
    print(f'ALL CHECKS PASSED; contracted instances={count}')
if __name__=='__main__':main()
