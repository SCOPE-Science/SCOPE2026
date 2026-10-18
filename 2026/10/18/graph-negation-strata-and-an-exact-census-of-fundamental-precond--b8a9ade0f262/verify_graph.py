"""Graph-first classification of F-preconditionals on P({0,1,2}).

Run: python3 verify_graph.py (Python standard library only).
Checks every candidate against each defining axiom on all 8^3 inputs,
independently of the row-based C++ generator.
"""
from collections import Counter
from itertools import combinations, product, permutations

U=7
EDGES=list(combinations(range(3),2))

def subset(a,b): return a&b==a

def common(graph,a):
    return sum(1<<i for i in range(3)
               if all(i!=j and tuple(sorted((i,j))) in graph
                      for j in range(3) if a>>j&1))

def enumerate_graph(graph):
    neg=[common(graph,a) for a in range(8)]
    pair_rows=[]
    for a in (3,5,6):
        i,j=[1<<h for h in range(3) if a>>h&1]
        other=U^a
        choices=[]
        for vi in (i,i|other,U):
            for vj in (j,j|other,U):
                if not subset(neg[a],vi) or not subset(neg[a],vj):continue
                if any(not subset(vi if (a&neg[d])==i else
                                  vj if (a&neg[d])==j else
                                  neg[a] if (a&neg[d])==0 else U, neg[d])
                       for d in (i,j)):
                    continue
                choices.append((vi,vj))
        pair_rows.append((a,i,j,choices))
    for choices in product(*(p[3] for p in pair_rows)):
        rows={}
        for a in range(8):
            rows[a]={b: neg[a] if b==0 else U if b==a else b
                     for b in range(8) if subset(b,a)}
        for p,(vi,vj) in zip(pair_rows, choices):
            a,i,j,_=p; rows[a][i]=vi; rows[a][j]=vj
        def op(a,b):return rows[a][a&b]
        valid=True
        for a,b,c in product(range(8),repeat=3):
            if (op(U,a)&a)!=op(U,a):valid=False;break # P1
            if not subset(a&b,op(a,b)):valid=False;break # P2
            if not subset(op(a,b),op(a,a&b)):valid=False;break # P3
            if not subset(op(a,b&c),op(a,b)):valid=False;break # P4
            if not subset(op(a,op(a&b,c)),op(a&b,c)):valid=False;break # P5
        if not valid: continue
        assert all(op(a,a)==U and (a&op(a,0))==0
                   and subset(a,op(op(a,0),0)) for a in range(8))
        yield tuple(op(a,b) for a in range(8) for b in range(8))

def permute(a,p):return sum(1<<p[i] for i in range(3) if a>>i&1)

def perm_table(t,p):
    ans=[0]*64
    for a,b in product(range(8),repeat=2):
        ans[8*permute(a,p)+permute(b,p)]=permute(t[8*a+b],p)
    return tuple(ans)

def canonical_graph_witness(graph, n):
    # x in N(A) iff x is joined in the undirected loopless graph to every member of A
    top=(1<<n)-1
    def neighbors(a):
        return sum(1<<i for i in range(n) if all(i!=j and (min(i,j),max(i,j)) in graph
                    for j in range(n) if a>>j&1))
    def op(a,b):return (a&b)|neighbors(a&~b)
    # complete checks for all graphs on 1-4 vertices, below
    for a,b,c in product(range(top+1),repeat=3):
        if not subset(op(top,a),a):return False
        if not subset(a&b,op(a,b)):return False
        if not subset(op(a,b),op(a,a&b)):return False
        if not subset(op(a,b&c),op(a,b)):return False
        if not subset(op(a,op(a&b,c)),op(a&b,c)):return False
    for a in range(top+1):
        if op(a,a)!=top or a&op(a,0) or not subset(a,op(op(a,0),0)):return False
    return True

all_tables=set();counts=[]
for bits in range(8):
    G={e for h,e in enumerate(EDGES) if bits>>h&1}
    r=set(enumerate_graph(G));counts.append(len(r));all_tables.update(r)
assert counts==[729,81,81,16,81,16,16,1]
assert len(all_tables)==1021
perms=list(permutations(range(3)))
fix=[sum(perm_table(t,p)==t for t in all_tables) for p in perms]
assert sorted(fix)==[10,10,41,41,41,1021]
assert sum(fix)//6==194
checks=0
for n in range(1,5):
    pairs=list(combinations(range(n),2))
    for bits in range(1<<len(pairs)):
        G={e for h,e in enumerate(pairs) if bits>>h&1}
        assert canonical_graph_witness(G,n)
        checks+=1
print(f"GRAPH_CLASSIFICATION_OK total={len(all_tables)} classes=194 graph_counts={counts} witness_graphs={checks}")
