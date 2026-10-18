"""Independent exhaustive checks for sequence b-colourings on co-biclique block graphs."""
from itertools import product, permutations
from collections import Counter

def graph(a,b):
    r=len(a)
    vertices=[]
    for i in range(r):
        vertices.extend([('A',i,t) for t in range(a[i])])
        vertices.extend([('B',i,t) for t in range(b[i])])
    edges=[]
    for u in range(len(vertices)):
        for v in range(u+1,len(vertices)):
            x,y=vertices[u],vertices[v]
            if x[0]!=y[0] and x[1]!=y[1]:edges.append((u,v))
    return vertices,edges

def actual_profiles(a,b):
    V,E=graph(a,b); n=len(V);r=len(a);found={}
    nbr=[set() for _ in V]
    for u,v in E:nbr[u].add(v);nbr[v].add(u)
    for k in range(2,min(r+1,n)+1):
        profiles=set(); num=0
        for f in product(range(k),repeat=n):
            if len(set(f))!=k:continue
            if any(f[u]==f[v] for u,v in E):continue
            counts=[0]*k
            for u in range(n):
                if len({f[v] for v in nbr[u]})==k-1:counts[f[u]]+=1
            if min(counts):profiles.add(tuple(sorted(counts,reverse=True)));num+=1
        found[k]=(profiles,num)
    return found

def predicted(a,b):
    r=len(a)
    return {2:({tuple(sorted([sum(a),sum(b)],reverse=True))},2), r:({tuple(sorted([a[i]+b[i] for i in range(r)],reverse=True))},__import__('math').factorial(r))}

def main():
    cases=[([1,1,1],[1,1,1]),([2,1,1],[1,1,1]),([2,1,1],[2,1,1]),([1,2,1],[2,1,1]),([2,2,1],[1,1,1]),([1,1,1,1],[1,1,1,1]),([2,1,1,1],[1,1,1,1]),([2,1,1],[1,2,1]),([2,1,1],[1,1,2]),([1,1,2],[1,1,1])]
    total=0
    for a,b in cases:
        got=actual_profiles(a,b); want=predicted(a,b)
        assert {k:v for k,v in got.items() if v[1]}==want,(a,b,got,want)
        total+=1
    print('PASS',total,'graph profiles; every named assignment for palette sizes 2 through r+1 checked')
if __name__=='__main__':main()
