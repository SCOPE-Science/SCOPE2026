#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
cert = json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))
MOD = cert["field"]["modulus_bits"]

def deg(p):
    return p.bit_length()-1

def pmod(a,m):
    dm=deg(m)
    while a and deg(a)>=dm:
        a ^= m << (deg(a)-dm)
    return a

def pmul(a,b):
    r=0
    while b:
        if b&1:
            r ^= a
        b >>= 1
        a <<= 1
    return r

def mul(a,b):
    return pmod(pmul(a,b),MOD)

def power(a,e):
    r=1
    while e:
        if e&1:
            r=mul(r,a)
        a=mul(a,a)
        e >>= 1
    return r

assert power(2,63)==1
assert power(2,21)!=1
assert power(2,9)!=1

F=list(range(64))
F4=[x for x in F if power(x,4)==x]
assert len(F4)==4
F4star=[x for x in F4 if x]

def tr(x):
    return x ^ power(x,4) ^ power(x,16)

assert all(tr(x) in F4 for x in F)

def phi(rho,x):
    return mul(rho,x) ^ power(x,4)

def adj(rho,y):
    return mul(rho,y) ^ power(y,16)

def inner(x,y):
    return tr(mul(x,y))

singular=[rho for rho in range(1,64) if power(rho,21)==1]
assert len(singular)==21

images={}
normals={}
for rho in singular:
    im=frozenset(phi(rho,x) for x in F)
    ker=frozenset(y for y in F if adj(rho,y)==0)
    assert len(im)==16
    assert len(ker)==4
    nz=[y for y in ker if y]
    assert len(nz)==3
    assert all(power(y,15)==rho for y in nz)
    y=nz[0]
    hyp=frozenset(z for z in F if inner(z,y)==0)
    assert im==hyp
    images[rho]=im
    normals[rho]=ker

assert len(set(images.values()))==21

# Projective lines in V=GF(64) over GF(4).
seen=set()
projective=[]
for y in range(1,64):
    line=frozenset(mul(a,y) for a in F4star)
    if line not in seen:
        seen.add(line)
        projective.append(line)
assert len(projective)==21

all_hyperplanes=set()
for line in projective:
    y=next(iter(line))
    all_hyperplanes.add(frozenset(z for z in F if inner(z,y)==0))
assert len(all_hyperplanes)==21
assert all_hyperplanes==set(images.values())

# Projective normal map is bijective.
rho_from_lines={power(next(iter(line)),15) for line in projective}
assert rho_from_lines==set(singular)

# Direct hull computation.
non_lcd=[]
for rho in singular:
    im=images[rho]
    perp=frozenset(y for y in F if all(inner(x,y)==0 for x in im))
    hull=im & perp
    assert len(perp)==4
    assert len(hull) in (1,4)
    if len(hull)==4:
        non_lcd.append(rho)
        y=next(v for v in normals[rho] if v)
        assert tr(y)==0
    else:
        y=next(v for v in normals[rho] if v)
        assert tr(y)!=0
assert len(non_lcd)==5

def exc_poly(r):
    return power(r,5) ^ power(r,4) ^ 1

roots=[r for r in F if exc_poly(r)==0]
assert set(roots)==set(non_lcd)
assert len(roots)==5

# Check factorization pointwise.
for r in F:
    lhs=exc_poly(r)
    f2=power(r,2)^r^1
    f3=power(r,3)^r^1
    assert lhs==mul(f2,f3)

quad=[r for r in roots if (power(r,2)^r^1)==0]
cubic=[r for r in roots if (power(r,3)^r^1)==0]
assert len(quad)==2
assert len(cubic)==3
assert all(power(r,3)==1 and r!=1 for r in quad)
assert all(power(r,7)==1 and r!=1 for r in cubic)

# Full projective family: 64 finite rho plus infinity.
hull_counts={0:0,1:0}
for rho in F:
    im=frozenset(phi(rho,x) for x in F)
    perp=frozenset(y for y in F if all(inner(x,y)==0 for x in im))
    hull=im & perp
    if len(hull)==1:
        hull_counts[0]+=1
    elif len(hull)==4:
        hull_counts[1]+=1
    else:
        raise AssertionError((rho,len(im),len(hull)))
# Infinity corresponds to scalar identity, hence full space and zero hull.
hull_counts[0]+=1
assert hull_counts=={0:60,1:5}
assert hull_counts=={int(k):v for k,v in cert["non_lcd_locus"]["full_projective_hull_distribution"].items()}

print("VERIFY_OK")
