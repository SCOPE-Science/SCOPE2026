#!/usr/bin/env python3
"""Exact binary-polynomial and projective orbit census of smooth plane-cubic pencils.

Uses only the Python standard library. All arithmetic is over GF(2).
"""
import collections
import itertools
import json


def monomials(deg):
    return [(i, j, deg-i-j) for i in range(deg+1) for j in range(deg+1-i)]

MON3=monomials(3)
IDX2={e:i for i,e in enumerate(monomials(2))}
IDX4={e:i for i,e in enumerate(monomials(4))}
MON2=monomials(2)


def bitrank(rows):
    pivots={}
    for v in rows:
        while v:
            h=v.bit_length()-1
            if h not in pivots:
                pivots[h]=v
                break
            v^=pivots[h]
    return len(pivots)


def is_smooth(mask):
    gradients=[0,0,0]
    for i,e in enumerate(MON3):
        if mask>>i&1:
            for j in range(3):
                if e[j]%2:
                    d=tuple(e[k]-(k==j) for k in range(3))
                    gradients[j]^=1<<IDX2[d]
    rows=[]
    for g in gradients:
        for d in MON2:
            row=0
            for i,e in enumerate(MON2):
                if g>>i&1:
                    row^=1<<IDX4[tuple(e[k]+d[k] for k in range(3))]
            rows.append(row)
    return bitrank(rows)==15


def linear_maps():
    mats=[]
    for rows in itertools.product(range(1,8),repeat=3):
        images={tuple((v&r).bit_count()%2 for r in rows) for v in range(8)}
        if len(images)==8:
            mats.append(rows)
    assert len(mats)==168
    return mats


def mul(P,Q):
    out={}
    for x in P:
        for y in Q:
            z=tuple(a+b for a,b in zip(x,y))
            out[z]=out.get(z,0)^1
    return {x for x,v in out.items() if v}


def group_form_actions():
    res=[]
    for mat in linear_maps():
        im=[]
        for exp in MON3:
            P={(0,0,0)}
            for powr,r in zip(exp,mat):
                lin={tuple(int(k==i) for k in range(3)) for i in range(3) if r>>i&1}
                for _ in range(powr):P=mul(P,lin)
            im.append(sum(1<<MON3.index(e) for e in P))
        actions=[0]*1024
        for f in range(1,1024):
            b=f&-f
            actions[f]=actions[f^b]^im[b.bit_length()-1]
        assert len(set(actions))==1024
        res.append(actions)
    return res


def rational_points():
    return [p for p in itertools.product((0,1),repeat=3) if any(p)]


def point_masks():
    return [sum(1<<i for i,e in enumerate(MON3)
                if all(not e[j] or p[j] for j in range(3)))
            for p in rational_points()]


def run():
    sm={f for f in range(1,1024) if is_smooth(f)}
    assert len(sm)==336
    pencils={tuple(sorted((a,b,a^b))) for a in sm for b in sm if a<b and a^b in sm}
    assert len(pencils)==5544
    masks=point_masks()
    base={}
    extensions={}
    for p in pencils:
        a,b,c=p
        base[p]=sum(all((f&mask).bit_count()%2==0 for f in (a,b)) for mask in masks)
        candidates=sum(x not in p and all(x^y in sm for y in p) for x in sm)
        assert candidates%4==0
        extensions[p]=candidates//4
    bi=collections.Counter((extensions[p],base[p]) for p in pencils)
    assert sum(k*n for (k,b),n in bi.items())==7*864
    assert max(extensions.values())==3
    actions=group_form_actions()
    unseen=set(pencils)
    orbits=[]
    for p in sorted(pencils):
        if p not in unseen:continue
        orbit={tuple(sorted(T[f] for f in p)) for T in actions}
        assert len(orbit)<=168 and orbit<=unseen
        unseen-=orbit
        assert {extensions[q] for q in orbit}=={extensions[p]}
        assert {base[q] for q in orbit}=={base[p]}
        size=len(orbit)
        assert 168%size==0
        orbits.append(dict(representative=list(p),size=size,stabilizer=168//size,
                           extensions=extensions[p],rational_base_points=base[p]))
    assert not unseen and len(orbits)==37
    dist=collections.Counter(168//r['size'] for r in orbits)
    fixed_by_order=collections.Counter()
    for mat,T in zip(linear_maps(),actions):
        images=[tuple((v&r).bit_count()%2 for r in mat) for v in range(8)]
        perm=[sum(u[i]<<i for i in range(3)) for u in images]
        power=list(range(8))
        order=0
        while True:
            order+=1
            power=[perm[power[v]] for v in range(8)]
            if power==list(range(8)):break
            assert order<=7
        nfixed=sum(tuple(sorted(T[f] for f in p))==p for p in pencils)
        fixed_by_order[order,nfixed]+=1
    assert sum(n*nfixed for (order,nfixed),n in fixed_by_order.items())==168*37
    assert fixed_by_order=={(1,5544):1,(2,8):21,(3,6):56,(4,4):42,(7,0):48}
    output={
        'monomial_order':['X^%dY^%dZ^%d'%e for e in MON3],
        'smooth_forms':len(sm),
        'all_smooth_pencils':len(pencils),
        'extendability_by_rational_base':[
          {'extensions':k,'rational_base_points':b,'pencils':bi[k,b],
           'projective_orbits':sum(r['extensions']==k and r['rational_base_points']==b for r in orbits)}
          for k,b in sorted(bi)],
        'extension_distribution':[{ 'extensions':k, 'pencils':sum(n for (l,b),n in bi.items() if l==k)}
          for k in sorted({k for k,b in bi})],
        'total_smooth_nets':sum(extensions.values())//7,
        'projective_orbits':len(orbits),
        'orbit_stabilizers':[{ 'stabilizer_order':k,'orbits':dist[k]} for k in sorted(dist)],
        'burnside': [{'element_order':order,'fixed_pencils':nfixed,'elements':n} for (order,nfixed),n in sorted(fixed_by_order.items())],
        'orbits':orbits
    }
    print(json.dumps(output,sort_keys=True,separators=(',',':')))

if __name__=='__main__':run()
