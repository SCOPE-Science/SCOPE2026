"""Independent exact counts of commuting idempotent transformations."""
from collections import defaultdict
from itertools import product
from math import comb, factorial

def direct(n):
    maps = [a for a in product(range(n), repeat=n) if all(a[a[i]] == a[i] for i in range(n))]
    result = defaultdict(int)
    for f in maps:
        r = len(set(f))
        for g in maps:
            if all(f[g[i]] == g[f[i]] for i in range(n)):
                s = len(set(g))
                h = len({f[g[i]] for i in range(n)})
                result[(r,s,h)] += 1
    return dict(result)

def grouped(n):
    # Direct multinomial counting, separate from rooted EGF recurrence.
    result=defaultdict(int)
    if n==0:return {(0,0,0):1}
    for h in range(1,n+1):
      for u in range(n-h+1):
       for v in range(n-h-u+1):
        w=n-h-u-v
        choose=factorial(n)//(factorial(h)*factorial(u)*factorial(v)*factorial(w))
        # Sum all assignments of the u labeled U vertices and v labeled V vertices to h roots.
        choices=0
        for ar in product(range(h),repeat=u):
          uc=[ar.count(i) for i in range(h)]
          for br in product(range(h),repeat=v):
            vc=[br.count(i) for i in range(h)]
            ways=sum((1+uc[i])*(1+vc[i]) for i in range(h))
            choices+=ways**w
        result[(h+u,h+v,h)]+=choose*choices
    return dict(result)

def rooted(N):
    b=[0]*(N+1); t=[1]+[0]*N
    for n in range(1,N+1):
       m=n-1
       b[n]=n*sum(factorial(m)//(factorial(a)*factorial(v)*factorial(m-a-v)) * ((a+1)*(v+1))**(m-a-v) for a in range(m+1) for v in range(m-a+1))
       t[n]=sum(comb(n-1,k-1)*b[k]*t[n-k] for k in range(1,n+1))
    return b,t

if __name__=='__main__':
    b,t=rooted(11)
    assert t==[1,1,7,58,601,7616,113989,1963060,38178193,826879312,19727279461,513864449396]
    for n in range(1,6):
        direct_ = direct(n)
        grouped_=grouped(n)
        assert direct_==grouped_, (n,direct_,grouped_)
        assert sum(direct_.values())==t[n]
        assert all(max(1,r+s-n)<=h<=min(r,s) for (r,s,h) in direct_)
        print(f'n={n}: commuting pairs={t[n]}, nonzero rank triples={len(direct_)}; EXACT_MATCH')
    n=6
    from collections import Counter
    idems=[a for a in product(range(n), repeat=n) if all(a[a[i]]==a[i] for i in range(n))]
    assert len(idems)==1057
    count=sum(all(f[g[i]]==g[f[i]] for i in range(n)) for f in idems for g in idems)
    assert count==t[n]
    print(f'n={n}: commuting pairs={count}, EXACT_MATCH')
    print('CHECKER_OK')
