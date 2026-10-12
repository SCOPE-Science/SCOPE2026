from itertools import product

def rank_mod(rows,ncols,p):
    A=[{j:(v%p) for j,v in row.items() if v%p} for row in rows]
    r=0
    for c in range(ncols):
        piv=next((i for i in range(r,len(A)) if A[i].get(c,0)),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],p-2,p)
        A[r]={j:(v*inv)%p for j,v in A[r].items()}
        for i in range(len(A)):
            if i==r: continue
            a=A[i].get(c,0)
            if not a: continue
            nr=dict(A[i])
            for j,v in A[r].items():
                nv=(nr.get(j,0)-a*v)%p
                if nv: nr[j]=nv
                elif j in nr: del nr[j]
            A[i]=nr
        r+=1
        if r==len(A): break
    return r

def constraints(parent,p):
    n=len(parent); w=[0 if parent[i] is None else (i+2)%p for i in range(n)]
    rows=[]; idx=lambda a,i:a*n+i
    def add(d):
        d={a:b%p for a,b in d.items() if b%p}
        if d: rows.append(d)
    for i in range(n):
      for j in range(i+1,n):
        by={}
        if parent[j] is not None:
            b=parent[j]; by.setdefault(b,{})[idx(j,i)]=w[j]
        if parent[i] is not None:
            b=parent[i]; d=by.setdefault(b,{}); d[idx(i,j)]=(d.get(idx(i,j),0)+w[i])%p
        for d in by.values(): add(d)
    for i,par in enumerate(parent):
      if par is None: continue
      c=w[i]
      for a in range(n):
        d={idx(a,par):c}
        if a==par: d[idx(i,i)]=(d.get(idx(i,i),0)-2*c)%p
        add(d)
    return rows

def acyclic(par):
    for i in range(len(par)):
      seen=set(); v=i
      while v is not None:
        if v in seen: return False
        seen.add(v); v=par[v]
    return True

def noisol(par):
    ch=[0]*len(par)
    for i,p in enumerate(par):
      if p is not None: ch[p]+=1
    return all(not (par[i] is None and ch[i]==0) for i in range(len(par)))

def formula(par):
    ch=[[] for _ in par]
    for i,p in enumerate(par):
      if p is not None: ch[p].append(i)
    S=[i for i,p in enumerate(par) if p is None]
    L=[i for i in range(len(par)) if not ch[i]]
    lam=[sum(1 for x in ch[p] if not ch[x]) for p in range(len(par))]
    return len(S)*(1+len(L))+sum(x*(x-1)//2 for x in lam)

tot=0
for n in range(2,6):
  choices=[None]+list(range(n))
  for par in product(choices, repeat=n):
    if any(par[i]==i for i in range(n)) or not acyclic(par) or not noisol(par): continue
    f=formula(par)
    for prime in (1000003,1000033):
      dim=n*n-rank_mod(constraints(par,prime),n*n,prime)
      assert dim==f,(n,par,prime,dim,f)
    tot+=1
assert tot==892
print(f"VERIFY_OK cases={tot} primes=2")
