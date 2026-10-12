#!/usr/bin/env python3
"""Direct finite-field census for invertible centralizer trace fibers.

Run: python3 verify.py.  No nonstandard packages are required.
"""
from itertools import product
from collections import Counter
from math import prod


def mul(x, y, q):
    if q != 4:
        return x*y % q
    z = 0
    for i in range(2):
        for j in range(2):
            if (x >> i) & (y >> j) & 1:
                z ^= 1 << (i+j)
    if z & 8: z ^= 8 ^ 4 ^ 2  # x^3=x^2+x
    if z & 4: z ^= 4 ^ 2 ^ 1  # x^2=x+1
    return z


def add(x, y, q):
    return x ^ y if q==4 else (x+y)%q


def neg(x, q):
    return x if q==4 else (-x)%q


def inv(x, q):
    assert x
    return next(y for y in range(1,q) if mul(x,y,q)==1)


def matmul(a,b,q):
    n=len(a)
    return [[sum_field((mul(a[i][k],b[k][j],q) for k in range(n)),q)
             for j in range(n)] for i in range(n)]


def sum_field(values,q):
    a=0
    for b in values: a=add(a,b,q)
    return a


def rank(rows,q):
    m=[r[:] for r in rows]
    if not m:return 0
    n=len(m[0]);t=0
    for col in range(n):
        idx=next((i for i in range(t,len(m)) if m[i][col]),None)
        if idx is None:continue
        m[t],m[idx]=m[idx],m[t]
        z=inv(m[t][col],q)
        m[t]=[mul(z,v,q) for v in m[t]]
        for i in range(len(m)):
            if i!=t and m[i][col]:
                fac=m[i][col]
                m[i]=[add(m[i][j],neg(mul(fac,m[t][j],q),q),q) for j in range(n)]
        t+=1
        if t==len(m):break
    return t


def nullspace(rows,q):
    a=[r[:] for r in rows]; n=len(a[0]); piv=[];t=0
    for col in range(n):
        k=next((i for i in range(t,len(a)) if a[i][col]),None)
        if k is None:continue
        a[t],a[k]=a[k],a[t]
        z=inv(a[t][col],q)
        a[t]=[mul(z,v,q) for v in a[t]]
        for i in range(len(a)):
            if i!=t and a[i][col]:
                fac=a[i][col]
                a[i]=[add(a[i][j],neg(mul(fac,a[t][j],q),q),q) for j in range(n)]
        piv.append(col); t+=1
        if t==len(a):break
    out=[]
    for free in [x for x in range(n) if x not in piv]:
        v=[0]*n;v[free]=1
        for k,j in enumerate(piv):v[j]=neg(a[k][free],q)
        out.append(v)
    return out


def det_nonzero(a,q):
    return rank(a,q)==len(a)


def commuting_basis(a,q):
    n=len(a); rows=[]
    for i in range(n):
        for j in range(n):
            row=[0]*(n*n)
            for k in range(n):
                row[k*n+j]=add(row[k*n+j],a[i][k],q)
                row[i*n+k]=add(row[i*n+k],neg(a[k][j],q),q)
            rows.append(row)
    return nullspace(rows,q)


def direct_sum(*blocks):
    n=sum(len(b) for b in blocks)
    out=[[0]*n for _ in range(n)]
    st=0
    for b in blocks:
        for i,row in enumerate(b):
            out[st+i][st:st+len(b)]=row[:]
        st+=len(b)
    return out


def jordan(size, eigenvalue, q):
    a=[[0]*size for _ in range(size)]
    for i in range(size):
        a[i][i]=eigenvalue
        if i+1<size:a[i][i+1]=1
    return a


def poly_mul(a,b,q):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]=add(c[i+j],mul(x,y,q),q)
    return c


def companion(poly,q):
    n=len(poly)-1
    assert poly[-1]==1
    a=[[0]*n for _ in range(n)]
    for i in range(n-1):a[i+1][i]=1
    for i in range(n):a[i][n-1]=neg(poly[i],q)
    return a


def gl_order(m,Q):
    return prod(Q**m-Q**i for i in range(m))


