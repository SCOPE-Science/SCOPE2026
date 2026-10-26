#!/usr/bin/env python3
"""Exact finite-field corroboration for tame cubic genus-two models over F2.
The mathematical completeness argument is in RESULT.md, not this script.
Uses F_64=F_2[t]/(t^6+t+1), represented by six-bit integers.
"""
from itertools import product

MOD=0x43
INF=64

def add(a,b): return a^b

def mul(a,b):
    out=0
    while b:
        if b&1: out^=a
        b>>=1; a<<=1
        if a&64: a^=MOD
    return out

def fpow(a,n):
    out=1
    while n:
        if n&1: out=mul(out,a)
        a=mul(a,a); n>>=1
    return out

def inv(a):
    assert a
    return fpow(a,62)

def div(a,b): return mul(a,inv(b))

def p_add(a,b):
    return [((a[i] if i<len(a) else 0)^(b[i] if i<len(b) else 0)) for i in range(max(len(a),len(b)))]

def p_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]^=mul(x,y)
    return out

def p_pow(a,n):
    out=[1]
    for _ in range(n):out=p_mul(out,a)
    return out

def trim(a):
    a=a[:]
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def substitute_homogeneous(poly,trans):
    a,b,c,d=trans
    u=[b,a]; v=[d,c]
    m=max(3,len(poly)-1)
    out=[0]
    for i,coeff in enumerate(poly):
        w=p_mul(p_pow(u,i),p_pow(v,m-i))
        out=p_add(out,[mul(coeff,z) for z in w])
    return trim(out)

def transform_equal(N,D,T,shift=0):
    nt=substitute_homogeneous(N,T)
    dt=substitute_homogeneous(D,T)
    lhs=p_mul(nt,D)
    rhs=p_mul(N,dt)
    if shift:rhs=p_add(rhs,p_mul(D,dt))
    return trim(lhs)==trim(rhs)

def eval_poly(p,x):
    out=0
    for a in reversed(p):out=mul(out,x)^a
    return out

def mob(T,x):
    a,b,c,d=T
    if x==INF:return div(a,c) if c else INF
    n=mul(a,x)^b; den=mul(c,x)^d
    return div(n,den) if den else INF

def roots(p):return [a for a in range(64) if not eval_poly(p,a)]

w=58; w2=59
assert mul(w,w)^w^1 ==0 and mul(w2,w2)^w2^1==0 and w^w2==1
S={'split':([1,1,1,1],[0,1,1]),
   'mixed':([1,1,1,1],[1,1,1]),
   'cubic':([0,1,1],[1,1,0,1])}
# split N=x^3+x^2+1, D=x^2+x
S['split']=([1,0,1,1],[0,1,1])
# mixed N=(x+1)^3, D=x^2+x+1
S['mixed']=([1,1,1,1],[1,1,1])
# cubic N=x^2+x, D=x^3+x+1
S['cubic']=([0,1,1],[1,1,0,1])
T={'split':(0,1,1,1),'mixed':(1,0,w,w2),'cubic':(0,1,1,1)}
for typ,(N,D) in S.items():
    assert transform_equal(N,D,T[typ]),typ
    pts=roots(D)+([INF] if len(D)<len(N) else [])
    if typ=='split':assert set(pts)=={0,1,INF}
    if typ=='mixed':assert set(pts)=={w,w2,INF}
    if typ=='cubic':assert len(pts)==3
    assert set(mob(T[typ],x) for x in pts)==set(pts)
    assert all(mob(T[typ],x)!=x for x in pts)
    print('CUBIC_AUTOMORPHISM',typ,'POLES',pts)

# Enumerate the 3/7 possible nonzero polar classes for quadratic/cubic supports.
quad=(1,1,1); cub=(1,1,0,1)
mixed_good=[]
for B,C in product(range(2),repeat=2):
    if B==C==0:continue
    # x+(Bx+C)/(x^2+x+1)
    N=p_add(p_mul([0,1],list(quad)),[C,B]); D=list(quad)
    if transform_equal(N,D,T['mixed']):mixed_good.append((B,C))
assert mixed_good==[(0,1)]
print('MIXED_INVARIANT_NUMERATORS',mixed_good)

cubic_good=[]
for A,B,C in product(range(2),repeat=3):
    if not (A or B or C):continue
    if transform_equal([C,B,A],list(cub),T['cubic']):cubic_good.append((A,B,C))
assert cubic_good==[(1,1,0)]
print('CUBIC_INVARIANT_NUMERATORS',cubic_good)

# Three base-PGL2(F2) stabilizers: check class of additive quadratic twists.
def pgl2():
    seen=[]
    for T0 in product(range(2),repeat=4):
        a,b,c,d=T0
        if a*d^b*c and T0 not in seen:seen.append(T0)
    return seen
assert len(pgl2())==6
for typ,(N,D) in S.items():
    pts=roots(D)+([INF] if len(D)<len(N) else [])
    stab=[x for x in pgl2() if set(mob(x,z) for z in pts)==set(pts)]
    assert len(stab)=={'split':6,'mixed':2,'cubic':3}[typ]
    shifts=[(x,int(transform_equal(N,D,x,1))) for x in stab]
    assert all(transform_equal(N,D,x) or transform_equal(N,D,x,1) for x in stab)
    if typ=='cubic':assert not any(flag for _,flag in shifts)
    else:assert any(flag for _,flag in shifts)
    print('STABILIZER',typ,len(stab),'CONSTANT_ONE_SHIFTS',sum(f for _,f in shifts))

# Count geometric branch values over F2 by the explicit critical-point evaluation.
for typ,(N,D) in S.items():
    critical=[0,1] if typ=='mixed' else [w,w2]
    vals=[div(eval_poly(N,x),eval_poly(D,x)) for x in critical]
    assert (set(vals)=={0,1} if typ=='mixed' else set(vals)=={w,w2})
    print('CRITICAL_VALUES',typ,vals)

# Point counts on smooth Artin-Schreier models over F2 and F4, pole fibers counted once.
def subfield(m):return [z for z in range(64) if fpow(z,1<<m)==z]
def field_trace(z,m):
    out=0
    for j in range(m):out^=fpow(z,1<<j)
    assert out in [0,1]
    return out

def count(typ,d,m):
    N,D=S[typ]
    poles=roots(D)+([INF] if len(D)<len(N) else [])
    total=0
    for x in subfield(m)+[INF]:
        if x in poles:total+=1
        else:
            v=(0 if x==INF else div(eval_poly(N,x),eval_poly(D,x)))^d
            total+=2*(field_trace(v,m)==0)
    return total
for typ in ['split','mixed','cubic']:
    for d in ([0,1] if typ=='cubic' else [0]):
        vals=(count(typ,d,1),count(typ,d,2),count(typ,d,3))
        assert vals=={('split',0):(3,3,9),('mixed',0):(3,7,9),('cubic',0):(6,6,9),('cubic',1):(0,6,9)}[(typ,d)]
        print('POINT_COUNTS',typ,d,vals)
print('VERIFIED')
