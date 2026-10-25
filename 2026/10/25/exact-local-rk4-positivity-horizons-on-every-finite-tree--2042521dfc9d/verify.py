"""Reproduce exact local coefficient identities for RK4 on unweighted trees.
Only Python standard library. Does not replace the general proof in RESULT.md.
"""
from fractions import Fraction as F
from collections import deque
from itertools import product
import random

def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def prufer_edges(code):
    n = len(code)+2
    deg = [1]*n
    for x in code: deg[x] += 1
    edges = []
    for x in code:
        leaf = next(i for i in range(n) if deg[i]==1)
        edges.append((leaf,x))
        deg[leaf]-=1;deg[x]-=1
    edges.append(tuple(i for i in range(n) if deg[i]==1))
    return edges

def check_tree(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges: adj[u].add(v);adj[v].add(u)
    d=[len(neigh) for neigh in adj]
    s=[sum(d[w] for w in adj[u]) for u in range(n)]
    A=[[int(j in adj[i]) for j in range(n)] for i in range(n)]
    A2=matmul(A,A);A4=matmul(A2,A2)
    L=[[ (d[i] if i==j else -int(j in adj[i])) for j in range(n)] for i in range(n)]
    L2=matmul(L,L);L3=matmul(L2,L);L4=matmul(L3,L)
    count=0
    for u in range(n):
        dist=[-1]*n;dist[u]=0;que=deque([u])
        while que:
            v=que.popleft()
            for w in adj[v]:
                if dist[w]<0:dist[w]=dist[v]+1;que.append(w)
        for v in range(u+1,n):
            dd=dist[v]
            if dd==1:
                a,b=d[u],d[v]
                q2=a+b;q3=a*a+a*b+b*b+a+b-1
                q4=(a+b)*(a*a+b*b)+2*(a*a+a*b+b*b)-2*(a+b)+s[u]+s[v]
                assert (L[u][v],L2[u][v],L3[u][v],L4[u][v])==(-1,-q2,-q3,-q4)
                assert q3 <= q2*q2 and 2*q4 >= q2**3
                assert 9*q2*q4 >4*q3*q3
            elif dd==2:
                w=next(x for x in adj[u] if v in adj[x])
                S=d[u]+d[w]+d[v]
                P=(S*S+d[u]**2+d[w]**2+d[v]**2)//2
                assert (L[u][v],L2[u][v],L3[u][v],L4[u][v])==(0,1,S,P+A4[u][v])
                assert 3*P>S*S
            elif dd==3:
                w=next(x for x in adj[u] if any(v in adj[y] for y in adj[x]))
                y=next(y for y in adj[w] if v in adj[y])
                S=d[u]+d[w]+d[y]+d[v]
                assert (L[u][v],L2[u][v],L3[u][v],L4[u][v])==(0,0,-1,-S)
            elif dd==4:
                assert (L[u][v],L2[u][v],L3[u][v],L4[u][v])==(0,0,0,1)
            else:
                assert dd>4 and (L[u][v],L2[u][v],L3[u][v],L4[u][v])==(0,0,0,0)
            count+=1
    for u in range(n):
        assert L2[u][u]==d[u]*(d[u]+1)
    return count

def check_broom():
    edges=[(0,1),(0,2),(0,3),(0,4),(4,5)]
    adj=[set() for _ in range(6)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    d=[len(v) for v in adj]; s=[sum(d[w] for w in adj[u]) for u in range(6)]
    a,b=d[0],d[4];q2=a+b;q3=a*a+a*b+b*b+a+b-1
    q4=(a+b)*(a*a+b*b)+2*(a*a+a*b+b*b)-2*(a+b)+s[0]+s[4]
    assert (q2,q3,q4)==(6,33,174)
    def edgeval(h): return 1-F(q2,2)*h+F(q3,6)*h*h-F(q4,24)*h*h*h
    assert edgeval(F(48,100))>0 and edgeval(F(49,100))<0
    assert F(4,8)==F(1,2)

if __name__=='__main__':
    random.seed(36)
    counter=0;cases=0
    for n in range(2,7):
        for code in product(range(n),repeat=n-2):
            counter+=check_tree(n,prufer_edges(code));cases+=1
    for n in range(7,24):
        for _ in range(15):
            code=[random.randrange(n) for j in range(n-2)]
            counter+=check_tree(n,prufer_edges(code));cases+=1
    check_broom()
    print('VERIFY_OK', cases, 'trees,', counter, 'exact unordered vertex-pair coefficient identities, tree-class inequalities, broom edge switch')
