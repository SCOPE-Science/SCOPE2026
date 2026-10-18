"""Independent orbit-of-Hasse-edge enumeration for generalized matching complexes of tetrahedra."""
from collections import Counter
from itertools import permutations
from gm_character import face_bits, permute_face, cycle_type, perm_cycles


def orbit_conflict_data(boundary,p):
    faces,E=face_bits(boundary)
    cycles=perm_cycles(E,p)
    orbits=[]
    for cy in cycles:
        used=[]
        for i in cy:
            used.extend(E[i])
        if len(set(used))==len(used):
            orbits.append((len(cy),tuple(used)))
    conflict=[]
    for i,(size,verts) in enumerate(orbits):
        conflict.append(sum(1<<j for j,(size2,verts2) in enumerate(orbits) if set(verts)&set(verts2)))
    return E,cycles,orbits,conflict

def signed_sum_by_orbit_count(conflict):
    n=len(conflict)
    terms=Counter()
    def rec(avail,k):
        if not avail:terms[k]+=1;return
        low=avail&-avail; i=low.bit_length()-1
        rec(avail^low,k)
        rec(avail&~conflict[i],k+1)
    rec((1<<n)-1,0)
    return terms

def run(boundary):
    chars={}
    for p in permutations(range(4)):
        typ=cycle_type(p)
        E,cycles,orbits,conflict=orbit_conflict_data(boundary,p)
        terms=signed_sum_by_orbit_count(conflict)
        val=-sum((-1)**k*count for k,count in terms.items())
        if typ in chars:assert chars[typ][0]==val
        else:chars[typ]=(val,len(cycles),len(orbits),[terms.get(k,0) for k in range(max(terms)+1)])
    print('boundary',boundary)
    for typ,(val,total,admissible,terms) in sorted(chars.items(),reverse=True):
        print(typ,'trace',val,'edge_orbits',total,'allowable_orbits',admissible,'independent_orbit_sets_by_size',terms)
    return {typ:val for typ,(val,*_) in chars.items()}

if __name__=='__main__':
    a=run(False);b=run(True)
    assert a==b
    assert [a[t] for t in [(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]]==[39,1,-5,0,3]
    chars={'trivial':[1,1,1,1,1],'sign':[1,-1,1,1,-1],
    'standard':[3,1,-1,0,-1],'two_two':[2,0,2,-1,0],
    'twisted_standard':[3,-1,-1,0,1]}
    sizes=[1,6,3,8,6];vals=[39,1,-5,0,3]
    mults={name:sum(sz*x*y for sz,x,y in zip(sizes,vals,row))//24 for name,row in chars.items()}
    print('S4 irreducible multiplicities',mults)
    assert mults=={'trivial':2,'sign':0,'standard':5,'two_two':2,'twisted_standard':6}
