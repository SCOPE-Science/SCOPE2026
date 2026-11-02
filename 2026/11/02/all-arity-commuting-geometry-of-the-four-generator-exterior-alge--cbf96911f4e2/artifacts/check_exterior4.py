"""Independent finite-field checks for commuting tuples in the exterior algebra on four generators.
Run with Python 3 standard library. No auxiliary files are required.
"""
from itertools import product
from collections import Counter

ODD = tuple(i for i in range(16) if i.bit_count()%2)
EVEN = tuple(i for i in range(16) if i.bit_count()%2==0)
DEG1 = tuple(1<<i for i in range(4))
DEG3 = tuple(i for i in ODD if i.bit_count()==3)
OUT = tuple(i for i in EVEN if i not in (0,))

def multiply(a, b, p):
    out = [0]*16
    for x in range(16):
        if not a[x]: continue
        for y in range(16):
            if not b[y] or x&y: continue
            inversions = sum((x >> (j+1)).bit_count() for j in range(4) if (y>>j)&1)
            sign = -1 if inversions%2 else 1
            out[x|y] = (out[x|y]+sign*a[x]*b[y])%p
    return out

def vector_in_odd(values):
    out=[0]*16
    for i,v in zip(ODD,values):out[i]=v
    return out

def rank(mat,p):
    a=[list(row) for row in mat]
    if not a:return 0
    rows=len(a); cols=len(a[0]); piv=0
    for c in range(cols):
        at=next((r for r in range(piv,rows) if a[r][c]%p),None)
        if at is None: continue
        a[piv],a[at]=a[at],a[piv]
        v=pow(a[piv][c]%p,-1,p)
        a[piv]=[(x*v)%p for x in a[piv]]
        for r in range(rows):
            if r!=piv and a[r][c]%p:
                w=a[r][c]
                a[r]=[(x-w*y)%p for x,y in zip(a[r],a[piv])]
        piv+=1
        if piv==rows:break
    return piv

def adjoint_odd_rank(values,p):
    x=vector_in_odd(values)
    cols=[]
    for basis in ODD:
        b=[0]*16;b[basis]=1
        xy=multiply(x,b,p);yx=multiply(b,x,p)
        cols.append([(xy[k]-yx[k])%p for k in OUT])
    return rank(list(zip(*cols)),p)

def odd_tuple_commutes(tup,p):
    for i in range(len(tup)):
        for j in range(i):
            a=vector_in_odd(tup[i]); b=vector_in_odd(tup[j])
            ab=multiply(a,b,p);ba=multiply(b,a,p)
            if any((ab[k]-ba[k])%p for k in range(16)):
                return False
    return True

