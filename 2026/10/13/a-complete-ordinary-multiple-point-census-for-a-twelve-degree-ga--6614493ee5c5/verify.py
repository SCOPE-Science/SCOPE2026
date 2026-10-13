#!/usr/bin/env python3
"""Exact finite-field certificate for a degree-twelve rational plane curve.

Uses the standard library only. The relevant fields are F_11 and
F_121 = F_11[u]/(u*u-2), with 2 nonsquare modulo 11.
"""
from collections import Counter, defaultdict

P = 11


def mm(a, b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % P
                 for i in range(2) for j in range(2))


def mn(a):
    a = tuple(v % P for v in a)
    lead = next(v for v in a if v)
    return tuple(v * pow(lead, -1, P) % P for v in a)


def subgroup(generators):
    generators = [mn(a) for a in generators]
    seen = {mn((1, 0, 0, 1))}
    pending = list(seen)
    while pending:
        a = pending.pop()
        for b in generators:
            c = mn(mm(a, b))
            if c not in seen:
                seen.add(c)
                pending.append(c)
    return seen


def linear_multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            result[i+j] = (result[i+j] + v*w) % P
    return result


def padadd(a, b):
    m = max(len(a), len(b))
    return [((a[i] if i < len(a) else 0) +
             (b[i] if i < len(b) else 0)) % P for i in range(m)]

D = [0] * 12
D[1] = -1 % P
D[11] = 1


def trace_numerator(subgroup_elements):
    total = [0]*13
    for a, b, c, d in subgroup_elements:
        if c:
            # Exact division of D=x^11-x by (c*x+d).
            quotient = [0]*11
            quotient[10] = pow(c, -1, P)
            for j in range(10, 0, -1):
                quotient[j-1] = (D[j]-d*quotient[j])*pow(c,-1,P)%P
            assert (d*quotient[0])%P == D[0]
            term = linear_multiply([b, a], quotient)
        else:
            term = linear_multiply([b*pow(d,-1,P)%P,
                                    a*pow(d,-1,P)%P], D)
        total = padadd(total, term)
    return total

G = subgroup([(0,2,1,0),(1,2,-1,-1),(2,5,1,4)])
H = subgroup([(2,1,1,0)])
assert len(G) == len(H) == 12
# The first group is V_4 semidirect C_3, hence A_4.
sigma, tau, eta = (mn((0,2,1,0)),mn((1,2,-1,-1)),
                   mn((2,5,1,4)))
assert len(subgroup([sigma,tau])) == 4
assert mn(mm(sigma,tau)) == mn(mm(tau,sigma))
assert len(subgroup([eta])) == 3
assert len(subgroup([mn((2,1,1,0))])) == 12
assert len(G.intersection(H)) == 1
assert len(subgroup(list(G | H))) == 1320

a = trace_numerator(G)
b = trace_numerator(H)
assert a == [9,0,5,3,9,7,0,9,5,10,1,0,1]
assert b == [10,9,0,0,0,0,0,0,0,0,0,0,1]

# Each of G and H acts regularly on P^1(F_11): the images of infinity
# under distinct group elements enumerate F_11 union {infinity}.
for group in (G, H):
    images = set()
    for aa, bb, cc, dd in group:
        images.add(None if cc==0 else aa*pow(cc,-1,P)%P)
    assert images == set(range(P)) | {None}

# Pairs (r,s) encode r+s*u in F_121, u^2=2.
Z = (0,0)
ONE = (1,0)

def fadd(v,w):
    return ((v[0]+w[0])%P, (v[1]+w[1])%P)

def fneg(v):
    return (-v[0]%P,-v[1]%P)

def fsub(v,w):
    return fadd(v, fneg(w))

def fmul(v,w):
    return ((v[0]*w[0]+2*v[1]*w[1])%P,
            (v[0]*w[1]+v[1]*w[0])%P)

def finv(v):
    norm = (v[0]*v[0]-2*v[1]*v[1]) % P
    if norm == 0:
        raise ZeroDivisionError(v)
    invnorm = pow(norm,-1,P)
    return (v[0]*invnorm%P,-v[1]*invnorm%P)

def fdiv(v,w):
    return fmul(v,finv(w))

def evaluate(poly,z):
    result = Z
    for c in reversed(poly):
        result = fadd(fmul(result,z),(c,0))
    return result

def derivative(poly):
    return [(j*poly[j])%P for j in range(1,len(poly))]

ad = derivative(a)
bd = derivative(b)
dd = derivative(D)


def mapped(z):
    if z is None:
        return ('infty', ONE)
    av, bv, dv = evaluate(a,z), evaluate(b,z), evaluate(D,z)
    if dv == Z:
        assert bv != Z
        return ('infty',fdiv(av,bv))
    return ('affine',fdiv(av,dv),fdiv(bv,dv))


def tangent(z):
    if z is None:
        # Local parameter w=1/x near infinity; a[12]=b[12]=1,
        # a[11]=b[11]=0, and D^hom(w)=w-w^11.
        return (Z, ONE)
    av, bv, dv = evaluate(a,z), evaluate(b,z), evaluate(D,z)
    ap,bp,dp=evaluate(ad,z),evaluate(bd,z),evaluate(dd,z)
    if dv == Z:
        return (fdiv(fsub(fmul(ap,bv),fmul(av,bp)),fmul(bv,bv)),
                fdiv(dp,bv))
    return (fdiv(fsub(fmul(ap,dv),fmul(av,dp)),fmul(dv,dv)),
            fdiv(fsub(fmul(bp,dv),fmul(bv,dp)),fmul(dv,dv)))

points = [(r,s) for r in range(P) for s in range(P)] + [None]
assert len(points) == 122
fibres=defaultdict(list)
for t in points:
    fibres[mapped(t)].append(t)
multiple={key:pts for key,pts in fibres.items() if len(pts)>1}
counts=Counter(len(v) for v in multiple.values())
assert counts == {2:25, 3:6, 4:2}, counts

for key, pts in multiple.items():
    ts = [tangent(z) for z in pts]
    for i in range(len(ts)):
        assert ts[i] != (Z,Z)
        for j in range(i):
            det=fsub(fmul(ts[i][0],ts[j][1]),
                     fmul(ts[i][1],ts[j][0]))
            assert det != Z, (key,pts[i],pts[j])

assert sum(len(v)*(len(v)-1)//2 for v in multiple.values()) == 55
# Exactly four nodes lie at projective infinity.
assert sum(key[0]=='infty' for key in multiple) == 4
# Rational singular points: five ordinary nodes, no triple or quadruple.
rational=lambda k: all(z[1]==0 for z in k[1:])
assert Counter(len(v) for k,v in multiple.items() if rational(k)) == {2:5}
# Each singular image has coordinates in F_121. Its Galois conjugate
# is another singular image; the non-rational counts are even.
for key in multiple:
    conjugate=tuple([(z[0], -z[1]%P) for z in key[1:]])
    assert (key[0], *conjugate) in multiple

print('VERIFY_OK: 122 source points; 25 nodes, 6 triples, 2 quadruples; '
      'all transverse; delta 55; 5 F11-rational nodes')
