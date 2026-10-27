"""Exact-rational regression checks for a regular-graph Gauss heat-step theorem.

Only standard-library Python; analytical arguments, not finite enumeration,
establish the all-graph statements.
"""
from fractions import Fraction as F


def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]


def mm(a,b):
    n=len(a);m=len(b[0]);k=len(b)
    return [[sum((a[i][t]*b[t][j] for t in range(k)),F(0)) for j in range(m)] for i in range(n)]


def inv(a):
    n=len(a)
    aug=[row[:]+ir[:] for row,ir in zip(a,eye(n))]
    for j in range(n):
        k=next((k for k in range(j,n) if aug[k][j]),None)
        assert k is not None,'singular matrix'
        aug[j],aug[k]=aug[k],aug[j]
        q=aug[j][j]; aug[j]=[x/q for x in aug[j]]
        for i in range(n):
            if i!=j:
                q=aug[i][j]
                if q:aug[i]=[x-q*y for x,y in zip(aug[i],aug[j])]
    return [row[n:] for row in aug]


def adjacent_cycle(m,n):
    return sorted({tuple(sorted((i,(i+1)%m))) for i in range(m)})


def cycle(n):
    return n,adjacent_cycle(n,n)


def cube(k):
    return 2**k,sorted((i,i^(1<<j)) for i in range(2**k) for j in range(k) if i<(i^(1<<j)))


def torus(m,n):
    edges=set()
    for i in range(m):
        for j in range(n):
            v=i*n+j
            for w in [((i+1)%m)*n+j,i*n+((j+1)%n)]:edges.add(tuple(sorted((v,w))))
    return m*n,sorted(edges)


def complete_bipartite(d):
    return 2*d,[(i,d+j) for i in range(d) for j in range(d)]


def adj_lap(n,edges):
    a=[[F(0) for _ in range(n)] for _ in range(n)]
    l=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,j in edges:
        assert i!=j and a[i][j]==0
        a[i][j]=a[j][i]=1
        l[i][j]=l[j][i]=-1
        l[i][i]+=1;l[j][j]+=1
    return a,l


def pseudoinv(l):
    n=len(l);j=[[F(1,n) for _ in range(n)] for _ in range(n)]
    return [[z-j[i][k] for k,z in enumerate(row)] for i,row in enumerate(inv([[l[i][k]+j[i][k] for k in range(n)] for i in range(n)]))]


def gauss(l,h):
    n=len(l); I=eye(n);L2=mm(l,l)
    P=[[12*I[i][j]-6*h*l[i][j]+h*h*L2[i][j] for j in range(n)]for i in range(n)]
    Q=[[12*I[i][j]+6*h*l[i][j]+h*h*L2[i][j] for j in range(n)]for i in range(n)]
    return mm(inv(Q),P)


def run():
    cases=[('cycle5',*cycle(5)),('cycle6',*cycle(6)),('cube3',*cube(3)),
           ('torus3x3',*torus(3,3)),('torus3x4',*torus(3,4)),
           ('bipartite3',*complete_bipartite(3)),('bipartite4',*complete_bipartite(4))]
    counts={'graphs':0,'exact_rational_steps':0,'row_sum_tests':0,'torus_formula_tests':0,'spectral_trace_tests':0}
    for name,n,edges in cases:
        A,L=adj_lap(n,edges);d=int(sum(A[0]));assert all(sum(row)==d for row in A)
        Pin=pseudoinv(L)
        assert mm(L,Pin)==[[F(int(i==j))-F(1,n) for j in range(n)]for i in range(n)]
        E=sum((Pin[i][j] for i,j in edges),F(0))
        trace=sum((A[i][j]*Pin[j][i] for i in range(n) for j in range(n)),F(0))
        assert trace==2*E;counts['spectral_trace_tests']+=1
        if n>=3*d:assert trace>0
        print(name,'order',n,'degree',d,'trace(A L+)',trace,'max_edge_L+',max(Pin[i][j] for i,j in edges))
        for h in [F(1,2),F(1),F(2),F(10),F(100)]:
            T=gauss(L,h)
            assert all(sum(row)==1 for row in T)
            assert all(T[i][j]==T[j][i] for i in range(n) for j in range(n))
            counts['exact_rational_steps']+=1
            counts['row_sum_tests']+=n
            if name=='torus3x3':
                den=(3*h*h+3*h+1)*(3*h*h+6*h+4)
                di=(9*h**4+3*h**3+h*h+2*h+4)/den
                ad=4*h*(h+1)/den
                na=2*h*h*(3*h+2)/den
                assert all(T[i][j]==(di if i==j else ad if A[i][j] else na) for i in range(n) for j in range(n))
                assert all(z>0 for row in T for z in row)
                counts['torus_formula_tests']+=n*n
            if name in ('torus3x4','cycle6') and h==100:
                neg=[(i,j) for i,j in edges if T[i][j]<0];assert neg
            if name.startswith('bipartite'):
                assert all(z>0 for row in T for z in row)
        counts['graphs']+=1
    print('PASSED',counts)

if __name__=='__main__':run()