def formula_odd_count(q,m):
    return q**(4*m) + ((q**4-1)//(q-1))*(q**m-1)*q**(3*m+1)

def formula_full_count(q,m):
    return q**(8*m)*formula_odd_count(q,m) if q%2 else q**(16*m)

def support_one(v,p):
    # 4 x m matrix supplied as list of columns of length four.
    return rank(list(zip(*v)),p)<=1

def direct_w_rank(v,p):
    # The unknowns are the 4*m degree-three coefficients, and the equations
    # come from the degree-four coefficient of the commutator for each pair.
    m=len(v)
    rows=[]
    for i in range(m):
        for j in range(i):
            row=[]
            for k in range(m):
                for b in DEG3:
                    a=vector_in_odd([0]*8)
                    for z,val in zip(DEG1,v[i]):a[z]=val
                    c=[0]*16;c[b]=1
                    ac=multiply(a,c,p);ca=multiply(c,a,p)
                    coeff_i=(ac[15]-ca[15])%p
                    a=[0]*16
                    for z,val in zip(DEG1,v[j]):a[z]=val
                    ac=multiply(a,c,p);ca=multiply(c,a,p)
                    coeff_j=(ac[15]-ca[15])%p
                    row.append((coeff_i if k==j else (-coeff_j if k==i else 0))%p)
            rows.append(row)
    return rank(rows,p)

def rank_one_columns(p,m):
    # Canonical generator of a line: first nonzero coordinate set to 1.
    for v in product(range(p),repeat=4):
        if not any(v):continue
        first=next(x for x in v if x)
        if first!=1:continue
        for t in product(range(p),repeat=m):
            if any(t):yield [tuple((s*x)%p for x in v) for s in t]

def check_exhaustive_rank3():
    p=3
    counts=Counter(adjoint_odd_rank(x,p) for x in product(range(p),repeat=8))
    expected={0:1,1:p**4-1,4:(p**4-1)*p**4}
    assert dict(counts)==expected,(counts,expected)
    actual=sum(num*p**(8-r) for r,num in counts.items())
    assert actual==formula_odd_count(p,2)
    print('EXHAUSTIVE_ADJOINT_F3',dict(sorted(counts.items())),'PAIR_ODD',actual)

def check_linear_fibers(p,m):
    columns=list(rank_one_columns(p,m))
    expected=((p**4-1)//(p-1))*(p**m-1)
    assert len(columns)==expected,(len(columns),expected)
    total=p**(4*m)
    histogram=Counter()
    for v in columns:
        r=direct_w_rank(v,p)
        histogram[r]+=1
        total+=p**(4*m-r)
    assert total==formula_odd_count(p,m),(p,m,total,formula_odd_count(p,m))
    assert histogram=={m-1:expected},(p,m,histogram)
    print('FIBER_COUNT',p,m,'rank1_vectors',expected,'equation_ranks',dict(histogram),'odd_total',total)

def check_sample(p,m,seed,count):
    import random
    rng=random.Random(seed)
    for _ in range(count):
        tup=[tuple(rng.randrange(p) for k in range(8)) for _ in range(m)]
        actual=odd_tuple_commutes(tup,p)
        if p==2:
            assert actual
            continue
        v=[];w=[]
        for x in tup:
            elem=vector_in_odd(x)
            v.append(tuple(elem[k] for k in DEG1))
            w.append(tuple(elem[k] for k in DEG3))
        # Directly construct the degree-1 rank condition, and then test
        # the full degree-four exterior product for every pair.
        expected=support_one(v,p)
        if expected:
            for i in range(m):
                for j in range(i):
                    aa=[0]*16;bb=[0]*16
                    for k,x in zip(DEG1,v[i]):aa[k]=x
                    for k,x in zip(DEG3,w[i]):aa[k]=x
                    for k,x in zip(DEG1,v[j]):bb[k]=x
                    for k,x in zip(DEG3,w[j]):bb[k]=x
                    prod=multiply(aa,bb,p)
                    if prod[15]:expected=False
        assert actual==expected,(p,m,tup,actual,expected)
    print('DIRECT_PRODUCT_SAMPLES',p,m,count)

def check_tangent_cones(p=3):
    # At degree-one zero, model the fixed cubic columns as a matrix W.
    # Compute the differential of the commuting equations, and independently
    # span all degree-one directions of actual rank-one deformation curves.
    for m in (2,3,4):
        for r in range(min(m,4)+1):
            w=[[int(i==j) if i<r else 0 for j in range(4)] for i in range(m)]
            linear=[]
            for i in range(m):
                for j in range(i):
                    row=[0]*(4*m)
                    for d in range(4):
                        row[4*i+d]=(row[4*i+d]+w[j][d])%p
                        row[4*j+d]=(row[4*j+d]-w[i][d])%p
                    linear.append(row)
            kdim=4*m-rank(linear,p)
            predicted=r*(r+1)//2+m*(4-r)
            assert kdim==predicted,(m,r,kdim,predicted)
            tangents=[]
            for vv in product(range(p),repeat=4):
                if not any(vv):continue
                s=[sum(w[i][d]*vv[d] for d in range(4))%p for i in range(m)]
                if any(s):
                    tangents.append([(s[i]*vv[d])%p for i in range(m) for d in range(4)])
                else:
                    for i in range(m):
                        tangents.append([vv[d] if j==i else 0 for j in range(m) for d in range(4)])
            span=rank(tangents,p)
            assert span==predicted,(m,r,span,predicted)
            assert predicted>4
            print('TANGENT_SPAN',p,m,r,predicted)

def gf4_mul(a,b):
    z=0
    for j in range(2):
        if (b>>j)&1:z ^= a<<j
    if z & 8:z ^= 0b1110
    if z & 4:z ^= 0b111
    return z

def check_gf4(seed=14032916,samples=3000):
    # F_4 = F_2[t]/(t^2+t+1), represented by two-bit integers.
    import random
    rng=random.Random(seed)
    for _ in range(samples):
        a=[rng.randrange(4) for _ in range(16)]
        b=[rng.randrange(4) for _ in range(16)]
        ab=[0]*16;ba=[0]*16
        for x in range(16):
            for y in range(16):
                if x&y:continue
                val=gf4_mul(a[x],b[y]);ab[x|y]^=val
                val=gf4_mul(b[x],a[y]);ba[x|y]^=val
        assert ab==ba
    print('GF4_FULL_EXTERIOR_COMMUTATIVE',samples)

def main():
    assert len(ODD)==len(EVEN)==8
    check_exhaustive_rank3()
    check_tangent_cones()
    check_gf4()
    for p,m in ((3,2),(3,3),(3,4),(5,2)):
        check_linear_fibers(p,m)
    for p,m in ((2,4),(3,2),(3,3),(5,3),(7,4)):
        check_sample(p,m,14032916+p*m,2000)
    print('EXTERIOR4_COMMUTING_GEOMETRY_OK')
if __name__=='__main__':main()
