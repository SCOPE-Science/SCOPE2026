#!/usr/bin/env python3
from math import isqrt

def factorint(n):
    f={}
    d=2
    while d*d<=n:
        while n%d==0:
            f[d]=f.get(d,0)+1
            n//=d
        d=3 if d==2 else d+2
    if n>1:
        f[n]=f.get(n,0)+1
    return f

def sigma_from_factor(f):
    s=1
    for p,e in f.items():
        s*=sum(p**j for j in range(e+1))
    return s

def is_prime(n):
    if n<2: return False
    if n%2==0: return n==2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True

def nearperfect_omega2(N):
    f=factorint(N)
    if len(f)!=2:
        return False,None
    sig=sigma_from_factor(f)
    d=sig-2*N
    return (0<d<N and N%d==0), d

def predicted(g,n,a):
    if n!=2 or g%2:
        return False
    # Family A.
    for p in range(2,20):
        M=2**p-1
        if is_prime(M) and g==M*M-1 and a==2**(p-1):
            return True
    # Family C.
    q=g+1
    if not is_prime(q) or q%2==0:
        return False
    for t in range(2,30):
        for k in range(0,t):
            if q==2**t-2**k-1 and a==2**(t-1) and 2**(t-1)>2**k+2:
                return True
    return False

def main():
    # Direct family checks beyond the small published base range.
    family_a=[]
    for p in (2,3,5,7):
        M=2**p-1
        if is_prime(M):
            g=M*M-1
            a=2**(p-1)
            N=a*(g+1)
            ok,d=nearperfect_omega2(N)
            assert ok and d==M and a<g
            family_a.append((g,a,N,d))

    family_c=[]
    for t,k in ((4,2),(4,1),(5,3),(5,1),(7,4)):
        q=2**t-2**k-1
        if is_prime(q) and 2**(t-1)>2**k+2:
            g=q-1
            a=2**(t-1)
            N=a*(g+1)
            ok,d=nearperfect_omega2(N)
            assert ok and d==2**k and a<g
            family_c.append((g,a,N,d))

    found=[]
    for g in range(2,31,2):
        for n in range(2,6):
            U=(g**n-1)//(g-1)
            for a in range(1,g):
                N=a*U
                ok,d=nearperfect_omega2(N)
                if ok:
                    found.append((g,n,a,N,d))
                    assert predicted(g,n,a), (g,n,a,N,d)

    expected=[
        (8,2,2,18,3),
        (10,2,8,88,4),
        (12,2,8,104,2),
        (22,2,16,368,8),
        (28,2,16,464,2),
    ]
    assert found==expected, found
    assert all(n==2 for _,n,_,_,_ in found)

    print('VERIFY_OK')
    print('even_base_max=30')
    print('digit_length_max=5')
    print('exhaustive_matches=' + str(len(found)))
    for row in found:
        print('match=' + ','.join(map(str,row)))
    print('family_a_samples=' + str(len(family_a)))
    print('family_c_samples=' + str(len(family_c)))

if __name__=='__main__':
    main()
