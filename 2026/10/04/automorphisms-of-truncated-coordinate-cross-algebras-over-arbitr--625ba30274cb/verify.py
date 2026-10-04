from itertools import product
from math import factorial

def det_mod(M,p):
    A=[row[:] for row in M]; n=len(A); det=1
    for c in range(n):
        piv=next((r for r in range(c,n) if A[r][c]%p),None)
        if piv is None:return 0
        if piv!=c:
            A[c],A[piv]=A[piv],A[c]; det=(-det)%p
        v=A[c][c]%p; det=det*v%p
        inv=pow(v,-1,p)
        for j in range(c,n): A[c][j]=A[c][j]*inv%p
        for r in range(c+1,n):
            q=A[r][c]%p
            if q:
                for j in range(c,n):A[r][j]=(A[r][j]-q*A[c][j])%p
    return det%p

def mul(u,v,n,d,p):
    # coordinates ordered (branch j, degree e=1..d-1)
    out=[0]*(n*(d-1))
    for j in range(n):
        off=j*(d-1)
        for a in range(1,d):
            ua=u[off+a-1]
            if not ua: continue
            for b in range(1,d-a):
                vb=v[off+b-1]
                if vb:
                    out[off+a+b-1]=(out[off+a+b-1]+ua*vb)%p
    return out

def valid_images(imgs,n,d,p):
    L=[[imgs[i][j*(d-1)]%p for i in range(n)] for j in range(n)] # rows target branch, cols source
    if det_mod(L,p)==0:return False
    z=[0]*(n*(d-1))
    for i in range(n):
        for k in range(i+1,n):
            if mul(imgs[i],imgs[k],n,d,p)!=z:return False
    return True

def has_normal_form(imgs,n,d,p):
    L=[[imgs[i][j*(d-1)]%p for i in range(n)] for j in range(n)]
    # each row/col exactly one nonzero
    if any(sum(1 for x in row if x)!=1 for row in L): return False
    for i in range(n):
        targets=[j for j in range(n) if L[j][i]]
        if len(targets)!=1:return False
        principal=targets[0]
        for j in range(n):
            if j==principal: continue
            off=j*(d-1)
            if any(imgs[i][off+e-1]%p for e in range(1,d-1)):
                return False
    return True

def count_case(p,n,d):
    rdim=n*(d-1)
    elems=[list(x) for x in product(range(p), repeat=rdim)]
    count=0; nf=0
    for imgs in product(elems, repeat=n):
        if valid_images(imgs,n,d,p):
            count+=1
            if d>=3 and has_normal_form(imgs,n,d,p): nf+=1
    if d==2:
        pred=1
        for i in range(n): pred*=p**n-p**i
        assert count==pred,(p,n,d,count,pred)
    else:
        pred=factorial(n)*(p-1)**n*p**(n*(n+d-3))
        assert count==pred,(p,n,d,count,pred)
        assert nf==count,(p,n,d,nf,count)
    print(f"p={p} n={n} d={d}: count={count} predicted={pred} normal_form={nf if d>=3 else 'n/a'}")

for case in [(2,2,2),(2,3,2),(2,2,3),(3,2,3),(2,2,4),(2,3,3)]:
    count_case(*case)
print('CHECK_OK')
