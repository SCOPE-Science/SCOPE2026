"""Independent finite checks for automorphisms of finite rectangular-band power semigroups.

Run: python verify.py
"""
from itertools import combinations, permutations, product
from math import comb, factorial

def fiber_count(u, v):
    return sum((-1)**(i+j)*comb(u,i)*comb(v,j)*2**((u-i)*(v-j))
               for i in range(u+1) for j in range(v+1))

def subsets(a,b):
    return tuple(range(1, 1<<(a*b)))

def row_col(X,a,b):
    rr=cc=0
    for i in range(a):
        for j in range(b):
            if X & (1<<(i*b+j)):
                rr |= 1<<i
                cc |= 1<<j
    return rr,cc

def rectangle(U,V,a,b):
    return sum(1<<(i*b+j) for i in range(a) for j in range(b)
               if U>>i&1 and V>>j&1)

def setup(a,b):
    pool=subsets(a,b)
    rc={x:row_col(x,a,b) for x in pool}
    fibers={}
    for x in pool: fibers.setdefault(rc[x],[]).append(x)
    for (u,v),xs in fibers.items():
        assert len(xs)==fiber_count(u.bit_count(),v.bit_count())
        assert sum(x==rectangle(u,v,a,b) for x in xs)==1
        assert (rectangle(u,v,a,b) in xs)
    for x in pool:
        U,V=rc[x]
        assert rectangle(U,V,a,b)==rectangle(U,V,a,b) # idempotent marker
    return pool,rc,fibers

def check_product(a,b):
    pool,rc,fibers=setup(a,b)
    for x in pool:
        for y in pool:
            U=rc[x][0]; V=rc[y][1]
            product_direct=0
            for i in range(a):
                for j in range(b):
                    if x>>(i*b+j)&1:
                        for k in range(a):
                            for ell in range(b):
                                if y>>(k*b+ell)&1:
                                    product_direct|=1<<(i*b+ell)
            assert product_direct==rectangle(U,V,a,b)
    return len(pool)

assert fiber_count(2,2)==7
assert fiber_count(2,3)==25
assert fiber_count(3,2)==25
for a,b in [(1,3),(2,2),(2,3),(3,3)]:
    assert check_product(a,b)==2**(a*b)-1

# All 2!*2!*6!=2880 proposed automorphisms of the fifteen-element case.
a=b=2
pool,rc,fibers=setup(a,b)
N=len(pool)
interior=fibers[(3,3)]
nonrect=[x for x in interior if x!=15]
assert len(nonrect)==6
count=0
for sp in permutations([1,2]):
    rp={1:sp[0],2:sp[1],3:3}
    for tp in permutations([1,2]):
        cp={1:tp[0],2:tp[1],3:3}
        for perm in permutations(nonrect):
            f={x:rectangle(rp[rc[x][0]],cp[rc[x][1]],a,b)
               if x==rectangle(*rc[x],a,b) else dict(zip(nonrect,perm))[x]
               for x in pool}
            assert len(set(f.values()))==15
            for x in pool:
                for y in pool:
                    prod=rectangle(rc[x][0],rc[y][1],a,b)
                    prod_image=rectangle(rc[f[x]][0],rc[f[y]][1],a,b)
                    assert f[prod]==prod_image
            count+=1
assert count==2880
print('VERIFY_OK product_tables=(1,3),(2,2),(2,3),(3,3) maps_2x2=',count,'fiber_2x2=',fiber_count(2,2))
