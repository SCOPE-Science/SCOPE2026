"""Finite examples for the ideal-image description of affine-quandle equation probabilities.
Run with Python 3 (standard library only). The general theorem is proved separately.
"""
from itertools import product
from fractions import Fraction


def add(A,B,m): return tuple((a+b)%m for a,b in zip(A,B))
def neg(A,m): return tuple(-a % m for a in A)
def mul(A,B,m,n):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%m for i in range(n) for j in range(n))
def apply(A,v,m,n): return tuple(sum(A[i*n+j]*v[j] for j in range(n))%m for i in range(n))
def zero(n): return (0,)*(n*n)
def ident(n): return tuple(int(i==j) for i in range(n) for j in range(n))
def block_diag(matrices):
    ns=[len(B) for B in matrices]
    n=sum(ns)
    out=[[0]*n for _ in range(n)]
    k=0
    for B in matrices:
        for i in range(len(B)):
            for j in range(len(B)): out[k+i][k+j]=B[i][j]
        k+=len(B)
    return tuple(v for row in out for v in row)

def ring(T,m,n):
    Z=zero(n); I=ident(n)
    seen={Z}; q=[Z]
    for a in q:
        for b in (add(a,I,m),mul(T,a,m,n)):
            if b not in seen:
                seen.add(b);q.append(b)
    return seen

def coefficient_clone(T,m,n,R,arity):
    Z=zero(n); I=ident(n)
    U=tuple(tuple(I if i==j else Z for i in range(arity)) for j in range(arity))
    seen=set(U)
    IT=add(I,neg(T,m),m)
    q=list(U)
    # The loop is finite; term operation on coefficient vectors is T*u+(1-T)*v.
    k=0
    while k<len(q):
        a=q[k];k+=1
        for b in list(q):
            for x,y in ((a,b),(b,a)):
                c=tuple(add(mul(T,xi,m,n),mul(IT,yi,m,n),m) for xi,yi in zip(x,y))
                if c not in seen:
                    seen.add(c);q.append(c)
    assert len(seen)==len(R)**(arity-1),(len(seen),len(R),arity)
    return seen

def subgroup_from_generators(vectors, m, n):
    z=(0,)*n
    S={z};q=[z]
    for v in vectors:
        i=0
        while i<len(q):
            b=tuple((q[i][k]+v[k])%m for k in range(n))
            if b not in S: S.add(b);q.append(b)
            i+=1
    return frozenset(S)

def ideal_images(R, elements,m,n):
    z=(0,)*n
    images={frozenset([z])}
    for A in R:
        ra={apply(A,x,m,n) for x in elements}
        new=set(images)
        for I in images:
            H=subgroup_from_generators(list(I)+list(ra),m,n)
            new.add(H)
        images=new
    return {len(x) for x in images}

def run(label,m,T,expected_R,expected_image_sizes,check_arity3=True):
    n=int(len(T)**0.5)
    assert n*n==len(T)
    E=list(product(range(m),repeat=n))
    I=ident(n);Z=zero(n)
    IT=add(I,neg(T,m),m)
    assert len({apply(T,x,m,n) for x in E})==len(E)
    assert len({apply(IT,x,m,n) for x in E})==len(E)
    R=ring(T,m,n)
    assert len(R)==expected_R,(label,len(R),expected_R)
    assert coefficient_clone(T,m,n,R,2)
    if check_arity3: assert coefficient_clone(T,m,n,R,3)
    sizes=ideal_images(R,E,m,n)
    assert sizes==set(expected_image_sizes),(label,sizes,expected_image_sizes)
    # Brute-force probabilities of every two-variable affine term-equation.
    frequencies=set()
    for A in R:
        for B in R:
            count=0
            for x in E:
                for y in E:
                    px=tuple((a+b)%m for a,b in zip(apply(A,x,m,n),apply(add(I,neg(A,m),m),y,m,n)))
                    py=tuple((a+b)%m for a,b in zip(apply(B,x,m,n),apply(add(I,neg(B,m),m),y,m,n)))
                    count+=(px==py)
            frequencies.add(Fraction(count,len(E)**2))
    assert frequencies=={Fraction(1,k) for k in sizes},(label,frequencies,sizes)
    print(label,'R',len(R),'module',len(E),'images',sorted(sizes),'spectrum',sorted(map(str,frequencies)))

# Cyclic module, field case.
run('Z5 T=2',5,(2,),5,{1,5})
# Genuine non-field coefficient ring and intermediate equation probability.
run('Z9 T=2',9,(2,),9,{1,3,9})
# The F4 scalar field is realized without constructing an extension-field package.
run('F2^2 irreducible',2,(0,1,1,1),4,{1,4})
# The F3 Jordan block has minimal polynomial (X-2)^2.
run('F3^2 Jordan',3,(2,1,0,2),9,{1,3,9})
# Direct sum of the unique F4 block and an F8 companion block of X^3+X+1.
A=((0,1),(1,1))
B=((0,1,0),(0,0,1),(1,1,0))
run('F2^4 two irreducible copies',2,block_diag((A,A)),4,{1,16})
run('F2^5 split F4+F8',2,block_diag((A,B)),32,{1,4,8,32},False)
print('VERIFY_OK')
