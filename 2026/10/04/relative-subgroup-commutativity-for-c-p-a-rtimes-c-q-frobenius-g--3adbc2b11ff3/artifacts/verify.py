from fractions import Fraction

def find_lambda(p,a,q):
    m=p**a
    for lam in range(2,m):
        if pow(lam,q,m)==1 and all(pow(lam,d,m)!=1 for d in range(1,q)) and (lam-1)%p:
            return lam
    raise AssertionError("no action")

def check(p,a,q,exhaustive=False):
    m=p**a
    lam=find_lambda(p,a,q)
    elems=[(u,j) for u in range(m) for j in range(q)]
    pw=[pow(lam,j,m) for j in range(q)]
    e=(0,0)

    def mul(g,h):
        u,j=g; v,k=h
        return ((u+pw[j]*v)%m,(j+k)%q)

    def inv(g):
        u,j=g
        return ((-pow(pw[j],-1,m)*u)%m,(-j)%q)

    def gen(gens):
        H={e}
        H.update(gens)
        changed=True
        while changed:
            changed=False
            cur=list(H)
            for x in cur:
                if inv(x) not in H:
                    H.add(inv(x)); changed=True
            cur=list(H)
            for x in cur:
                for y in cur:
                    z=mul(x,y)
                    if z not in H:
                        H.add(z); changed=True
        return frozenset(H)

    Ps=[]
    for i in range(a+1):
        step=p**(a-i)
        Ps.append(frozenset((u,0) for u in range(0,m,step)))

    Hs=[]
    types=[]
    for i in range(a+1):
        for t in range(p**(a-i)):
            H=gen(list(Ps[i])+[(t,1)])
            Hs.append(H)
            types.append((i,t))

    subs=list(dict.fromkeys(Ps+Hs))
    S=lambda i:(p**(i+1)-1)//(p-1)
    L=a+1+S(a)
    assert len(subs)==L

    for H in subs:
        assert e in H
        for x in H:
            assert inv(x) in H
            for y in H:
                assert mul(x,y) in H

    if exhaustive:
        known=set(subs)
        for x in elems:
            assert gen([x]) in known
        for x in elems:
            for y in elems:
                assert gen([x,y]) in known

    def setprod(A,B):
        return frozenset(mul(x,y) for x in A for y in B)

    perm={}
    for A in subs:
        for B in subs:
            perm[(A,B)]=(setprod(A,B)==setprod(B,A))

    def formula(i):
        li=i+1+S(i)
        num=(i+1)*L
        for j in range(i+1):
            num += p**(i-j)*(2*a-j+1+S(j))
        return Fraction(num,li*L)

    for P in Ps:
        LH=[K for K in subs if K.issubset(P)]
        got=Fraction(sum(perm[(K,J)] for K in LH for J in subs),len(LH)*L)
        assert got==1

    for H,(j,t) in zip(Hs,types):
        partners=sum(perm[(H,J)] for J in subs)
        assert partners==2*a-j+1+S(j)
        LH=[K for K in subs if K.issubset(H)]
        got=Fraction(sum(perm[(K,J)] for K in LH for J in subs),len(LH)*L)
        assert got==formula(j)

for case in [
    (3,2,2,True),
    (3,3,2,False),
    (5,2,2,False),
    (7,2,3,False),
]:
    check(*case)

print("VERIFY_OK")
