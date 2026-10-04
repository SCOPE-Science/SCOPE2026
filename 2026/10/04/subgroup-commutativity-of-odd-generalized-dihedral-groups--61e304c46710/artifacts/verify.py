from collections import deque
from fractions import Fraction
from itertools import product

def add(a,b,mods):
    return tuple((x+y) % m for x,y,m in zip(a,b,mods))

def neg(a,mods):
    return tuple((-x) % m for x,m in zip(a,mods))

def elements_A(mods):
    return [tuple(x) for x in product(*[range(m) for m in mods])]

def subgroup_generated(H,x,mods):
    S=set(H)
    S.add(x)
    changed=True
    while changed:
        changed=False
        cur=list(S)
        for a in cur:
            for b in cur:
                c=add(a,b,mods)
                if c not in S:
                    S.add(c)
                    changed=True
    return frozenset(S)

def subgroups_A(mods):
    z=tuple(0 for _ in mods)
    els=elements_A(mods)
    subs={frozenset([z])}
    q=deque(subs)
    while q:
        H=q.popleft()
        for x in els:
            if x not in H:
                K=subgroup_generated(H,x,mods)
                if K not in subs:
                    subs.add(K)
                    q.append(K)
    return list(subs)

def mulG(x,y,mods):
    a,e=x
    b,f=y
    if e:
        b=neg(b,mods)
    return (add(a,b,mods),(e+f)&1)

def classified_subgroups_G(mods):
    AS=subgroups_A(mods)
    AE=elements_A(mods)
    GS=[]
    for B in AS:
        GS.append(frozenset((b,0) for b in B))
    for B in AS:
        seen=set()
        for x in AE:
            cos=frozenset(add(x,b,mods) for b in B)
            if cos in seen:
                continue
            seen.add(cos)
            GS.append(frozenset(
                [(b,0) for b in B]+[(z,1) for z in cos]
            ))
    return AS,GS

def permutes(H,K,mods):
    HK={mulG(h,k,mods) for h in H for k in K}
    KH={mulG(k,h,mods) for h in H for k in K}
    return HK==KH

def lattice_formula(mods):
    AS,GS=classified_subgroups_G(mods)
    m=len(elements_A(mods))
    ell=len(AS)
    omega=sum(m//len(B) for B in AS)
    eta=sum(
        m//len(set(B)&set(C))
        for B in AS for C in AS
    )
    predicted=ell*ell+2*ell*omega+eta
    direct=sum(
        permutes(H,K,mods)
        for H in GS for K in GS
    )
    assert len(GS)==ell+omega
    assert direct==predicted
    return Fraction(predicted,len(GS)**2)

expected={
    (3,):Fraction(5,6),
    (5,):Fraction(11,16),
    (9,):Fraction(71,128),
    (3,3):Fraction(34,49),
}
for mods,want in expected.items():
    got=lattice_formula(mods)
    assert got==want,(mods,got,want)

def gaussian(n,k,p):
    if k<0 or k>n:
        return 0
    num=den=1
    for h in range(k):
        num*=p**(n-h)-1
        den*=p**(k-h)-1
    return num//den

def elementary_stats(p,r):
    ell=sum(gaussian(r,i,p) for i in range(r+1))
    omega=sum(
        gaussian(r,i,p)*p**(r-i)
        for i in range(r+1)
    )
    eta=0
    for i in range(r+1):
        for j in range(r+1):
            for k in range(max(0,i+j-r),min(i,j)+1):
                eta += (
                    gaussian(r,i,p)
                    * gaussian(i,k,p)
                    * gaussian(r-i,j-k,p)
                    * p**((i-k)*(j-k)+r-k)
                )
    return ell,omega,eta,Fraction(
        ell*ell+2*ell*omega+eta,
        (ell+omega)**2
    )

for p in (3,5,7,11):
    ell,omega,eta,sd=elementary_stats(p,1)
    assert ell==2
    assert omega==p+1
    assert eta==3*p+1
    assert sd==Fraction(7*p+9,(p+3)**2)

ell,omega,eta,sd=elementary_stats(3,2)
assert (ell,omega,eta,sd)==(6,22,244,Fraction(34,49))

print("VERIFY_OK")
