from itertools import product
from math import comb

def h_from_set(X,q):
    # Coefficients low-to-high of product_{a in X} (x-a) over the prime field Z/qZ.
    # This helper is used only in prime-field obstruction examples below.
    h=[1]
    for a in sorted(X):
        nh=[0]*(len(h)+1)
        for i,c in enumerate(h):
            nh[i]=(nh[i]-a*c)%q
            nh[i+1]=(nh[i+1]+c)%q
        h=nh
    return h

def divmod_poly(f,g,q):
    f=f[:]
    while f and f[-1]%q==0: f.pop()
    while g and g[-1]%q==0: g=g[:-1]
    assert g
    if not f: return [],[]
    inv=pow(g[-1],-1,q)
    quot=[0]*max(0,len(f)-len(g)+1)
    while len(f)>=len(g):
        c=f[-1]*inv%q
        d=len(f)-len(g)
        quot[d]=c
        for i,a in enumerate(g):
            f[d+i]=(f[d+i]-c*a)%q
        while f and f[-1]%q==0: f.pop()
    return quot,f

def inclusion_exclusion(n,m):
    total=0
    for js in product(range(m+1), repeat=n):
        ways=1
        cells=1
        for j in js:
            ways*=comb(m,j)
            cells*=m-j
        total += (-1)**sum(js)*ways*(2**cells)
    return total

def formula(q,n):
    return 1+sum(comb(q,m)*inclusion_exclusion(n,m) for m in range(1,q+1))

def brute(q,n):
    pts=list(product(range(q), repeat=n))
    total=0
    by_m={}
    noncore_example=None
    for mask in range(1<<len(pts)):
        if mask==0:
            total+=1
            by_m[0]=by_m.get(0,0)+1
            continue
        proj=[set() for _ in range(n)]
        for idx,p in enumerate(pts):
            if (mask>>idx)&1:
                for j,a in enumerate(p):
                    proj[j].add(a)
        ok=all(proj[j]==proj[0] for j in range(1,n))
        if ok:
            total+=1
            m=len(proj[0])
            by_m[m]=by_m.get(m,0)+1
        elif noncore_example is None and q in (2,3):
            noncore_example=proj
    return total,by_m,noncore_example

cases=[(2,2),(2,3),(2,4),(3,2),(4,2)]
expected={
    (2,2):10,
    (2,3):196,
    (2,4):63778,
    (3,2):290,
    (4,2):42610,
}
for q,n in cases:
    b,h,example=brute(q,n)
    f=formula(q,n)
    assert b==f==expected[(q,n)],(q,n,b,f)
    # Decomposition by common projection-set size:
    for m,count in h.items():
        if m==0:
            assert count==1
        else:
            assert count==comb(q,m)*inclusion_exclusion(n,m)
    print({"q":q,"n":n,"core_subsets":b,"by_projection_size":h})

# Explicit prime-field right-ideal obstruction:
# if X_j != X_k, then h_k does not divide h_j in at least one direction.
for q in (2,3):
    Xj={0}
    Xk={0,1}
    hj=h_from_set(Xj,q)
    hk=h_from_set(Xk,q)
    _,rem=divmod_poly(hj,hk,q)
    assert rem != []
    # A polynomial matrix with hj in column j lies in the column-divisibility null ideal,
    # but moving that entry to column k by right multiplication by a matrix unit fails.
    print({"q":q,"obstruction_hj":hj,"required_hk":hk,"remainder":rem})

print("VERIFY_OK")
