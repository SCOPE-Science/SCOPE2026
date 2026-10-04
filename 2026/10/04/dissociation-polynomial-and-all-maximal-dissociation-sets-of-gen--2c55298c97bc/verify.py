from math import comb

def windmill(n,m):
    # W_{n,m}=K_1 join nK_m, with n,m>=2.
    N=1+n*m
    adj=[set() for _ in range(N)]
    blades=[]
    cur=1
    for _ in range(n):
        B=list(range(cur,cur+m)); cur+=m
        blades.append(B)
        for v in B:
            adj[0].add(v); adj[v].add(0)
        for a in range(m):
            for b in range(a+1,m):
                u,v=B[a],B[b]
                adj[u].add(v); adj[v].add(u)
    return adj,blades

def is_dissociation(adj,mask):
    for v in range(len(adj)):
        if (mask>>v)&1:
            if sum((mask>>u)&1 for u in adj[v])>1:
                return False
    return True

def structural(blades,mask):
    center=(mask&1)!=0
    counts=[sum((mask>>v)&1 for v in B) for B in blades]
    if center:
        return sum(counts)<=1
    return all(c<=2 for c in counts)

def maximal(adj,mask):
    if not is_dissociation(adj,mask):
        return False
    return all(((mask>>v)&1) or not is_dissociation(adj,mask|(1<<v))
               for v in range(len(adj)))

def predicted_poly(n,m):
    q=[1,m,comb(m,2)]
    a=[1]
    for _ in range(n):
        b=[0]*(len(a)+2)
        for i,x in enumerate(a):
            for j,y in enumerate(q):
                b[i+j]+=x*y
        a=b
    if len(a)<3:
        a += [0]*(3-len(a))
    a[1]+=1
    a[2]+=n*m
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a

types=subsets=diss_sets=max_sets=0
for n in range(2,8):
    for m in range(2,7):
        N=1+n*m
        if N>18:
            continue
        adj,blades=windmill(n,m)
        coeff=[0]*(N+1)
        sizes=[]
        for mask in range(1<<N):
            subsets+=1
            actual=is_dissociation(adj,mask)
            pred=structural(blades,mask)
            assert actual==pred,(n,m,mask,actual,pred)
            if actual:
                diss_sets+=1
                coeff[mask.bit_count()]+=1
                if maximal(adj,mask):
                    max_sets+=1
                    sizes.append(mask.bit_count())
        while len(coeff)>1 and coeff[-1]==0:
            coeff.pop()
        assert coeff==predicted_poly(n,m),(n,m,coeff,predicted_poly(n,m))
        assert sum(coeff)==(1+m+comb(m,2))**n+1+n*m
        assert set(sizes)=={2,2*n},(n,m,set(sizes))
        assert sizes.count(2)==n*m,(n,m,sizes.count(2))
        assert sizes.count(2*n)==comb(m,2)**n,(n,m,sizes.count(2*n))
        assert max(i for i,c in enumerate(coeff) if c)==2*n
        types+=1

print("VERIFY_OK")
print("windmill_parameter_pairs_checked =",types)
print("vertex_subsets_checked =",subsets)
print("dissociation_sets_checked =",diss_sets)
print("maximal_dissociation_sets_checked =",max_sets)
print("parameters n,m>=2 with 1+n*m<=18")
print("all direct degree tests matched the structural classification")
print("all dissociation-polynomial coefficients matched")
print("all total counts, maximum sizes, and maximal-set multiplicities matched")
