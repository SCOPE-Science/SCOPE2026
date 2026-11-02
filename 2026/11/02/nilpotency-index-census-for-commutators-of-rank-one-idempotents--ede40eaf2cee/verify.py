"""Direct exhaustive rank-one-idempotent commutator classification checks.
Run: python3 idempotent_commutator_check.py
Finite fields include F4 represented by t^2+t+1.
"""
from collections import Counter
from itertools import product

def mul(a,b,q):
    if q!=4:return a*b%q
    z=0
    for k in range(2):
        for j in range(2):
            if (a>>k)&1 and (b>>j)&1:z^=(1<<(k+j))
    if z&8:z^=0b1100
    if z&4:z^=0b111
    return z

def add(a,b,q):return a^b if q==4 else (a+b)%q

def neg(a,q):return a if q==4 else (-a)%q

def mm(a,b,n,q):
    return tuple(add_all((mul(a[i*n+k],b[k*n+j],q) for k in range(n)),q) for i in range(n) for j in range(n))

def add_all(xs,q):
    x=0
    for y in xs:x=add(x,y,q)
    return x

def projectors(n,q):
    P=set()
    for u in product(range(q),repeat=n):
        if not any(u):continue
        for v in product(range(q),repeat=n):
            if add_all((mul(u[i],v[i],q) for i in range(n)),q)!=1:continue
            P.add(tuple(mul(u[i],v[j],q) for i in range(n) for j in range(n)))
    return tuple(sorted(P))

def expected(n,q):
    m=n-1
    H=(q**m-1)*q**(m-1)
    J=H//(q-1)
    return (1+J,2*H+2*q**m-2,(q**m-1)*(q**(m-1)-1),(q-2)*H)

def run():
    tests=[(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2)]
    for n,q in tests:
        ps=projectors(n,q)
        assert len(ps)==((q**n-1)//(q-1))*q**(n-1),(n,q,len(ps))
        Z=(0,)*(n*n)
        cnt=Counter()
        for P in ps:
            for Q in ps:
                PQ=mm(P,Q,n,q);QP=mm(Q,P,n,q)
                C=tuple(add(a,neg(b,q),q) for a,b in zip(PQ,QP))
                if C==Z:cls=0
                else:
                    C2=mm(C,C,n,q)
                    if C2==Z:cls=1
                    elif mm(C2,C,n,q)==Z:cls=2
                    else:cls=3
                cnt[cls]+=1
        got=tuple(cnt[i] for i in range(4))
        want=tuple(len(ps)*x for x in expected(n,q))
        assert got==want,(n,q,got,want)
        print('PASS',n,q,len(ps),got)
    print('RANK_ONE_IDEMPOTENT_COMMUTATOR_OK',len(tests),'exhaustive pair enumerations')

if __name__=='__main__':run()
