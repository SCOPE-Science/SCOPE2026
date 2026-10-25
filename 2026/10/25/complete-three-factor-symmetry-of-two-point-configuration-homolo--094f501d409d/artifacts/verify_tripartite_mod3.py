"""Exact-rank finite-field cross-check independent of the character identity."""
from verify_tripartite import make, char_formula
from math import comb


def rank(columns):
    basis={}
    for col in columns:
        x={k:v%3 for k,v in col.items() if v%3}
        while x:
            k=max(x)
            if k not in basis:
                inv={1:1,2:2}[x[k]]
                basis[k]={i:(v*inv)%3 for i,v in x.items() if v%3}
                break
            factor=x[k]
            for i,v in basis[k].items():
                y=(x.get(i,0)-factor*v)%3
                if y:x[i]=y
                elif i in x:del x[i]
    return len(basis)

for sizes in [(3,3,3),(3,3,4),(3,4,4)]:
    cells,ranks2=make(sizes)
    groups,vertices,edges,c0,c1,c2=cells
    c0i={c:i for i,c in enumerate(c0)};c1i={c:i for i,c in enumerate(c1)}
    D1=[]
    for v,e in c1:
        a,b=edges[e]
        D1.append({c0i[tuple(sorted((v,b)))]:1,c0i[tuple(sorted((v,a)))]:-1})
    D2=[]
    for e,f in c2:
        a,b=edges[e];c,d=edges[f]
        D2.append({c1i[(b,f)]:1,c1i[(a,f)]:-1,c1i[(d,e)]:-1,c1i[(c,e)]:1})
    for col in D2:
        ch={}
        for i,v in col.items():
            for j,w in D1[i].items():ch[j]=(ch.get(j,0)+v*w)%3
        assert not any(ch.values())
    r1=rank(D1);r2=rank(D2)
    B1=len(c1)-r1-r2;B2=len(c2)-r2
    Nv=sum(sizes);Ne=len(edges)
    assert (B1,B2)==(Ne-Nv+1,char_formula(sizes,[0,0,0])),(sizes,B1,B2)
    assert ranks2[2]==B1+1 and ranks2[3]==B2+1
    print('RATIONAL_RANKS_GF3_CHECK',sizes,'rank_d1',r1,'rank_d2',r2,'beta1',B1,'beta2',B2,flush=True)
print('VERIFY_OK_MOD3_TRIPARTITE')
