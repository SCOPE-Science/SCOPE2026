#!/usr/bin/env python3
"""Independent finite confirmation of the three-pebble extension lemma for symmetric 2-designs."""
from collections import Counter

def cyclic(v,d):
    return (v, [frozenset((x+a)%v for a in d) for x in range(v)])

CASES = {
    'Fano_7_3_1': cyclic(7, (0,1,3)),
    'complement_Fano_7_4_2': cyclic(7, (2,4,5,6)),
    'biplane_11_5_2': cyclic(11, (0,2,3,4,8)),
    'projective_13_4_1': cyclic(13, (0,1,3,9)),
    'biplane_37_9_2': cyclic(37, (1,7,9,10,12,16,26,33,34)),
}

def validate(v,blocks):
    assert len(blocks)==v and len(set(blocks))==v
    k=len(blocks[0]); assert 2<=k<=v-2
    assert all(len(b)==k for b in blocks)
    reps=[sum(p in b for b in blocks) for p in range(v)]
    assert reps == [k]*v
    lam=sum(0 in b and 1 in b for b in blocks)
    assert lam>=1 and (v-1)*lam==k*(k-1)
    assert all(sum(x in b and y in b for b in blocks)==lam for x in range(v) for y in range(x+1,v))
    assert all(len(blocks[i]&blocks[j])==lam for i in range(v) for j in range(i+1,v))
    return (v,k,lam)

def type_of(v,blocks,x,y):
    sx='P' if x<v else 'B'; sy='P' if y<v else 'B'
    if x==y:return (sx,sy,'=')
    if sx==sy:return (sx,sy,'different')
    p=x if sx=='P' else y
    b=(y-v) if sy=='B' else (x-v)
    return (sx,sy,'I' if p in blocks[b] else 'N')

def profiles(v,blocks):
    n=2*v
    keys={}
    for x in range(n):
      for y in range(n):
        a=type_of(v,blocks,x,y)
        ext=frozenset((type_of(v,blocks,z,x),type_of(v,blocks,z,y)) for z in range(n))
        if a in keys:
          assert keys[a]==ext, ('nonuniform',v,a)
        else: keys[a]=ext
    return keys

def main():
    reference=None
    for name,(v,blocks) in CASES.items():
        params=validate(v,blocks)
        spectra=profiles(v,blocks)
        if reference is None:reference=spectra
        assert reference==spectra,('cross-design mismatch',name)
        print(name,'v,k,lambda=',params,'ordered_pair_classes=',len(spectra),'extension_patterns=',sum(map(len,spectra.values())))

    # A deliberately excluded symmetric 2-(4,3,2) design:
    v=4;blocks=[frozenset(set(range(4))-{i}) for i in range(4)]
    assert len(blocks)==v and (v-len(blocks[0]))==1
    bad=profiles(v,blocks)
    assert bad!=reference
    print('excluded_trivial_design_4_3_2','different_extension_spectrum=True')

    # Exact separation: girth-six Fano incidence graph versus complement's four-cycle.
    for name in ('Fano_7_3_1','complement_Fano_7_4_2'):
        v,blocks=CASES[name]
        c4=sum(1 for a in range(v) for b in range(a+1,v) for i in range(v) for j in range(i+1,v) if a in blocks[i] and b in blocks[i] and a in blocks[j] and b in blocks[j])
        assert (c4>0)==(name=='complement_Fano_7_4_2')
        print(name,'incidence_four_cycles=',c4)
    print('PASS: uniform 3-pebble extension profiles and strict four-variable witness')

if __name__=="__main__":
    main()
