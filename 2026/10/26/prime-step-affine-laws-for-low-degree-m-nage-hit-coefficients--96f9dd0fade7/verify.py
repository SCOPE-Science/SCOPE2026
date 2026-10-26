from math import factorial, comb

def h(n,r):
    if n < r:return 0
    if n==0:return int(r==0)
    out=0
    for k in range(r,n+1):
        b=2*n*factorial(2*n-k-1)*factorial(n-k)//(factorial(2*n-2*k)*factorial(k-r)*factorial(r))
        out+=(-1)**(k-r)*b
    return out

def fallen(a,m):
    out=1
    for j in range(m):out*=a-j
    return out

def modform(n,r,p):
    A=B=0
    if r==0:
        for j in range(p):
            t=(-1)**j*factorial(j)
            N=n+j
            A+=t*(comb(N,2*j) if 2*j<=N else 0)
            N=n+j-1
            A+=t*(comb(N,2*j) if 2*j<=N else 0)
            if 2*j>=p:
                B+=t*(comb(n+j,2*j-p)+comb(n+j-1,2*j-p))
    else:
        inv=pow(factorial(r),-1,p)
        for j in range(p):
            t=(-1)**j*factorial(j)*fallen(n-j-1,r-1)*2*n
            N=n+j-1
            if 2*j<=N:A+=t*comb(N,2*j)
            if 2*j>=p:B+=t*comb(N,2*j-p)
        A*=inv; B*=inv
    return A%p,B%p

primes=[2,3,5,7,11,13,17]
count=0
for p in primes:
    for r in range(p):
        for n in range(1,25):
            A,B=modform(n,r,p)
            for k in range(5):
                val=h(n+k*p,r)%p
                target=(-1)**(n+k*p-r)*(A+k*B)%p
                assert val==target,('linear',p,n,k,r,A,B,val,target)
                count+=1
            assert (h(n,r)+2*h(n+p,r)+h(n+2*p,r))%p==0
assert h(4,3)==8 and h(7,3)==994
assert [h(n,2) for n in range(1,13)] == [0, 2, 3, 4, 40, 210, 1477, 11672, 104256, 1036050, 11338855, 135494844]
for n in range(1,65):
    assert h(n+4,2)%2 == h(n,2)%2
assert (h(1,3)+2*h(4,3)+h(7,3))%3==2
print('VERIFY_OK: base direct rook values and',count,'affine-residue cases; p=3 degree-3 failure = 2')
assert count == 6960
