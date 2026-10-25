"""Exact finite checks of path reversal on higher-independence homology.
Run with python3 verification.py; standard library only.
"""

def degree_rank(r,n):
    d=r+2;k,t=divmod(n,d)
    if n<=r:return (-1,0)
    return (r*(k+1)-1,1) if t==d-1 else ((r*k-1,1) if t==0 else (-1,0))

def predicted(r,n):
    d=r+2;k,t=divmod(n,d)
    if n<=r or t not in (0,d-1):return None
    if t==d-1:k+=1
    if k%2==0: return (-1)**(r*k//2)
    return (-1)**(r*((k-1)//2)+(r+1)//2) if t==d-1 else (-1)**(r*((k-1)//2)+r//2)

def T(r):
    return tuple(tuple((1 if j==0 else (-1 if j==i+1 and i<r else 0)) for j in range(r+1)) for i in range(r+1))

def mul(A,B):
    n=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)) for i in range(n))

def power(A,n):
    m=len(A);out=tuple(tuple(int(i==j) for j in range(m)) for i in range(m))
    while n:
        if n&1:out=mul(out,A)
        A=mul(A,A);n//=2
    return out

def am(r,m):
    return sum(power(T(r),m)[0])

def mat_trace(r,n):
    m=n//2
    if n%2==0:
        F=sum((-1)**ell*am(r,m-ell-1) for ell in range(r//2+1))
    else:
        F=am(r,m)+sum((-1)**(ell+1)*am(r,m-ell-1) for ell in range((r-1)//2+1))
    q,rank=degree_rank(r,n)
    assert rank==1
    return (-1)**(q+1)*F

def word_trace(r,n):
    m=(n+1)//2;F=0
    for choose in range(1<<m):
        half=[(choose>>i)&1 for i in range(m)]
        full=half+(half[::-1] if n%2==0 else half[-2::-1])
        assert len(full)==n
        if any(all(full[j:j+r+1]) for j in range(n-r)):continue
        F+=(-1)**choose.bit_count()
    q,rank=degree_rank(r,n)
    assert rank==1
    return (-1)**(q+1)*F

def rank2(cols):
    piv={}
    for c in cols:
        while c:
            j=c.bit_length()-1
            if j not in piv:piv[j]=c;break
            c^=piv[j]
    return len(piv)

def homology(r,n):
    layers=[[] for _ in range(n+1)]
    for mask in range(1<<n):
        if any(all((mask>>(i+j))&1 for j in range(r+1)) for i in range(n-r)):
            continue
        layers[mask.bit_count()].append(mask)
    ranks=[0]*(n+1)
    for k in range(1,n+1):
        idx={x:i for i,x in enumerate(layers[k-1])};cols=[]
        for x in layers[k]:
            bits=x;c=0
            while bits:
                v=bits&-bits;bits-=v;c^=1<<idx[x^v]
            cols.append(c)
        ranks[k]=rank2(cols)
    return {k-1:len(layers[k])-ranks[k]-(ranks[k+1] if k<n else 0) for k in range(n+1) if len(layers[k])-ranks[k]-(ranks[k+1] if k<n else 0)}

checks=0
for r in range(1,14):
    d=r+2;ident=tuple(tuple(-1 if i==j and r%2 else int(i==j) for j in range(r+1)) for i in range(r+1))
    assert power(T(r),d)==ident
    for k in range(1,10):
        for n in (d*k-1,d*k):
            assert mat_trace(r,n)==predicted(r,n),(r,n)
            checks+=1
            if n<=19:assert word_trace(r,n)==predicted(r,n),(r,n)

chains=0
for r in range(1,5):
    for n in range(max(r+1,2),12):
        q,rank=degree_rank(r,n)
        expected={q:1} if rank else {}
        assert homology(r,n)==expected,(r,n,homology(r,n))
        chains+=1
print('PATH_HIGHER_INDEPENDENCE_REFLECTION_VERIFIED',checks,chains)
