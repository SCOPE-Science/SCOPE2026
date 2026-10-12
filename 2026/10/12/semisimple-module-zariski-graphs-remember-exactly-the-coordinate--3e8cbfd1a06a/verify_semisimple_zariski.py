from itertools import product, combinations, permutations
from math import prod, factorial


def inv(a,p): return pow(a,p-2,p)

def rref(mat,p):
    a=[list(map(lambda x:x%p,row)) for row in mat]
    if not a: return tuple()
    m,n=len(a),len(a[0]); rr=0; piv=[]
    for c in range(n):
        k=next((i for i in range(rr,m) if a[i][c]%p),None)
        if k is None: continue
        a[rr],a[k]=a[k],a[rr]
        z=inv(a[rr][c],p); a[rr]=[(x*z)%p for x in a[rr]]
        for i in range(m):
            if i!=rr and a[i][c]%p:
                z=a[i][c]%p; a[i]=[(x-z*y)%p for x,y in zip(a[i],a[rr])]
        piv.append(c); rr+=1
        if rr==m: break
    return tuple(tuple(row) for row in a[:rr])

def span(vs,p,d):
    return rref(vs,p)

def subspaces(p,d):
    vecs=[v for v in product(range(p), repeat=d) if any(v)]
    subs={tuple()}
    # closure under adding vectors; dimensions tiny in tests
    frontier=[tuple()]
    while frontier:
        B=frontier.pop()
        for v in vecs:
            C=span(B+(v,),p,d)
            if C not in subs:
                subs.add(C); frontier.append(C)
    return sorted(subs, key=lambda B:(len(B),B))

def in_subspace(v,B,p):
    return span(B+(tuple(v),),p,len(v))==B

def proper_count(p,d):
    return len(subspaces(p,d))-1

def supports_graph(a):
    r=len(a)
    supports=[frozenset(S) for k in range(1,r) for S in combinations(range(r),k)]
    w={S:prod(a[i] for i in range(r) if i not in S) for S in supports}
    # expanded graph vertices (S,j)
    V=[(S,j) for S in supports for j in range(w[S])]
    adj={v:set() for v in V}
    for x,y in combinations(V,2):
        if x[0].isdisjoint(y[0]): adj[x].add(y); adj[y].add(x)
    return supports,w,V,adj

def twin_classes(V,adj):
    groups={}
    for v in V: groups.setdefault(frozenset(adj[v]),[]).append(v)
    return list(groups.values())

def quotient_aut_count(r):
    supp=[frozenset(S) for k in range(1,r) for S in combinations(range(r),k)]
    idx={S:i for i,S in enumerate(supp)}
    A=[[False]*len(supp) for _ in supp]
    for i,S in enumerate(supp):
        for j,T in enumerate(supp):
            if i!=j and S.isdisjoint(T): A[i][j]=True
    cnt=0
    for p in permutations(range(len(supp))):
        ok=True
        for i in range(len(supp)):
            for j in range(i+1,len(supp)):
                if A[i][j]!=A[p[i]][p[j]]: ok=False; break
            if not ok: break
        cnt+=ok
    return cnt

def direct_definition_check(primes_dims):
    # R=product F_p, M=direct sum F_p^d; verify prime-submodule and V/adacency/support formulas directly
    comps=[]
    for p,d in primes_dims:
        ss=subspaces(p,d); comps.append((p,d,ss,ss[-1]))
    allN=list(product(*[c[2] for c in comps]))
    full=[c[3] for c in comps]
    def fsupp(N): return frozenset(i for i,B in enumerate(N) if B==full[i])
    # predicted prime submodules: exactly one nonfull coordinate, and there any proper subspace
    pred=[]
    r=len(comps)
    for j,(p,d,ss,F) in enumerate(comps):
        for U in ss[:-1]:
            P=list(full); P[j]=U; pred.append(tuple(P))
    # direct prime definition exhaustive over scalar tuples and module vectors
    scalars=list(product(*[range(c[0]) for c in comps]))
    vectors=list(product(*[list(product(range(c[0]), repeat=c[1])) for c in comps]))
    def vec_in(v,N): return all(in_subspace(v[i],N[i],comps[i][0]) for i in range(r))
    def scalar_in_colon(a,N):
        for i,(p,d,ss,F) in enumerate(comps):
            if a[i]%p and N[i]!=F: return False
        return True
    def act(a,v): return tuple(tuple((a[i]*x)%comps[i][0] for x in v[i]) for i in range(r))
    actual=[]
    for P in allN:
        if P==tuple(full): continue
        ok=True
        for a in scalars:
            for v in vectors:
                if vec_in(act(a,v),P) and (not scalar_in_colon(a,P)) and (not vec_in(v,P)):
                    ok=False; break
            if not ok: break
        if ok: actual.append(P)
    assert set(actual)==set(pred), (len(actual),len(pred))
    # V(N) from definition via colon inclusion
    prime_colon=[fsupp(P) for P in actual]  # full coords of P = [r]\{j}
    def Vset(N):
        S=fsupp(N)
        out=[]
        for z,CP in enumerate(prime_colon):
            if S.issubset(CP): out.append(z)
        return frozenset(out)
    T=frozenset(range(len(actual)))
    vertices=[N for N in allN if N!=tuple(full) and Vset(N)!=T and any(Vset(N)|Vset(K)==T and Vset(K)!=T for K in allN if K!=tuple(full))]
    assert all(fsupp(N) and fsupp(N)!=frozenset(range(r)) for N in vertices)
    predV=[N for N in allN if fsupp(N) and fsupp(N)!=frozenset(range(r))]
    assert set(vertices)==set(predV)
    for N,K in combinations(vertices,2):
        adj=(Vset(N)|Vset(K)==T)
        assert adj==(fsupp(N).isdisjoint(fsupp(K)))
    # fiber sizes
    a=[len(c[2])-1 for c in comps]
    for S in {fsupp(N) for N in vertices}:
        got=sum(fsupp(N)==S for N in vertices)
        want=prod(a[i] for i in range(r) if i not in S)
        assert got==want,(S,got,want)
    return {'dims':primes_dims,'prime_submodules':len(actual),'vertices':len(vertices),'a':a}

checks=[]
checks.append(direct_definition_check([(2,2),(3,1)]))
checks.append(direct_definition_check([(2,2),(2,2)]))
for a in ([2,3],[2,3,4],[1,2,3]):
    supp,w,V,adj=supports_graph(a)
    tc=twin_classes(V,adj)
    assert len(tc)==2**len(a)-2
    got=sorted(len(c) for c in tc); want=sorted(w.values())
    assert got==want
assert quotient_aut_count(2)==factorial(2)
assert quotient_aut_count(3)==factorial(3)
a23=proper_count(2,3); a132=proper_count(13,2)
assert a23==15 and a132==15
# r=2 collision gives K_15,15 on both sides
s,w,V,adj=supports_graph([a23,a23]); assert len(V)==30 and all(len(adj[v])==15 for v in V)
s,w,V,adj=supports_graph([a132,a132]); assert len(V)==30 and all(len(adj[v])==15 for v in V)
print('PASS')
for c in checks: print(c)
print('proper_subspaces_F2^3=',a23,'proper_subspaces_F13^2=',a132)
print('quotient_aut_counts=',quotient_aut_count(2), quotient_aut_count(3))
