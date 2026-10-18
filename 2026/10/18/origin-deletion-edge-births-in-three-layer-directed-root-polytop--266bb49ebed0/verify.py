"""Exact support and nonedge witnesses for three-layer directed edge polytopes.

No numerical tolerance or external package is used. Executing this file checks
all triples 1 <= a,b,c <= 5. The separate mathematical proof handles all sizes.
"""
from itertools import combinations, product


def test(a, b, c):
    A, B, C = range(a), range(a,a+b), range(a+b,a+b+c)
    arcs = [(u,v) for X,Y in ((A,B),(A,C),(B,C)) for u in X for v in Y]
    n=a+b+c
    def t(e):
        u,v=e
        return 'AB' if u in A and v in B else ('AC' if u in A and v in C else 'BC')
    def predicted(e,f):
        p,q=t(e),t(f)
        if p==q: return e[0]==f[0] or e[1]==f[1]
        if set((p,q))=={'AB','AC'}: return e[0]==f[0]
        if set((p,q))=={'AC','BC'}: return e[1]==f[1]
        if p=='BC':e,f=f,e
        return e[1]!=f[0] or b==1
    def expose(e,f):
        p,q=t(e),t(f)
        x=[0]*n
        if p==q:
            layer={'AB':(20,0,10),'AC':(20,10,0),'BC':(10,20,0)}[p]
            for g,v in zip((A,B,C),layer):
                for i in g:x[i]=v
            if e[0]==f[0]:
                x[e[0]]+=2;x[e[1]]-=2;x[f[1]]-=2
            else:
                x[e[1]]-=2;x[e[0]]+=2;x[f[0]]+=2
        elif {p,q}=={'AB','AC'}:
            if p=='AC':e,f=f,e
            for i in A:x[i]=0
            for i in B:x[i]=1
            for i in C:x[i]=1
            x[e[0]]=2;x[e[1]]=0;x[f[1]]=0
        elif {p,q}=={'AC','BC'}:
            if p=='BC':e,f=f,e
            for i in A:x[i]=0
            for i in B:x[i]=1
            for i in C:x[i]=1
            x[e[0]]=2;x[f[0]]=2;x[e[1]]=0
        else:
            if p=='BC':e,f=f,e
            for i in A:x[i]=-1
            for i in B:x[i]=1
            for i in C:x[i]=3
            if e[1]!=f[0]:
                x[e[0]]=1;x[e[1]]=0;x[f[0]]=2;x[f[1]]=1
            else:
                assert b==1
                for i in A:x[i]=-2
                for i in C:x[i]=4
                x[e[0]]=0;x[e[1]]=1;x[f[1]]=2
        selected=x[e[0]]-x[e[1]]
        assert selected==x[f[0]]-x[f[1]]
        for g in arcs:
            if g not in (e,f): assert x[g[0]]-x[g[1]]<selected, (a,b,c,e,f,g,x)
        return selected
    sums={}
    for i,j in combinations(range(len(arcs)),2):
        y=[0]*n
        for k in (i,j):
            u,v=arcs[k];y[u]+=1;y[v]-=1
        sums.setdefault(tuple(y),[]).append((i,j))
    count=0; neg=0
    adj={e:set() for e in arcs}
    for i,j in combinations(range(len(arcs)),2):
        e,f=arcs[i],arcs[j]
        if predicted(e,f):
            tmax=expose(e,f)
            neg += (tmax<0)
            adj[e].add(f);adj[f].add(e);count+=1
        else:
            y=[0]*n
            for u,v in (e,f):y[u]+=1;y[v]-=1
            assert len(sums[tuple(y)])>=2, (a,b,c,e,f)
    N=n-1
    E=sum(p*q*(p+q-2)//2 for p,q in ((a,b),(a,c),(b,c)))+a*b*c*(b+1)+ (a*c if b==1 else 0)
    assert E==count,(a,b,c,count,E)
    da=a+b-2+b*c + (c if b==1 else 0)
    db=b+c-2+a*b + (a if b==1 else 0)
    dc=a+c+2*b-2
    for e in arcs:
        expected={'AB':da,'BC':db,'AC':dc}[t(e)]
        assert len(adj[e])==expected,(a,b,c,e,len(adj[e]),expected)
    for e,f in combinations(arcs,2):
        assert f in adj[e] or len(adj[e]&adj[f])>0, (a,b,c,e,f)
    assert neg==(a*c if b==1 else 0), (a,b,c,neg)
    return len(arcs),count


def main():
    cases=0;v=0;e=0
    for a,b,c in product(range(1,6),repeat=3):
        vv,ee=test(a,b,c);cases+=1;v+=vv;e+=ee
    print('VERIFY_OK', 'parameter_profiles=',cases,'vertices_total=',v,'edges_total=',e)

if __name__=='__main__':main()
