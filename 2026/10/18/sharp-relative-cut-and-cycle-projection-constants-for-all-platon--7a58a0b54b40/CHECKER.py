"""Exact, standalone finite checks for Platonic-graph cycle/cut projection norms.
Python 3 standard library only. No numerical tolerances or external tables.
"""
from fractions import Fraction as F
from collections import Counter


def graph(n, edges):
    edges=sorted({tuple(sorted((int(u),int(v)))) for u,v in edges})
    assert all(0<=u<v<n for u,v in edges)
    ad=[set() for _ in range(n)]
    for u,v in edges: ad[u].add(v);ad[v].add(u)
    return n,edges,ad


def tetrahedron():
    return graph(4,((a,b) for a in range(4) for b in range(a+1,4)))


def cube():
    return graph(8,((a,a^(1<<j)) for a in range(8) for j in range(3)))


def dodecahedron():
    e=[]
    for i in range(10):
        e += [(i,(i+1)%10), (i,10+i), (10+i,10+(i+2)%10)]
    return graph(20,e)


def automorphisms(g):
    n,_,adj=g
    degree=[len(a) for a in adj]
    mapping=[-1]*n
    taken=[False]*n
    def rec(depth):
        if depth==n:
            yield tuple(mapping)
            return
        best=None; best_cands=None
        for u in range(n):
            if mapping[u]!=-1:continue
            cands=[]
            for v in range(n):
                if taken[v] or degree[v]!=degree[u]: continue
                if all(((w in adj[u])==(mapping[w] in adj[v])) for w in range(n) if mapping[w]!=-1):
                    cands.append(v)
            if not cands: return
            if best is None or len(cands)<len(best_cands):
                best=u;best_cands=cands
                if len(cands)==1: break
        for v in best_cands:
            mapping[best]=v;taken[v]=True
            yield from rec(depth+1)
            taken[v]=False;mapping[best]=-1
    return list(rec(0))


def solve(A,b):
    n=len(A)
    x=[[F(t) for t in row]+[F(b[i])] for i,row in enumerate(A)]
    for j in range(n):
        k=next(k for k in range(j,n) if x[k][j])
        x[j],x[k]=x[k],x[j]
        p=x[j][j];x[j]=[z/p for z in x[j]]
        for k in range(n):
            if k!=j and x[k][j]:
                p=x[k][j];x[k]=[a-p*b for a,b in zip(x[k],x[j])]
    return [x[i][-1] for i in range(n)]


def edge_current(g,ref):
    n,edges,adj=g
    a,b=ref
    L=[[F(-int(j in adj[i])) if i!=j else F(len(adj[i])) for j in range(n-1)] for i in range(n-1)]
    v=[F(int(i==a)-int(i==b)) for i in range(n-1)]
    x=solve(L,v)+[F(0)]
    col=[x[u]-x[v] for u,v in edges]
    j=edges.index(ref)
    # Direct primal potential checks before computing any norm.
    assert all(sum(x[u]-x[w] for w in adj[u]) == int(u==a)-int(u==b) for u in range(n))
    assert col[j]>0
    q=sum(map(abs,col))
    c=F(1)+q-2*col[j]
    return q,c,col[j],Counter(col),tuple(x)


def check(name,g,autnum,lambdaQ,lambdaC,diag):
    n,edges,adj=g;m=len(edges)
    assert all(len(adj[u]) for u in range(n))
    aut=automorphisms(g)
    assert len(aut)==autnum,(name,len(aut))
    char=Counter();inner=0
    for p in aut:
        assert len(set(p))==n and all(tuple(sorted((p[u],p[v]))) in edges for u,v in edges)
        chiB=sum(p[u]==u for u in range(n))-1
        chiE=sum(1 if (p[u],p[v])==(u,v) else -1 if (p[u],p[v])==(v,u) else 0 for u,v in edges)
        chiC=chiE-chiB
        char[(chiB,chiC)]+=1
        inner+=chiB*chiC
    assert inner==0,(name,inner)
    assert sum(k[0]*k[1]*val for k,val in char.items())==0
    orbit={tuple(sorted((autp[edges[0][0]],autp[edges[0][1]]))) for autp in aut}
    assert len(orbit)==m,(name,len(orbit))
    q,c,diag0,counts,potential=edge_current(g,edges[0])
    assert (q,c,diag0)==(F(lambdaQ),F(lambdaC),F(diag)),(name,(q,c,diag0))
    assert sum(counts.values())==m
    print(name,'n=',n,'m=',m,'|Aut|=',len(aut),'Hom=',inner//len(aut),'Q=',q,'C=',c,'effective_resistance=',diag0)
    print('  joint_character_counts:',sorted(char.items()))
    print('  current_levels:',sorted(counts.items()))
    print('  potentials:',potential)
    return q,c


def main():
    t=check('tetrahedron',tetrahedron(),24,'3/2','3/2','1/2')
    c=check('cube',cube(),48,'2','11/6','7/12')
    d=check('dodecahedron',dodecahedron(),120,'38/15','34/15','19/30')
    # Planar duality identifies the primal cut space with the dual cycle space
    # by a signed permutation of edge coordinates; hence their exact minima swap.
    table=[('tetrahedron',t),('cube',c),('octahedron',c[::-1]),('dodecahedron',d),('icosahedron',d[::-1])]
    assert table==[('tetrahedron',(F(3,2),F(3,2))),('cube',(F(2),F(11,6))),('octahedron',(F(11,6),F(2))),('dodecahedron',(F(38,15),F(34,15))),('icosahedron',(F(34,15),F(38,15)))]
    print('ALL EXACT CHECKS PASSED')
if __name__=='__main__':main()
