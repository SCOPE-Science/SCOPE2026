#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product

# Sparse polynomials in x,y,z: exponent triple -> Fraction.
def clean(p):
    return {m:c for m,c in p.items() if c}

def add(p,q,scale=Fraction(1)):
    r=dict(p)
    for m,c in q.items(): r[m]=r.get(m,Fraction(0))+scale*c
    return clean(r)

def mul_monom(p, exp, coeff=Fraction(1)):
    return clean({(m[0]+exp[0],m[1]+exp[1],m[2]+exp[2]):c*coeff for m,c in p.items()})

def mon(exp, coeff=1): return {tuple(exp):Fraction(coeff)}

def lead(p):
    m=max(p)  # lex on exponent triples
    return m,p[m]

def divides(a,b): return all(a[i] <= b[i] for i in range(3))

def reduce_poly(f,G):
    f=clean(dict(f)); r={}
    while f:
        m,c=lead(f); done=False
        for g in G:
            mg,cg=lead(g)
            if divides(mg,m):
                e=tuple(m[i]-mg[i] for i in range(3))
                f=add(f,mul_monom(g,e,c/cg),Fraction(-1)); done=True; break
        if not done:
            r[m]=r.get(m,Fraction(0))+c
            f.pop(m)
    return clean(r)

def spol(f,g):
    mf,cf=lead(f); mg,cg=lead(g)
    l=tuple(max(mf[i],mg[i]) for i in range(3))
    ef=tuple(l[i]-mf[i] for i in range(3)); eg=tuple(l[i]-mg[i] for i in range(3))
    return add(mul_monom(f,ef,Fraction(1,1)/cf), mul_monom(g,eg,Fraction(1,1)/cg), Fraction(-1))

def deriv(p,j):
    r={}
    for m,c in p.items():
        if m[j]:
            mm=list(m); k=mm[j]; mm[j]-=1
            r[tuple(mm)]=r.get(tuple(mm),Fraction(0))+c*k
    return clean(r)

def eq(p,q): return clean(p)==clean(q)

for n in range(2,11):
    g={
      (n+1,0,0):Fraction(1),
      (n,1,0):Fraction(1),
      (0,n,1):Fraction(1),
      (0,0,n):Fraction(1),
    }
    gx,gy,gz=(deriv(g,j) for j in range(3))
    lhs=mul_monom(g,(0,0,0),Fraction(n+1))
    lhs=add(lhs,mul_monom(gx,(1,0,0)),Fraction(-1))
    lhs=add(lhs,mul_monom(gy,(0,1,0)),Fraction(-1))
    lhs=add(lhs,mul_monom(gz,(0,0,1)),Fraction(-1))
    assert eq(lhs,mon((0,0,n)))

    G=[
      add(mon((n,0,0)),mon((0,n-1,1),n)),
      add(mon((n-1,1,0)),mon((0,n-1,1),-(n+1))),
      mon((n-1,0,n-1)),
      mon((1,n-1,1)),
      add(mon((0,n,0)),mon((0,0,n-1),n)),
      mon((0,0,n)),
    ]
    for i,j in combinations(range(len(G)),2):
        assert reduce_poly(spol(G[i],G[j]),G)=={}, (n,i,j,reduce_poly(spol(G[i],G[j]),G))
    for h in (g,gx,gy,gz,mon((0,0,n))):
        assert reduce_poly(h,G)=={}, (n,h,reduce_poly(h,G))

    # Standard monomials of the initial ideal; pure powers bound exponents by n-1.
    LM=[lead(q)[0] for q in G]
    tau=0
    for a,b,c in product(range(n),repeat=3):
        m=(a,b,c)
        if not any(divides(l,m) for l in LM): tau += 1
    tau_formula=(n-1)*(n*n-n+3)
    mu_formula=(n-1)*(n*n+1)
    assert tau==tau_formula
    assert mu_formula-tau_formula==(n-1)*(n-2)

print('VERIFY_OK')
