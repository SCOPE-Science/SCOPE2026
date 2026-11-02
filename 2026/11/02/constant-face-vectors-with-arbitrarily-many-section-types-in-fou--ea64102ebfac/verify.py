"""Finite checks of the central sections of standard double bipyramids."""
from collections import Counter

def section_data(n, k):
    assert n >= 5 and 1 <= k < n
    apices=('a+', 'a-', 'b+', 'b-')
    sign={('v',i): (1 if i<k else -1) for i in range(n)}
    sign.update({('a',1):1,('a',-1):-1,('b',1):1,('b',-1):-1})
    a=(('a',1),('a',-1))
    b=(('b',1),('b',-1))
    edges=set()
    faces=[]
    for i in range(n):
        vi=('v',i); vj=('v',(i+1)%n)
        edges.add(frozenset((vi,vj)))
        for apex in (*a,*b):
            edges.add(frozenset((vi,apex)))
        for apex in (*a,*b):
            faces.append((vi,vj,apex))
        for ax in a:
            for bx in b:
                faces.append((vi,ax,bx))
    for ax in a:
        for bx in b:edges.add(frozenset((ax,bx)))
    crossed={edge for edge in edges if len({sign[p] for p in edge})==2}
    adj={e:set() for e in crossed}
    for face in faces:
        crossing=[frozenset((face[i],face[j])) for i,j in ((0,1),(0,2),(1,2))
                  if sign[face[i]] != sign[face[j]]]
        assert len(crossing) in (0,2)
        if crossing:
            x,y=crossing
            adj[x].add(y);adj[y].add(x)
    facets=[]
    for i in range(n):
        for ax in a:
            for bx in b:
                fv=(('v',i),('v',(i+1)%n),ax,bx)
                c=sum(sign[p] == 1 for p in fv)
                if 0<c<4:facets.append(3 if c in (1,3) else 4)
    deg=Counter(map(len,adj.values()))
    hubs=[x for x in crossed if len(adj[x]) == n]
    assert len(hubs)==2 and deg=={4:2*n+2,n:2} if n!=4 else True
    for hub in hubs:
        nbr=adj[hub]
        todo=set(nbr)
        comp_sizes=[]
        while todo:
            q=[todo.pop()]; sz=0
            while q:
                u=q.pop();sz+=1
                for w in (adj[u]&nbr)&todo:
                    todo.remove(w);q.append(w)
            comp_sizes.append(sz)
        assert sorted(comp_sizes)==sorted((k,n-k)),(n,k,comp_sizes)
    return (len(crossed),sum(map(len,adj.values()))//2,len(facets),Counter(facets))

def main():
    for n in range(5,101):
        for k in range(1,n):
            r=section_data(n,k)
            assert r==(2*n+4,5*n+4,3*n+2,{3:2*n,4:n+2}), (n,k,r)
    print('PASS: all 4944 ordered sign-run cases (5 <= n <= 100); hub neighborhood classes, f-vector, facet polygon counts.')
if __name__=='__main__':main()
