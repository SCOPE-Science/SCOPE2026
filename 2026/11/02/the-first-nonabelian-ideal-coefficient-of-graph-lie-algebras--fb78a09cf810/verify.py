import itertools, math

def rref_subspaces(d, r, q):
    for piv in itertools.combinations(range(d), r):
        slots=[(i,j) for i in range(r) for j in range(piv[i]+1,d) if j not in piv]
        for val in itertools.product(range(q),repeat=len(slots)):
            rows=[[0]*d for _ in range(r)]
            for i, p in enumerate(piv):rows[i][p]=1
            for (i,j),v in zip(slots,val):rows[i][j]=v
            yield rows, piv

def in_span(vec,rows,piv,q):
    x=list(vec)
    for row,p in zip(rows,piv):
        t=x[p]
        if t:
            for j in range(p,len(x)):
                x[j]=(x[j]-t*row[j])%q
    return all(a==0 for a in x)

def count_ideals(n,edges,q):
    d=n+len(edges)
    if d<3:return 0
    eindex={tuple(sorted(e)):n+i for i,e in enumerate(edges)}
    good=0
    for rows,pivs in rref_subspaces(d,d-3,q):
        ok=True
        for row in rows:
            for v in range(n):
                out=[0]*d
                for a in range(n):
                    k=eindex.get((min(a,v),max(a,v))) if a!=v else None
                    if k is not None:out[k]=(out[k]+row[a]*(1 if a<v else -1))%q
                if not in_span(out,rows,pivs,q):
                    ok=False;break
            if not ok:break
        good+=ok
    return good

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    nu=math.prod(q**n-q**i for i in range(k))
    de=math.prod(q**k-q**i for i in range(k))
    return nu//de

def subcomp(n,edges,q):
    E={tuple(sorted(e)) for e in edges}
    sum2=0
    for mask in range(1,1<<n):
        S=[v for v in range(n) if mask>>v&1]
        unseen=set(S)
        c=0
        while unseen:
            c+=1
            cur=[unseen.pop()]
            while cur:
                v=cur.pop()
                adj=[u for u in unseen if tuple(sorted((v,u))) not in E]
                for u in adj:unseen.remove(u);cur.append(u)
        sum2+=(q-1)**len(S)*((q+1)**c-(q+1))
    assert sum2%((q*q-1)*(q*q-q))==0
    return gaussian(n,3,q)+q**(n-2)*(sum2//((q*q-1)*(q*q-q)))

if __name__=='__main__':
    cases=[]
    for q in [2,3]:
        for n in range(2,4):
            universe=list(itertools.combinations(range(n),2))
            for bits in range(1<<len(universe)):
                edges=[e for i,e in enumerate(universe) if bits>>i&1]
                if n+len(edges)<3:continue
                expect=subcomp(n,edges,q)
                actual=count_ideals(n,edges,q)
                assert actual==expect,(n,edges,q,expect,actual)
                cases.append((n,edges,q,actual))
    for edges in [[(0,1),(1,2)],[(0,1),(1,2),(2,3)],[(0,1),(2,3)]]:
        n=4;q=2
        actual=count_ideals(n,edges,q); expect=subcomp(n,edges,q)
        assert actual==expect,(n,edges,actual,expect)
        cases.append((n,edges,q,actual))
    print('VERIFY_OK cases='+str(len(cases)))
    for x in cases:print(x)
