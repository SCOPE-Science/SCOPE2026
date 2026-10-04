import itertools, math

def partitions(n,r,lo=1):
    if r==0:
        if n==0: yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1): break
        for q in partitions(n-x,r-1,x): yield (x,)+q

def labels(parts):
    L=[]
    for i,a in enumerate(parts): L += [i]*a
    return L

def valid_direct(vals,L):
    n=len(L)
    pos=[v for v,x in enumerate(vals) if x>0]
    for v,x in enumerate(vals):
        neigh=[u for u in range(n) if L[u]!=L[v]]
        if x==0 and sum(vals[u] for u in neigh)<2: return False
        if x>0 and not any(vals[u]>0 for u in neigh): return False
    return True

def valid_criterion(vals,L,r):
    N=len(L); W=sum(vals)
    p=[0]*r; w=[0]*r; z=[0]*r
    for v,x in enumerate(vals):
        i=L[v]
        if x>0: p[i]+=1
        else: z[i]+=1
        w[i]+=x
    if sum(x>0 for x in p)<2: return False
    return all(z[i]==0 or W-w[i]>=2 for i in range(r))

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def powpoly(base,n):
    p=[1]
    for _ in range(n): p=conv(p,base)
    return p

def formula(parts):
    N=sum(parts); r=len(parts)
    maxd=2*N
    A=powpoly([1,1,1],N)+[0]*(maxd+1-(2*N+1))
    q=A[:]
    # subtract sum A_i, add r-1 constant
    for ni in parts:
        Ai=powpoly([1,1,1],ni)
        for k,x in enumerate(Ai): q[k]-=x
    q[0]+=r-1
    # bad_i
    for ni in parts:
        Ai=powpoly([1,1,1],ni)
        Bi=powpoly([0,1,1],ni)
        L=max(len(Ai),len(Bi)); M=[0]*L
        for k in range(L):
            M[k]=(Ai[k] if k<len(Ai) else 0)-(Bi[k] if k<len(Bi) else 0)
        M[0]-=1
        c=N-ni
        for k,x in enumerate(M):
            if k+1<len(q): q[k+1]-=c*x
    # pair intersections
    for i in range(r):
        if parts[i]<2: continue
        for j in range(i+1,r):
            if parts[j]>=2: q[2]+=parts[i]*parts[j]
    return q

def gamma_formula(parts):
    q=sum(n==1 for n in parts); r=len(parts)
    if q>=2: return 2
    if q==1 or r>=3 or min(parts)==2: return 3
    return 4

types=assign=valids=0
for N in range(2,10):
  for r in range(2,N+1):
    for parts in partitions(N,r):
      L=labels(parts); actual=[0]*(2*N+1)
      for vals in itertools.product(range(3), repeat=N):
        assign+=1
        d=valid_direct(vals,L)
        c=valid_criterion(vals,L,r)
        assert d==c,(parts,vals,d,c)
        if d:
          actual[sum(vals)]+=1; valids+=1
      pred=formula(parts)
      assert actual==pred,(parts,actual,pred)
      g=next(k for k,x in enumerate(actual) if x)
      assert g==gamma_formula(parts),(parts,g,gamma_formula(parts))
      types+=1
print('VERIFY_OK')
print('multipartite_types_checked =',types)
print('ternary_assignments_checked =',assign)
print('valid_functions_checked =',valids)
print('orders = 2..9')
print('structural criterion matched direct neighborhood tests')
print('all weight-enumerator coefficients matched')
print('minimum-weight corollary matched')
