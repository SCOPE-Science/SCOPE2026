"""Independent finite-field tests of weighted-zero Rota--Baxter identities.

Usage: python3 verify.py
No third-party dependencies.
"""
from itertools import product
from math import prod


def add(a, b, q):
    return a ^ b if q == 4 else (a+b) % q


def mul(a, b, q):
    if q != 4:
        return (a*b) % q
    a0, a1 = a & 1, a >> 1
    b0, b1 = b & 1, b >> 1
    return (a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1) << 1)


def dot(row, vec, q):
    z = 0
    for a, b in zip(row, vec):
        z = add(z, mul(a, b, q), q)
    return z


def matvec(A, v, q):
    return tuple(dot(row, v, q) for row in A)


def times(x, y, q):
    return (mul(x[0], y[0], q),) + tuple(
        add(mul(x[0], y[i], q), mul(y[0], x[i], q), q)
        for i in range(1, len(x))
    )


def rb_direct(P, q):
    d = len(P)
    basis = [tuple(int(i==j) for i in range(d)) for j in range(d)]
    for x in basis:
        for y in basis:
            px, py = matvec(P, x, q), matvec(P, y, q)
            first = times(px, py, q)
            xp, pyx = times(x, py, q), times(px, y, q)
            second = matvec(P, tuple(add(a, b, q) for a, b in zip(xp, pyx)), q)
            if first != second:
                return False
    return True


def squarezero(B, q):
    n = len(B)
    return all(dot(B[i], tuple(B[k][j] for k in range(n)), q)==0
               for i in range(n) for j in range(n))


def proposed(P, q):
    n = len(P)-1
    if any(P[0]):
        return False
    B = tuple(tuple(row[1:]) for row in P[1:])
    v = tuple(row[0] for row in P[1:])
    return squarezero(B, q) and (q % 2 == 0 or not any(matvec(B, v, q)))


def mat_rank(A, q):
    a = [list(row) for row in A]
    m = len(a); n = len(a[0]) if m else 0
    r = 0
    for j in range(n):
        ix = next((i for i in range(r,m) if a[i][j]), None)
        if ix is None:
            continue
        a[ix], a[r] = a[r], a[ix]
        inv = next(x for x in range(1,q) if mul(x,a[r][j],q)==1)
        a[r] = [mul(x,inv,q) for x in a[r]]
        for i in range(m):
            if i != r and a[i][j]:
                fac = a[i][j]
                a[i] = [add(x,mul(fac,y,q),q) if q==4 or q==2
                        else (x-mul(fac,y,q))%q for x,y in zip(a[i],a[r])]
        r+=1
    return r


def gaussian(n, r, q):
    if r<0 or r>n:
        return 0
    numer=prod(q**(n-i)-1 for i in range(r))
    denom=prod(q**(r-i)-1 for i in range(r))
    return numer//denom


def rankcount(n, r, q):
    return gaussian(n,r,q)*gaussian(n-r,r,q)*prod(q**r-q**i for i in range(r))


