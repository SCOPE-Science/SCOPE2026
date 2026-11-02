#!/usr/bin/env python3
"""Independent finite-field check for the 3x3 Jordan square-zero-sum theorem."""
from itertools import product, permutations
MOD={2:0b11,4:0b111,8:0b1011,16:0b10011}

def mul(x,y,q):
    r=0
    while y:
        if y&1:r^=x
        y>>=1
        x<<=1
        if x&q:x^=MOD[q]
    return r

def inv(a,q):
    assert a
    return next(b for b in range(1,q) if mul(a,b,q)==1)

def determinant3(m,q):
    return _xor(mul(mul(m[0][p[0]],m[1][p[1]],q),m[2][p[2]],q) for p in permutations(range(3)))

def _xor(arr):
    x=0
    for y in arr:x^=y
    return x

def rank(m,q):
    a=[row[:] for row in m]
    r=0
    for col in range(3):
        piv=next((i for i in range(r,3) if a[i][col]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        v=inv(a[r][col],q)
        a[r]=[mul(x,v,q) for x in a[r]]
        for i in range(3):
            if i!=r and a[i][col]:
                z=a[i][col]
                a[i]=[x^mul(z,y,q) for x,y in zip(a[i],a[r])]
        r+=1
    return r

def diagonalizable(d,q):
    # Check eigenspace dimensions against algebraic multiplicities, without assuming a square-free polynomial.
    co2 = d[0][0]^d[1][1]^d[2][2]
    co1 = (mul(d[0][0],d[1][1],q)^mul(d[0][1],d[1][0],q)^
           mul(d[0][0],d[2][2],q)^mul(d[0][2],d[2][0],q)^
           mul(d[1][1],d[2][2],q)^mul(d[1][2],d[2][1],q))
    co0 = determinant3(d,q)
    roots=[]
    for x in range(q):
        val=mul(mul(x,x,q),x,q)^mul(co2,mul(x,x,q),q)^mul(co1,x,q)^co0
        if not val:roots.append(x)
    if not roots:return False,co1,co0
    dimensions=0
    for x in roots:
        m=[[d[i][j]^(x if i==j else 0) for j in range(3)] for i in range(3)]
        dimensions+=3-rank(m,q)
    return dimensions==3,co1,co0

def all_projective_vectors(q):
    for u in product(range(q),repeat=3):
        if u==(0,0,0):continue
        first=next(a for a in u if a)
        if first!=1:continue
        yield u

def check(q):
    count=0; total=1; distribution={}
    for u in all_projective_vectors(q):
        for v in product(range(q),repeat=3):
            if v==(0,0,0):continue
            if _xor(mul(u[i],v[i],q) for i in range(3))!=0:continue
            n=[[mul(ui,vj,q) for vj in v] for ui in u]
            d=[[n[i][j]^(1 if j==i+1 else 0) for j in range(3)] for i in range(3)]
            okay,alpha,beta=diagonalizable(d,q)
            # Consequences of determinant lemma, checked independently from the matrix.
            assert alpha == (mul(v[0],u[1],q)^mul(v[1],u[2],q))
            assert beta == mul(v[0],u[2],q)
            if okay:
                count+=1
                distribution[(alpha,beta)]=distribution.get((alpha,beta),0)+1
            total+=1
    expected=q*q*(q-1)*(q-2)//6
    polys=(q-1)*(q-2)//6
    assert count==expected,(q,count,expected)
    assert len(distribution)==polys,(q,len(distribution),polys)
    assert all(v==q*q for v in distribution.values())
    assert total==1+(q*q+q+1)*(q*q-1)
    print(f'q={q}: square_zero={total}, diagonalizable_sums={count}, distinct_spectra={len(distribution)}, fiber={q*q}, PASS')

if __name__=='__main__':
    for q in (2,4,8,16):check(q)
    print('VERIFY_OK')
