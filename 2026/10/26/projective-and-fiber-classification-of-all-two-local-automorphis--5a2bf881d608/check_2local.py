"""Standalone exact checks for the finite-Heisenberg 2-local automorphism census.

Run: python3 check_2local.py
This verifies 2-locality independently through automorphism orbits on pairs.
"""
from itertools import permutations, product
from math import factorial
import random


def elements(q):
    return list(product(range(q), repeat=3))


def all_automorphisms(q):
    # Prime-field arithmetic; called below only for q=2,3.
    pts = elements(q)
    idx = {x: i for i,x in enumerate(pts)}
    maps = []
    for a,b,c,d in product(range(q), repeat=4):
        det = (a*d-b*c)%q
        if not det:
            continue
        for u,v in product(range(q), repeat=2):
            vals = []
            for x,y,z in pts:
                vals.append(idx[((a*x+b*y)%q,(c*x+d*y)%q,
                                 (u*x+v*y+det*z)%q)])
            assert len(set(vals)) == q**3
            maps.append(tuple(vals))
    assert len(maps) == q*q*(q*q-1)*(q*q-q)
    return pts, maps


def pair_orbits(size, automorphisms):
    orbit = [-1]*(size*size)
    num = 0
    for key in range(size*size):
        if orbit[key] != -1:
            continue
        i,j = divmod(key,size)
        images = {M[i]*size+M[j] for M in automorphisms}
        assert all(orbit[k] in (-1,num) for k in images)
        for k in images:
            orbit[k] = num
        num += 1
    assert -1 not in orbit
    return orbit, num


def projective_lines(q):
    # Representative vectors (1,m) for all m, followed by (0,1).
    return [(1,t) for t in range(q)]+[(0,1)]


def canonical(v,q):
    x,y=v
    if x:
        lam=x
        rep=(1,(y*pow(x,-1,q))%q)
    else:
        lam=y
        rep=(0,1)
    assert lam != 0
    return rep,lam


def candidate_map(q, proj, lifts, fibers, center):
    # proj permutes ordered projective representatives; lifts are nonzero scalars.
    pts=elements(q)
    reps=projective_lines(q)
    ridx={r:i for i,r in enumerate(reps)}
    idx={x:i for i,x in enumerate(pts)}
    out=[]
    for x,y,z in pts:
        if x==y==0:
            out.append(idx[(0,0,center*z%q)])
        else:
            rep,lam=canonical((x,y),q)
            i=ridx[rep]
            R=reps[proj[i]]
            u=(lam*lifts[i]*R[0])%q
            v=(lam*lifts[i]*R[1])%q
            zz=(lam*fibers[i][(z*pow(lam,-1,q))%q])%q
            out.append(idx[(u,v,zz)])
    assert len(set(out)) == q**3
    return tuple(out)


def preserves_pair_orbits(mapping,orbit):
    size=len(mapping)
    for i in range(size):
        for j in range(size):
            if orbit[i*size+j] != orbit[mapping[i]*size+mapping[j]]:
                return False
    return True


def main():
    rng=random.Random(16160205187)
    q=2
    pts,aut=all_automorphisms(q)
    orb,norbits=pair_orbits(q**3,aut)
    all_two_local=[]
    for perm in permutations(range(q**3)):
        if preserves_pair_orbits(perm,orb):
            all_two_local.append(perm)
    predicted=set()
    for proj in permutations(range(q+1)):
        for lifts in product(range(1,q),repeat=q+1):
            for fs in product(list(permutations(range(q))),repeat=q+1):
                for c in range(1,q):
                    predicted.add(candidate_map(q,proj,lifts,fs,c))
    assert set(all_two_local)==predicted
    assert len(all_two_local)==48
    assert len(aut)==24
    print('q=2: exactly %s 2-local maps among 8!=40320 bijections; 24 automorphisms; %s pair-orbits' % (len(all_two_local),norbits))

    q=3
    pts,aut=all_automorphisms(q)
    orb,norbits=pair_orbits(q**3,aut)
    assert len(aut)==432
    for _ in range(120):
        proj=tuple(rng.sample(range(q+1),q+1))
        lifts=tuple(rng.randrange(1,q) for i in range(q+1))
        fs=tuple(tuple(rng.sample(range(q),q)) for i in range(q+1))
        center=rng.randrange(1,q)
        m=candidate_map(q,proj,lifts,fs,center)
        assert preserves_pair_orbits(m,orb)
    predicted_count=(q-1)**(q+2)*factorial(q+1)*factorial(q)**(q+1)
    assert predicted_count==995328
    print('q=3: 120 random classification maps preserve all 729 ordered-pair orbit conditions; %s pair-orbits; formula yields %s maps; 432 automorphisms' % (norbits,predicted_count))
    # Check a genuinely non-prime field (characteristic two, order four).
    q=4
    def mul(a,b):
        raw=0
        for j in range(2):
            if (b>>j)&1:
                raw ^= a<<j
        if raw&4:
            raw ^= 0b111 # x^2 = x+1
        return raw
    inv={a:next(b for b in range(1,4) if mul(a,b)==1) for a in range(1,4)}
    pts=elements(q)
    idx={x:i for i,x in enumerate(pts)}
    aut=[]
    for a,b,c,d in product(range(q),repeat=4):
        det=mul(a,d)^mul(b,c)
        if det==0:continue
        for u,v in product(range(q),repeat=2):
            aut.append(tuple(idx[(mul(a,x)^mul(b,y),mul(c,x)^mul(d,y),
                                   mul(u,x)^mul(v,y)^mul(det,z))] for x,y,z in pts))
    assert len(aut)==2880
    orb,norbits=pair_orbits(q**3,aut)
    reps=projective_lines(q)
    ridx={r:i for i,r in enumerate(reps)}
    def gf4_candidate(proj,lifts,fibers,center):
        out=[]
        for x,y,z in pts:
            if x==y==0:
                out.append(idx[(0,0,mul(center,z))]);continue
            if x:
                lam=x
                rep=(1,mul(y,inv[x]))
            else:
                lam=y
                rep=(0,1)
            i=ridx[rep]
            R=reps[proj[i]]
            m=mul(lam,lifts[i])
            out.append(idx[(mul(m,R[0]),mul(m,R[1]),
                            mul(lam,fibers[i][mul(z,inv[lam])]) )])
        assert len(set(out))==q**3
        return tuple(out)
    for _ in range(100):
        proj=tuple(rng.sample(range(q+1),q+1))
        lifts=tuple(rng.randrange(1,q) for i in range(q+1))
        fs=tuple(tuple(rng.sample(range(q),q)) for i in range(q+1))
        center=rng.randrange(1,q)
        m=gf4_candidate(proj,lifts,fs,center)
        assert preserves_pair_orbits(m,orb)
    print('q=4: 100 random classification maps preserve all 4096 pair orbit conditions; %s pair-orbits; 2880 automorphisms' % norbits)
    print('HEISENBERG_TWO_LOCAL_OK')


if __name__=='__main__':
    main()
