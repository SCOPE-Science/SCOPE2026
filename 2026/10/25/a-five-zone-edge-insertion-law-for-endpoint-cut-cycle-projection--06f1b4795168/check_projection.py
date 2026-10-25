"""Exact rational checks for canonical graph cut/cycle projection formulas.

Standard library only. Graphs: K_{m,n} with a single added edge inside the m-part.
The proof for all integers is in RESULT.md; finite tests are supplementary.
"""
from fractions import Fraction as F


def inverse(a):
    n = len(a)
    q = [[F(t) for t in row] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for k in range(n):
        z = next(i for i in range(k, n) if q[i][k])
        q[k], q[z] = q[z], q[k]
        t = q[k][k]
        q[k] = [x/t for x in q[k]]
        for i in range(n):
            if i != k and q[i][k]:
                h = q[i][k]
                q[i] = [x-h*y for x,y in zip(q[i],q[k])]
    return [row[n:] for row in q]


def formula(m,n):
    q0 = 3-F(2,m)-F(2,n)+F(2,m*n)
    p0 = F(4*(m-1)*(n-1),m*n)
    dt = F(2-n,n*(n+2)) if m <= n+2 else F(1,n+2)-F(2*(n-1),m*n)
    qt = q0 + dt
    pt = p0 + dt + F(2,n*(n+2))
    qnew = F(2*(n+1),n+2)
    pnew = F(3*n,n+2)
    qcandidates = [qt,qnew] + ([q0] if m>=3 else [])
    pcandidates = [pt,pnew] + ([p0] if m>=3 else [])
    return max(qcandidates),max(pcandidates),{'touched':(qt,pt),'new':(qnew,pnew),**({'far':(q0,p0)} if m>=3 else {})},q0,p0


def graph_projection(m,n):
    v = m+n
    edges = [(i,m+j) for i in range(m) for j in range(n)] + [(0,1)]
    N=len(edges)
    columns=[]
    for a,b in edges:
        z = [F(0) for _ in range(v-1)]
        if a<v-1:z[a]+=1
        if b<v-1:z[b]-=1
        columns.append(z)
    lap = [[sum(columns[e][i]*columns[e][j] for e in range(N)) for j in range(v-1)] for i in range(v-1)]
    li = inverse(lap)
    q = [[sum(columns[e][i]*li[i][j]*columns[f][j] for i in range(v-1) for j in range(v-1)) for f in range(N)] for e in range(N)]
    out={}
    for e,(a,b) in enumerate(edges):
        typ='new' if (a,b)==(0,1) else ('touched' if a<2 else 'far')
        qsum=sum(abs(q[f][e]) for f in range(N))
        psum=sum(abs((F(e==f)-q[f][e])) for f in range(N))
        if typ in out: assert out[typ]==(qsum,psum)
        else: out[typ]=(qsum,psum)
    return out,N


def run():
    cases=0; columns=0
    for m,n in ([(m,n) for m in range(2,9) for n in range(2,9)]
                + [(m,5) for m in range(9,14)]
                + [(m,6) for m in range(11,15)]):
        actual,N=graph_projection(m,n)
        q,p,orbits,q0,p0=formula(m,n)
        assert actual==orbits,(m,n,actual,orbits)
        assert max(t[0] for t in actual.values())==q
        assert max(t[1] for t in actual.values())==p
        if n>=5:
            qd=q-q0; pd=p-p0
            if m==2: assert qd<0 and pd>0
            elif m==3: assert qd==0 and pd>0
            elif m<=2*n-2: assert qd==0 and pd==0
            elif m<=2*n+1: assert qd==0 and pd>0
            else: assert qd>0 and pd>0
        cases+=1; columns+=N
    print(f'GRAPH_PROJECTION_CERTIFICATE_OK cases={cases} columns={columns}')

if __name__=='__main__': run()
