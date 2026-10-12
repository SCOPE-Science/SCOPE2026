from itertools import product
from math import gcd

def delta(c,Q,n):
    return sum(c[i]*(2**(n-1-i)) for i in range(n)) % Q

def delta_rot(c,Q,n,r):
    return sum(c[(i+r)%n]*(2**(n-1-i)) for i in range(n)) % Q

def predicted_iso(c,b,q,n):
    Q=q-1
    d=gcd(2**n-1,Q)
    a=delta(c,Q,n)%d
    z=delta(b,Q,n)%d
    return any(a==(pow(2,r,d)*z)%d for r in range(n)) if d>1 else True

def brute_iso(c,b,q,n):
    Q=q-1
    m=2**n-1
    dc=delta(c,Q,n)
    for r in range(n):
        db=delta_rot(b,Q,n,r)
        target=(dc-db)%Q
        for lam0 in range(Q):
            if (m*lam0-target)%Q:
                continue
            lam=lam0
            for i in range(n):
                lam=(2*lam+b[(i+r)%n]-c[i])%Q
            assert lam==lam0
            return True
    return False

def predicted_class_count(q,n):
    d=gcd(2**n-1,q-1)
    return sum(gcd(d,2**r-1) for r in range(n))//n

def orbit_key(c,q,n):
    Q=q-1
    d=gcd(2**n-1,Q)
    x=delta(c,Q,n)%d
    if d==1:
        return 0
    return min((pow(2,r,d)*x)%d for r in range(n))

def brute_idempotent_count(c,q,n):
    Q=q-1
    m=2**n-1
    dc=delta(c,Q,n)
    nonzero=sum(1 for x in range(Q) if (m*x+dc)%Q==0)
    return 1+nonzero

def predicted_idempotent_count(c,q,n):
    d=gcd(2**n-1,q-1)
    return d+1 if delta(c,q-1,n)%d==0 else 1

def brute_aut_count(c,q,n):
    Q=q-1
    m=2**n-1
    dc=delta(c,Q,n)
    total=0
    for r in range(n):
        dr=delta_rot(c,Q,n,r)
        target=(dc-dr)%Q
        for lam0 in range(Q):
            if (m*lam0-target)%Q==0:
                lam=lam0
                for i in range(n):
                    lam=(2*lam+c[(i+r)%n]-c[i])%Q
                assert lam==lam0
                total+=1
    return total

def predicted_aut_count(c,q,n):
    d=gcd(2**n-1,q-1)
    x=delta(c,q-1,n)%d
    if d==1:
        stab=n
    else:
        stab=sum(1 for r in range(n) if ((pow(2,r,d)-1)*x)%d==0)
    return d*stab

# Pairwise exhaustive isomorphism checks on complete coefficient spaces.
for q,n in ((4,3),(7,2),(8,3),(5,4)):
    Q=q-1
    coeffs=list(product(range(Q),repeat=n))
    for c in coeffs:
        for b in coeffs:
            assert brute_iso(c,b,q,n)==predicted_iso(c,b,q,n)
    print({"pairwise_iso_verified":(q,n),"coefficient_tuples":len(coeffs)})

# Full coefficient-space checks of classes, idempotents, and automorphisms.
for q,n in ((7,2),(8,3),(16,4),(9,3)):
    Q=q-1
    coeffs=list(product(range(Q),repeat=n))
    classes=set()
    for c in coeffs:
        classes.add(orbit_key(c,q,n))
        assert brute_idempotent_count(c,q,n)==predicted_idempotent_count(c,q,n)
        assert brute_aut_count(c,q,n)==predicted_aut_count(c,q,n)
    assert len(classes)==predicted_class_count(q,n)
    print({
        "q":q,
        "n":n,
        "d":gcd(2**n-1,q-1),
        "class_count":len(classes),
    })

assert predicted_class_count(7,2)==2
assert predicted_class_count(8,3)==3
assert predicted_class_count(16,4)==5

# The q=16,n=4 quotient C15 has these exact doubling orbits and stabilizer orders.
d=15
unseen=set(range(d))
orbits=[]
while unseen:
    x=min(unseen)
    orb={pow(2,r,d)*x%d for r in range(4)}
    orbits.append(sorted(orb))
    unseen-=orb
assert orbits==[
    [0],
    [1,2,4,8],
    [3,6,9,12],
    [5,10],
    [7,11,13,14],
]
orders=[d*(4//len(o)) for o in orbits]
assert orders==[60,15,15,30,15]

print("VERIFY_OK")
