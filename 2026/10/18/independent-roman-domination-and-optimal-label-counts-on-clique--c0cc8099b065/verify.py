from itertools import product, combinations

def independent_roman_optima(q,n):
    best=10**6; count=0; good_examples=[]
    for colors in product(range(q),repeat=n):
        if any(colors[j]==colors[(j+1)%n] for j in range(n)):
            continue
        for mask in range(1<<n):
            weight=2*n-mask.bit_count()
            if weight>best:continue
            works=True
            for j in range(n):
                if not ((mask>>j)&1):continue
                target=set(range(q))-{colors[j]}
                if ((mask>>((j-1)%n))&1 or (mask>>((j+1)%n))&1 or {colors[(j-1)%n],colors[(j+1)%n]} !=target):
                    works=False;break
            if works:
                if weight<best:best=weight;count=0;good_examples=[]
                count+=1
                if len(good_examples)<2:good_examples.append((colors,mask))
    return best,count,good_examples

def expected(q,n):
    if q>=4:
        return 2*n, (q-1)**n+(-1)**n*(q-1)
    if n%2==0:
        k=n//2
        return 2*n-k,2*(2**k+2*(-1)**k)
    k=(n-1)//2
    return 2*n-k,n*(2**(k+1)+2*(-1)**(k+1))

def brute(q,n):
  N=q*n
  adj=[0]*N
  for col in range(n):
    for row in range(q):
      v=col*q+row
      for s in range(q):
        if s!=row:adj[v] |= 1<<(col*q+s)
      adj[v] |= 1<<(((col-1)%n)*q+row)
      adj[v] |= 1<<(((col+1)%n)*q+row)
  best=10**9;count=0;supports=0
  for k in range(1,n+1):
    for tup in combinations(range(N),k):
      supp=sum(1<<v for v in tup)
      if any(adj[v] & (supp ^(1<<v)) for v in tup):continue
      supports+=1
      target=((1<<N)-1)^supp
      for pat in range(1<<k):
        W=k+pat.bit_count()
        if W>best:continue
        neigh=0
        for i,v in enumerate(tup):
          if pat>>i&1:neigh |= adj[v]
        if target&~neigh:continue
        if W<best:best=W;count=0
        count+=1
  return best,count,supports

if __name__ == "__main__":
    enc = 0
    for q, limit in ((3, 9), (4, 7), (5, 6)):
        for n in range(3, limit):
            assert independent_roman_optima(q, n)[:2] == expected(q, n), (q, n)
            enc += 1
    direct = 0
    for q, n in ((3, 3), (3, 4), (3, 5), (3, 6), (4, 3), (4, 4), (5, 3)):
        assert brute(q, n)[:2] == expected(q, n), (q, n)
        direct += 1
    print(f"VERIFIED: {enc} independent layer-state enumerations and {direct} direct graph enumerations")
