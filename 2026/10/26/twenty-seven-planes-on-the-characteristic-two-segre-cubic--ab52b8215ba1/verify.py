"""Exact enumeration of planes on the characteristic-two Segre cone via lines on its cubic base."""
from itertools import combinations,product

def mul(a,b,q):
    if q==2: return a&b
    out=0
    while b:
        if b&1: out^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return out

def add(*args):
    t=0
    for a in args:t^=a
    return t

def norm(v):
    j=next(i for i,x in enumerate(v) if x)
    if q==2:return tuple(v)
    return tuple(mul(x,inv[v[j]],q) for x in v)

def f(v):
    # 5 coordinates with sum zero, use first four freely
    a,b,c,d=v
    e=add(a,b,c,d)
    return add(*[mul(mul(z,z,q),z,q) for z in (a,b,c,d,e)])

def line_ok(u,v):
    # F(u s + v t) coefficient s^3,t^3,s^2t,st^2
    # cubic is sum of individual coordinate cubes for 5 coordinates
    U=(*u,add(*u));V=(*v,add(*v))
    return all(x==0 for x in (f(u),f(v),add(*[mul(mul(a,a,q),b,q) for a,b in zip(U,V)]), add(*[mul(a,mul(b,b,q),q) for a,b in zip(U,V)])))

for q in (2,4):
    inv={x:next(y for y in range(1,q) if mul(x,y,q)==1) for x in range(1,q)}
    points=sorted({norm(x) for x in product(range(q),repeat=4) if any(x)})
    on=[x for x in points if f(x)==0]
    lines={}
    for i,u in enumerate(on):
        for v in on[i+1:]:
            if not line_ok(u,v):continue
            pts=frozenset(norm(tuple(add(a,mul(t,b,q)) for a,b in zip(u,v))) for t in range(q))|{norm(v)}
            assert len(pts)==q+1
            lines[tuple(sorted(pts))]=1
    print('q',q,'base_points',len(on),'lines',len(lines))
    assert len(lines)==(15 if q==2 else 27)
    assert len(on)==(15 if q==2 else 45)
print('VERIFY_OK')
