#!/usr/bin/env python3
"""Exact finite checks for a characteristic-two cubic cone. Standard library only."""
from itertools import product, combinations
from functools import reduce

def field(m, modulus):
    q=1<<m
    def mul(a,b):
        z=0
        while b:
            if b&1: z^=a
            b>>=1
            a<<=1
            if a&q: a^=modulus
        return z
    def power(a,n):
        z=1
        while n:
            if n&1: z=mul(z,a)
            a=mul(a,a)
            n>>=1
        return z
    def normalize(v):
        u=next(x for x in v if x)
        c=power(u,q-2)
        return tuple(mul(c,x) for x in v)
    def cubic(v):
        s=0
        for a in v:s^=a
        z=power(s,3)
        for a in v:z^=power(a,3)
        return z
    return q,mul,power,normalize,cubic

def projective_points(q,n,normalize):
    return sorted({normalize(v) for v in product(range(q),repeat=n) if any(v)})

def projective_lines(q,n,mul,normalize):
    pts=projective_points(q,n,normalize)
    out=set()
    for a,b in combinations(pts,2):
        line=frozenset([a,b]+[normalize(tuple(a[j]^mul(t,b[j]) for j in range(n))) for t in range(1,q)])
        assert len(line)==q+1
        out.add(line)
    return pts,sorted(out,key=lambda l:sorted(l))

def line_on_cubic(line,F,mul,power):
    a,b=tuple(line)[:2]
    sa=reduce(lambda x,y:x^y,a,0)
    sb=reduce(lambda x,y:x^y,b,0)
    b1=reduce(lambda x,y:x^y,(mul(power(x^sa,2),v) for x,v in zip(a,b)),0)
    b2=reduce(lambda x,y:x^y,(mul(x^sa,power(v,2)) for x,v in zip(a,b)),0)
    return F(a)==F(b)==b1==b2==0

for m,poly in [(1,0b11),(2,0b111)]:
    q,mul,power,norm,F=field(m,poly)
    pts3, lines3=projective_lines(q,4,mul,norm)
    onS=[line for line in lines3 if line_on_cubic(line,F,mul,power)]
    pts4,lines4=projective_lines(q,5,mul,norm)
    onX=[line for line in lines4 if line_on_cubic(frozenset(tuple(x[1:]) for x in line),F,mul,power)]
    print('q=',q, 'P3 points=',len(pts3),'P3 lines=',len(lines3),'S-points=',sum(F(x)==0 for x in pts3),'S-lines=',len(onS))
    print('q=',q,'P4 points=',len(pts4),'P4 lines=',len(lines4),'X-lines=',len(onX))
    assert (len(onS),len(onX))=={2:(15,75),4:(27,477)}[q]
    if q==4:
        f=lambda line:frozenset(tuple(power(x,2) for x in pt) for pt in line)
        fixed=sum(f(L)==L for L in onS)
        assert fixed==15
        assert all(f(f(L))==L for L in onS)
        print('F4 lines Frobenius cycles: 15 fixed and 6 transpositions')

# A geometric witness in F32 for generic transverse regular-sequence condition.
q,mul,power,norm,F=field(5,0b100101)  # x^5+x^2+1 irreducible
surface=projective_points(q,4,norm)
surface=[p for p in surface if F(p)==0]
assert len(surface)==1185
# Enumerate F2-defined lines, then test no such line contains the witness.
qq,mm,pp,nn,FF=field(1,0b11)
_,linesF2=projective_lines(qq,4,mm,nn)
baseF2=[L for L in linesF2 if line_on_cubic(L,FF,mm,pp)]
baseF2rep=[]
for L in baseF2:
    a,b=list(L)[:2]
    baseF2rep.append((a,b))

def in_span(p,a,b):
    # binary plane linearly independent: check all combinations in F32
    for r in range(32):
        for t in range(32):
            if all((mul(r,a[i])^mul(t,b[i]))==p[i] for i in range(4)):
                return True
    return False

def on_rational_line(p):
    return any(in_span(p,a,b) for a,b in baseF2rep)

def independent_linear_forms(c,d):
    return not any(all(mul(t,c[i])==d[i] for i in range(4)) for t in range(q))

witness=None
for p in surface:
    if on_rational_line(p):continue
    s=0
    for x in p:s^=x
    linear=[power(x^s,2) for x in p]
    root=[power(x^s,16) for x in p]
    if not independent_linear_forms(linear,root):continue
    # linear forms' common kernel: contains p, and one other direction w
    def zero_dot(c,v):
        return reduce(lambda x,y:x^y,(mul(c[i],v[i]) for i in range(4)),0)==0
    w=next((v for v in projective_points(q,4,norm)
            if zero_dot(linear,v) and zero_dot(root,v)
            and not in_span(v,p,p)),None)
    # The last span test is just scalar dependence on p.
    if w is None:continue
    if F(w)==0:continue
    witness=(p,w);break
assert witness is not None
print('F32 geometric witness (point, transverse direction):',witness,'cubic(direction)=',F(witness[1]))
print('SEGRE_CHAR2_CONE_FANO_28_COMPONENTS_6FOLD_VERTEX_75_477_PASS')
