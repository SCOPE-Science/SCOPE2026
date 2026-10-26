#!/usr/bin/env python3
"""Independent exact enumeration of regular equivariant endomorphism image types."""
from itertools import product
from collections import Counter
from math import comb

def elements(moduli):
    return list(product(*[range(d) for d in moduli]))

def add(a,b,moduli):
    return tuple((x+y)%d for x,y,d in zip(a,b,moduli))

def subgroups(moduli):
    G=elements(moduli)
    zero=tuple(0 for _ in moduli)
    got={frozenset([zero])}
    for _ in range(len(G)):
        old=len(got)
        for H in list(got):
            for x in G:
                K={add(h,tuple((k*y)%d for y,d in zip(x,moduli)),moduli)
                   for h in H for k in range(len(G))}
                if len(K)>len(H): got.add(frozenset(K))
        if len(got)==old: break
    return sorted(got,key=lambda H:(-len(H),sorted(H)))

def build(moduli,multiplicities):
    G=elements(moduli); Hs=subgroups(moduli); zero=tuple(0 for _ in moduli)
    orbits=[]; all_points=[]; action={}; points_by_orbit=[]
    for H in Hs:
        for _ in range(multiplicities.get(H,0)):
            i=len(orbits); orbits.append(H)
            cs={frozenset(add(g,h,moduli) for h in H) for g in G}
            reps=sorted(cs,key=lambda x: sorted(x))
            ps=[(i,j) for j in range(len(reps))]; points_by_orbit.append(ps); all_points.extend(ps)
            for g in G:
                for j,C in enumerate(reps):
                    new=frozenset(add(g,c,moduli) for c in C)
                    action[(g,ps[j])]=(i,reps.index(new))
    # All images for each source orbit representative, independently constructed via group action.
    choices=[]
    for i,H in enumerate(orbits):
        options=[]
        for y in all_points:
            if all(action[(h,y)]==y for h in H):
                mp={action[(g,(i,0))]:action[(g,y)] for g in G}
                if len(mp)==len(points_by_orbit[i]):options.append(mp)
        choices.append(options)
    if not choices:return Hs,orbits,all_points,[()],[]
    maps=[]
    for selections in product(*choices):
        f={}
        for mp in selections:f.update(mp)
        maps.append(tuple(all_points.index(f[x]) for x in all_points))
    return Hs,orbits,all_points,maps,choices

def theory(moduli,multiplicities):
    Hs=subgroups(moduli); G=elements(moduli)
    def block(H,r):
        m=multiplicities.get(H,0)
        B=sum((len(G)//len(K))*r[K] for K in Hs if len(K)>len(H) and H.issubset(K))
        w=len(G)//len(H); k=r[H]
        return comb(m,k)*sum((-1)**(k-j)*comb(k,j)*(B+w*j)**m for j in range(k+1))
    ans=Counter()
    for rv in product(*[range(multiplicities.get(H,0)+1) for H in Hs]):
        r=dict(zip(Hs,rv));v=1
        for H in Hs:v*=block(H,r)
        assert v>=0
        if v:ans[rv]=v
    return ans

def trial(moduli,raw_counts):
    Hs=subgroups(moduli);G=elements(moduli)
    mult={H:raw_counts.get(len(H),0) for H in Hs} if all(isinstance(k,int) for k in raw_counts) else raw_counts
    Hs,orbits,points,maps,_=build(moduli,mult)
    M=len(points); assert M and len(maps)<=10000
    # Independent test: regular if and only if there exists an explicitly enumerated equivariant inverse witness.
    bucket=Counter(); phi=[]
    for f in maps:
        image=set(f)
        r=tuple(len({points[y][0] for y in image if orbits[points[y][0]]==H}) for H in Hs)
        phi.append((f,r))
    for f,r in phi:
        regular=False
        for g,_ in phi:
            if all(f[g[f[x]]]==f[x] for x in range(M)):
                regular=True;break
        if regular:bucket[r]+=1
    expected=theory(moduli,mult)
    assert bucket==expected,(moduli,mult,bucket,expected)
    expected_all=1
    for H in Hs:
        available=sum((len(G)//len(K))*mult.get(K,0) for K in Hs if H.issubset(K))
        expected_all*=available**mult.get(H,0)
    assert len(maps)==expected_all
    print('PASS',moduli,'orbit_multiplicities',[mult.get(H,0) for H in Hs], 'points',M,'endomorphisms',len(maps),'regular',sum(bucket.values()),'profiles',len(bucket))
    return len(maps),sum(bucket.values())

if __name__=='__main__':
    tally=0;reg=0
    cases=[((2,),{2:2,1:1}),((2,),{2:2,1:2}),((4,),{4:1,2:1,1:1}),((2,2),{4:2,2:1,1:1})]
    for mod,m in cases:
        a,b=trial(mod,m);tally+=a;reg+=b
    print('ALL_REGULAR_EQUIVARIANT_ORBIT_PROFILE_CHECKS_PASSED', 'cases='+str(len(cases)),'maps='+str(tally),'regular='+str(reg))
