from itertools import combinations

def prism(n):
    N=2*n; adj=[set() for _ in range(N)]
    for l in (0,1):
        for i in range(n):
            u=l*n+i; v=l*n+((i+1)%n); adj[u].add(v); adj[v].add(u)
    for i in range(n):
        adj[i].add(n+i); adj[n+i].add(i)
    return adj

def zf(adj,S):
    B=set(S)
    while True:
        forces=[]
        for u in list(B):
            W=[v for v in adj[u] if v not in B]
            if len(W)==1: forces.append(W[0])
        if not forces: break
        old=len(B); B.update(forces)
        if len(B)==old: break
    return len(B)==len(adj)

def classified(n,S):
    by=[set() for _ in range(n)]
    for v in S: by[v%n].add(v//n)
    occ=[len(x) for x in by]
    ds=[i for i,x in enumerate(occ) if x==2]
    ss=[i for i,x in enumerate(occ) if x==1]
    if len(ds)==2:
        return len(ss)==0 and ((ds[0]-ds[1])%n in (1,n-1))
    if len(ds)==0:
        if len(ss)!=4: return False
        for rail in (0,1):
            if all(by[i]=={rail} for i in ss):
                T=set(ss)
                if any(T=={(a+j)%n for j in range(4)} for a in range(n)): return True
        return False
    if len(ds)!=1 or len(ss)!=2: return False
    d=ds[0]
    offs={((s-d)%n) for s in ss}
    # full column + same-rail singles in four allowed offset pairs
    if len({next(iter(by[s])) for s in ss})==1 and offs in ({1,2},{n-2,n-1},{n-1,2},{1,n-2}):
        return True
    # full column + opposite-rail singles in the two adjacent columns
    if offs=={1,n-1}:
        rails=[next(iter(by[s])) for s in ss]
        return rails[0]!=rails[1]
    return False

checks=0
for n in range(5,12):
    adj=prism(n)
    # prove by finite check no <=3 set and size-4 iff classification
    for k in range(0,4):
        for S in combinations(range(2*n),k):
            checks+=1
            assert not zf(adj,S), (n,S)
    zsets=[]
    for S in combinations(range(2*n),4):
        checks+=1
        a=zf(adj,S); b=classified(n,S)
        assert a==b,(n,S,a,b)
        if a:zsets.append(S)
    assert len(zsets)==13*n,(n,len(zsets))
print(f'VERIFY_OK n_range=5..11 subset_checks={checks} basis_count_formula=13n max_order=22')
