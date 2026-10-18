"""Exact integer certificate for primitive zero-sums in the radius-two lattice disk.
Run: python3 verify_ball2.py (standard library only).
"""
from collections import Counter
from itertools import product, combinations
from math import comb

BASE = ((1,0), (2,0), (0,1), (0,2), (1,1), (1,-1))
BOUND = 21

def comps4(total):
    for a in range(total+1):
        for b in range(total-a+1):
            for c in range(total-a-b+1):
                yield (a,b,c,total-a-b-c)

def comps6(total):
    for a in range(total+1):
        for b in range(total-a+1):
            for c in range(total-a-b+1):
                for d in range(total-a-b-c+1):
                    for e in range(total-a-b-c-d+1):
                        yield (a,b,c,d,e,total-a-b-c-d-e)

def divides(a,b):
    return all(x<=y for x,y in zip(a,b))

def oriented(mask):
    return tuple(((1 if not ((mask>>j)&1) else -1)*x,
                   (1 if not ((mask>>j)&1) else -1)*y)
                  for j,(x,y) in enumerate(BASE))

def unpack(mask, counts):
    vec=oriented(mask)
    return tuple(sorted(v for v,n in zip(vec,counts) for _ in range(n)))

def kernel_atoms():
    complete=set(); inspected=0; rooted_atoms=0
    for mask in range(64):
        v=oriented(mask)
        pivots=max(((i,j) for i in range(6) for j in range(i+1,6)),
                   key=lambda z:abs(v[z[0]][0]*v[z[1]][1]-v[z[0]][1]*v[z[1]][0]))
        i,j=pivots
        det=v[i][0]*v[j][1]-v[i][1]*v[j][0]
        assert det != 0
        free=tuple(k for k in range(6) if k not in (i,j))
        atoms=[]
        for total in range(BOUND+1):
            for vals in comps4(total):
                inspected+=1
                x=-sum(vals[h]*v[free[h]][0] for h in range(4))
                y=-sum(vals[h]*v[free[h]][1] for h in range(4))
                n_i=x*v[j][1]-y*v[j][0]
                n_j=v[i][0]*y-v[i][1]*x
                if n_i % det or n_j % det:
                    continue
                n_i//=det; n_j//=det
                if n_i<0 or n_j<0 or not(total+n_i+n_j) or total+n_i+n_j>BOUND:
                    continue
                row=[0]*6
                for h,k in enumerate(free):row[k]=vals[h]
                row[i]=n_i;row[j]=n_j
                row=tuple(row)
                # Any proper zero-sum subrelation has strictly lower free-degree.
                if any(divides(a,row) for a in atoms):
                    continue
                atoms.append(row)
                complete.add(unpack(mask,row))
        rooted_atoms+=len(atoms)
    assert inspected==64*comb(BOUND+4,4), (inspected,comb(BOUND+4,4))
    return complete, inspected, rooted_atoms

def direct_small(bound=9):
    # Independent enumeration: enumerate *all* multiplicity vectors,
    # check their actual two coordinate sums, and do not solve pivots.
    complete=set()
    for mask in range(64):
        v=oriented(mask); atoms=[]
        for total in range(1,bound+1):
            for a in comps6(total):
                if sum(a[i]*v[i][0] for i in range(6))!=0 or sum(a[i]*v[i][1] for i in range(6))!=0:
                    continue
                if not any(divides(old,a) for old in atoms):
                    atoms.append(a)
                    complete.add(unpack(mask,a))
    return complete

def transform(seq,swap,sx,sy):
    return tuple(sorted((sx*(y if swap else x),sy*(x if swap else y)) for x,y in seq))

def orbit_key(seq):
    return min(transform(seq,swap,sx,sy) for swap,sx,sy in product((0,1),(-1,1),(-1,1)))

def run():
    assert sum(1 for x in range(-2,3) for y in range(-2,3) if x*x+y*y<=4)==13
    # Euclidean Steinitz constant sqrt(5)/2 implies partial sums lie in
    # the closed radius-sqrt(5) disk: it contains 21 lattice points.
    assert sum(1 for x in range(-3,4) for y in range(-3,4) if x*x+y*y<=5)==21
    complete, inspected, rooted=kernel_atoms()
    shorter=direct_small()
    assert shorter=={s for s in complete if len(s)<=9}
    # Directly check every enumerated positive-length atom by independent
    # subset selection (not by the pivot/antichain logic).
    for seq in complete:
        assert sum(x for x,y in seq)==sum(y for x,y in seq)==0
        for size in range(1,len(seq)):
            for subset in combinations(range(len(seq)),size):
                assert (sum(seq[i][0] for i in subset),
                        sum(seq[i][1] for i in subset)) != (0,0)
    assert Counter(map(len,complete))=={3:12,4:16,5:12}
    maxima={s for s in complete if len(s)==max(map(len,complete))}
    orbits={}
    for s in maxima:orbits.setdefault(orbit_key(s),set()).add(s)
    assert max(map(len,complete))==5
    assert len(maxima)==12
    assert len(orbits)==2
    assert sorted(map(len,orbits.values()))==[4,8]
    assert sorted(len(set(k)) for k in orbits)==[3,5]
    print('CERTIFICATE_OK', 'examined_free_tuples='+str(inspected),
          'oriented_atoms='+str(rooted),
          'unique_atoms='+str(len(complete)),
          'maximum_length=5', 'maximal_multisets=12',
          'orbit_sizes=4,8')
    print('all_atom_lengths',sorted(Counter(map(len,complete)).items()))
    for k in sorted(orbits):
        print('orbit',len(orbits[k]),'representative',sorted(Counter(k).items()))

if __name__=='__main__':run()
