#!/usr/bin/env python3
"""Direct finite checks for the rank-stratified retraction census.

Only Python standard library; all ring calculations use explicit monomial bases.
The full theorem for arbitrary ranks and characteristics is proved in RESULT.md.
"""
from collections import Counter
from itertools import product
from math import prod


def gaussian(m, r, q):
    numerator = prod(q**(m-i)-1 for i in range(r))
    denominator = prod(q**(r-i)-1 for i in range(r))
    return numerator//denominator


def predicted(p, q, m, r):
    assert q % p == 0 and 0 <= r <= m
    exponent = r*(p**m-p**r)+(m-r)*(p**r-1)-r*(m-r)
    return gaussian(m,r,q)*q**exponent


def mul_binary(a, b, m):
    """Bit masks of monomials x_S; repeated variables multiply to zero."""
    out=0
    n=1 << m
    for s in range(n):
        if (a>>s)&1:
            for t in range(n):
                if ((b>>t)&1) and not (s&t):
                    out ^= 1 << (s|t)
    return out


def rank_binary(columns, m):
    basis={}
    for x in columns:
        while x:
            j=x.bit_length()-1
            if j not in basis:
                basis[j]=x
                break
            x ^= basis[j]
    return len(basis)


def is_idempotent_linear(columns, m):
    for col in columns:
        out=0
        for j in range(m):
            if (col>>j)&1:
                out ^= columns[j]
        if out != col:
            return False
    return True


def exhaustive_binary(m):
    assert m in (2,3)
    # Coefficients of x_S correspond to bit S in a polynomial integer.
    basis_monomials=range(1,1<<m)
    linear_masks=[1<<i for i in range(m)]
    nonlinear_masks=[j for j in basis_monomials if j not in linear_masks]
    lin_polys=[]
    for col in range(1<<m):
        lin_polys.append(sum(1 << (1<<i) for i in range(m) if (col>>i)&1))
    higher_polys=[sum(1<<mask for j,mask in enumerate(nonlinear_masks)
                      if (bits>>j)&1) for bits in range(1<<len(nonlinear_masks))]
    mul_table={}
    def mul(a,b):
        key=(a,b) if a<=b else (b,a)
        if key not in mul_table:
            mul_table[key]=mul_binary(a,b,m)
        return mul_table[key]
    result=Counter()
    # The cotangent map of an idempotent algebra homomorphism must be idempotent;
    # the following loops inspect ALL maps satisfying this necessary condition.
    for cols in product(range(1<<m), repeat=m):
        if not is_idempotent_linear(cols,m):
            continue
        rank=rank_binary(cols,m)
        for highs in product(higher_polys, repeat=m):
            images=[lin_polys[c]^h for c,h in zip(cols,highs)]
            prods=[0]*(1<<m)
            prods[0]=1
            for s in range(1,1<<m):
                lsb=s & (-s)
                i=lsb.bit_length()-1
                prods[s]=mul(prods[s^lsb],images[i])
            def phi(x):
                out=0
                for s in range(1,1<<m):
                    if (x>>s)&1:
                        out ^= prods[s]
                return out
            if all(phi(y)==y for y in images):
                result[rank]+=1
    expected={r:predicted(2,2,m,r) for r in range(m+1)}
    assert dict(result)==expected, (m,result,expected)
    return expected


def power_poly(a, b, p, m):
    """Multiply polynomials over F_p in p-truncated m-variable monomials."""
    out=[0]*(p**m)
    powers=[p**i for i in range(m)]
    digits=[tuple((i//pw)%p for pw in powers) for i in range(p**m)]
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b):
                if bj and all(digits[i][h]+digits[j][h]<p for h in range(m)):
                    k=sum((digits[i][h]+digits[j][h])*powers[h] for h in range(m))
                    out[k]=(out[k]+ai*bj)%p
    return tuple(out)


def check_ternary_images():
    # Additional explicit algebra verification for the nonbinary case p=q=3,m=2.
    import random
    rnd=random.Random(119037)
    p=3
    m=2
    size=p**m
    x=[[0]*size for _ in range(m)]
    for i in range(m): x[i][p**i]=1
    zero=tuple([0]*size)
    one=tuple([1]+[0]*(size-1))
    x=[tuple(v) for v in x]
    def evaluate(images, poly):
        total=[0]*size
        for j,c in enumerate(poly):
            if not c: continue
            term=one
            for v in range(m):
                for _ in range((j//(p**v))%p):
                    term=power_poly(term,images[v],p,m)
            for z,val in enumerate(term): total[z]=(total[z]+c*val)%p
        return tuple(total)
    assert power_poly(x[0],x[0],p,m)!=zero
    for _ in range(200):
        # An arbitrary nilpotent generating tuple defines an algebra endomorphism.
        images=[tuple([0]+[rnd.randrange(p) for _ in range(size-1)]) for i in range(m)]
        assert power_poly(power_poly(images[0],images[0],p,m),images[0],p,m)==zero
        for i in range(m):
            if i==0 and images[i]==x[i]: break
        # Check substitution preserves multiplication on two selected generators.
        assert evaluate(images,power_poly(x[0],x[1],p,m))==power_poly(images[0],images[1],p,m)
    # Enumerate all generated rank-one images: k[y] with y^3=0.
    def rref2(u,v):
        rows=[list(u),list(v)]
        pivot=0
        for col in range(len(u)):
            if pivot==2:break
            k=next((j for j in range(pivot,2) if rows[j][col]),None)
            if k is None:continue
            rows[pivot],rows[k]=rows[k],rows[pivot]
            inv=pow(rows[pivot][col],-1,3)
            rows[pivot]=[(z*inv)%3 for z in rows[pivot]]
            for j in range(2):
                if j!=pivot:
                    factor=rows[j][col]
                    rows[j]=[(x-factor*y)%3 for x,y in zip(rows[j],rows[pivot])]
            pivot+=1
        assert pivot==2
        return tuple(tuple(row) for row in rows)
    images=set()
    embedding_count=0
    for a in range(3**8):
        digits=[]
        z=a
        for _ in range(8):
            digits.append(z%3);z//=3
        y=(0,)+tuple(digits)
        if y[1]==0 and y[3]==0:continue
        y2=power_poly(y,y,3,2)
        images.add(rref2(y[1:],y2[1:]))
        embedding_count+=1
    assert embedding_count==5832
    assert len(images)==972, len(images)
    assert len(images)==gaussian(2,1,3)*3**5
    assert predicted(3,3,2,1)==len(images)*3**2==8748
    return 'GF3_M2_RANKONE_IMAGES_EXHAUSTIVE_OK embeddings=5832 images=972 per-image-retractions=9' 


def main():
    assert exhaustive_binary(2)=={0:1,1:12,2:1}
    assert exhaustive_binary(3)=={0:1,1:448,2:3584,3:1}
    print('P2_M2_AND_M3_IDEMPOTENTS_EXHAUSTIVE_OK')
    print('p=2,q=2,m=2 ranks 0..2: 1 12 1')
    print('p=2,q=2,m=3 ranks 0..3: 1 448 3584 1')
    print(check_ternary_images())
    print('TRUNCATED_RETRACTION_CENSUS_OK')

if __name__=='__main__':main()