def test_exhaustive(q, n):
    d=n+1
    hist={}
    total=0
    # Independent enumeration: all coefficient arrays, not just the proposed normal form.
    for entries in product(range(q),repeat=d*d):
        P=tuple(tuple(entries[i*d:(i+1)*d]) for i in range(d))
        actual=rb_direct(P,q)
        predicted=proposed(P,q)
        assert actual == predicted, (q,n,P,actual,predicted)
        if actual:
            total+=1
            B=tuple(tuple(row[1:]) for row in P[1:])
            v=tuple(row[0] for row in P[1:])
            r=mat_rank(B,q)
            order=3 if any(matvec(B,v,q)) else (1 if not any(any(row) for row in P) else 2)
            hist[(r,order)]=hist.get((r,order),0)+1
    expect={}
    for r in range(n//2+1):
        R=rankcount(n,r,q)
        ker=q**(n-r)
        expect[(r,2)]=R*(ker- (1 if r==0 else 0)) if q%2 == 0 else R*ker-(1 if r==0 else 0)
        # For r=0, P=0 is recorded separately; for r>0 all P are nonzero.
        if q%2==0:
            expect[(r,3)]=R*(q**n-ker)
    expect[(0,1)]=1
    expect={k:v for k,v in expect.items() if v}
    assert hist==expect,(q,n,hist,expect)
    print('EXHAUSTIVE_OK', 'field=',q,'radical_dimension=',n,'operators=',total,'rank_index=',sorted(hist.items()))


def test_gf4_n2():
    q=4;n=2
    hist={}
    basis=tuple(tuple(int(i==j) for i in range(3)) for j in range(3))
    for b in product(range(q),repeat=n*n):
        B=tuple(tuple(b[i*n:(i+1)*n]) for i in range(n))
        if not squarezero(B,q):
            continue
        for v in product(range(q),repeat=n):
            P=((0,0,0),)+tuple((v[i],)+B[i] for i in range(n))
            assert rb_direct(P,q)
            idx=3 if any(matvec(B,v,q)) else (1 if not any(any(row) for row in P) else 2)
            hist[idx]=hist.get(idx,0)+1
    assert hist=={1:1,2:75,3:180},hist
    print('GF4_OK', 'radical_dimension=2', 'nilpotency_hist=',hist)

if __name__=='__main__':
    for q,n in [(2,1),(2,2),(2,3),(3,1),(3,2)]:
        test_exhaustive(q,n)
    test_gf4_n2()
    print('VERIFY_OK')

# Direct conjugacy tests are defined separately so that the base-field exhaustive
# Rota--Baxter checks do not depend on the orbit classification.
def matmul(A,B,q):
    if not A:
        return ()
    bt=list(zip(*B))
    return tuple(tuple(dot(row,col,q) for col in bt) for row in A)


def inverse(A,q):
    n=len(A)
    aug=[list(A[i])+[int(j==i) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if aug[i][j]),None)
        if pivot is None:return None
        aug[pivot],aug[j]=aug[j],aug[pivot]
        s=next(x for x in range(1,q) if mul(aug[j][j],x,q)==1)
        aug[j]=[mul(s,x,q) for x in aug[j]]
        for i in range(n):
            if i != j:
                t=aug[i][j]
                aug[i]=[add(x,mul(t,y,q),q) if q%2==0 else (x-mul(t,y,q))%q for x,y in zip(aug[i],aug[j])]
    return tuple(tuple(row[n:]) for row in aug)


def orbit_tests(q,n):
    matrices=[]
    for flat in product(range(q),repeat=n*n):
        M=tuple(tuple(flat[i*n:(i+1)*n]) for i in range(n))
        inv=inverse(M,q)
        if inv is not None:matrices.append((M,inv))
    zero=tuple(0 for i in range(n))
    actual={}
    for flat in product(range(q),repeat=n*n):
        B=tuple(tuple(flat[i*n:(i+1)*n]) for i in range(n))
        if not squarezero(B,q):continue
        r=mat_rank(B,q)
        for v in product(range(q),repeat=n):
            if q%2 and any(matvec(B,v,q)):continue
            if not any(v):kind='zero'
            elif any(matvec(B,v,q)):kind='outside_kernel'
            else:
                aug = tuple(tuple(list(B[i])+[v[i]]) for i in range(n))
                kind='image_nonzero' if mat_rank(aug,q)==r else 'kernel_not_image'
            key=(r,kind)
            actual.setdefault(key,set()).add((B,v))
    for key, members in actual.items():
        B,v=next(iter(members))
        images=set()
        for G,Gi in matrices:
            images.add((matmul(matmul(G,B,q),Gi,q),matvec(G,v,q)))
        assert images==members, (q,n,key,len(images),len(members))
    expected=2+4*(n//2)-(1 if n%2==0 else 0) if q%2==0 else 2+3*(n//2)-(1 if n%2==0 else 0)
    assert len(actual)==expected,(q,n,len(actual),expected)
    print('ORBITS_OK', 'field=',q,'radical_dimension=',n,'orbit_count=',len(actual),
          'sizes=',[(str(k),len(v)) for k,v in sorted(actual.items())])

if __name__=='__main__':
    for q,n in [(2,2),(2,3),(3,2)]:
        orbit_tests(q,n)
    print('FULL_VERIFY_OK')