def predicted(q, terms):
    """Terms (label, degree, size, multiplicity), one per positive multiplicity."""
    p=2 if q==4 else q
    D=0
    for f,d,s,m in terms:
        for g,e,t,k in terms:
            if f==g:D+=d*m*k*min(s,t)
    d0=sum(d*m*m for f,d,s,m in terms)
    J=q**(D-d0)
    G=J*prod(gl_order(m,q**d) for f,d,s,m in terms)
    active=[(f,d,s,m) for f,d,s,m in terms if s%p]
    if not active:
        return [G]+[0]*(q-1),D
    B=J
    for f,d,s,m in terms:
        if s%p:B*=(-1)**m*(q**d)**(m*(m-1)//2)
        else:B*=gl_order(m,q**d)
    assert (G+(q-1)*B)%q==0 and (G-B)%q==0
    return [(G+(q-1)*B)//q]+[(G-B)//q]*(q-1),D


def check(q,name,a,terms):
    want,dim=predicted(q,terms)
    basis=commuting_basis(a,q)
    assert len(basis)==dim,(q,name,len(basis),dim)
    n=len(a);seen=[0]*q
    for scalars in product(range(q),repeat=dim):
        x=[[0]*n for _ in range(n)]
        for k,s in enumerate(scalars):
            if not s:continue
            b=basis[k]
            for i in range(n):
                for j in range(n):
                    x[i][j]=add(x[i][j],mul(s,b[i*n+j],q),q)
        if det_nonzero(x,q):
            tr=sum_field((x[i][i] for i in range(n)),q)
            seen[tr]+=1
    assert seen==want,(q,name,seen,want)
    print('OK',q,name,'dim',dim,'trace_fibers',seen)


def suite():
    for q in (2,3,4,5):
        r=0 if q==2 else 1
        for n in (1,2,3):
            if q==5 and n==3:continue
            if q==4 and n==3:continue
            if q==3 and n==3:pass
            check(q,f'scalar_n{n}',jordan(1,r,q) if n==1 else [[r if i==j else 0 for j in range(n)] for i in range(n)], [('L',1,1,n)])
            if n>=2:
                check(q,f'Jordan_n{n}',jordan(n,r,q), [('L',1,n,1)])
        check(q,'J2_plus_J1',direct_sum(jordan(2,r,q),jordan(1,r,q)), [('L',1,2,1),('L',1,1,1)])
        check(q,'distinct_eigenvalues',direct_sum(jordan(1,0,q),jordan(1,1,q)), [('L0',1,1,1),('L1',1,1,1)])
        if q>2:
            check(q,'J2_plus_other',direct_sum(jordan(2,0,q),jordan(1,1,q)), [('L0',1,2,1),('L1',1,1,1)])
        if q==2:
            qpoly=[1,1,1]
        elif q==3:
            qpoly=[1,0,1]
        elif q==4:
            qpoly=[2,1,1]
        else:
            qpoly=[2,0,1] # x^2+2 irreducible over F5
        # The choices are checked for lack of a root.
        assert all(sum_field((mul(c, pow_field(x,i,q),q) for i,c in enumerate(qpoly)),q)!=0 for x in range(q))
        check(q,'irreducible_quadratic',companion(qpoly,q), [('Q',2,1,1)])
        if q<=4:
            check(q,'quadratic_plus_linear',direct_sum(companion(qpoly,q),jordan(1,0,q)), [('Q',2,1,1),('L0',1,1,1)])
            check(q,'irreducible_quadratic_squared',companion(poly_mul(qpoly,qpoly,q),q), [('Q',2,2,1)])
        if q<=3:
            cubic=[1,1,0,1] if q==2 else [1,2,0,1]
            assert all(sum_field((mul(c,pow_field(x,i,q),q) for i,c in enumerate(cubic)),q)!=0 for x in range(q))
            check(q,'irreducible_cubic',companion(cubic,q), [('C',3,1,1)])
            check(q,'J2_J2',direct_sum(jordan(2,0,q),jordan(2,0,q)), [('L0',1,2,2)])
            check(q,'J3_J1',direct_sum(jordan(3,0,q),jordan(1,0,q)), [('L0',1,3,1),('L0',1,1,1)])
            check(q,'J2_J1_J1',direct_sum(jordan(2,0,q),jordan(1,0,q),jordan(1,0,q)), [('L0',1,2,1),('L0',1,1,2)])

def pow_field(x,i,q):
    v=1
    for _ in range(i):v=mul(v,x,q)
    return v

if __name__=='__main__':
    suite()
    print('VERIFY_OK')
