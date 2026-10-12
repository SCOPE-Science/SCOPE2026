"""Direct finite-field enumerations for the Kronecker path-algebra Hom/retraction theorem.
Usage: python checker.py  (Python 3 standard library only).
"""
from itertools import product
from math import prod, comb
from collections import Counter

def mul(x,y,q):
    return ((x[0]*y[0])%q, (x[1]*y[1])%q, *tuple((x[0]*y[j]+x[j]*y[1])%q for j in range(2,len(x))))

def add(x,y,q):
    return tuple((a+b)%q for a,b in zip(x,y))

def rank_cols(vectors,q):
    if not vectors:return 0
    a=[list(row) for row in zip(*vectors)]
    h=0; width=len(vectors)
    for c in range(width):
        pivot=next((i for i in range(h,len(a)) if a[i][c]),None)
        if pivot is None:continue
        a[h],a[pivot]=a[pivot],a[h]
        inv=pow(a[h][c],-1,q)
        a[h]=[(t*inv)%q for t in a[h]]
        for j in range(len(a)):
            if j!=h:
                f=a[j][c]
                if f:a[j]=[(p-f*t)%q for p,t in zip(a[j],a[h])]
        h+=1
        if h==len(a):break
    return h

def binom_q(n,k,q):
    if k<0 or k>n:return 0
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    return num//den

def predict_end_idem(r,q):
    result=Counter({1:2})
    for d in range(r+1):
        result[d+2]+=binom_q(r,d,q)*q**((d+1)*(r-d))
    return result

def enumerate_hom(r,s,q):
    nb=r+2; mb=s+2
    zero=(0,)*mb
    one=(1,1)+(0,)*s
    sbasis=[]
    for k in range(nb):
        z=[0]*nb;z[k]=1;sbasis.append(tuple(z))
    obasis=[]
    for k in range(mb):
        z=[0]*mb;z[k]=1;obasis.append(tuple(z))
    source_products=[]
    for x in range(nb):
        for y in range(nb):
            xy=mul(sbasis[x],sbasis[y],q)
            nonzeros=tuple((i,v) for i,v in enumerate(xy) if v)
            source_products.append((x,y,nonzeros))
    endo=Counter();count=0
    for columns in product(product(range(q),repeat=mb),repeat=nb):
        if add(columns[0],columns[1],q)!=one:continue
        if any(mul(columns[i],columns[j],q)!=tuple(sum(v*columns[k][h] for k,v in nz)%q for h in range(mb)) for i,j,nz in source_products):continue
        count+=1
        if r==s:
            idem=all(tuple(sum(col[k]*columns[k][h] for k in range(nb))%q for h in range(mb))==col for col in columns)
            if idem:endo[rank_cols(columns,q)]+=1
    predicted=q**(s*(r+1))+q**s+2
    assert count==predicted,(r,s,q,count,predicted)
    if r==s: assert endo==predict_end_idem(r,q),(r,q,endo,predict_end_idem(r,q))
    print(f'r={r}, s={s}, q={q}: hom={count}, retraction_ranks={dict(sorted(endo.items()))}')

def main():
    for args in [(1,1,2),(1,2,2),(2,1,2),(2,2,2),(1,1,3)]:
        enumerate_hom(*args)
    for r in range(1,8):
        for q in (2,3,5):
            polynomial=predict_end_idem(r,q)
            assert sum(polynomial.values()) == 2+sum(binom_q(r,d,q)*q**((d+1)*(r-d)) for d in range(r+1))
            assert polynomial[r+2]==1 and polynomial[1]==2
    print('VERIFY_OK')

if __name__=='__main__':main()
