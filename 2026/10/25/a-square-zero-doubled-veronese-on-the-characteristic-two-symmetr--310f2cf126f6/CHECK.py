"""Exact F_2 checks for the singular scheme of a 3-by-3 symmetric determinant.
Run: python3 CHECK.py. Uses only the Python standard library.
These finite symbolic identities support, but do not replace, the geometric proof.
"""
from itertools import combinations_with_replacement
from math import comb

N = 6  # (a,b,c,d,e,f)
zero = (0,) * N

def mono(**kw):
    z = [0] * N
    for name, power in kw.items(): z['abcdef'.index(name)] = power
    return frozenset([tuple(z)])

def add(*fs):
    v = set()
    for f in fs: v.symmetric_difference_update(f)
    return frozenset(v)

def mul(f,g):
    v = set()
    for p in f:
        for q in g:
            m = tuple(p[i]+q[i] for i in range(N))
            if m in v: v.remove(m)
            else: v.add(m)
    return frozenset(v)

def scal(f,m): return frozenset(tuple(p[i]+m[i] for i in range(N)) for p in f)

def deriv(f,i):
    v=set()
    for p in f:
        if p[i]%2:
            m=list(p);m[i]-=1;v.add(tuple(m))
    return frozenset(v)

def red(f,basis):
    p=set(f); rem=set()
    while p:
        x=max(p)
        for g in basis:
            lead=max(g)
            if all(x[j]>=lead[j] for j in range(N)):
                m=tuple(x[j]-lead[j] for j in range(N))
                p.symmetric_difference_update(scal(g,m));break
        else: p.remove(x);rem.add(x)
    return frozenset(rem)

def spol(f,g):
    u=max(f);v=max(g); l=tuple(max(u[i],v[i]) for i in range(N))
    return add(scal(f,tuple(l[i]-u[i] for i in range(N))),
               scal(g,tuple(l[i]-v[i] for i in range(N))))

A,B,C,D,E,F = [mono(**{v:1}) for v in 'abcdef']
sq=lambda x:mul(x,x)
q1=add(mul(A,C),sq(B));q2=add(mul(A,E),sq(D));q3=add(mul(C,E),sq(F))
u=add(mul(A,F),mul(B,D));v=add(mul(C,D),mul(B,F));w=add(mul(E,B),mul(D,F))
det=add(mul(mul(A,C),E),mul(A,sq(F)),mul(C,sq(D)),mul(E,sq(B)))
assert det==add(mul(A,q3),mul(C,q2),mul(E,q1))
partials=[deriv(det,i) for i in range(N)]
assert partials==[q3,frozenset(),q2,frozenset(),q1,frozenset()]
# Lex Groebner basis for the three principal minors, proven by S-pairs.
g3=add(mul(A,sq(F)),mul(C,sq(D)))
g4=add(mul(sq(B),E),mul(C,sq(D)))
g5=add(mul(sq(B),sq(F)),mul(sq(C),sq(D)))
GB=[q1,q2,g3,g4,g5,q3]
for i in range(len(GB)):
    for j in range(i): assert not red(spol(GB[i],GB[j]),GB),(i,j)
for p in (q1,q2,q3):assert not red(p,GB)
for x,y in combinations_with_replacement([u,v,w],2): assert not red(mul(x,y),GB)
assert red(u,GB) and red(v,GB) and red(w,GB)
# Hilbert series of a codimension-three quadratic complete intersection.
def hilb(n):
    return sum(((-1)**k)*comb(3,k)*comb(n-2*k+5,5) for k in range(4) if n-2*k>=0)
assert hilb(0)==1
for n in range(1,21):
    assert hilb(n)==4*n*n+2
    reduced=comb(2*n+2,2)
    nil=comb(2*n-1,2) if n>=2 else 0
    assert reduced+nil==hilb(n)
print('VERIFY_OK: char2 determinant derivatives, S-pair Groebner proof, six nilpotent products, degree-eight CI Hilbert function 0..20')
