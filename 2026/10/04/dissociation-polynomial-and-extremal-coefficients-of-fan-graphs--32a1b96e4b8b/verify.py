from math import comb

def fan(n):
    # F_n = K_1 join P_n. Vertex 0 is the cone; 1..n form the path.
    N=n+1
    adj=[set() for _ in range(N)]
    for v in range(1,n+1):
        adj[0].add(v); adj[v].add(0)
    for v in range(1,n):
        adj[v].add(v+1); adj[v+1].add(v)
    return adj

def is_dissociation(adj,mask):
    for v in range(len(adj)):
        if (mask>>v)&1:
            deg=sum((mask>>u)&1 for u in adj[v])
            if deg>1:
                return False
    return True

def structural(n,mask):
    cone=mask&1
    p=mask>>1
    if cone:
        return p.bit_count()<=1
    # A selected subset of P_n induces max degree <=1 iff it has no 111.
    return all(((p>>i)&7)!=7 for i in range(max(0,n-2)))

def poly_add(a,b):
    m=max(len(a),len(b))
    c=[0]*m
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def poly_shift(a,k):
    return [0]*k+a[:]

def path_poly_rec(n):
    # Weighted binary strings of length n avoiding 111.
    Q=[[1],[1,1],[1,2,1]]
    if n<=2:
        return Q[n]
    for m in range(3,n+1):
        q=poly_add(Q[m-1],poly_shift(Q[m-2],1))
        q=poly_add(q,poly_shift(Q[m-3],2))
        Q.append(q)
    return Q[n]

def path_coeff_formula(n,k):
    # b = number of 1-blocks, each of length 1 or 2.
    total=0
    lo=(k+1)//2
    hi=min(k,n-k+1)
    for b in range(lo,hi+1):
        total += comb(b,k-b)*comb(n-k+1,b)
    return total

def fan_poly_pred(n):
    q=path_poly_rec(n)
    out=q+[0]*max(0,3-len(q))
    out[1]+=1
    out[2]+=n
    return out

def max_count_path(n):
    # closed count at alpha_1(P_n)=ceil(2n/3)
    q,r=divmod(n,3)
    if r==0:
        return (q+1)*(q+2)//2
    if r==1:
        return q+1
    return 1

graphs=subsets=dsets=0
for n in range(2,18):
    adj=fan(n)
    N=n+1
    coeff=[0]*(N+1)
    for mask in range(1<<N):
        subsets+=1
        a=is_dissociation(adj,mask)
        s=structural(n,mask)
        assert a==s,(n,mask,a,s)
        if a:
            dsets+=1
            coeff[mask.bit_count()]+=1
    while len(coeff)>1 and coeff[-1]==0:
        coeff.pop()
    pred=fan_poly_pred(n)
    while len(pred)>1 and pred[-1]==0:
        pred.pop()
    assert coeff==pred,(n,coeff,pred)

    q=path_poly_rec(n)
    for k in range(n+1):
        got=q[k] if k<len(q) else 0
        assert got==path_coeff_formula(n,k),(n,k,got,path_coeff_formula(n,k))

    diss=(2*n+2)//3  # ceil(2n/3)
    assert max(i for i,c in enumerate(coeff) if c)==diss,(n,coeff)
    maxcount=coeff[diss]
    if n==2:
        assert maxcount==3
    elif n==3:
        assert maxcount==6
    else:
        assert maxcount==max_count_path(n),(n,maxcount,max_count_path(n))
    graphs+=1

print("VERIFY_OK")
print("fan_graphs_checked =",graphs)
print("vertex_subsets_checked =",subsets)
print("dissociation_sets_checked =",dsets)
print("path_sizes n = 2..17")
print("all direct degree tests matched the cone/path structural split")
print("all fan polynomial coefficients matched the tribonacci recurrence")
print("all path coefficients matched the closed block-count formula")
print("all dissociation numbers and maximum-set counts matched")
