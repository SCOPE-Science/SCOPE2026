from itertools import product
from collections import Counter

BAS=((1,0),(0,1))

def add(x,y,p):
    return ((x[0]+y[0])%p,(x[1]+y[1])%p)

def neg(x,p):
    return ((-x[0])%p,(-x[1])%p)

def mul(x,y,p):
    return ((x[0]*y[0])%p,(x[0]*y[1]+x[1]*y[0])%p)

def mv(M,x,p):
    a,b,c,d=M
    return ((a*x[0]+b*x[1])%p,(c*x[0]+d*x[1])%p)

def is_arb(M,p):
    for x in BAS:
        for y in BAS:
            Tx,Ty=mv(M,x,p),mv(M,y,p)
            lhs=mul(Tx,Ty,p)
            inner=add(mul(Tx,y,p),mul(x,Ty,p),p)
            rhs=neg(mv(M,inner,p),p)
            if lhs!=rhs:
                return False
    return True

def is_strong(M,p):
    if not is_arb(M,p): return False
    for x in BAS:
        for y in BAS:
            for z in BAS:
                lhs=mul(mul(mv(M,x,p),mv(M,y,p),p),z,p)
                rhs=mul(mul(x,mv(M,y,p),p),mv(M,z,p),p)
                if lhs!=rhs:
                    return False
    return True

def rank(M,p):
    a,b,c,d=M
    if not any(v%p for v in M): return 0
    return 2 if (a*d-b*c)%p else 1

def conj(M,u,p):
    a,b,c,d=M
    return (a,(b*pow(u,-1,p))%p,(u*c)%p,d)

def criterion(M,p):
    a,b,c,d=M
    return (
      (3*a*a+2*b*c)%p==0 and
      (2*c*(2*a+d))%p==0 and
      (b*(3*a+d))%p==0 and
      (2*a*d+2*b*c+d*d)%p==0 and
      (3*b*b)%p==0 and
      (4*b*d)%p==0
    )

for p in (2,3,5,7):
    S=[]
    for M in product(range(p),repeat=4):
        assert is_arb(M,p)==criterion(M,p)
        if is_arb(M,p): S.append(M)
    expected=2*p*p-1 if p==3 else p
    assert len(S)==expected
    if p==3:
        assert Counter(rank(M,p) for M in S)==Counter({0:1,1:p*p+p-2,2:p*(p-1)})
        assert sum(is_strong(M,p) for M in S)==p*p
        assert sum(rank(M,p)==2 for M in S)==p*(p-1)
    else:
        assert all(is_strong(M,p) for M in S)

    pool=set(S); orbits=[]
    while pool:
        M=next(iter(pool))
        O={conj(M,u,p) for u in range(1,p)}
        O &= set(S)
        orbits.append(O)
        pool-=O
    expected_orbits=4*p-1 if p==3 else 2
    assert len(orbits)==expected_orbits,(p,len(orbits))
    print({"p":p,"operators":len(S),"strong":sum(is_strong(M,p) for M in S),
           "ranks":dict(sorted(Counter(rank(M,p) for M in S).items())),
           "orbits":len(orbits)})
print("VERIFY_OK")
