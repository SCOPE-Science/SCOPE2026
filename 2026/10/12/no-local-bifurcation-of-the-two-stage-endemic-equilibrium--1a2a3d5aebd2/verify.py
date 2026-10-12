#!/usr/bin/env python3
from itertools import permutations

VARS = ('mu','delta1','gamma1','theta1','delta2','theta2','alpha','q','z')
N = len(VARS)
ZERO = (0,)*N

def clean(p):
    return {m:c for m,c in p.items() if c}

def const(c):
    return {} if c == 0 else {ZERO:int(c)}

def var(i):
    e=[0]*N; e[i]=1
    return {tuple(e):1}

def add(*ps):
    out={}
    for p in ps:
        for m,c in p.items(): out[m]=out.get(m,0)+c
    return clean(out)

def neg(p): return {m:-c for m,c in p.items()}
def sub(p,q): return add(p,neg(q))

def mul(p,q):
    out={}
    for m,c in p.items():
        for n,d in q.items():
            k=tuple(a+b for a,b in zip(m,n))
            out[k]=out.get(k,0)+c*d
    return clean(out)

def prod(*ps):
    r=const(1)
    for p in ps: r=mul(r,p)
    return r

def sign_perm(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1

def det4(M):
    out={}
    for p in permutations(range(4)):
        term=const(sign_perm(p))
        for i,j in enumerate(p): term=mul(term,M[i][j])
        out=add(out,term)
    return out

def coeff_z(p,k):
    out={}
    for m,c in p.items():
        if m[-1]==k:
            mm=m[:-1]+(0,)
            out[mm]=out.get(mm,0)+c
    return clean(out)

def all_positive_coeffs(p):
    return bool(p) and all(c>0 for c in p.values())

def monomial_stats(p):
    cs=list(p.values())
    return len(cs), min(cs), max(cs)

mu,d1,g1,t1,d2,t2,alpha,q,z = [var(i) for i in range(N)]
x1=add(mu,d1,g1,t1)
x2=add(mu,d2,t2)
a=add(alpha,mu)
b=add(mu,q)

# Jacobian at an endemic equilibrium uses beta*S*=x1 and q=beta*I1*>0.
M=[
    [add(z,mu,q), x1, const(0), neg(alpha)],
    [neg(q), z, const(0), const(0)],
    [const(0), neg(g1), add(z,x2), const(0)],
    [const(0), neg(t1), neg(t2), add(z,a)],
]
char_det=det4(M)
char_formula=add(
    prod(z,add(z,a),add(z,x2),add(z,b)),
    prod(x1,q,add(z,a),add(z,x2)),
    neg(prod(alpha,q,add(prod(t1,add(z,x2)),prod(t2,g1))))
)
assert char_det == char_formula, 'characteristic determinant identity failed'

A4=coeff_z(char_det,0); A3=coeff_z(char_det,1); A2=coeff_z(char_det,2); A1=coeff_z(char_det,3); A0=coeff_z(char_det,4)
assert A0 == const(1), 'not monic quartic'
H2=sub(mul(A1,A2),A3)
H3=sub(sub(prod(A1,A2,A3),mul(A3,A3)),prod(A1,A1,A4))

for name,p in [('A1',A1),('A2',A2),('A3',A3),('A4',A4),('H2',H2),('H3',H3)]:
    assert all_positive_coeffs(p), f'{name} has a non-positive expanded coefficient'

stats={name:monomial_stats(p) for name,p in [('A1',A1),('A2',A2),('A3',A3),('A4',A4),('H2',H2),('H3',H3)]}
assert stats['H3'][0] == 331
assert stats['H3'][1] == 1
assert stats['H3'][2] == 58
print('VERIFY_OK')
for name in ('A1','A2','A3','A4','H2','H3'):
    n,lo,hi=stats[name]
    print(f'{name}: monomials={n} min_coeff={lo} max_coeff={hi}')
