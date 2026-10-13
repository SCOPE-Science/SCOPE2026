"""Direct, reproducible small-field checks for rank-one derivation counts."""
from itertools import product


def add(x,y,q):
    return x^y if q==4 else (x+y)%q

def mul(x,y,q):
    if q!=4: return (x*y)%q
    a=(x&1)*(y&1)
    b=((x&1)*((y>>1)&1)+((x>>1)&1)*(y&1))&1
    c=((x>>1)&1)*((y>>1)&1)
    return (a^c)|((b^c)<<1) # alpha^2=alpha+1

def dot(x,y,B,q):
    s=0
    for i,xi in enumerate(x):
        for j,yj in enumerate(y):
            s=add(s,mul(mul(xi,B[i][j],q),yj,q),q)
    return s

def matrank(M,q):
    R=[list(row) for row in M]
    nr,nc=len(R),len(R[0]); t=0
    for c in range(nc):
        h=next((i for i in range(t,nr) if R[i][c]),None)
        if h is None: continue
        R[t],R[h]=R[h],R[t]
        piv=R[t][c]
        inv=next(x for x in range(1,q) if mul(piv,x,q)==1)
        for j in range(c,nc): R[t][j]=mul(R[t][j],inv,q)
        for i in range(nr):
            if i==t or not R[i][c]: continue
            f=R[i][c]
            for j in range(c,nc):
                # subtraction is + for even characteristic and ordinary - for odd
                v=mul(f,R[t][j],q)
                R[i][j]=add(R[i][j],v,q) if q%2==0 else (R[i][j]-v)%q
        t+=1
        if t==nr: break
    return t

def matmul(M,N,q):
    return [[sum((mul(a,b,q) for a,b in zip(row,col)))%q if q!=4 else xor_sum(mul(a,b,q) for a,b in zip(row,col)) for col in zip(*N)] for row in M]

def xor_sum(vals):
    a=0
    for v in vals: a^=v
    return a

def eq_derivation(D,B,q):
    n=len(B); h=n+1
    # on z and each ordered basis bracket (basis bracket zero whenever z occurs)
    for i in range(h):
      for j in range(h):
        cij=B[i][j] if i<n and j<n else 0
        # D([ei,ej]) = cij*D(z)
        for k in range(n):
            if mul(cij,D[k][n],q)!=0:return False
        left=mul(cij,D[n][n],q)
        right=0
        if j<n:
            for k in range(n):right=add(right,mul(D[k][i],B[k][j],q),q)
        if i<n:
            for k in range(n):right=add(right,mul(D[k][j],B[i][k],q),q)
        if left!=right:return False
    return True

def count_actual(B,q):
    n=len(B); h=n+1
    counts={'rank1':0,'idem':0,'squarezero':0,'non_nilpotent':0,'scalar_by_eigenvalue':{}}
    for v in product(range(q), repeat=h*h):
        D=[[v[i*h+j] for j in range(h)] for i in range(h)]
        if matrank(D,q)!=1 or not eq_derivation(D,B,q):continue
        counts['rank1']+=1
        sq=matmul(D,D,q)
        if sq==D:counts['idem']+=1
        if all(not any(row) for row in sq):counts['squarezero']+=1
        else: counts['non_nilpotent']+=1
        for scalar in range(1,q):
            if sq==[[mul(scalar,x,q) for x in row] for row in D]:
                counts['scalar_by_eigenvalue'][scalar]=counts['scalar_by_eigenvalue'].get(scalar,0)+1
    return counts

def expected(B,q):
    n=len(B)
    S=[[add(B[i][j],B[j][i],q) for j in range(n)] for i in range(n)]
    r=n-matrank(S,q)
    if q%2==0:
        # Directly enumerate W for the small-dimensional test cases.
        W=[v for v in product(range(q),repeat=n) if all(xor_sum(mul(S[i][j],v[j],q) for j in range(n))==0 for i in range(n))]
        nonalt=any(dot(v,v,B,q) for v in W)
    else: nonalt=False
    allrank=q**n-1+q*(q**r-1)
    scalar_counts={v:q**r for v in range(1,q)} if nonalt else {}
    nonnil=(q-1)*q**r if nonalt else 0
    return {'rank1':allrank,'idem':q**r if nonalt else 0,'squarezero':allrank-nonnil,'non_nilpotent':nonnil,'scalar_by_eigenvalue':scalar_counts},r,nonalt

def main():
    tests=[
       (2,[[1,0],[0,1]]),
       (2,[[0,1],[1,0]]),
       (2,[[1,1],[0,1]]),
       (2,[[1,0,0],[0,1,0],[0,0,1]]),
       (2,[[0,1,0],[1,0,0],[0,0,1]]),
       (3,[[1,0],[0,1]]),
       (3,[[0,1],[2,0]]),
       (3,[[1,1],[0,1]]),
       (4,[[1,0],[0,1]]),
       (4,[[0,1],[1,0]]),
       (4,[[1,1],[0,1]]),
    ]
    for q,B in tests:
        e,r,nonalt=expected(B,q)
        a=count_actual(B,q)
        if e!=a: raise AssertionError((q,B,r,nonalt,e,a))
        print('CASE_OK',q,len(B),r,nonalt,a['rank1'],a['idem'],a['squarezero'])
    print('VERIFY_OK')

if __name__=='__main__': main()
