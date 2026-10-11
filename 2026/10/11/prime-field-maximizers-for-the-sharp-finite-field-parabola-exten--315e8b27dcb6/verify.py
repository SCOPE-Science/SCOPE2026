from itertools import product

def inv(a,p): return pow(a,p-2,p)
def rank_mod(M,p):
    A=[r[:] for r in M if any(x%p for x in r)]; rank=0; n=len(A[0]) if A else 0
    for c in range(n):
        q=next((i for i in range(rank,len(A)) if A[i][c]%p),None)
        if q is None: continue
        A[rank],A[q]=A[q],A[rank]; s=inv(A[rank][c]%p,p); A[rank]=[(x*s)%p for x in A[rank]]
        for i in range(len(A)):
            if i!=rank and A[i][c]%p:
                s=A[i][c]%p; A[i]=[(A[i][j]-s*A[rank][j])%p for j in range(n)]
        rank+=1
    return rank
def Q(u,v,p): return (u*u+u*v+v*v)%p
def constraints(p):
    M=[]
    for m,u,v in product(range(p),repeat=3):
        if Q(u,v,p)==0: continue
        r=[0]*p
        for x,s in [(m+u,1),(m+v,1),(m-u-v,1),(m-u,-1),(m-v,-1),(m+u+v,-1)]: r[x%p]=(r[x%p]+s)%p
        if any(r): M.append(r)
    return M
def bridge(p):
    js=[j for j in range(p) if (j*j+j+1)%p==0]; n=0
    for u in range(1,p):
        for j in js:
            v=j*u%p; assert Q(u,v,p)==0
            assert any(all(Q(a%p,b%p,p)!=0 for a,b in [(u,w),(u+w,v),(w,v),(u,v+w)]) for w in range(p)); n+=1
    return n
for p in [5,7,11,13,17,19,23,31]:
    M=constraints(p); r=rank_mod(M,p); assert p-r==3; b=bridge(p)
    for c,a,d in (list(product(range(p),repeat=3)) if p<=7 else [(1,2,3),(0,1,1),(4%p,5%p,6%p)]):
        h=[(c+a*x+d*x*x)%p for x in range(p)]
        assert all(sum(row[i]*h[i] for i in range(p))%p==0 for row in M)
    print(f"p={p} rank={r} dim={p-r} bridge_cases={b} constraints={len(M)}")
print("VERIFY_OK")
