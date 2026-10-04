from math import comb

def parts(n,r,lo=1):
    if r==0:
        if n==0: yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1): break
        for q in parts(n-x,r-1,x): yield (x,)+q

def labels(p):
    out=[]
    for i,n in enumerate(p): out += [i]*n
    return out

def ok(mask,L):
    V=[i for i in range(len(L)) if mask>>i&1]
    return all(sum(1 for u in V if u!=v and L[u]!=L[v])<=1 for v in V)

def pred(p):
    N=sum(p); c=[0]*(N+1); c[0]=1; c[1]=N; c[2]=comb(N,2)
    for k in range(3,N+1): c[k]=sum(comb(n,k) for n in p if n>=k)
    return c

types=subsets=0
for N in range(2,11):
  for r in range(2,N+1):
    for p in parts(N,r):
      L=labels(p); a=[0]*(N+1)
      for m in range(1<<N):
        subsets+=1
        if ok(m,L): a[m.bit_count()]+=1
      assert a==pred(p),(p,a,pred(p)); types+=1

ext=0
for N in range(2,26):
  for r in range(2,N+1):
    q,s=divmod(N,r)
    bal=tuple(sorted([q+1]*s+[q]*(r-s)))
    spl=tuple(sorted([N-r+1]+[1]*(r-1)))
    cb,cs=pred(bal),pred(spl)
    for p in parts(N,r):
      cp=pred(p)
      assert all(cb[k]<=cp[k]<=cs[k] for k in range(N+1))
      if p!=bal: assert cp[3]>cb[3]
      if p!=spl: assert cp[3]<cs[3]
      ext+=1
print("VERIFY_OK")
print("multipartite_types_bruteforced =",types)
print("vertex_subsets_checked =",subsets)
print("coefficientwise_extremal_shapes_checked =",ext)
