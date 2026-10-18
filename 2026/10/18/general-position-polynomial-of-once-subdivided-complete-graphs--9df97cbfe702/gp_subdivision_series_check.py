"""Exact coefficient replay by labelled-component recurrence, stdlib only."""
from math import comb, factorial

def add(a,b):
    c=a.copy()
    for k,v in b.items(): c[k]=c.get(k,0)+v
    return c

def mult(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():c[i+j]=c.get(i+j,0)+x*y
    return c

def component(k):
    if k==1:return {0:1}
    if k==2:return {1:1}
    a={k-1:k}
    if k==3:a=add(a,{3:1})
    return a

A=[{0:1}]
for n in range(1,10):
    a={}
    for k in range(1,n+1):
        weighted={d:comb(n-1,k-1)*v for d,v in mult(component(k),A[n-k]).items()}
        a=add(a,weighted)
    A.append(a)

expected={
 3:[1,6,15,2],
 4:[1,10,45,30,5],
 5:[1,15,105,175,100,11],
 6:[1,21,210,655,900,357,31]
}
for n in range(3,10):
    p={}
    for u in range(n+1):
        p=add(p,{u+k:comb(n,u)*v for k,v in A[n-u].items()})
    p=add(p,{2:n*(n-1)})
    coeff=[p.get(i,0) for i in range(n+1)]
    assert max(p)<=n, (n,coeff)
    if n in expected:assert coeff==expected[n],(n,coeff)
    m=sum(factorial(n)//(factorial(n-3*t)*6**t*factorial(t))
          for t in range(n//3+1))
    assert coeff[n]==m, (n,coeff[n],m)
    print(f'n={n} max_coeff={m} total_sets={sum(coeff)} coeff={coeff}')
print('SERIES_VERIFICATION_OK n=3..9')
