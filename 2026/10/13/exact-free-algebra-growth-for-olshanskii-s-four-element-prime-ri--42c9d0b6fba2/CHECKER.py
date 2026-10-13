from itertools import product

# Olshanskii's four-element algebra A over F_2 has elements (a,b)=a e+b f
# and multiplication (a,b)(c,d)=(0, ac+ad+bd).
def mul(x,y):
    a,b=x; c,d=y
    return (0,(a*c)^(a*d)^(b*d))

def add(x,y):
    return (x[0]^y[0],x[1]^y[1])

def eval_projection(n,i,points):
    vals=[]
    for p in points:
        vals.append(p[i])
    return vals

def pack(vals):
    z=0
    for j,(a,b) in enumerate(vals):
        z |= (a&1)<<(2*j)
        z |= (b&1)<<(2*j+1)
    return z

def unpack(z,m):
    return [((z>>(2*j))&1,(z>>(2*j+1))&1) for j in range(m)]

def vmul(u,v,m):
    U=unpack(u,m); V=unpack(v,m)
    return pack([mul(x,y) for x,y in zip(U,V)])

def insert_basis(basis,x):
    y=x
    for p in sorted(basis, reverse=True):
        y=min(y,y^basis[p]) if ((y>>p)&1) else y
    if y==0: return False
    p=y.bit_length()-1
    # eliminate pivot from old rows to keep reduced enough for stable closure
    for q in list(basis):
        if (basis[q]>>p)&1:
            basis[q]^=y
    basis[p]=y
    return True

def closure_dimension(n):
    points=list(product([(0,0),(1,0),(0,1),(1,1)], repeat=n))
    m=len(points)
    basis={}
    for i in range(n):
        insert_basis(basis,pack(eval_projection(n,i,points)))
    changed=True
    while changed:
        changed=False
        vecs=list(basis.values())
        prods=[]
        for u in vecs:
            for v in vecs:
                prods.append(vmul(u,v,m))
        for w in prods:
            if insert_basis(basis,w): changed=True
    return len(basis)

for n in (1,2,3):
    d=closure_dimension(n)
    expected=n+4**n-1
    assert d==expected,(n,d,expected)
    print(f'n={n}: dimension={d}, expected={expected}, order=2^{d}')

# Direct pointwise check of the critical square q_i=x_i^2: over A it is zero only at x_i=0.
A=[(0,0),(1,0),(0,1),(1,1)]
zeros=[x for x in A if mul(x,x)==(0,0)]
assert zeros==[(0,0)]
print('square-zero-set=',zeros)
print('CHECK_OK')
