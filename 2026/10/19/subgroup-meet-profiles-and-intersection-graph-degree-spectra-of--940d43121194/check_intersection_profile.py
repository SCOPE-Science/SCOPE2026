from itertools import combinations,product
from math import prod,gcd
from collections import Counter

def rank(M,p):
 a=[list(row) for row in M if any(x%p for x in row)];n=len(a);m=len(a[0]) if n else 0;r=0
 for j in range(m):
  piv=next((i for i in range(r,n) if a[i][j]%p),None)
  if piv is None:continue
  a[r],a[piv]=a[piv],a[r];s=pow(a[r][j],-1,p);a[r]=[(v*s)%p for v in a[r]]
  for i in range(n):
   if i!=r and a[i][j]:
    t=a[i][j];a[i]=[(x-t*y)%p for x,y in zip(a[i],a[r])]
  r+=1
  if r==n:break
 return r

def subspaces(p,n):
 v=list(product(range(p),repeat=n))
 spaces=set()
 for k in range(n+1):
  for piv in combinations(range(n),k):
   free=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
   for vals in product(range(p),repeat=len(free)):
    rows=[[0]*n for i in range(k)]
    for i,j in enumerate(piv):rows[i][j]=1
    for (i,j),v0 in zip(free,vals):rows[i][j]=v0
    s=frozenset(tuple(sum(c*rows[i][j] for i,c in enumerate(coeff))%p for j in range(n)) for coeff in product(range(p),repeat=k))
    spaces.add(s)
 return list(spaces)

def gn(n,k,p):
 if k<0 or k>n:return 0
 v=1
 a=prod(p**(n-i)-1 for i in range(k));b=prod(p**(k-i)-1 for i in range(k))
 return a//b

def subs(p,n,m):
 assert (p-1)%m==0
 scal=next(x for x in range(1,p) if pow(x,m,p)==1 and all(pow(x,j,p)!=1 for j in range(1,m)))
 vec=list(product(range(p), repeat=n));Ss=subspaces(p,n);V=frozenset(vec)
 out=[]
 for U in Ss:
  k=next(i for i in range(n+1) if p**i==len(U))
  for d in [d for d in range(1,m+1) if m%d==0]:
   if d==1:
    H=frozenset((u,0) for u in U)
    out.append((k,d,U,(0,)*n,H));continue
   seen=set()
   for a in vec:
    if a in seen:continue
    shift=frozenset(tuple((a[i]+u[i])%p for i in range(n)) for u in U);seen.update(shift)
    H=set()
    for j in range(0,m,m//d):
     lam=pow(scal,j,p)
     for u in U:
      H.add((tuple(((1-lam)*a[i]+u[i])%p for i in range(n)),j))
    out.append((k,d,U,a,frozenset(H)))
 return out

def formula_degree(p,n,m,k,d):
 div=[x for x in range(1,m+1) if m%x==0];tau=len(div);N=sum(gn(n,l,p)*(1+(tau-1)*p**(n-l)) for l in range(n+1))
 c=sum(1 for e in div if e>1 and gcd(e,d)>1) if d>1 else 0
 trivial=sum(gn(n-k,l,p)*p**(k*l)*(1+(tau-1)*p**(n-l)-c*p**k) for l in range(n-k+1))
 return N-trivial-2


if __name__ == '__main__':
    checked = 0
    for p,n,m in [(3,1,2),(3,2,2),(3,3,2),(5,1,4),(5,2,4),(7,2,3),(7,2,6)]:
        sub = subs(p,n,m)
        assert len({x[4] for x in sub}) == len(sub)
        total = len(sub)
        degrees = Counter()
        for k,d,U,a,H in sub:
            if len(H)==1 or len(H)==p**n*m:
                continue
            degree = sum(len(H&K)>1 for _,_,_,_,K in sub)-2
            assert degree == formula_degree(p,n,m,k,d)
            degrees[degree] += 1
        assert sum(degrees.values())==total-2
        print('DEGREES_MATCH',p,n,m,sorted(degrees.items()))
        checked += 1
    for p,n,m in [(3,2,2),(3,3,2),(5,2,4),(7,2,3),(7,2,6)]:
        sub = subs(p,n,m)
        observed = Counter()
        for k,d,U,a,H in sub:
            for ell,e,W,b,K in sub:
                r = next(i for i in range(n+1) if p**i == len(U&W))
                observed[(k,ell,r,d,e,len(H&K))] += 1
        predicted = Counter()
        ds = [d for d in range(1,m+1) if m%d==0]
        for k in range(n+1):
            for ell in range(n+1):
                for r in range(max(0,k+ell-n),min(k,ell)+1):
                    base = gn(n,k,p)*gn(k,r,p)*gn(n-k,ell-r,p)*p**((k-r)*(ell-r))
                    for d in ds:
                        for e in ds:
                            total = (p**(n-k) if d>1 else 1)*(p**(n-ell) if e>1 else 1)
                            matching = p**(n-r) if gcd(d,e)>1 and d>1 and e>1 else 0
                            predicted[(k,ell,r,d,e,p**r)] += base*(total-matching)
                            if matching:
                                predicted[(k,ell,r,d,e,p**r*gcd(d,e))] += base*matching
        assert +observed == +predicted, (p,n,m,observed-predicted,predicted-observed)
        print('MEET_PROFILE_MATCH',p,n,m,len(sub)**2,'ordered subgroup pairs')
        checked += 1
    print('ALL_INTERSECTION_PROFILE_CHECKS_PASSED',checked)
