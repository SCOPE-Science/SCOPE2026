#!/usr/bin/env python3
"""Reproduce strong-edge-coloring and strong-clique calculations for uniform theta graphs.

Usage: python3 verify_theta.py
No third-party packages are required. Finite tests supplement, not replace, the proof.
"""

def graph(k, length):
    assert k >= 3 and length >= 2
    adj = [set(), set()]
    edges = {}
    for path in range(k):
        middle = []
        for _ in range(length - 1):
            middle.append(len(adj))
            adj.append(set())
        vertices = [0] + middle + [1]
        for j in range(length):
            a,b=vertices[j],vertices[j+1]
            adj[a].add(b)
            adj[b].add(a)
            edges[path,j+1]=(a,b)
    return adj,edges


def conflict_masks(adj,edges):
    keys = sorted(edges)
    masks=[0]*len(keys)
    for x in range(len(keys)):
        a,b=edges[keys[x]]
        for y in range(x):
            c,d=edges[keys[y]]
            if (a in (c,d) or b in (c,d) or
                c in adj[a] or d in adj[a] or c in adj[b] or d in adj[b]):
                masks[x] |= 1<<y
                masks[y] |= 1<<x
    return keys,masks


def expected(k,length):
    return (2*k if length==2 else k+2 if length==4 else k+1)


def strong_clique_expected(k,length):
    return (2*k if length==2 else k+1)


def constructive_coloring(k,length):
    out={}
    for p in range(k):
        i=p+1
        if length==2:
            row=[i,k+i]
        elif length==3:
            row=[i,k+1,(i % k)+1]
        elif length==4:
            row=[i,k+1,k+2,i]
        elif length==5:
            row=[i,k+1,(3 if i==2 else 2),1,(k+1 if i==1 else i)]
        else:
            interior_size=length-4
            choices=[]
            for offset in range(3):
                seq=[1+(j+offset)%3 for j in range(interior_size)]
                if seq[0]!=i and seq[-1]!=i:
                    choices=seq
                    break
            assert choices
            row=[i,k+1] + choices + [k+1,i]
        assert len(row)==length
        for j,c in enumerate(row,1):out[(p,j)]=c
    return out


def valid_coloring(keys,masks,col):
    for a in range(len(keys)):
        v=masks[a]
        while v:
            bit=v & -v
            b=bit.bit_length()-1
            v-=bit
            if col[keys[a]]==col[keys[b]]:
                return False, (keys[a],keys[b])
    return True,None


def can_color(masks,limit):
    """Independent DSATUR/backtracking decision on the conflict graph."""
    n=len(masks)
    chosen=[-1]*n
    saturated=[0]*n
    degrees=[q.bit_count() for q in masks]
    def solve(left,used):
        if not left:return True
        v=max((i for i in range(n) if chosen[i]<0),
              key=lambda i:(saturated[i].bit_count(),degrees[i]))
        available = (~saturated[v]) & ((1<<min(limit,used+1))-1)
        while available:
            bit=available & -available
            color=bit.bit_length()-1
            available-=bit
            chosen[v]=color
            impacted=[]
            remaining=masks[v]
            while remaining:
                b=remaining & -remaining
                remaining-=b
                j=b.bit_length()-1
                if chosen[j]<0 and not (saturated[j] & bit):
                    saturated[j]|=bit
                    impacted.append(j)
            if all(saturated[j].bit_count()<limit
                   for j in range(n) if chosen[j]<0):
                if solve(left-1,max(used,color+1)):
                    return True
            for j in impacted:saturated[j]^=bit
            chosen[v]=-1
        return False
    return solve(n,0)


def maximum_clique(masks):
    """Exact Bron--Kerbosch maximal-clique search, independent of the formula."""
    best=[0]
    def visit(Rsize,P,X):
        if not P and not X:
            best[0]=max(best[0],Rsize)
            return
        if Rsize+P.bit_count()<=best[0]:return
        union=P|X
        if union:
            pivot=max((i for i in range(len(masks)) if union & (1<<i)),
                      key=lambda i:(P & masks[i]).bit_count())
            todo=P & ~masks[pivot]
        else:todo=P
        while todo:
            b=todo & -todo
            todo-=b
            v=b.bit_length()-1
            visit(Rsize+1,P&masks[v],X&masks[v])
            P^=b
            X|=b
            if Rsize+P.bit_count()<=best[0]:break
    visit(0,(1<<len(masks))-1,0)
    return best[0]


def main():
    constructed=0; solved=0; cliques=0
    # Constructive coloring checked directly on the graph, well beyond the proof cases.
    for k in range(3,19):
        for length in range(2,31):
            A,E=graph(k,length)
            keys,conf=conflict_masks(A,E)
            coloring=constructive_coloring(k,length)
            ok,bad=valid_coloring(keys,conf,coloring)
            assert ok,(k,length,bad)
            assert len(set(coloring.values()))==expected(k,length)
            constructed+=1
    # Independently solve chromatic minimization at manageable orders.
    for k in range(3,6):
        for length in range(2,12):
            A,E=graph(k,length)
            keys,conf=conflict_masks(A,E)
            target=expected(k,length)
            assert can_color(conf,target),(k,length,target)
            assert not can_color(conf,target-1),(k,length,target-1)
            solved+=1
    # Exact maximum strong cliques on the squared line graphs.
    for k in range(3,8):
        for length in range(2,12):
            A,E=graph(k,length)
            keys,conf=conflict_masks(A,E)
            omega=maximum_clique(conf)
            assert omega==strong_clique_expected(k,length),(k,length,omega)
            cliques+=1
    print(f'VERIFY_OK constructive_graphs={constructed} exact_chromatic_instances={solved} exact_clique_instances={cliques}')

if __name__=='__main__':main()
