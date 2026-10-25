#!/usr/bin/env python3
"""Exact small-domain verification for two-agent complementary-pair allocations.

For each even number of goods up to eight, enumerate both agents' perfect
matching complement lists and all complete two-agent allocations. The
reference optimum is obtained directly from cycles of the union of matchings.
"""
from functools import lru_cache
from collections import Counter
from itertools import product

@lru_cache(None)
def matchings(vertices):
    if not vertices:
        return ((),)
    x=vertices[0]
    return tuple(((x,y),)+tail for z,y in enumerate(vertices[1:])
                 for tail in matchings(vertices[1:z+1]+vertices[z+2:]))

def cycles(m1,m2):
    n=2*len(m1)
    p=[None]*n;q=[None]*n
    for a,b in m1:p[a]=b;p[b]=a
    for a,b in m2:q[a]=b;q[b]=a
    seen=set();out=[]
    for start in range(n):
        if start in seen:continue
        todo=[start];part=[]
        while todo:
            x=todo.pop()
            if x in seen:continue
            seen.add(x);part.append(x)
            todo.extend((p[x],q[x]))
        out.append(len(part)//2)
    return tuple(sorted(out))

def predicted(m1,m2):
    lens=cycles(m1,m2);T=sum(lens)
    reach={0}
    for z in lens:reach|={r+z for r in tuple(reach)}
    return T if any(abs(T-2*r)<=1 for r in reach) else T-1

def ordered_components(m1,m2):
    n=2*len(m1)
    p=[None]*n;q=[None]*n
    for a,b in m1:p[a]=b;p[b]=a
    for a,b in m2:q[a]=b;q[b]=a
    seen=set();components=[]
    for s in range(n):
        if s in seen:continue
        vertices=[];z=s
        while z not in seen:
            vertices.extend([z,p[z]])
            seen.add(z);seen.add(p[z]);z=q[p[z]]
        size=len(vertices)//2
        red=[(vertices[2*j],vertices[2*j+1]) for j in range(size)]
        blue=[(vertices[2*j+1],vertices[(2*j+2)%(2*size)]) for j in range(size)]
        components.append((size,red,blue))
    return components

def construct(m1,m2):
    """Return complete allocation (item masks) with predicted optimal EFX welfare."""
    comp=ordered_components(m1,m2)
    T=sum(c[0] for c in comp)
    reach={0:((),())}
    for j,(size,_,_) in enumerate(comp):
        nxt=dict(reach)
        for v,choice in reach.items():
            if v+size not in nxt:
                nxt[v+size]=(choice[0]+(j,),choice[1])
        reach=nxt
    winners=[r for r in reach if abs(T-2*r)<=1]
    e1=[];e2=[]
    if winners:
        assign1=set(reach[winners[0]][0])
        for j,(size,red,blue) in enumerate(comp):
            (e1 if j in assign1 else e2).extend(red if j in assign1 else blue)
    else:
        jbig=max(range(len(comp)), key=lambda j:comp[j][0])
        r=b=0
        for j,(size,red,blue) in enumerate(comp):
            if j==jbig:continue
            if r<=b:e1.extend(red);r+=size
            else:e2.extend(blue);b+=size
        size,red,blue=comp[jbig]
        x=next(x for x in range(size) if abs(r+x-(b+size-1-x))<=1)
        e1.extend(red[:x]);e2.extend(blue[x:size-1]);r+=x;b+=size-1-x
    mask1=mask2=0
    for a,b in e1:mask1|=(1<<a)|(1<<b)
    for a,b in e2:mask2|=(1<<a)|(1<<b)
    assert mask1&mask2==0
    unassigned=((1<<(2*T))-1)^(mask1|mask2)
    assert unassigned.bit_count() in (0,2)
    if unassigned:
        if len(e1)<=len(e2):mask1|=unassigned
        else:mask2|=unassigned
    assert mask1|mask2==(1<<(2*T))-1
    return mask1,mask2

def vals_for_matching(m, size):
    v=[0]*(1<<size)
    pairs=[(1<<a)|(1<<b) for a,b in m]
    for s in range(1<<size):v[s]=sum((s&e)==e for e in pairs)
    return v

def exact_efx(m1,m2):
    n=2*len(m1);allmask=(1<<n)-1
    va=vals_for_matching(m1,n);vb=vals_for_matching(m2,n)
    opt=-1
    for s in range(1<<n):
        t=allmask^s
        a=va[s];b=vb[t]
        if any(a<va[t^(1<<g)] for g in range(n) if t>>g&1):continue
        if any(b<vb[s^(1<<g)] for g in range(n) if s>>g&1):continue
        opt=max(opt,a+b)
    return opt

def main():
    total=0;split=Counter()
    for n in (2,4,6,8):
        ms=matchings(tuple(range(n)))
        for a in ms:
            for b in ms:
                guess=predicted(a,b)
                actual=exact_efx(a,b)
                if actual!=guess:
                    raise AssertionError((n,a,b,cycles(a,b),guess,actual))
                x,y=construct(a,b)
                va=vals_for_matching(a,n);vb=vals_for_matching(b,n)
                assert va[x]+vb[y]==guess, (n,a,b,x,y,guess,va[x]+vb[y])
                assert all(va[x]>=va[y^(1<<g)] for g in range(n) if (y>>g)&1)
                assert all(vb[y]>=vb[x^(1<<g)] for g in range(n) if (x>>g)&1)
                split[(n,tuple(cycles(a,b)),actual)]+=1
                total+=1
        print(f'goods={n}; matching pairs={len(ms)**2}; PASS',flush=True)
    print('TOTAL_CASES=',total)
    for key,v in sorted(split.items()):print('cycle-profile',key,'multiplicity',v)

if __name__=='__main__':main()
