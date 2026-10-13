#!/usr/bin/env python3
BASIS=("a","b","c","d")
idx={x:i for i,x in enumerate(BASIS)}
zero=(0,0,0,0)
def e(name):
    v=[0,0,0,0]; v[idx[name]]=1; return tuple(v)
T={(x,y):zero for x in BASIS for y in BASIS}
T[("b","b")]=e("a"); T[("b","c")]=e("b"); T[("c","b")]=e("c")
T[("c","c")]=e("d"); T[("a","b")]=e("d")
def add(u,v,p):
    return tuple((u[i]+v[i])%p for i in range(4))
def smul(s,u,p):
    return tuple((s*x)%p for x in u)
def mul(u,v,p):
    out=zero
    for i,x in enumerate(BASIS):
        for j,y in enumerate(BASIS):
            if u[i] and v[j]:
                out=add(out,smul(u[i]*v[j],T[(x,y)],p),p)
    return out

assert T[("b","b")]==e("a")
assert T[("b","c")]==e("b")
assert T[("c","b")]==e("c")
assert T[("c","c")]==e("d")
assert T[("a","b")]==e("d")

for p in (2,3,5,7):
    elems=[(a,b,c,d) for a in range(p) for b in range(p) for c in range(p) for d in range(p)]
    dline={(0,0,0,t) for t in range(p)}
    adplane={(s,0,0,t) for s in range(p) for t in range(p)}
    ann=set(); z2=set()
    for x in elems:
        prods=[mul(x,e(y),p) for y in BASIS]+[mul(e(y),x,p) for y in BASIS]
        if all(v==zero for v in prods):
            ann.add(x)
        if all(v in dline for v in prods):
            z2.add(x)
    assert ann==dline
    assert z2==adplane
    print(f"F_{p}: ann={len(ann)} z2={len(z2)} OK")
print("A2_EQUALS_A")
print("ANN_SPAN_D")
print("Z2_SPAN_A_D")
print("CHECK_OK")
