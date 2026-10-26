"""Exact-rational validation of canonical cut/cycle projection columns on
balanced complete bipartite graphs with a deleted matching.
Run: python3 check.py. Uses only the Python standard library.
"""
from fractions import Fraction as F


def inverse(a):
    n = len(a)
    v = [[F(a[i][j]) for j in range(n)] + [F(i == j) for j in range(n)]
         for i in range(n)]
    for j in range(n):
        pivot = next(k for k in range(j, n) if v[k][j])
        v[j], v[pivot] = v[pivot], v[j]
        factor = v[j][j]
        v[j] = [x / factor for x in v[j]]
        for i in range(n):
            if i != j:
                f = v[i][j]
                if f:
                    v[i] = [x-f*y for x,y in zip(v[i],v[j])]
    return [row[n:] for row in v]


def formulas(s,t,a,b):
    h = s*(s-2)
    T = h+t
    U = s*(a+b)
    z2 = t-2*U+s*s*(a+b)
    R = F(2*s-1,s*s)+F(z2,h*s*s)-F((U-t)**2,h*s*s*T)
    if a and b:
        E = F(s*s-4*s+2*t,h*T)
    elif a or b:
        E = F((s-t)*(t-1),h*T)
    else:
        E = F(0)
    return R,3-2*R+2*E,4-4*R+2*E


def transfer(s,t,e,f):
    h=s*(s-2);T=h+t
    z=lambda edge: [s*(int(edge[0]==i)+int(edge[1]==i))-1 for i in range(t)]
    ze,zf=z(e),z(f)
    return (F(e[0]==f[0],s)+F(e[1]==f[1],s)-F(1,s*s)
        +F(sum(x*y for x,y in zip(ze,zf)),h*s*s)
        -F(sum(ze)*sum(zf),h*s*s*T))


def run():
    graphs=0; columns=0; current_entries=0; strict_signs=0
    for s in range(3,9):
        for t in range(0,s+1):
            edges=[(a,b) for a in range(s) for b in range(s)
                   if not (a==b and a<t)]
            assert len(edges)==s*s-t
            N=2*s-1  # final right-side vertex is grounded
            L=[[0]*N for _ in range(N)]
            for a,b in edges:
                u,v=a,s+b
                if u<N: L[u][u]+=1
                if v<N: L[v][v]+=1
                if u<N and v<N: L[u][v]-=1;L[v][u]-=1
            inv=inverse(L)
            pred={}
            for e in edges:
                a,b=e
                flags=(int(a<t),int(b<t))
                R,cut,cycle=formulas(s,t,*flags)
                src=[F(int(i==a)-int(i==s+b)) for i in range(N)]
                potential=[sum(inv[i][j]*src[j] for j in range(N)) for i in range(N)]+[F(0)]
                qcol=[potential[u]-potential[s+v] for u,v in edges]
                assert qcol[edges.index(e)]==R
                assert all(qcol[k]==transfer(s,t,e,f) for k,f in enumerate(edges))
                actual_cut=sum(map(abs,qcol))
                actual_cycle=1-R+sum(abs(x) for k,x in enumerate(qcol) if edges[k]!=e)
                assert (actual_cut,actual_cycle)==(cut,cycle),(s,t,e,actual_cut,actual_cycle,cut,cycle)
                if 1<=t<s:
                    exp=(3-2*(F(2*s-1,s*s)+F(t,s*s*(s*s-2*s+t))),
                         4-4*(F(2*s-1,s*s)+F(t,s*s*(s*s-2*s+t))))
                    if a>=t and b>=t: assert (cut,cycle)==exp
                    else:assert cut<exp[0] and cycle<exp[1]
                if t==s:
                    assert (cut,cycle)==(3-F(4,s),4-F(8*s-6,s*(s-1)))
                for k,f in enumerate(edges):
                    if f[0]==a or f[1]==b:
                        assert qcol[k]>0
                    else:
                        assert qcol[k]<=0 or (
                            (a<t and b<t and f==(b,a))
                            or (t>1 and a<t and b>=t and f[0]>=t and f[1]==a)
                            or (t>1 and a>=t and b<t and f[0]==b and f[1]>=t))
                        if qcol[k]>0:strict_signs+=1
                columns+=1;current_entries+=len(edges)
            graphs+=1
    print('MATCHING_DELETION_ENDPOINT_EXACT_OK',
          'graphs='+str(graphs),'columns='+str(columns),
          'current_entries='+str(current_entries),
          'positive_disjoint_entries='+str(strict_signs))
if __name__=='__main__':run()
