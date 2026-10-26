#!/usr/bin/env python3
"""Independent finite examples of polynomial-coefficient reachability and equation ranks.
Run: python3 verify.py. Only Python standard library is required.
The general theorem is proved separately; this program checks sample instances.
"""
from itertools import product

def add(a,b,p):
    return tuple((x+y)%p for x,y in zip(a,b))
def sub(a,b,p):
    return tuple((x-y)%p for x,y in zip(a,b))
def mul(a,b,p,n):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%p
                 for i in range(n) for j in range(n))
def scalar(a,c,p):
    return tuple(c*x%p for x in a)
def ident(n):
    return tuple(int(i==j) for i in range(n) for j in range(n))
def rank(rows,p):
    a=[list(r) for r in rows]; piv=0
    if not a: return 0
    nc=len(a[0])
    for col in range(nc):
        ind=next((i for i in range(piv,len(a)) if a[i][col]%p),None)
        if ind is None:continue
        a[piv],a[ind]=a[ind],a[piv]
        t=pow(a[piv][col],-1,p)
        a[piv]=[(v*t)%p for v in a[piv]]
        for i in range(len(a)):
            if i!=piv and a[i][col]:
                t=a[i][col]
                a[i]=[(v-t*w)%p for v,w in zip(a[i],a[piv])]
        piv+=1
        if piv==len(a):break
    return piv

def mat_rank(m,p,n):
    return rank([m[i*n:(i+1)*n] for i in range(n)],p)

def check(label,p,n,T,expected):
    I=ident(n); Z=(0,)*(n*n); J=sub(I,T,p)
    assert mat_rank(T,p,n)==n and mat_rank(J,p,n)==n, label
    # The ring F_p[T] computed independently as all polynomial evaluations.
    powers=[I]
    for _ in range(1,n): powers.append(mul(powers[-1],T,p,n))
    ring={Z}
    for coeff in product(range(p),repeat=n):
        r=Z
        for c,power in zip(coeff,powers):r=add(r,scalar(power,c,p),p)
        ring.add(r)
    # Every coefficient from a term t(x,y) is obtained recursively via f*g=T f+(I-T)g.
    term={Z,I}
    while True:
        nxt=set(term)
        for a in term:
            for b in term:
                nxt.add(add(mul(T,a,p,n),mul(J,b,p,n),p))
        assert nxt<=ring
        if len(nxt)==len(term): break
        term=nxt
    assert term==ring,(label,len(term),len(ring))
    ranks={mat_rank(M,p,n) for M in term}
    assert ranks==set(expected),(label,ranks,expected)
    # Every matrix-coefficient term equation t_f(x,y)=y has p^{-rank f} probability.
    # Count directly for small A, not solely by a rank formula.
    if p**n<=25:
        vectors=list(product(range(p),repeat=n))
        for M in term:
            z=0
            for v in vectors:
                if all(sum(M[i*n+j]*v[j] for j in range(n))%p==0 for i in range(n)):
                    z+=1
            assert z*p**mat_rank(M,p,n)==p**n,label
    print(f'OK {label}: |F_p[T]|={len(ring)}, rank set={sorted(ranks)}, spectrum={[f"1/{p**r}" for r in sorted(ranks) if r]+(["1"] if 0 in ranks else [])}')

if __name__=='__main__':
    check('scalar 2 in F3',3,1,(2,),{0,1})
    check('scalar 2 on F3^2',3,2,(2,0,0,2),{0,2})
    check('distinct eigenvalues 2,3 on F5^2',5,2,(2,0,0,3),{0,1,2})
    check('nontrivial Jordan block at 2 on F3^2',3,2,(2,1,0,2),{0,1,2})
    check('irreducible x^2+x+1 on F2^2',2,2,(0,1,1,1),{0,2})
    check('irreducible x^3+x+1 on F2^3',2,3,(0,0,1,1,0,1,0,1,0),{0,3})
    check('scalar 2 on F3^3',3,3,(2,0,0,0,2,0,0,0,2),{0,3})
    check('split repeated 2,2 and 3 on F5^3',5,3,(2,0,0,0,2,0,0,0,3),{0,1,2,3})
    print('VERIFY_OK cases=8')
