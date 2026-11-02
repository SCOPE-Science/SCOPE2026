"""Independent small-instance matrix and rank check for a corner-loop parity grid."""
from functools import reduce

def grid(n, corner):
    h=3; d=3*n; rows=[]
    for i in range(h):
        for j in range(n):
            a=0
            for k,l in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0<=k<h and 0<=l<n:a ^= 1<<(k*n+l)
            if corner and i==j==0:a ^= 1
            rows.append(a)
    return rows

def apply(rows,v):
    return sum(((row&v).bit_count()&1)<<i for i,row in enumerate(rows))

def rank(vectors):
    piv={}
    for v in vectors:
        while v:
            k=v.bit_length()-1
            if k not in piv:piv[k]=v;break
            v^=piv[k]
    return len(piv)

def stable_rank(rows):
    d=len(rows);cols=[1<<j for j in range(d)];old=-1
    for t in range(4*d+1):
        k=rank(cols)
        if k==old:return t-1,k
        old=k
        cols=[apply(rows,v) for v in cols]
    raise AssertionError('no stabilization')

def poly_pred(b):
    n=(1<<b)-1
    return (1<<n)^(1<<(n-1))^reduce(int.__xor__,(1<<((1<<b)-(1<<j)) for j in range(3,b+1)),0)

def exp_moments(rows,d):
    a=1; out=[]
    for k in range(d):
        if a&1:out.append(k)
        a=apply(rows,a)
    return out

for b in (3,4,5):
    n=(1<<b)-1;A=grid(n,False);B=grid(n,True)
    periods=exp_moments(A,3*n)
    expect=[0]+[(1<<j)-2 for j in range(3,b+1)]
    assert periods==expect,(b,periods,expect)
    assert apply(A,0)==0
    assert stable_rank(A)[1]==0
    s,r=stable_rank(B)
    assert r==n,(b,s,r)
    fixed_nullity=3*n-rank([v ^ (1<<i) for i,v in enumerate(B)])
    assert fixed_nullity==int(b%2==0),(b,fixed_nullity)
    assert all(((poly_pred(b)>>i)&1) for i in (0,n,n-1))
    print(f'b={b} n={n}: moments={periods} stable_rank={r} transient_cutoff={s} char_unit_poly_bits={poly_pred(b):x}')
print('VERIFY_MATRIX_OK')
