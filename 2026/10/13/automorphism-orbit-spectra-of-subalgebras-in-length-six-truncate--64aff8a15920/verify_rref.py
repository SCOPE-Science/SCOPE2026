import itertools, collections

def F(q):
    assert q in (2,3,4,5)
    if q==4:
        def add(a,b): return a^b
        def mul(a,b):
            z=0
            for j in range(2):
                if (b>>j)&1: z^=a<<j
            if z&8: z^=0b1100 # x^3=(x^2+x)*x=x^2+x+1 if x^2=x+1, reduce
            if z&4: z^=0b111 # x^2=x+1
            return z
    else:
        def add(a,b):return (a+b)%q
        def mul(a,b):return a*b%q
    return add,mul

def classify(q,n):
    add,mul=F(q); neg=lambda x: (x if q==4 else (-x)%q)
    zero=(0,)*n; tot=collections.Counter(); bydim=collections.Counter(); bad=[]
    for k in range(n+1):
      for piv in itertools.combinations(range(n),k):
        cells=[(i,j) for i,p in enumerate(piv) for j in range(p+1,n) if j not in piv]
        for vs in itertools.product(range(q),repeat=len(cells)):
            basis=[[0]*n for i in range(k)]
            for i,p in enumerate(piv):basis[i][p]=1
            for (i,j),v in zip(cells,vs):basis[i][j]=v
            def inside(v):
                v=v[:]
                for i,p in enumerate(piv):
                    c=v[p]
                    if c:
                        for j in range(p,n):v[j]=add(v[j],mul(neg(c),basis[i][j]))
                return all(t==0 for t in v)
            def product(x,y):
                z=[0]*n
                for i,a in enumerate(x):
                    for j,b in enumerate(y):
                        if a and b and i+j+1<n: z[i+j+1]=add(z[i+j+1],mul(a,b))
                return z
            good=all(inside(product(basis[i],basis[j])) for i in range(k) for j in range(i,k))
            if good:
                bydim[k+1]+=1
                tot[tuple(p+1 for p in piv)]+=1
            else:bad.append((piv,basis))
    return dict(bydim),dict(sorted(tot.items())),len(bad)

if __name__=='__main__':
  for n in (2,3,4,5):
    for q in (2,3,4,5):
      dim,piv,bad=classify(q,n)
      if n==5:
          expected={():1,(1,2,3,4,5):1,(2,3,4,5):1,(3,4,5):1,(4,5):1,(5,):1,(2,4):q*q,(2,4,5):q,(3,):q*q,(3,4):q*q,(3,5):q,(4,):q}
          assert piv==dict(sorted(expected.items())),(q,piv,expected)
          assert sum(dim.values())==6+3*q+3*q*q
      print('n',n+1,'q',q,'total',sum(dim.values()),'dim',dim,'piv',piv,'non_subalgebras',bad,flush=True)
  print('VERIFY_OK')
