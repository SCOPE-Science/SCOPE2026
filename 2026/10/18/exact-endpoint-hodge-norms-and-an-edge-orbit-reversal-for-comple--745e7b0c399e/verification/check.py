"""Exact-rational checks for multipartite cut/cycle projection formulas.
Run: python3 verification/check.py (Python >=3.9; no nonstandard packages).
"""
from fractions import Fraction as F
from itertools import combinations


def inverse(A):
    n=len(A)
    T=[[F(x) for x in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next(i for i in range(j,n) if T[i][j])
        T[j],T[k]=T[k],T[j]
        pivot=T[j][j]
        T[j]=[a/pivot for a in T[j]]
        for i in range(n):
            if i!=j and T[i][j]:
                fac=T[i][j]
                T[i]=[a-fac*b for a,b in zip(T[i],T[j])]
    return [row[n:] for row in T]


def scores(N,a):
    f=F(N*N-2*N+2-a*a,N*(N-a))
    g=f-2*F(N-1,N*(N-a))
    return f,g


def edges(parts):
    ids=[]
    for i,p in enumerate(parts):ids.extend([i]*p)
    return [(u,v) for u in range(len(ids)) for v in range(u+1,len(ids)) if ids[u]!=ids[v]],ids


def inspect(parts):
    N=sum(parts)
    E,ids=edges(parts)
    Lap=[[F(0) for _ in range(N)] for _ in range(N)]
    for u,v in E:
        Lap[u][u]+=1;Lap[v][v]+=1
        Lap[u][v]-=1;Lap[v][u]-=1
    T=[[Lap[i][j]+F(1,N) for j in range(N)] for i in range(N)]
    G=inverse(T)
    eQ=[]; eC=[]
    for u,v in E:
        potentials=[G[w][u]-G[w][v] for w in range(N)]
        assert [sum(Lap[w][j]*potentials[j] for j in range(N)) for w in range(N)] == [F((w==u)-(w==v)) for w in range(N)]
        Qcol=[potentials[x]-potentials[y] for x,y in E]
        q=sum(abs(c) for c in Qcol)
        r=potentials[u]-potentials[v]
        c=1+q-2*r
        f1,g1=scores(N,parts[ids[u]])
        f2,g2=scores(N,parts[ids[v]])
        assert q==f1+f2,(parts,(u,v),'Q',q,f1+f2)
        assert c==1+g1+g2,(parts,(u,v),'C',c,1+g1+g2)
        eQ.append(q);eC.append(c)
    tQ=max(scores(N,a)[0]+scores(N,b)[0] for a,b in combinations(parts,2))
    tC=1+max(scores(N,a)[1]+scores(N,b)[1] for a,b in combinations(parts,2))
    assert (max(eQ),max(eC))==(tQ,tC)
    return len(E)


def partitions(N,lo=1):
    if N==0:
        yield []
        return
    for x in range(lo,N+1):
        for rest in partitions(N-x,x):yield [x]+rest


def main():
    count=columns=0
    for N in range(2,11):
        for P in partitions(N):
            if len(P)<2:continue
            columns+=inspect(P)
            count+=1
    for P in [(1,2,10),(2,3,5),(3,4,4)]:
        columns+=inspect(P); count+=1
    for N in range(6,101):
        a,b,c=N-3,2,1
        af,ag=scores(N,a);bf,bg=scores(N,b);cf,cg=scores(N,c)
        assert af>bf>cf
        assert bg>=cg>ag
        assert 1+bg+cg>af+bf
        assert 1+bg+cg-(af+bf)==2*F((N-5)*(N-1),3*N*(N-2))
    print('VERIFY_OK: %d multipartitions, %d exact edge columns; 95 extremizer-reversal instances' % (count,columns))

if __name__=='__main__':main()
