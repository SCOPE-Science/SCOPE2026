#!/usr/bin/env python3
"""Exact finite certificates for a cyclic Lovasz neighborhood-complex family.
All computations use sets, integer offsets and mod-two parity; no extra modules.
Usage: python3 verify.py collapse_templates.json
"""
import collections
import itertools
import json
import sys

TEMPLATES = json.load(open(sys.argv[1] if len(sys.argv)>1 else 'collapse_templates.json', encoding='utf-8'))
BASE = (0,1,2,3,5,6,7,8)


def normalized(face):
    return tuple(sorted(x-min(face) for x in face))


def orbit_types():
    out = set()
    for k in range(1,9):
        out.update(normalized(c) for c in itertools.combinations(BASE,k))
    return out


def local_face(face):
    # Every face containing 0 has a witnessing neighborhood center at
    # one of the eight offsets +/-1,...,+/-4. All possible new vertices
    # lie in [-8,8], distinct residues for any n>=17.
    return any(all(1 <= abs(x-c) <= 4 for x in face)
               for c in (-4,-3,-2,-1,1,2,3,4))


def local_cofaces(face):
    return [normalized((*face,x)) for x in range(-8,9)
            if x not in face and local_face((*face,x))]


def cyclic_canon(f,n):
    ff=sorted(f)
    if len(ff)==1:return (0,)
    gaps=[(ff[(j+1)%len(ff)]-ff[j])%n for j in range(len(ff))]
    cuts=[j for j,g in enumerate(gaps) if g>8]
    assert len(cuts)==1,(n,f,gaps)
    first=ff[(cuts[0]+1)%len(ff)]
    return tuple(sorted((v-first)%n for v in ff))

def prisms(n):
    return [tuple(sorted(((i % n), ((i+8) % n),
                  *(((i+j+4*bit) % n) for j,bit in enumerate(bits,1)))))
            for i in range(n) for bits in itertools.product((0,1),repeat=3)]


def sigma(n,i):
    return {tuple(sorted(((i+j+4*bit) % n for j,bit in enumerate(bits))))
            for bits in itertools.product((0,1),repeat=4)}


def full_faces(n):
    faces=set()
    for i in range(n):
        facet=tuple(sorted(((i+t)%n for t in (-4,-3,-2,-1,1,2,3,4))))
        for k in range(1,9):faces.update(itertools.combinations(facet,k))
    return faces


def all_subfaces(facets):
    faces=set()
    for facet in facets:
        for k in range(1,len(facet)+1):
            faces.update(itertools.combinations(facet,k))
    return faces


def verify_symbolic():
    types=orbit_types()
    assert len(types)==170
    core={cyclic_canon(c,17) for c in all_subfaces(prisms(17))}
    assert len(core)==54 and core <= types
    remaining=set(types)
    assert len(TEMPLATES)==58
    for k,t in enumerate(TEMPLATES):
        a=tuple(t['free']); b=tuple(t['coface'])
        assert a in remaining-core and b in remaining-core,(k,a,b)
        assert len(b)==len(a)+1
        assert [c for c in local_cofaces(a) if c in remaining]==[b], (k,a,b)
        remaining.remove(a);remaining.remove(b)
    assert remaining==core
    print('LOCAL_ORBIT_CERTIFICATE_OK types=170 core=54 collapse_orbits=58')


