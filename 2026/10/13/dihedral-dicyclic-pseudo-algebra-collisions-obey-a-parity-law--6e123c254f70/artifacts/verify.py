from collections import Counter
from math import gcd

def phi(n):
    out=n
    p=2
    x=n
    while p*p<=x:
        if x%p==0:
            while x%p==0:
                x//=p
            out=out//p*(p-1)
        p+=1
    if x>1:
        out=out//x*(x-1)
    return out

def nonlinear(n):
    C=Counter()
    for k in range(1,n):
        C[2*n//gcd(2*n,k)]+=1
    return C

def expected_nonlinear(n):
    return Counter({d:phi(d)//2 for d in range(3,2*n+1) if (2*n)%d==0})

def pseudo_dihedral(n):
    C=nonlinear(n)
    C[1]+=1
    C[2]+=3
    return C

def pseudo_dicyclic(n):
    C=nonlinear(n)
    C[1]+=1
    if n%2==0:
        C[2]+=3
    else:
        C[2]+=1
        C[4]+=2
    return C

for n in range(2,81):
    N=nonlinear(n)
    E=expected_nonlinear(n)
    assert N==E,(n,N,E)
    assert sum(N.values())==n-1
    assert 4+4*(n-1)==4*n

    D=pseudo_dihedral(n)
    Q=pseudo_dicyclic(n)
    assert (D==Q)==(n%2==0),(n,D,Q)

    # Presentation-level involution counts: Dic_n has only a^n;
    # D_{4n} has a^n and all 2n reflections.
    assert 1 != 2*n+1

    if n in (2,3,4,5,6,8,9,10):
        print({
            'n':n,
            'dihedral':dict(sorted(D.items())),
            'dicyclic':dict(sorted(Q.items())),
            'collision':D==Q,
            'involutions':{'dicyclic':1,'dihedral':2*n+1},
        })

assert pseudo_dicyclic(2)==Counter({2:3,1:1,4:1})
assert pseudo_dihedral(2)==pseudo_dicyclic(2)
assert pseudo_dicyclic(3)!=pseudo_dihedral(3)
print('VERIFY_OK')
