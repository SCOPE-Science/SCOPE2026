"""Independent exhaustive checks for k-limited domination on two-layer clique prisms."""
from itertools import product
from collections import Counter
from math import factorial, comb

def multinomial(n, z):
    r=factorial(n)
    for a in z:r//=factorial(a)
    return r

def predicted(n,k):
    res=Counter()
    if k>=1:res[n]+=2
    for c in range(n+1):
        for x in range(n-c+1):
            for y in range(n-c-x+1):
                d=n-c-x-y
                a=c+x;b=c+y
                if a==n or b==n:continue
                if a+(y>0)>k or b+(x>0)>k:continue
                res[x+y+2*d]+=multinomial(n,(c,x,y,d))
    return res

def brute(n,k):
    nei=[]
    for row in (0,1):
        for i in range(n):
            nei.append(tuple(row*n+j for j in range(n) if j!=i)+( (1-row)*n+i,))
    res=Counter()
    for mask in range(1<<2*n):
        yes=True
        for v in range(2*n):
            if (mask>>v)&1:
                if sum(1 for w in nei[v] if not((mask>>w)&1))>k:yes=False;break
            else:
                if not any((mask>>w)&1 for w in nei[v]):yes=False;break
        if yes:res[mask.bit_count()]+=1
    return res

def min_count(n,k):
    if k==0:return 2*n,1
    if k>=n:return 2,n*n+(2 if n==2 else 0)
    if 2*k<n:return n,2
    if 2*k==n:return n,2+comb(n,k)
    return 2*(n-k),comb(n,k)

if __name__=='__main__':
    tests=0;total=0
    for n in range(2,9):
        for k in range(n+1):
            x=predicted(n,k);y=brute(n,k)
            assert x==y,(n,k,x,y)
            actual=min(y)
            assert (actual,y[actual])==min_count(n,k),(n,k,actual,y[actual],min_count(n,k))
            tests+=1;total+=sum(y.values())
    for n in range(9,36):
        for k in range(n+1):
            if k in [0,1,n//2,(n+1)//2,n-1,n]:
                p=predicted(n,k)
                assert (min(p),p[min(p)])==min_count(n,k),(n,k,min(p),p[min(p)])
    print(f'VERIFY_OK exhaustive_graph_parameter_pairs={tests} feasible_sets_total={total} n_range=2..8; analytic_min_cases=9..35')
