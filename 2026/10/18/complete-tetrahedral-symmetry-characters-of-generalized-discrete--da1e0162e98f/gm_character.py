#!/usr/bin/env python3
"""Exact simplicial signed-Lefschetz census for Hasse-matching complexes of a labeled tetrahedron.
Underlying faces are nonempty subsets; the empty matching is included only for reduced augmentation.
"""
from itertools import permutations
from collections import Counter
from math import factorial


def face_bits(boundary):
    faces=tuple(x for x in range(1,16) if not (boundary and x==15))
    pairs=tuple((s,t) for s in faces for t in faces if (s&t)==s and t.bit_count()==s.bit_count()+1)
    return faces,pairs

def matchings(faces,pairs):
    # Enumerates each Hasse matching once by the first free incident edge choice.
    conflict=[]
    for a,b in pairs:
        conflict.append(sum(1<<i for i,(c,d) in enumerate(pairs) if a in (c,d) or b in (c,d)))
    out=[]
    def visit(available,selected):
        if not available:
            out.append(selected);return
        bit=available & -available
        i=bit.bit_length()-1
        visit(available ^ bit,selected)
        visit(available & ~conflict[i],selected | bit)
    visit((1<<len(pairs))-1,0)
    return out

def permute_face(s,p):
    return sum(1<<p[v] for v in range(4) if s>>v&1)

def cycle_type(p):
    seen=set(); lens=[]
    for i in range(4):
        if i not in seen:
            j=i;k=0
            while j not in seen:
                seen.add(j);k+=1;j=p[j]
            lens.append(k)
    return tuple(sorted(lens,reverse=True))

def perm_cycles(pairs,p):
    ix={e:i for i,e in enumerate(pairs)}
    perm=[ix[(permute_face(a,p),permute_face(b,p))] for a,b in pairs]
    seen=set();cycles=[]
    for i in range(len(pairs)):
        if i not in seen:
            j=i;cy=[]
            while j not in seen:
                seen.add(j);cy.append(j);j=perm[j]
            cycles.append(tuple(cy))
    return cycles

def traces_on_fixed_matchings(M,cycles):
    # A simplex fixed setwise iff it is a union of full vertex-orbits.
    orbits=[sum(1<<i for i in cy) for cy in cycles]
    signs=[-1 if (len(cy)-1)&1 else 1 for cy in cycles]
    lut={orb:i for i,orb in enumerate(orbits)}
    reduced=-1;f=Counter()
    # All matchings including empty; each union of orbits automatically fixed.
    for selected in M:
        if not selected:continue
        rem=selected;sgn=1;valid=True
        for j,orb in enumerate(orbits):
            if rem & orb:
                if rem & orb != orb:valid=False;break
                sgn*=signs[j]
                rem^=orb
        if valid:
            size=selected.bit_count()
            f[size-1]+=sgn
            reduced+=(-1)**(size-1)*sgn
    return reduced,dict(sorted(f.items()))

def run(boundary):
    faces,pairs=face_bits(boundary)
    M=matchings(faces,pairs)
    f=Counter(x.bit_count()-1 for x in M if x)
    print('boundary',boundary,'Hasse_faces',len(faces),'Hasse_edges',len(pairs),'matching_faces',len(M)-1,'f_vector',tuple(f[k] for k in range(max(f)+1)))
    classes={}
    for p in permutations(range(4)):
        ct=cycle_type(p)
        cycles=perm_cycles(pairs,p)
        trace,dim_f=traces_on_fixed_matchings(M,cycles)
        if ct in classes:assert classes[ct][0]==trace, (ct,classes[ct],trace)
        else:classes[ct]=(trace,dim_f,p)
    for ct,(tr,ff,p) in sorted(classes.items(),reverse=True):print('class',ct,'character',tr,'representative',p,'signed_fixed',ff)
    return {ct:v[0] for ct,v in classes.items()}
if __name__=='__main__':
    b=run(False);c=run(True)
    print('differences',[(k,b[k]-c[k]) for k in sorted(b,reverse=True)])
