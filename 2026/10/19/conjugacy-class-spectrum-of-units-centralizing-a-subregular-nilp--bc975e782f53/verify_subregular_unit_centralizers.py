"""Exact finite-field checks for centralizers of units of End(k[t]/t^m + k).
These are direct finite computations; the proof in RESULT.md applies to every field.
"""
from itertools import product


def add(a, b, q):
    return (a ^ b) if q == 4 else (a + b) % q


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    x = 0
    while b:
        if b & 1:
            x ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7  # x^2+x+1
    return x


def neg(a, q):
    return a if q == 4 else (-a) % q


def sub(a, b, q):
    return add(a, neg(b,q), q)


def mat(a, q):
    f,u,v,s = a
    m=len(f)
    d=m+1
    A=[[0]*d for _ in range(d)]
    for j in range(m):
        for i in range(m-j):
            A[i+j][j]=f[i]
    A[m-1][m]=u
    A[m][0]=v
    A[m][m]=s
    return A


def mmul(A,B,q):
    n=len(A)
    return [[sumprod(A[i][k],B[k][j],q,n) for j in range(n)] for i in range(n)]


def sumprod(a,b,q,n):
    x=0
    for i in range(n):
        x=add(x,mul(a[i],b[i],q),q)
    return x


def commute_explicit(a,b,q):
    A,B=mat(a,q),mat(b,q)
    n=len(A)
    for i in range(n):
        for j in range(n):
            x=0; y=0
            for t in range(n):
                x=add(x,mul(A[i][t],B[t][j],q),q)
                y=add(y,mul(B[i][t],A[t][j],q),q)
            if x!=y:
                return False
    return True


def commute_coords(a,b,q):
    f,u,v,s=a
    g,U,V,t=b
    x=sub(f[0],s,q)
    y=sub(g[0],t,q)
    w=sub(mul(u,V,q),mul(U,v,q),q)
    h=sub(mul(x,U,q),mul(y,u,q),q)
    z=sub(mul(v,y,q),mul(V,x,q),q)
    return not (w or h or z)


def units(q,m):
    nonzero=range(1,q)
    return [((a,)+tail, u,v,s) for a in nonzero for tail in product(range(q),repeat=m-1)
                for u in range(q) for v in range(q) for s in nonzero]


def category(a,q):
    f,u,v,s=a
    x=sub(f[0],s,q)
    if x: return 2
    if u or v: return 1
    return 0


def test(q,m,full_matrix=False):
    U=units(q,m)
    assert len(U)==(q-1)**2*q**(m+1)
    predicted_counts=[(q-1)*q**(m-1),
                      (q-1)*q**(m-1)*(q*q-1),
                      (q-1)*(q-2)*q**(m+1)]
    observed=[0,0,0]
    samples=[None,None,None]
    for a in U:
        r=category(a,q)
        observed[r]+=1
        if samples[r] is None:
            samples[r]=a
    assert observed==predicted_counts,(q,m,observed,predicted_counts)
    predicted_cent=[len(U),q**m*(q-1),q**(m-1)*(q-1)**2]
    for a in U:
        r=category(a,q)
        count=sum(commute_coords(a,b,q) for b in U)
        if count != predicted_cent[r]:
            raise AssertionError((q,m,a,r,count,predicted_cent[r]))
        if full_matrix:
            for b in U:
                assert commute_coords(a,b,q)==commute_explicit(a,b,q),(q,m,a,b)
    total=sum(a*b for a,b in zip(observed,predicted_cent))
    classes=sum((observed[r]*predicted_cent[r])//len(U) for r in range(3))
    assert total* q**3*(q-1)==len(U)**2*(q*q+1)
    assert classes==(q-1)*(q*q+1)*q**(m-2)
    print('PASS',q,m,'units',len(U),'types',observed,
          'centralizers',predicted_cent,'classes',classes,
          'commuting_pairs',total,'explicit_matrices',full_matrix)


if __name__=='__main__':
    for q,m,full in [(2,2,True),(2,3,True),(2,4,False),(2,5,False),
                     (3,2,True),(3,3,False),(4,2,False)]:
        test(q,m,full)
    print('VERIFY_OK_SUBREGULAR_UNIT_CENTRALIZERS')
