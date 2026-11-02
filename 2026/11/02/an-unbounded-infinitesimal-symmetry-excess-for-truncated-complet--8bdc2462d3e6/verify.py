"""Independent finite-field sanity checks for unital k-algebra automorphisms.

Ring basis: 1,y,...,y^(n-1),x,xy,...,xy^(n-1).
No external dependencies; all enumerations are finite checks, not proofs for all n.
"""
from itertools import product

def mul2(a,b,n):
    z=0
    for i in range(2*n):
        if not ((a>>i)&1):continue
        for j in range(2*n):
            if not ((b>>j)&1):continue
            u,v=divmod(i,n); w,t=divmod(j,n)
            if u+w<=1 and v+t<n:z ^= 1<<((u+w)*n+v+t)
    return z

def pow2(a,d,n):
    z=1
    for _ in range(d):z=mul2(z,a,n)
    return z

def brute_f2(n):
    N=2*n
    xs=[x for x in range(0,1<<N,2) if mul2(x,x,n)==0]
    ys=[y for y in range(0,1<<N,2) if pow2(y,n,n)==0]
    count=0
    for x in xs:
        for y in ys:
            det=((x>>n)&1)*((y>>1)&1)^((x>>1)&1)*((y>>n)&1)
            if not det:continue
            assert ((x>>1)&1)==0 and ((x>>n)&1)==1 and ((y>>1)&1)==1
            assert n%2==0 or ((y>>n)&1)==0
            count+=1
    expect=2**(3*n-4+n//2+(n%2==0))
    assert count==expect,(n,count,expect)
    print('AUT_CHECK_OK field=F2 n=',n,'count=',count)

def fm(a,b):
    out=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1:out ^= 1<<(i+j)
    if out&4:out ^= 7 # t^2 = t+1
    return out

def pm4(a,b,n):
    z=[0]*(2*n)
    for i,v in enumerate(a):
        if not v:continue
        u,bi=divmod(i,n)
        for j,w in enumerate(b):
            if not w:continue
            vj,bj=divmod(j,n)
            if u+vj<=1 and bi+bj<n:z[(u+vj)*n+bi+bj] ^= fm(v,w)
    return tuple(z)

def pp4(a,d,n):
    z=(1,)+(0,)*(2*n-1)
    for _ in range(d):z=pm4(z,a,n)
    return z

def brute_f4_n3():
    n=3
    zero=(0,)*(2*n)
    xs=[]; ys=[]
    for v in product(range(4),repeat=2*n-1):
        a=(0,)+v
        if pm4(a,a,n)==zero:xs.append(a)
        if pp4(a,n,n)==zero:ys.append(a)
    count=0
    for x in xs:
        for y in ys:
            det=fm(x[n],y[1]) ^ fm(x[1],y[n])
            if not det:continue
            assert x[1]==0 and x[n]!=0 and y[1]!=0 and y[n]==0
            count+=1
    expected=3**2*4**6
    assert count==expected,(count,expected)
    print('AUT_CHECK_OK field=F4 n=3 count=',count)

def check_derivations():
    for n in (3,4):
        total=0
        for dx in range(1<<(2*n)):
            for dy in range(1<<(2*n)):
                if n%2 and mul2(1<<(n-1),dy,n):continue
                total+=1
        expect=2**(4*n-(2 if n%2 else 0))
        assert total==expect,(n,total,expect)
        print('DER_CHECK_OK field=F2 n=',n,'count=',total)

if __name__=='__main__':
    brute_f2(3);brute_f2(4);brute_f4_n3();check_derivations()
    print('ASYMMETRIC_TRUNCATION_OK')
