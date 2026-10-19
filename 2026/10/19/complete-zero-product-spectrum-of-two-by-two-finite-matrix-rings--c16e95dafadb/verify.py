#!/usr/bin/env python3
"""Exact independent finite-field tests of the matrix-ring zero-product spectrum.
No third-party libraries are needed. Run: python3 verify.py
"""
from itertools import product


def field(q):
    assert q in (2,3,4,5)
    if q==4:
        add=lambda x,y:x^y
        def mul(x,y):
            v=0
            for i in range(2):
                if (x>>i)&1:
                    for j in range(2):
                        if (y>>j)&1:v^=1<<(i+j)
            if v&8:v^=0b1100 # x^3=x*(x+1)=x^2+x=(x+1)+x=1; reduction x^3+1
            if v&4:v^=0b111  # x^2=x+1
            return v
    else:
        add=lambda x,y:(x+y)%q
        mul=lambda x,y:(x*y)%q
    return add,mul

def mul2(A,B,add,mul):
    a,b,c,d=A;e,f,g,h=B
    return (add(mul(a,e),mul(b,g)),add(mul(a,f),mul(b,h)),
            add(mul(c,e),mul(d,g)),add(mul(c,f),mul(d,h)))

def zero(A):return not any(A)

def det2(A,add,mul,q):
    # In characteristic two negation is itself; otherwise additive inverse mod q.
    v=mul(A[0],A[3]);w=mul(A[1],A[2])
    return add(v,w if q==4 or q==2 else (-w)%q)

def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def poly_pow(a,k):
    b=[1]
    for _ in range(k):b=poly_mul(b,a)
    return b

def charpoly(M):
    # Exact Faddeev-LeVerrier, descending coefficients.
    n=len(M)
    B=[[int(i==j) for j in range(n)] for i in range(n)]
    cs=[1]
    for k in range(1,n+1):
        B=matmul(M,B)
        t=sum(B[i][i] for i in range(n))
        assert t%k==0,(k,t)
        c=-t//k; cs.append(c)
        for i in range(n):B[i][i]+=c
    assert not any(any(row) for row in B)
    return cs

def predicted_B(q):
    n=q+1;s=q-1
    trivial=[1,-(2*q*(q-1)-1),-(q-1)*(2*q*q+q-2)]
    standard=[1,-q*(q-2),-(q-1)*(q*q-2)]
    return poly_mul(poly_mul(trivial,poly_pow(standard,q)),
       poly_mul(poly_pow([1,q*s],q),
         poly_mul(poly_pow([1,s],(q+1)*(q-2)//2),
                  poly_pow([1,-s],q*(q-1)//2))))

def predicted_A(q):
    return poly_mul(predicted_B(q),
                    poly_mul(poly_pow([1,0],q*(q+1)*(q-2)),
                             poly_pow([1,1],(q+1)*(q-2))))

def field_lines(q,add,mul):
    return [(1,t) for t in range(q)]+[(0,1)]

def typ(A,lines,q,add,mul):
    k=[]
    for i,(x,y) in enumerate(lines):
        if add(mul(A[0],x),mul(A[1],y))==0 and add(mul(A[2],x),mul(A[3],y))==0:k.append(i)
    assert len(k)==1,(A,k)
    col=(A[0],A[2]) if (A[0],A[2])!=(0,0) else (A[1],A[3])
    imgs=[]
    for i,(x,y) in enumerate(lines):
        lhs=mul(col[0],y);rhs=mul(col[1],x)
        if lhs==rhs:imgs.append(i)
    assert len(imgs)==1,(A,imgs)
    return (k[0],imgs[0])

def run(q):
    add,mul=field(q)
    V=[x for x in product(range(q),repeat=4) if not zero(x) and det2(x,add,mul,q)==0]
    n=q+1;s=q-1; assert len(V)==(q-1)*(q+1)**2
    lines=field_lines(q,add,mul)
    types=[typ(A,lines,q,add,mul) for A in V]
    counts={t:types.count(t) for t in product(range(n),repeat=2)}
    assert set(counts.values())=={q-1}
    for i,A in enumerate(V):
        k1,m1=types[i]
        for j,B in enumerate(V):
            k2,m2=types[j]
            actual=(i!=j and (zero(mul2(A,B,add,mul)) or zero(mul2(B,A,add,mul))))
            expect=(i!=j and (m1==k2 or m2==k1))
            assert actual==expect,(q,A,B,actual,expect)
    idx=list(product(range(n),repeat=2))
    H=[[int(j==k or l==i) for k,l in idx] for i,j in idx]
    B=[[s*H[a][b]-int(a==b and idx[a][0]==idx[a][1]) for b in range(n*n)]for a in range(n*n)]
    cp=charpoly(B)
    assert cp==predicted_B(q),(q,cp,predicted_B(q))
    if q<=3:
        A=[[int(i!=j and (types[i][1]==types[j][0] or types[j][1]==types[i][0]))
            for j in range(len(V))]for i in range(len(V))]
        ap=charpoly(A)
        assert ap==predicted_A(q),(q,ap,predicted_A(q))
    print('q=%s vertices=%s type_quotient=%s characteristic_poly_OK'% (q,len(V),n*n))

if __name__=='__main__':
    for q in (2,3,4,5):run(q)
    print('VERIFY_OK')