def verify_sample(n):
    total=full_faces(n); top=prisms(n)
    assert len(top)==8*n and len(set(top))==8*n
    core=all_subfaces(top)
    assert core <=total
    assert len(total)==170*n and len(core)==54*n,(n,len(total),len(core))
    count=collections.Counter(map(len,core))
    assert [count[k] for k in range(1,6)]==[n,7*n,18*n,20*n,8*n]
    types={tuple(sorted(((v-min(f))%n for v in f))) for f in total}
    # Normalize using unique wrap gap rather than literal minimum.
    def canon(f):
        ff=sorted(f)
        if len(ff)==1:return (0,)
        gaps=[(ff[(j+1)%len(ff)]-ff[j])%n for j in range(len(ff))]
        cuts=[j for j,g in enumerate(gaps) if g>8]
        assert len(cuts)==1,(n,f,gaps)
        first=ff[(cuts[0]+1)%len(ff)]
        return tuple(sorted((v-first)%n for v in ff))
    assert {canon(s) for s in total}==orbit_types()
    assert {canon(s) for s in core}=={cyclic_canon(s,17) for s in all_subfaces(prisms(17))}
    S=set(total)
    for t in TEMPLATES:
        a=tuple(t['free']); b=tuple(t['coface'])
        for i in range(n):
            small=tuple(sorted((i+x)%n for x in a))
            options=[w for w in range(-8,9) if w not in a and local_face((*a,w)) and normalized((*a,w))==b]
            assert len(options)==1,(a,b,options)
            delta=min((*a,options[0]))
            large=tuple(sorted((i+delta+x)%n for x in b))
            assert small in S and large in S
            # Check every genuine coface, not just orbit types.
            actual=[tuple(sorted((*small,v))) for v in range(n)
                    if v not in small and tuple(sorted((*small,v))) in S]
            assert actual==[large],(n,i,small,large,actual)
            S.remove(small);S.remove(large)
    assert S==core,(n,len(S^core))
    # closed 4-pseudomanifold property by checking every 3-face
    incidence=collections.Counter(t for f in top for t in itertools.combinations(f,4))
    assert all(v==2 for v in incidence.values())
    print('FINITE_REPLAY_OK',n,'simplex_counts',len(total),len(core),'pairs',58*n)


def parity(chain,sub_size):
    out=set()
    for s in chain:
        for face in itertools.combinations(s,sub_size):
            if face in out:out.remove(face)
            else:out.add(face)
    return out


def verify_cup(n):
    top=set(prisms(n));assert len(top)==8*n
    assert not parity(top,4)
    # alpha is the cut/winding one-cocycle on edges of K.
    alpha=lambda a,b: int(b-a>8)
    for s in full_faces(n):
        if len(s)==3:
            a,b,c=s
            assert (alpha(a,b)^alpha(a,c)^alpha(b,c))==0
    cap=set()
    for f in top:
        if alpha(f[0],f[1]):
            r=f[1:]
            if r in cap:cap.remove(r)
            else:cap.add(r)
    assert cap==sigma(n,n-8),(n,len(cap))
    # Dual cycle in the 4-facet adjacency graph detects Sigma_0.
    # A_i and B_i differ in one vertex; A_i and B_(i+1)
    # likewise differ in one vertex. Their shared tetrahedra form a
    # degree-two dual loop. Pairing with Sigma_0 is one.
    detected=set()
    def xor(face):
        f=tuple(sorted(face))
        if f in detected:detected.remove(f)
        else:detected.add(f)
    for i in range(n):
        A={(i+j)%n for j in (0,1,2,3,8)}
        B={(i+j)%n for j in (0,1,2,7,8)}
        nextB={(i+j)%n for j in (1,2,3,8,9)}
        assert tuple(sorted(A)) in top and tuple(sorted(B)) in top
        assert tuple(sorted(nextB)) in top
        assert len(A&B)==len(A&nextB)==4
        xor(A&B);xor(A&nextB)
    # All tetrahedra involved are distinct as needed for parity
    # (any repeats would cancel). Their indicator is a 3-cocycle:
    # every top facet is hit an even number of times.
    for f in top:
        assert sum(1 for t in itertools.combinations(f,4) if t in detected)%2==0
    assert len(detected & sigma(n,0))%2==1,(n,detected & sigma(n,0))
    # Hence Sigma_0 is not a 4-boundary and alpha cap Gamma !=0.
    # Over F2, UCT supplies beta in H^3 with beta(Sigma_0)=1;
    # alpha cup beta evaluates 1 on Gamma.
    print('CUP_NONZERO_OK',n,'4cycle',len(top),'cap_sphere_facets',len(cap),
          'dual_tetrahedra',len(detected))


if __name__=='__main__':
    verify_symbolic()
    for n in (17,18,19,23,32):
        verify_sample(n)
        verify_cup(n)
    print('VERIFY_OK')
