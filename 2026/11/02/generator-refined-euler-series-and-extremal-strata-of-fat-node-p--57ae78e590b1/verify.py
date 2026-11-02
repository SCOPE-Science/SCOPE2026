"""Independent finite checks of generator-refined Euler series on x^u y^v=0.
Uses only the Python standard library. It does not certify infinite identities.
"""
from collections import defaultdict

LIMIT = 38

def add(A,B):
    C=defaultdict(int,A)
    for t,v in B.items(): C[t]+=v
    return {t:v for t,v in C.items() if v}

def scale_shift(A, dq=0, da=0, coeff=1):
    return {(i+dq,j+da):coeff*v for (i,j),v in A.items() if i+dq<=LIMIT and v}

def mul(A,B):
    C=defaultdict(int)
    for (i,j),a in A.items():
        for (k,l),b in B.items():
            if i+k<=LIMIT:C[i+k,j+l]+=a*b
    return {t:v for t,v in C.items() if v}

def numerator(A,degree):
    return add(add(A,scale_shift(A,degree,0,-1)),scale_shift(A,degree,1,1))

def reciprocal(A,degree):
    out={}
    for k in range(LIMIT//degree+1):out=add(out,scale_shift(A,k*degree))
    return out

def B(u):
    r={(0,0):1}
    for j in range(1,u+1):r=reciprocal(numerator(r,j),j)
    return r

def T(u,k):
    r={(0,0):1}
    for j in range(k):r=numerator(r,j)
    for j in range(1,k+1):r=reciprocal(r,j)
    return scale_shift(r,(u+1)*k)

def theoretical(u,v):
    b=B(u); before=B(u-1)
    total={}
    for k in range(v+1):total=add(total,T(u,k))
    main=scale_shift(mul(b,total),da=1)
    boundary=mul(add(b,scale_shift(before,coeff=-1)),T(u,v))
    correction=add(boundary,scale_shift(boundary,da=1,coeff=-1))
    return add(main,correction)

def partitions(n,maximum=None):
    if n==0:
        yield ()
    else:
        for m in range(min(n,maximum or n),0,-1):
            for p in partitions(n-m,m):yield (m,)+p

def direct(u,v):
    r=defaultdict(int)
    for n in range(LIMIT+1):
        for p in partitions(n):
            if len(p)>v and p[v]>u:continue
            distinct=len(set(p))
            ambient=distinct+1
            special=(len(p)>=v+1 and p[v]==u and p[v-1]>u)
            generators=ambient-int(special)
            r[n,generators]+=1
    return dict(r)

def extremal(u,v):
    r={(u+v)*(u+v-1)//2:1}
    for j in list(range(1,u+1))+list(range(1,v+1)):
        ans=defaultdict(int)
        for n,c in r.items():
            for k in range((LIMIT-n)//j+1):ans[n+k*j]+=c
        r=dict(ans)
    return r

if __name__=='__main__':
    instances=0; coefficients=0
    for u in range(1,6):
        for v in range(1,7):
            f=theoretical(u,v); e=direct(u,v)
            assert f==e,(u,v,[(key,f.get(key,0),e.get(key,0)) for key in set(f)|set(e) if f.get(key,0)!=e.get(key,0)][:10])
            ex=extremal(u,v)
            actual={n:count for (n,g),count in f.items() if g==u+v}
            assert actual==ex,(u,v,actual,ex)
            assert f==theoretical(v,u),(u,v,'symmetry')
            instances+=1;coefficients+=len(f)
    u,v=3,6
    f=theoretical(u,v)
    print('VERIFY_OK:', instances, 'parameter pairs;',coefficients,'nonzero generator-graded coefficients')
    print('u=3,v=6, maximal generator m=9, first coefficients:',
          sorted((n,c) for (n,g),c in f.items() if g==9)[:8])
    print('u=3,v=6 n=12 generator distribution:',
          sorted((g,c) for (n,g),c in f.items() if n==12))
