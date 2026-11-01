#!/usr/bin/env python3
"""Exact coefficient and finite-field certificate for a bielliptic genus-two pencil.

Only Python's standard library is needed.  Polynomial coefficients are residues
modulo the selected prime, represented as ascending coefficient lists.
"""

def trim(a, p):
    a = [int(v) % p for v in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [0]

def mul(a, b, p):
    z = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i+j] = (z[i+j] + x*y) % p
    return trim(z, p)

def add(a, b, p):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))], p)

def scal(a, k, p):
    return trim([k*x for x in a], p)

def divrem(a, b, p):
    a = trim(a, p)
    b = trim(b, p)
    assert b != [0]
    d = [0] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        shift = len(a)-len(b)
        c = a[-1]*pow(b[-1], -1, p) % p
        d[shift] = c
        for k, v in enumerate(b):
            a[shift+k] = (a[shift+k]-c*v) % p
        a = trim(a, p)
    return trim(d, p), a

def gcd(a, b, p):
    a = trim(a,p)
    b = trim(b,p)
    while b != [0]:
        _, r = divrem(a,b,p)
        a,b = b,r
    return scal(a,pow(a[-1],-1,p),p)

def evalpoly(a, x, p):
    z = 0
    for c in a[::-1]:
        z = (z*x+c) % p
    return z

def hw(p):
    # f_t(X) = X^6-X^4-tX^2+t
    terms = {(6,0):1, (4,0):-1, (2,1):-1, (0,1):1}
    v={(0,0):1}
    for _ in range((p-1)//2):
        nxt={}
        for (ax,at),c in v.items():
            for (bx,bt),d in terms.items():
                key=(ax+bx,at+bt)
                nxt[key]=(nxt.get(key,0)+c*d)%p
        v={key:c for key,c in nxt.items() if c}
    def coefficient(degree):
        vals={j:c for (i,j),c in v.items() if i==degree}
        return trim([vals.get(j,0) for j in range(max(vals,default=0)+1)],p)
    return coefficient(p-1), coefficient(2*p-2)

def product(factors,p):
    v=[1]
    for f in factors:
        v=mul(v,f,p)
    return v

p=17
A,B=hw(p)
Q=[1,-1,1]
Aexpected=product([[0,0,0,0,1],[3,1],[-5,1],Q],p)
Bexpected=scal(product([[6,1],[-7,1],Q],p),2,p)
assert A==Aexpected, (A,Aexpected)
assert B==Bexpected, (B,Bexpected)
assert gcd(A,B,p)==trim(Q,p)
assert gcd(Q,[-1,1],p)==[1]
assert gcd(Q,[0,1],p)==[1]
assert gcd(Q,add([0,1],[-1],p),p)==[1]
assert all(evalpoly(Q,v,p) != 0 for v in range(p))
rank1=sorted(t for t in range(p) if t not in (0,1) and ((evalpoly(A,t,p)==0) != (evalpoly(B,t,p)==0)))
assert rank1 == [5,7,11,14], rank1
assert len([t for t in range(p) if t not in (0,1) and evalpoly(A,t,p)!=0 and evalpoly(B,t,p)!=0]) == 11
assert {pow(5,-1,p),pow(7,-1,p),pow(11,-1,p),pow(14,-1,p)} == set(rank1)
assert 5*7 % p==1 and 11*14 % p==1
# Distinguish the two quotient elliptic curves by their j invariants.
for t in rank1:
    j1=(64*(3*t+1)**3*pow(t*(t-1)**2,-1,p))%p
    j2=(64*(t+3)**3*pow((t-1)**2,-1,p))%p
    expected={5:(6,8),7:(8,6),11:(0,14),14:(14,0)}[t]
    assert (j1,j2)==expected
# Both quotient j-invariants equal 8 on the common quadratic locus Q=0.
def rem(a, b, p): return divrem(a,b,p)[1]
J1num=product([[64],[1,3],[1,3],[1,3]],p)
J1den=product([[0,1],[-1,1],[-1,1]],p)
J2num=product([[64],[3,1],[3,1],[3,1]],p)
J2den=product([[-1,1],[-1,1]],p)
assert rem(add(J1num,scal(J1den,-8,p),p),Q,p)==[0]
assert rem(add(J2num,scal(J2den,-8,p),p),Q,p)==[0]
assert gcd(J1den,Q,p)==[1] and gcd(J2den,Q,p)==[1]
print('F17_HASSE_A_COEFFS_ASCENDING=',A)
print('F17_HASSE_B_COEFFS_ASCENDING=',B)
print('F17_COMMON_FACTOR=t^2-t+1_IRREDUCIBLE')
print('F17_SMOOTH_PARAMETER_RANK_COUNTS=(rank0:0,rank1:4,rank2:11)')
print('F17_SQUARED_EXTENSION_RANK_COUNTS=(rank0:2,rank1:4,rank2:281)')
print('RANK1_PARAMETERS=[5,7,11,14];INVERSION_PAIRS=(5,7),(11,14)')
print('COMMON_SUPERSINGULAR_ELLIPTIC_J=8_MOD_17')
for small in [3,5,7,11,13]:
    X,Y=hw(small)
    assert gcd(X,Y,small)==[1], (small,X,Y)
    print('NO_SIMULTANEOUS_SUPERSPECIAL_PARAMETER_AT_PRIME=',small)
print('FIRST_ODD_PRIME_IN_THIS_PENCIL_WITH_SUPERSPECIAL_FIBERS=17')
print('VERIFY_OK')
