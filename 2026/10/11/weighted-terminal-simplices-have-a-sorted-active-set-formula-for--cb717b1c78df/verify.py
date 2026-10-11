#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product

def solve_linear(A,b):
    n=len(A)
    M=[list(map(Fraction,A[i]))+[Fraction(b[i])] for i in range(n)]
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c] != 0),None)
        if p is None:
            return None
        M[c],M[p]=M[p],M[c]
        q=M[c][c]
        M[c]=[x/q for x in M[c]]
        for r in range(n):
            if r==c: continue
            q=M[r][c]
            if q:
                M[r]=[M[r][j]-q*M[c][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def norm2(x):
    return dot(x,x)

def sub(x,y):
    return tuple(a-b for a,b in zip(x,y))

def formula(a,bs):
    a=Fraction(a)
    sb=sorted(Fraction(x) for x in bs)
    d=len(sb)

    # Minimum ball of the base vertices.
    base=None
    for p in range(2,d+1):
        m=d-p
        S2=sum(1/(sb[i]*sb[i]) for i in range(m,d))
        mu=Fraction(p-2,1)/S2
        lower_ok=(m==0 or sb[m-1]*sb[m-1] <= mu)
        upper_ok=(mu < sb[m]*sb[m])
        if lower_ok and upper_ok:
            c=[Fraction(0) for _ in range(d)]
            for i in range(m,d):
                c[i]=(sb[i]*sb[i]-mu)/(2*sb[i])
            kappa=2*a*sum(c)+d*a*a
            base=(p,m,mu,c,kappa)
            break
    assert base is not None
    p,m,mu,c,kappa=base
    if kappa <= mu:
        return tuple(c), norm2(c)+mu, ("base",p)

    # Apex-active branch.
    found=[]
    for p in range(1,d+1):
        m=d-p
        S1=sum(1/sb[i] for i in range(m,d))
        S2=sum(1/(sb[i]*sb[i]) for i in range(m,d))
        B1=sum(sb[i] for i in range(m,d))
        A=1+a*S1
        D=A*A+a*a*(d-p)*S2
        K=(A*(a*B1+d*a*a)-a*a*(d-p)*(2-p))/D
        t=(Fraction(2-p,1)+S2*K)/(2*A)
        if t <= 0:
            continue
        lower_ok=(m==0 or sb[m-1]*sb[m-1]+2*a*t*sb[m-1] <= K)
        upper_ok=(K < sb[m]*sb[m]+2*a*t*sb[m])
        if lower_ok and upper_ok:
            c=[-a*t for _ in range(d)]
            for i in range(m,d):
                c[i]=(sb[i]*sb[i]-K)/(2*sb[i])
            found.append((tuple(c),norm2(c)+K,("apex",p)))
    assert len(found)==1, found
    return found[0]

def generic_meb(a,bs):
    a=Fraction(a)
    bs=[Fraction(x) for x in bs]
    d=len(bs)
    V=[tuple(-a for _ in range(d))]
    for i,b in enumerate(bs):
        v=[Fraction(0) for _ in range(d)]
        v[i]=b
        V.append(tuple(v))

    certs=[]
    for k in range(2,d+2):
        for C in combinations(range(d+1),k):
            # Unknown barycentric weights alpha on C.
            # sum alpha=1 plus equal-distance equations to C[0].
            A=[[Fraction(1) for _ in range(k)]]
            rhs=[Fraction(1)]
            v0=V[C[0]]
            for idx in range(1,k):
                vj=V[C[idx]]
                row=[]
                for h in range(k):
                    vh=V[C[h]]
                    row.append(2*dot(sub(vj,v0),vh))
                A.append(row)
                rhs.append(norm2(vj)-norm2(v0))
            alpha=solve_linear(A,rhs)
            if alpha is None or any(x < 0 for x in alpha):
                continue
            c=tuple(sum(alpha[h]*V[C[h]][j] for h in range(k)) for j in range(d))
            R2=norm2(sub(V[C[0]],c))
            if all(norm2(sub(v,c)) <= R2 for v in V):
                certs.append((R2,c,C,alpha))
    assert certs
    best=min(x[0] for x in certs)
    winners=[x for x in certs if x[0]==best]
    centers={x[1] for x in winners}
    assert len(centers)==1
    return next(iter(centers)),best

cases=0
weight_sets=[
    (1,1),
    (1,2),
    (1,3),
    (2,3),
    (1,1,1),
    (1,2,4),
    (1,3,7),
    (2,5,6),
    (1,1,2,5),
    (1,2,3,8),
    (2,3,7,9),
    (1,1,1,2,6),
    (1,2,4,8,16),
    (2,3,5,7,11),
    (1,1,2,3,5,8),
    (1,2,3,5,8,13),
    (1,1,2,3,5,8,13),
    (1,2,4,7,11,16,22),
]
for bs0 in weight_sets:
    d=len(bs0)
    if d<2 or d>7:
        continue
    for a in (1,2,5,11):
        c1,r1,mode=formula(a,bs0)
        c2,r2=generic_meb(a,sorted(bs0))
        assert r1==r2,(a,bs0,r1,r2,mode)
        assert c1==c2,(a,bs0,c1,c2,mode)
        cases+=1

# Standard terminal closed form.
for d in range(2,8):
    c,r2,mode=formula(1,[1]*d)
    q=Fraction(1-d,2*(d+1))
    want=Fraction(d*(d+3)*(d+3),4*(d+1)*(d+1))
    assert all(x==q for x in c)
    assert r2==want
    assert mode==("apex",d)

print(f"VERIFY_OK weighted-terminal-MEB cases={cases} d=2..7 generic_contact_enumeration=yes")
