#!/usr/bin/env python3
"""Independent finite-field checks of retraction/image formulas for exterior algebras on three generators.

Uses monomial-mask exterior multiplication and direct substitution of generator images.
Requires only Python's standard library. Intended as finite checks, not an infinite-field proof.
"""
from itertools import product

N=8
SIGN={}
for a in range(8):
    for b in range(8):
        if a&b:
            continue
        swaps=sum((b & ((1<<i)-1)).bit_count() for i in range(3) if (a>>i)&1)
        SIGN[a,b]= -1 if swaps%2 else 1

def mul(a,b,p):
    out=[0]*8
    for i,x in enumerate(a):
        if not x: continue
        for j,y in enumerate(b):
            if y and (i,j) in SIGN:
                out[i|j]=(out[i|j]+SIGN[i,j]*x*y)%p
    return tuple(out)

def add(a,b,p):return tuple((x+y)%p for x,y in zip(a,b))
def scale(a,c,p):return tuple((c*x)%p for x in a)
def vec(mask,c=1):
    out=[0]*8;out[mask]=c;return tuple(out)
ZERO=vec(0,0)
ONE=vec(0)

def eval_elem(a,f,p):
    mon=[ONE]
    for mask in range(1,8):
        # build product of generator images in increasing basis order
        v=ONE
        for i in range(3):
            if mask>>i&1:v=mul(v,f[i],p)
        mon.append(v)
    out=ZERO
    for c,v in zip(a,mon):
        if c:out=add(out,scale(v,c,p),p)
    return out

def good_rel(f,p):
    for i in range(3):
        if mul(f[i],f[i],p)!=ZERO:return False
        for j in range(i+1,3):
            if add(mul(f[i],f[j],p),mul(f[j],f[i],p),p)!=ZERO:return False
    return True

def idempotent(f,p):return all(eval_elem(a,f,p)==a for a in f)

def canonical(rank):
    f=[]
    for j in range(3):f.append(vec(1<<j) if j<rank else ZERO)
    return tuple(f)

def enumerate_fixed_tangent(p,rank):
    # The degree-two/tangent conditions are checked first, then all cubic lifts are tried.
    base=canonical(rank)
    cnt=0;vcount=0
    for coeff in product(range(p),repeat=9):
        f=[]
        for i in range(3):
            v=list(base[i])
            for j,m in enumerate((3,5,6)):v[m]=coeff[3*i+j]
            f.append(tuple(v))
        f=tuple(f)
        if not good_rel(f,p):continue
        if any(eval_elem(a,f,p)[m]!=a[m] for a in f for m in (1,2,4,3,5,6)):
            continue
        vcount+=1
        for tc in product(range(p),repeat=3):
            images=[]
            for i in range(3):
                a=list(f[i]);a[7]=tc[i];images.append(tuple(a))
            images=tuple(images)
            assert good_rel(images,p)
            if idempotent(images,p):cnt+=1
    return cnt,vcount

def subspace_id(vs,p):
    # Reduced row echelon form is a canonical subspace key.
    a=[list(v) for v in vs]
    row=0
    for col in range(8):
        pivot=next((j for j in range(row,len(a)) if a[j][col]%p),None)
        if pivot is None:continue
        a[row],a[pivot]=a[pivot],a[row]
        fac=pow(a[row][col],-1,p)
        a[row]=[(x*fac)%p for x in a[row]]
        for j in range(len(a)):
            if j!=row and a[j][col]:
                fac=a[j][col]
                a[j]=[(x-fac*y)%p for x,y in zip(a[j],a[row])]
        row+=1
        if row==len(a):break
    return tuple(tuple(x) for x in a[:row])

def image_counts_fixed_tangent(p,rank):
    images=set();bases=0
    if rank==1:
        # Fixed tangent line spanned by x; vary all higher coefficients of a.
        for c in product(range(p),repeat=4):
            a=list(vec(1));
            for m,v in zip((3,5,6,7),c):a[m]=v
            if mul(a,a,p)!=ZERO:continue
            bases+=1
            images.add(subspace_id((ONE,tuple(a)),p))
    else:
        # Fixed tangent plane <x,y>; independent lifts a,b with all higher coefficients.
        for c in product(range(p),repeat=8):
            a=list(vec(1));b=list(vec(2))
            for m,v in zip((3,5,6,7),c[:4]):a[m]=v
            for m,v in zip((3,5,6,7),c[4:]):b[m]=v
            a=tuple(a);b=tuple(b)
            if mul(a,a,p)!=ZERO or mul(b,b,p)!=ZERO:continue
            if add(mul(a,b,p),mul(b,a,p),p)!=ZERO:continue
            bases+=1
            images.add(subspace_id((ONE,a,b,mul(a,b,p)),p))
    return len(images),bases

def check_canonical_image_fibers(p):
    # For a specified rank-one image K+Kx, every map to that image is fixed by
    # three coefficients; the condition e(x)=x leaves two free.
    count1=0
    for a,b,c in product(range(p),repeat=3):
        f=(scale(vec(1),a,p),scale(vec(1),b,p),scale(vec(1),c,p))
        if good_rel(f,p) and idempotent(f,p) and f[0]==vec(1):count1+=1
    assert count1==p**2
    # A rank-two image K<x,y> is fixed pointwise; z may map to a*x+b*y+c*xy.
    count2=0
    for a,b,c in product(range(p),repeat=3):
        f=(vec(1),vec(2),add(add(scale(vec(1),a,p),scale(vec(2),b,p),p),scale(vec(3),c,p),p))
        if good_rel(f,p) and idempotent(f,p):count2+=1
    assert count2==p**3
    print('canonical prescribed-image fibers:',p,count1,count2)

def main():
    for p in (3,):
        for r in range(4):
            n,v=enumerate_fixed_tangent(p,r)
            expected=(1,p**3,p**4,1)[r]
            print('fixed',p,r,'idempotents',n,'V-solutions',v)
            assert n==expected,(p,r,n,expected)
        for r in (1,2):
            n,bases=image_counts_fixed_tangent(p,r)
            print('images fixed tangent',p,r,'images',n,'generating tuples',bases)
            assert n==p**3 and bases==(p**3 if r==1 else p**5)
    check_canonical_image_fibers(3)
    # Independent sample replay for larger odd primes.
    for p in (5,7):
        for a,b,c,d in product(range(p),repeat=4):
            # For a rank-two standard tangent projection, the idempotent normal form.
            f=[list(vec(1)),list(vec(2)),list(ZERO)]
            f[0][5]=a;f[0][7]=b
            f[1][6]=a;f[1][7]=c
            f[2][3]=d
            f=tuple(tuple(x) for x in f)
            assert good_rel(f,p) and idempotent(f,p)
        print('rank-two normal-form checked:',p,p**4)
    print('ALL_EXACT_CHECKS_PASSED')
if __name__=='__main__':main()
