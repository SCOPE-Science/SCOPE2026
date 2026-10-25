"""Independent exact-rational checks of canonical cut/cycle projections on clique-path products.
Run: python3 check_clique_path.py (Python 3 standard library only).
Finite tests corroborate, but do not replace, the proof for all parameters.
"""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt


def inverse(a):
    n=len(a)
    z=[[F(a[i][j]) for j in range(n)]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if z[i][k])
        z[k],z[pivot]=z[pivot],z[k]
        fac=z[k][k]
        z[k]=[u/fac for u in z[k]]
        for i in range(n):
            if i!=k and z[i][k]:
                factor=z[i][k]
                z[i]=[u-factor*v for u,v in zip(z[i],z[k])]
    return [r[n:] for r in z]


def full_graph_norms(m,n):
    vertices=[(a,x) for a in range(m) for x in range(n)]
    vid={u:i for i,u in enumerate(vertices)}
    h=[];v=[]
    for x in range(n):
        for a,b in combinations(range(m),2):h.append((vid[a,x],vid[b,x],x))
    for x in range(n-1):
        for a in range(m):v.append((vid[a,x],vid[a,x+1],x))
    edges=[('H',*e) for e in h]+[('V',*e) for e in v]
    dim=m*n-1
    lap=[[F(0) for _ in range(dim)] for _ in range(dim)]
    for _,a,b,_ in edges:
        for t in (a,b):
            if t<dim:lap[t][t]+=1
        if a<dim and b<dim:lap[a][b]-=1;lap[b][a]-=1
    inv=inverse(lap)
    grad=[]
    for _,a,b,_ in edges:
        grad.append([F(int(i==b)-int(i==a)) for i in range(dim)])
    solved=[[sum(inv[i][j]*g[j] for j in range(dim)) for i in range(dim)] for g in grad]
    q=[];p=[]
    for j,g in enumerate(grad):
        col=[sum(grad[i][k]*solved[j][k] for k in range(dim)) for i in range(len(edges))]
        q.append(sum(map(abs,col)))
        p.append(sum(abs(F(int(i==j))-col[i]) for i in range(len(edges))))
    return edges,q,p


def reduced_norms(m,n):
    # Path vertex Green operator and path edge Dirichlet Green operator.
    N=n-1
    B=[[F((m+2) if i==j else (-1 if abs(i-j)==1 else 0)) for j in range(N)] for i in range(N)]
    E=inverse(B)
    A=[[F((m+(1 if i in (0,n-1) else 2)) if i==j else (-1 if abs(i-j)==1 else 0)) for j in range(n)] for i in range(n)]
    R=inverse(A)
    hQ=[F(2*(m-1),m)+4*R[x][x]-2*(R[0][x]+R[-1][x]) for x in range(n)]
    hP=[F(3)-F(2,m)-2*(R[0][x]+R[-1][x]) for x in range(n)]
    vQ=[1+2*(m-1)*sum(E[y][x] for y in range(N)) for x in range(N)]
    vP=[2*(m-1)*(sum(E[y][x] for y in range(N))+E[x][x]) for x in range(N)]
    return hQ,vQ,hP,vP


def check(m,n):
    edges,q,p=full_graph_norms(m,n)
    hQ,vQ,hP,vP=reduced_norms(m,n)
    iH=0;iV=0
    for i,e in enumerate(edges):
        if e[0]=='H':
            assert q[i]==hQ[e[3]], (m,n,i,'H Q',q[i],hQ[e[3]])
            assert p[i]==hP[e[3]], (m,n,i,'H P',p[i],hP[e[3]])
            iH+=1
        else:
            assert q[i]==vQ[e[3]], (m,n,i,'V Q',q[i],vQ[e[3]])
            assert p[i]==vP[e[3]], (m,n,i,'V P',p[i],vP[e[3]])
            iV+=1
    k=(n-2)//2
    assert max(q)==vQ[k]
    if m==3:
        assert max(p)==hP[(n-1)//2]
        assert (max(q)>max(p)) == (n%2==0)
    else:
        assert max(p)==vP[k] and max(p)>max(q)
    assert max(vQ)==vQ[k] and max(vP)==vP[k]
    print(f'PASS K_{m} x P_{n}: {len(edges)} exact cut and cycle columns; '
          f'Q={max(q)}, P={max(p)}')
    return len(edges)

if __name__=='__main__':
    total=0
    for m,n in [(3,4),(3,5),(3,6),(3,7),(4,4),(4,5),(5,4),(5,5)]:
        total+=check(m,n)
    print(f'PASS: {total} complete exact-rational edge columns, '
          f'{2*total} column sums and full-entry identity checks.')
