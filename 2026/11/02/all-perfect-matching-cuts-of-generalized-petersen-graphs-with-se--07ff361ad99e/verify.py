#!/usr/bin/env python3
"""Exact finite-state certificate and independent finite-instance checks."""

def local_edge(bits):
    d=[]
    for i in (1,3,5):
        di=(bits[i-1]!=bits[i])+(bits[i+1]!=bits[i])
        if di>1: return False
        d.append(di)
    y=[bits[i]^(1-di) for i,di in zip((1,3,5),d)]
    return int(y[0]!=y[1])+int(y[1]!=y[2])==d[1]

def core_certificate():
    ed=[]
    for value in range(128):
        bits=[(value>>i)&1 for i in range(6,-1,-1)]
        if local_edge(bits):
            word=''.join(map(str,bits))
            ed.append((word[:6],word[1:],word))
    assert len(ed)==28
    nodes=set(v for a,b,_ in ed for v in (a,b))
    rounds=[]
    while True:
        indeg={v:0 for v in nodes};outdeg=indeg.copy()
        for a,b,_ in ed:
            if a in nodes and b in nodes:
                outdeg[a]+=1;indeg[b]+=1
        dead={v for v in nodes if indeg[v]==0 or outdeg[v]==0}
        if not dead:break
        rounds.append(len(dead));nodes-=dead
    remaining=[(a,b,w) for a,b,w in ed if a in nodes and b in nodes]
    assert rounds==[20,4,2],rounds
    assert len(nodes)==12 and len(remaining)==12
    expected={'0000000','1111111','0001100','0011000','0110001','1100011','1000110','0011100','0111001','1110011','1100111','1001110'}
    assert {w for _,_,w in remaining}==expected
    successor={a:b for a,b,_ in remaining}
    assert len(successor)==12
    components=[]
    unseen=set(nodes)
    while unseen:
        v=min(unseen);cycle=[]
        while v not in cycle:
            cycle.append(v);unseen.remove(v)
            v=successor[v]
        assert v==cycle[0]
        components.append(cycle)
    assert sorted(map(len,components))==[1,1,5,5]
    return components

def all_legal_labels(n):
    # Independent original graph-level check; zero-th vertex has fixed color 0.
    assert n>=5
    neigh=[[] for i in range(2*n)]
    edges=set()
    for i in range(n):
        for a,b in ((i,(i+1)%n),(n+i,n+(i+2)%n),(i,n+i)):
            edge=tuple(sorted((a,b)));edges.add(edge)
    assert len(edges)==3*n
    for a,b in edges:
        neigh[a].append(b);neigh[b].append(a)
    assert all(len(adj)==3 for adj in neigh)
    valid=[]
    for mask in range(1<<(2*n-1)):
        colors=[0]+[(mask>>(j-1))&1 for j in range(1,2*n)]
        if all(sum(colors[j]!=colors[i] for j in neigh[i])==1 for i in range(2*n)):
            valid.append(colors)
    return valid

def formula_labels(n):
    # Enumerate outer-row words and reconstruct inner bits via local rules.
    valid=[]
    for mask in range(1<<n):
        x=[(mask>>i)&1 for i in range(n)]
        d=[(x[(i-1)%n]!=x[i])+(x[(i+1)%n]!=x[i]) for i in range(n)]
        if any(t>1 for t in d):continue
        y=[x[i]^(1-d[i]) for i in range(n)]
        if any((y[(i-2)%n]!=y[i])+(y[(i+2)%n]!=y[i]) != d[i] for i in range(n)):continue
        if x[0]==0:valid.append(tuple(x+y))
    return valid

def main():
    components=core_certificate()
    for n in range(5,11):
        direct={tuple(x) for x in all_legal_labels(n)}
        via=set(formula_labels(n))
        assert direct==via,(n, len(direct),len(via))
        assert len(direct)==1+5*(n%5==0),(n,len(direct))
    for n in range(11,19):
        assert len(formula_labels(n))==1+5*(n%5==0),(n,len(formula_labels(n)))
    for n in range(5,211):
        x=[int(i%5 in (0,1)) for i in range(n)]
        if n%5:continue
        d=[(x[(i-1)%n]!=x[i])+(x[(i+1)%n]!=x[i]) for i in range(n)]
        y=[x[i]^(1-d[i]) for i in range(n)]
        assert all(di<=1 for di in d)
        assert all((y[(i-2)%n]!=y[i])+(y[(i+2)%n]!=y[i])==d[i] for i in range(n))
    print('VERIFY_OK: 128 windows; 28-to-12 cyclic core; two loops and two 5-cycles; direct graphs n=5..10; outer-word n=11..18; construction n<=210')

if __name__=='__main__':main()
