def barbell(a,b):
    # Left clique is {0,...,a-1}; right clique is {a,...,a+b-1}.
    # The bridge is 0--a.
    n=a+b
    u=0
    v=a
    A=list(range(1,a))
    B=list(range(a+1,n))
    adj=[set() for _ in range(n)]
    for i in range(a):
        for j in range(i+1,a):
            adj[i].add(j); adj[j].add(i)
    for i in range(a,n):
        for j in range(i+1,n):
            adj[i].add(j); adj[j].add(i)
    adj[u].add(v); adj[v].add(u)
    return adj,u,v,A,B

def is_zero_forcing(adj,mask):
    n=len(adj)
    blue=mask
    full=(1<<n)-1
    while True:
        changed=False
        for x in range(n):
            if not ((blue>>x)&1):
                continue
            whites=[y for y in adj[x] if not ((blue>>y)&1)]
            if len(whites)==1:
                blue |= 1<<whites[0]
                changed=True
                break
        if not changed:
            return blue==full

def structural(a,b,u,v,A,B,mask):
    x=sum((mask>>w)&1 for w in A)
    y=sum((mask>>w)&1 for w in B)
    if x < a-2 or y < b-2:
        return False
    # If both bridge endpoints start white, the unique dead configuration
    # at the local thresholds has two whites trapped in each clique.
    if not ((mask>>u)&1) and not ((mask>>v)&1) and x==a-2 and y==b-2:
        return False
    return True

def predicted_coeffs(a,b):
    # Z(B_{a,b};x)=x^(a+b-3)[x^3+(a+b)x^2+(ab+a+b-2)x+(2ab-a-b)]
    n=a+b
    c=[0]*(n+1)
    base=a+b-3
    c[base]=2*a*b-a-b
    c[base+1]=a*b+a+b-2
    c[base+2]=a+b
    c[base+3]=1
    return c

types=subsets=forcing_sets=0
for a in range(3,8):
    for b in range(3,8):
        adj,u,v,A,B=barbell(a,b)
        n=a+b
        coeff=[0]*(n+1)
        for mask in range(1<<n):
            subsets += 1
            actual=is_zero_forcing(adj,mask)
            pred=structural(a,b,u,v,A,B,mask)
            assert actual==pred,(a,b,mask,actual,pred)
            if actual:
                forcing_sets += 1
                coeff[mask.bit_count()] += 1
        assert coeff==predicted_coeffs(a,b),(a,b,coeff,predicted_coeffs(a,b))
        z=next(i for i,c in enumerate(coeff) if c)
        assert z==a+b-3
        assert coeff[z]==2*a*b-a-b
        # Direct total from structural count:
        assert sum(coeff)==4*a*b-(a-1)*(b-1)
        types += 1

print("VERIFY_OK")
print("barbell_parameter_pairs_checked =",types)
print("vertex_subsets_checked =",subsets)
print("zero_forcing_sets_checked =",forcing_sets)
print("parameters a,b = 3..7")
print("all direct color-change tests matched the structural classification")
print("all polynomial coefficients matched the closed formula")
print("all zero-forcing numbers, minimum-set counts, and total counts matched")
