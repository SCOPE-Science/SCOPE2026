"""Exhaustive multiplication-kernel check for the unitized R_3 quandle algebra.
Run: python3 verify.py. Uses no third-party packages.
"""
from itertools import product

FIELDS = [(2,1,[0,1]),(3,1,[0,1]),(2,2,[1,1,1]),
          (5,1,[0,1]),(7,1,[0,1]),(2,3,[1,1,0,1]),
          (3,2,[1,0,1])]

def is_prime(p):
    return p >= 2 and all(p % j for j in range(2,int(p**.5)+1))

def field(p,d,poly):
    q=p**d
    assert is_prime(p)
    def digs(z):
        return [(z//(p**j))%p for j in range(d)]
    def enc(v):return sum((c%p)*(p**j) for j,c in enumerate(v))
    A=[[enc([(digs(i)[k]+digs(j)[k])%p for k in range(d)]) for j in range(q)] for i in range(q)]
    M=[]
    for i in range(q):
        row=[]
        for j in range(q):
            x=digs(i);y=digs(j); z=[0]*(2*d-1)
            for a in range(d):
                for b in range(d):z[a+b]=(z[a+b]+x[a]*y[b])%p
            for k in range(2*d-2,d-1,-1):
                c=z[k]
                for a in range(d):z[k-d+a]=(z[k-d+a]-c*poly[a])%p
            row.append(enc(z[:d]))
        M.append(row)
    # Check nonzero elements have inverses.
    assert all(any(M[x][y]==1 for y in range(1,q)) for x in range(1,q))
    return q,A,M

def rank(v,q,ADD,MUL):
    arr=[list(x) for x in v]; m=len(arr);r=0
    inv={a:next(b for b in range(1,q) if MUL[a][b]==1) for a in range(1,q)}
    for j in range(len(arr[0])):
        piv=next((i for i in range(r,m) if arr[i][j]),None)
        if piv is None:continue
        arr[r],arr[piv]=arr[piv],arr[r]
        z=inv[arr[r][j]]
        arr[r]=[MUL[z][c] for c in arr[r]]
        for i in range(m):
            if i==r:continue
            c=arr[i][j]
            if c:
                arr[i]=[ADD[arr[i][k]][minus_mul(c,arr[r][k],q,ADD,MUL)] for k in range(len(arr[0]))]
        r+=1
        if r==m:break
    return r

def minus_mul(a,b,q,ADD,MUL):
    t=MUL[a][b]
    return next(x for x in range(q) if ADD[x][t]==0)

def expected(q):
    if q%3==0:n=2*q*q
    elif q%3==1:n=2*q*q-2*q+1
    else:n=2*q*q-1
    return q**3-1+(q-1)*n

# e_i e_j=e_i if equal, and the third basis element otherwise.
def check(p,d,poly):
    q,ADD,MUL=field(p,d,poly)
    def rm(i,j):return i if i==j else 3-i-j
    nzd=0; singular_by_a=[0]*q
    for a,x,y,z in product(range(q),repeat=4):
        coeff=[x,y,z]
        # column j corresponds to e_j, j=0 represents the adjoined unit;
        # column j+1 corresponds to the j-th quandle basis element.
        mat=[[0]*4 for _ in range(4)]
        mat[0][0]=a
        for i in range(3):mat[i+1][0]=coeff[i]
        for j in range(3):
            for i in range(3):
                output=rm(i,j)
                mat[1+output][j+1]=ADD[mat[1+output][j+1]][coeff[i]]
            mat[1+j][1+j]=ADD[mat[1+j][1+j]][a]
        # rank 4 is equivalent to absence of a nonzero annihilator.
        is_singular=rank(mat,q,ADD,MUL)<4
        if is_singular:
            singular_by_a[a]+=1;nzd+=1
    predicted=expected(q)+1
    assert nzd==predicted,(q,nzd,predicted)
    assert singular_by_a[0]==q**3
    assert len(set(singular_by_a[1:]))==1
    print('q=',q, 'singular_including_zero=',nzd,'nonzero_zero_divisors=',nzd-1,
          'nonsingular=',q**4-nzd,'per_nonzero_scalar_coefficient=',singular_by_a[1] if q>1 else '-')
for a in FIELDS:check(*a)
print('VERIFY_OK')
