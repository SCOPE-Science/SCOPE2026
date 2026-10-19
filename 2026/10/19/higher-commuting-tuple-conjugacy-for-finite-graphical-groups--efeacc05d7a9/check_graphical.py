"""Finite checks for higher simultaneous conjugacy in graphical groups.
No source external to this file is required. Python 3.10+.
"""
from itertools import product, combinations
from collections import Counter

def graph_edges(n,mask):
    pairs=list(combinations(range(n),2))
    return [pair for i,pair in enumerate(pairs) if mask & (1<<i)]

def support_prediction(n,edges,q,k):
    m=len(edges); weights=Counter()
    for mask in range(1<<n):
        support={i for i in range(n) if mask>>i&1}
        touching=set(support)
        for i,j in edges:
            if i in support: touching.add(j)
            if j in support: touching.add(i)
        c=0;seen=set()
        for i in support:
            if i in seen:continue
            c+=1;todo=[i];seen.add(i)
            while todo:
                v=todo.pop()
                for x,y in edges:
                    w=y if x==v else (x if y==v else None)
                    if w is not None and w in support and w not in seen:
                        seen.add(w);todo.append(w)
        r=len(touching)-c
        # each nonzero vertex vector belongs to a line of F_q^k
        projective_lines=(q**k-1)//(q-1)
        weights[r]+=(q-1)**len(support)*projective_lines**c*q**(k*m-r)
    return weights

def row_rank(rows,p,n):
    a=[r[:] for r in rows];rank=0
    for col in range(n):
        idx=next((i for i in range(rank,len(a)) if a[i][col]%p),None)
        if idx is None:continue
        a[rank],a[idx]=a[idx],a[rank]
        inv=pow(a[rank][col],-1,p)
        a[rank]=[(v*inv)%p for v in a[rank]]
        for i in range(len(a)):
            if i!=rank and a[i][col]:
                w=a[i][col]
                a[i]=[(a[i][j]-w*a[rank][j])%p for j in range(n)]
        rank+=1
        if rank==n:break
    return rank

def direct_linear_action(n,edges,q,k):
    """Enumerate coordinate vectors, test every edge commutator,
    and calculate full-group conjugation orbit sizes by row elimination.
    Independent of support/component and neighborhood formula.
    """
    m=len(edges); profile=Counter()
    for vals in product(range(q),repeat=n*k):
        x=[vals[i*k:(i+1)*k] for i in range(n)]
        if any((x[u][i]*x[v][j]-x[u][j]*x[v][i])%q
                for u,v in edges for i in range(k) for j in range(i+1,k)):
            continue
        matrix=[]
        for u,v in edges:
            for i in range(k):
                row=[0]*n
                row[u]=x[v][i]
                row[v]=(-x[u][i])%q
                matrix.append(row)
        rank=row_rank(matrix,q,n)
        profile[rank]+=q**(m*k-rank)
    return profile

def test():
    total=0
    for n in range(1,5):
        for mask in range(1<<(n*(n-1)//2)):
            e=graph_edges(n,mask)
            a=support_prediction(n,e,2,2)
            b=direct_linear_action(n,e,2,2)
            assert a==b,(n,e,a,b)
            total+=1
    print('PASS all',total,'labeled graphs on at most four vertices over F_2, k=2')
    for n,edges,q,k in [
        (4,[(0,1),(0,2),(0,3)],2,3),
        (4,[(0,1),(0,2),(0,3)],3,2),
        (4,[(0,1),(1,2)],3,2),
        (4,[(0,1),(0,2),(1,2)],3,2),
        (5,[(0,1),(1,2),(2,3),(3,4)],2,2)]:
        assert support_prediction(n,edges,q,k)==direct_linear_action(n,edges,q,k)
        print('PASS',n,edges,'q',q,'k',k,'profile',dict(support_prediction(n,edges,q,k)))
    star=[(0,1),(0,2),(0,3)]
    triangle=[(0,1),(0,2),(1,2)]
    f1=support_prediction(4,star,2,1)
    f2=support_prediction(4,triangle,2,1)
    assert sum(f1.values())==sum(f2.values())==44
    b1=sum(support_prediction(4,star,2,2).values())
    b2=sum(support_prediction(4,triangle,2,2).values())
    assert (b1,b2)==(2272,1600)
    print('CLASS-EQUALITY NUMERIC q=2:',sum(f1.values()),sum(f2.values()))
    print('HIGHER-DISTINCTION q=2 k=2:',b1,b2)
    print('CHECKER_OK')
if __name__=='__main__':test()
