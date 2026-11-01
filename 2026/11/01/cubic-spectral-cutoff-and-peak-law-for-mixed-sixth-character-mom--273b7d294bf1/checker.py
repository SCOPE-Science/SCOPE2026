"""Recompute mixed SU(3) character moments by independent exact methods."""
from math import comb


def product(A, B):
    out = {}
    for (a,b), x in A.items():
        for (c,d), y in B.items():
            key = (a+c,b+d)
            out[key] = out.get(key,0) + x*y
    return {key:value for key,value in out.items() if value}


def conjugate(A):
    return {(-a,-b):x for (a,b),x in A.items()}


def h(m):
    d = {}
    for a in range(m+1):
        for b in range(m-a+1):
            c = m-a-b
            k=(a-c,b-c)
            d[k]=d.get(k,0)+1
    return d


def w_factor():
    # |z_i-z_j|^2=(z_i-z_j)(z_i^{-1}-z_j^{-1}) on the torus.
    z=[{(1,0):1},{(0,1):1},{(-1,-1):1}]
    out={(0,0):1}
    for i,j in ((0,1),(0,2),(1,2)):
        dif=z[i].copy()
        for key,value in z[j].items(): dif[key]=dif.get(key,0)-value
        out=product(out,product(dif,conjugate(dif)))
    return out

W=w_factor()
assert W[(0,0)] == 6, W[(0,0)]

def exact_weyl_moment(m, k):
    hm=h(m)
    hk=h(k)
    m2=product(hm,conjugate(hm))
    k2=product(hk,conjugate(hk))
    f=product(product(m2,m2),k2)
    return sum(v*W.get((-a,-b),0) for (a,b),v in f.items())//6


def triangular(i,j,k):
    z=min(i,j,k,i+j-k,i+k-j,j+k-i)
    return max(z+1,0)

def derivative(m,k):
    return sum(triangular(i,j,k) for i in range(m+1) for j in range(m+1))

def formula(m,k):
    if k>2*m:return 0
    if k<=m:return (k+1)**2*(m-k+1)+(comb(k+1,3) if k>=2 else 0)
    return comb(2*m-k+3,3)

count=0
for m in range(20):
    for k in range(2*m+4):
        assert derivative(m,k)==formula(m,k),(m,k)
        count += 1
for m in range(5):
    for k in range(2*m+2):
        calculated=exact_weyl_moment(m,k)
        predicted=sum(formula(m,r) for r in range(k+1))
        assert calculated == predicted,(m,k,calculated,predicted)
        count += 1
for m in range(50):
    a=sum(formula(m,k) for k in range(m+1))
    H=comb(m+2,2)
    assert a==H*(H+1)//2
    count+=1
print('PASS',count,'independent exact numerical assertions')
