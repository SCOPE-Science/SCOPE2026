"""Finite verification of the graph-cycle representation for two-point star configurations.
Only finite cases are checked; the theorem for every n follows from the supplied proof.
"""
from itertools import permutations
from collections import deque

def verify(n):
    vertices=[(s,i) for s in range(2) for i in range(n)]
    edges=[(i,j) for i in range(n) for j in range(n) if i!=j] # oriented (0,i)->(1,j)
    adj={v:[] for v in vertices}
    for k,(i,j) in enumerate(edges):
        a=(0,i); b=(1,j)
        adj[a].append((b,k,1)); adj[b].append((a,k,-1))
    # BFS tree
    root=(0,0); parent={root:None}; q=deque([root]); tree=set()
    while q:
        v=q.popleft()
        for w,k,sgn in adj[v]:
            if w not in parent:
                parent[w]=(v,k,sgn);tree.add(k);q.append(w)
    assert len(parent)==2*n and len(tree)==2*n-1
    chords=[k for k in range(len(edges)) if k not in tree]
    assert len(chords)==n*n-3*n+1
    def path(u,v): # return coefficients for u->v along tree
        up={}; z=u
        while z is not None:
            up[z]=True
            z=parent[z][0] if parent[z] else None
        z=v; back=[]
        while z not in up:
            p,k,sgn=parent[z];back.append((k,-sgn));z=p
        common=z
        forward=[];z=u
        while z!=common:
            p,k,sgn=parent[z];forward.append((k,-sgn));z=p
        return forward+[(k,-sgn) for k,sgn in back[::-1]]
    cycles=[]
    for k in chords:
        i,j=edges[k]; z={k:1}
        for ee,sign in path((1,j),(0,i)):
            z[ee]=z.get(ee,0)+sign
        # boundary verify
        boundary={v:0 for v in vertices}
        for e,c in z.items():
            a,b=edges[e]; boundary[(0,a)]-=c;boundary[(1,b)]+=c
        assert all(x==0 for x in boundary.values())
        assert z[k]==1
        cycles.append(z)
    index={ij:k for k,ij in enumerate(edges)}
    tests=0
    for sigma in permutations(range(n)):
        f=sum(sigma[i]==i for i in range(n))
        two=sum(i<j and sigma[i]==j and sigma[j]==i for i in range(n) for j in range(i+1,n))
        for swap in (0,1):
            trace=0
            for chord,cyc in zip(chords,cycles):
                for e,coef in cyc.items():
                    i,j=edges[e]
                    target=(sigma[j],sigma[i]) if swap else (sigma[i],sigma[j])
                    if index[target]==chord:
                        trace+=(-1 if swap else 1)*coef
            expected=(1-2*two) if swap else (f*f-3*f+1)
            assert trace==expected,(n,sigma,swap,trace,expected)
            tests+=1
    return len(vertices),len(edges),len(chords),tests

if __name__=='__main__':
    tot=0
    for n in range(3,8):
        v,e,b,t=verify(n);tot+=t
        print(f'n={n} V={v} E={e} beta1={b} checked_group_elements={t}')
    print('PASS group actions checked:',tot)
