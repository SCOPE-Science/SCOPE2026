from collections import Counter
from math import gcd

def phi(n):
    out=n
    x=n
    p=2
    while p*p<=x:
        if x%p==0:
            while x%p==0:
                x//=p
            out-=out//p
        p+=1
    if x>1:
        out-=out//x
    return out

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def order_in_cyclic(N, j):
    return 1 if j%N==0 else N//gcd(N,j)

def direct_table(p,n):
    M=p**(n-1)*(p-1)
    Gorder=p**n*M
    C=Counter()

    # Linear quotient characters.
    for j in range(M):
        d=order_in_cyclic(M,j)
        C[d]+=1

    # Nonlinear monomial parameters.
    degree_sq=M  # M linear characters, degree one.
    for k in range(1,n+1):
        root_order=p**(n-k)
        deg=phi(p**k)
        for j in range(root_order):
            omega_order=order_in_cyclic(root_order,j)
            s=0
            z=omega_order
            while z>1:
                assert z%p==0
                z//=p
                s+=1
            ker=p**(2*(n-k)-s)
            cod=Gorder//(ker*deg)
            assert cod==p**(k+s)
            C[cod]+=1
            degree_sq+=deg*deg

    assert degree_sq==Gorder
    return dict(sorted(C.items()))

def formula_table(p,n):
    C=Counter({1:1})
    for t in range(1,n):
        C[p**t]=p**t
    C[p**n]=p**(n-1)
    for e in divisors(p-1):
        if e==1:
            continue
        for s in range(n):
            C[e*p**s]=phi(e)*phi(p**s)
    return dict(sorted(C.items()))

for p in (3,5,7,11):
    for n in range(2,6):
        A=direct_table(p,n)
        B=formula_table(p,n)
        assert A==B,(p,n,A,B)
        top=max(A)
        mult=A[top]
        rp=top//mult
        assert rp==p
        z=top
        rn=0
        while z%p==0:
            z//=p
            rn+=1
        assert z==1 and rn==n
        print({"p":p,"n":n,"top":top,"top_multiplicity":mult,"characters":sum(A.values())})

assert direct_table(3,2)=={1:1,2:1,3:3,6:2,9:3}
print("VERIFY_OK")
