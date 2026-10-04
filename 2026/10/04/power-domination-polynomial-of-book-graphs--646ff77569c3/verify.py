from itertools import combinations

def book_graph(r):
    # common spine vertices x=0,y=1
    # page i has a_i=2+2i, b_i=3+2i and cycle x-a_i-b_i-y-x
    n=2+2*r
    adj=[set() for _ in range(n)]
    adj[0].add(1); adj[1].add(0)
    for i in range(r):
        a=2+2*i; b=a+1
        for u,v in [(0,a),(a,b),(b,1)]:
            adj[u].add(v); adj[v].add(u)
    return adj

def is_power_dominating(adj, mask):
    blue={v for v in range(len(adj)) if (mask>>v)&1}
    initial=list(blue)
    for v in initial:
        blue.update(adj[v])
    while True:
        changed=False
        for v in list(blue):
            white=[u for u in adj[v] if u not in blue]
            if len(white)==1:
                blue.add(white[0])
                changed=True
                break
        if not changed:
            return len(blue)==len(adj)

def structural(r, mask):
    if mask & 0b11:
        return True
    untouched=0
    for i in range(r):
        a=2+2*i; b=a+1
        if not ((mask>>a)&1) and not ((mask>>b)&1):
            untouched += 1
    return untouched <= 1 and mask != 0

def predicted_coeffs(r):
    # q=x(x+2); P=q(1+x)^(2r) + q^r + r q^(r-1)
    # compute with elementary coefficient arithmetic
    n=2*r+2
    out=[0]*(n+1)
    # q(1+x)^(2r) = (2x+x^2)(1+x)^(2r)
    from math import comb
    for k in range(n+1):
        if 0 <= k-1 <= 2*r:
            out[k] += 2*comb(2*r,k-1)
        if 0 <= k-2 <= 2*r:
            out[k] += comb(2*r,k-2)
    # q^r = x^r(x+2)^r
    for j in range(r+1):
        out[r+j] += comb(r,j)*(2**(r-j))
    # r q^(r-1)
    for j in range(r):
        out[(r-1)+j] += r*comb(r-1,j)*(2**((r-1)-j))
    return out

graphs=subsets=pds=0
for r in range(2,9):
    adj=book_graph(r)
    n=len(adj)
    coeff=[0]*(n+1)
    for mask in range(1<<n):
        subsets += 1
        actual=is_power_dominating(adj,mask)
        pred=structural(r,mask)
        assert actual==pred,(r,mask,actual,pred)
        if actual:
            pds += 1
            coeff[mask.bit_count()] += 1
    assert coeff==predicted_coeffs(r),(r,coeff,predicted_coeffs(r))
    assert sum(coeff)==3*(4**r)+(r+3)*(3**(r-1))
    assert next(k for k,c in enumerate(coeff) if c)==1
    if r==2:
        assert coeff[1]==6
    else:
        assert coeff[1]==2
    graphs += 1

print("VERIFY_OK")
print("book_parameters_checked =",graphs)
print("vertex_subsets_checked =",subsets)
print("power_dominating_sets_checked =",pds)
print("parameters r = 2..8")
print("all direct propagation tests matched the page-intersection classification")
print("all polynomial coefficients matched the closed formula")
print("all total-set counts and minimum-set counts matched")
