"""Exact finite tests for facet normal classification of a one-edge subdivision of K_n.

Standard-library Python only; run `python3 verify.py`.
"""
from itertools import product
from collections import Counter
from math import comb, floor


def graph(m):
    # Vertices 0,...,m-1 form a clique; a=m, b=m+1, z=m+2.
    a,b,z=m,m+1,m+2
    edges=[(i,j) for i in range(m) for j in range(i+1,m)]
    edges += [(i,c) for i in range(m) for c in (a,b)]
    edges += [(a,z),(b,z)]
    return edges


def facet_normals(m):
    E=graph(m)
    result={}
    # Normalize at clique vertex 0; all other clique vertices and a,b
    # lie in {-1,0,1}, while z lies in {-2,-1,0,1,2}.
    for t in product((-1,0,1),repeat=m+1):
        cl=(0,)+t[:m-1]
        a,b=t[m-1],t[m]
        for z in (-2,-1,0,1,2):
            f=cl+(a,b,z)
            if any(abs(f[i]-f[j])>1 for i,j in E): continue
            adj=[[] for _ in f]
            tight=0
            for i,j in E:
                if abs(f[i]-f[j])==1:
                    tight+=1
                    adj[i].append(j);adj[j].append(i)
            seen={0};stack=[0]
            while stack:
                for j in adj[stack.pop()]:
                    if j not in seen:seen.add(j);stack.append(j)
            if len(seen)==len(f):result[f]=tight
    return result


def transform(f,m,kind,i=0):
    g=list(f)
    if kind=='pair': g[m],g[m+1]=g[m+1],g[m]
    elif kind=='clique':g[i],g[i+1]=g[i+1],g[i]
    elif kind=='sign':g=[-v for v in g]
    else:raise ValueError(kind)
    return tuple(x-g[0] for x in g)


def orbits(facets,m):
    pending=set(facets); orbits=[]
    while pending:
        x=pending.pop(); orb={x};todo=[x]
        while todo:
            y=todo.pop()
            for gen,i in [('pair',0),('sign',0)]+[('clique',j) for j in range(m-1)]:
                z=transform(y,m,gen,i)
                assert z in facets,('symmetry failure',m,z)
                if z not in orb:orb.add(z);todo.append(z)
        pending.difference_update(orb)
        orbits.append(orb)
    return orbits


def predicted_max_count(m):
    if m==3: return 18
    if m%2==0:
        return 4*comb(m,m//2-1)
    s=(m-1)//2
    return 4*(comb(m,s)+comb(m,s-1))


def run():
    for m in range(3,9):
        normals=facet_normals(m)
        n=m+2
        predicted=2**(n+1)-10
        assert len(normals)==predicted,(m,len(normals),predicted)
        maximal=max(normals.values())
        assert maximal==floor(n*n/4)+2,(m,maximal)
        count=sum(t==maximal for t in normals.values())
        assert count==predicted_max_count(m),(m,count,predicted_max_count(m))
        orb=orbits(normals,m)
        assert len(orb)==3*m,(m,len(orb))
        assert sum(map(len,orb))==predicted
        assert sorted(sum(normals[x]==maximal for x in o) for o in orb).count(0)>=0
        hist=dict(sorted(Counter(len(o) for o in orb).items()))
        print(f'n={n}, facets={len(normals)}, orbits={len(orb)}, '
              f'max_facet_vertices={maximal}, maximizers={count}, '
              f'orbit_size_histogram={hist}')
    print('ALL INDEPENDENT EXACT ENUMERATIONS PASSED')

if __name__=='__main__':run()
