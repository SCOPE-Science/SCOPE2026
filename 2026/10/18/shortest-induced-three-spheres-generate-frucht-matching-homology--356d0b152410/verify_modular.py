#!/usr/bin/env python3
"""Independent modular boundary-rank and octahedral-carrier sanity check."""
from itertools import combinations, product
E=((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),(4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
F={k:[c for c in combinations(range(len(E)),k) if len({v for j in c for v in E[j]})==2*k] for k in range(1,7)}

def modrank(cols,prime):
    pivot={}
    for src in cols:
        c={i:v%prime for i,v in src.items() if v%prime}
        while c:
            i=min(c)
            if i not in pivot:
                a=pow(c[i],-1,prime)
                pivot[i]={j:(a*v)%prime for j,v in c.items()}
                break
            a=c[i]
            for j,v in pivot[i].items():
                x=(c.get(j,0)-a*v)%prime
                if x:c[j]=x
                else:c.pop(j,None)
    return len(pivot)

def boundary(k):
    row={a:i for i,a in enumerate(F[k-1])}
    return [{row[c[:j]+c[j+1:]]:(-1)**j for j in range(k)} for c in F[k]]
W=[]
for i,j in combinations(range(len(E)),2):
    a=frozenset(E[i]+E[j])
    if len(a)==3:W.append(((i,j),a))
C=[]
def visit(start, chosen, vs):
    if len(chosen)==4:
        C.append(tuple(chosen));return
    for index in range(start,len(W)):
        pair,used=W[index]
        if vs.isdisjoint(used):visit(index+1,chosen+[pair],vs|used)
visit(0,[],frozenset())
assert len(C)==87
row={f:i for i,f in enumerate(F[4])}
Z=[]
for c in C:
    z={}
    for b in product((0,1),repeat=4):
        selected=[c[j][b[j]] for j in range(4)]
        invers=sum(selected[i]>selected[j] for i in range(4) for j in range(i+1,4))
        z[row[tuple(sorted(selected))]]=(-1)**(sum(b)+invers)
    Z.append(z)
for prime in (2,3,5,101):
    r=[modrank(boundary(k),prime) for k in range(2,7)]
    combined=modrank(boundary(5)+Z,prime)
    assert r==[17,100,233,144,8]
    assert combined==164
    print('MODULAR_OK',prime,'boundary_ranks',r,'augmented_rank',combined)
