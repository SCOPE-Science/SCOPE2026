#!/usr/bin/env python3
from itertools import combinations_with_replacement, combinations
from collections import Counter, defaultdict
import json, hashlib, sys

N=9
V=range(1,16)

def parity(x): return x.bit_count() & 1

def min_distance(cols):
    # For generator columns cols in F_2^4, codeword aG has weight
    # number of columns with a dot c = 1.
    return min(sum(parity(a & c) for c in cols) for a in V)

def subset_xors(cols):
    xs=[0]*(1<<N)
    for m in range(1,1<<N):
        b=m & -m
        i=b.bit_length()-1
        xs[m]=xs[m^b]^cols[i]
    return xs

def four_disjoint_A(masks):
    # Direct recursive set packing: four pairwise-disjoint recovery masks.
    masks=sorted(masks, key=lambda m:(m.bit_count(),m))
    def rec(start, used, need):
        if need==0: return True
        # Union-size pruning: each remaining set is nonempty.
        if N-used.bit_count() < need: return False
        for j in range(start,len(masks)):
            m=masks[j]
            if not (m & used) and rec(j+1, used|m, need-1):
                return True
        return False
    return rec(0,0,4)

def four_disjoint_B(masks):
    # Independent formulation: create unions of two disjoint recovery sets;
    # four pairwise-disjoint sets exist iff two such pair-unions are disjoint.
    unions=set()
    L=masks
    for i,a in enumerate(L):
        for b in L[i+1:]:
            if not (a & b):
                unions.add(a|b)
    U=sorted(unions)
    for i,a in enumerate(U):
        for b in U[i+1:]:
            if not (a & b):
                return True
    return False

def good_targets(cols):
    xs=subset_xors(cols)
    by=[[] for _ in range(16)]
    for m in range(1,1<<N): by[xs[m]].append(m)
    gA=[]; gB=[]
    for t in V:
        a=four_disjoint_A(by[t]); b=four_disjoint_B(by[t])
        if a: gA.append(t)
        if b: gB.append(t)
    if gA!=gB:
        raise AssertionError((cols,gA,gB))
    return tuple(gA)

def rank4(vs):
    basis=[0]*4
    r=0
    for x in vs:
        y=x
        while y:
            i=y.bit_length()-1
            if basis[i]: y ^= basis[i]
            else:
                basis[i]=y; r+=1; break
    return r

def is_basis(vs): return len(vs)==4 and rank4(vs)==4

def all_gl_maps():
    out=[]
    for imgs in combinations(V,4):
        # combinations doesn't include ordered bases, so expand permutations via recursive below would be awkward.
        pass
    # Direct: choose ordered images and test rank incrementally.
    from itertools import permutations
    for imgs in permutations(V,4):
        if rank4(imgs)==4:
            mp=[0]*16
            for x in range(16):
                y=0
                for i,b in enumerate((1,2,4,8)):
                    if x&b: y ^= imgs[i]
                mp[x]=y
            out.append(tuple(mp))
    # Every invertible map is identified by ordered images of basis.
    if len(out)!=20160 or len(set(out))!=20160:
        raise AssertionError(len(out))
    return out

def transform(cols,mp): return tuple(sorted(mp[c] for c in cols))

def main():
    dist4=[]
    total=0
    for cols in combinations_with_replacement(V,N):
        total+=1
        if min_distance(cols)>=4:
            dist4.append(cols)
    assert total==817190, total
    assert len(dist4)==1345, len(dist4)

    accepted=[]; target_hist=Counter(); distinct_hist=Counter(); std_basis=0
    goodmap={}
    for idx,cols in enumerate(dist4):
        gt=good_targets(cols)
        goodmap[cols]=gt
        target_hist[len(gt)]+=1
        if rank4(gt)==4:
            accepted.append(cols)
            distinct_hist[len(set(cols))]+=1
            if all(t in gt for t in (1,2,4,8)): std_basis+=1
    assert len(accepted)==1120, len(accepted)
    assert distinct_hist==Counter({8:840,9:280}), distinct_hist
    assert std_basis==896, std_basis
    assert target_hist[15]==280 and target_hist[14]==840, target_hist
    # No accepted type should have some other target-count.
    assert sum(target_hist[k] for k in target_hist if k not in (14,15)) == len(dist4)-1120

    # Structural statements.
    for cols in accepted:
        gt=goodmap[cols]
        C=Counter(cols)
        if len(set(cols))==9:
            assert len(gt)==15 and max(C.values())==1
        else:
            assert len(set(cols))==8 and sorted(C.values())==[1]*7+[2]
            assert len(gt)==14

    gl=all_gl_maps()
    A=set(accepted)
    unseen=set(accepted); orbits=[]
    while unseen:
        rep=min(unseen)
        orb={transform(rep,mp) for mp in gl}
        if not orb <= A:
            raise AssertionError('GL image left accepted set')
        orbits.append((rep,orb))
        unseen-=orb
    sizes=sorted(len(o) for _,o in orbits)
    assert sizes==[280,840], sizes
    # Canonical order by projective/nonprojective.
    orbit_data=[]
    for rep,orb in sorted(orbits,key=lambda ro:len(ro[1])):
        gt=goodmap[rep]
        missing=sorted(set(V)-set(gt))
        orbit_data.append({
          'size':len(orb),
          'stabilizer_order':20160//len(orb),
          'representative':[format(x,'04b') for x in rep],
          'distinct_columns':len(set(rep)),
          'four_recoverable_target_count':len(gt),
          'missing_targets':[format(x,'04b') for x in missing]
        })

    # Check the representative displayed in the 2020 short-block paper belongs
    # to the projective orbit. Columns transcribed from its 4x9 matrix.
    lit=tuple(sorted(int(s,2) for s in ['1000','0100','0010','0001','1010','1110','1001','1101','1111']))
    assert lit in A and len(set(lit))==9 and len(goodmap[lit])==15
    proj_orb=next(orb for rep,orb in orbits if len(orb)==280)
    assert lit in proj_orb

    result={
      'ambient_length9_nonzero_multisets':total,
      'distance_at_least4_multisets':len(dist4),
      'basis_flexible_4pir_multisets':len(accepted),
      'standard_basis_4pir_multisets':std_basis,
      'projective_multisets':distinct_hist[9],
      'one_double_point_multisets':distinct_hist[8],
      'gl4_order':len(gl),
      'orbit_sizes':sizes,
      'orbits':orbit_data,
      'literature_matrix_in_projective_orbit':True,
      'algorithm_agreement':'all 1345 distance-at-least-4 candidates, all 15 nonzero targets'
    }
    raw=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
    result['core_result_sha256']=hashlib.sha256(raw).hexdigest()
    with open('/mnt/data/pir44_run/census.json','w',encoding='utf-8') as f:
        json.dump(result,f,sort_keys=True,indent=2); f.write('\n')
    print('VERIFY_OK',
          'ambient=817190',
          'd4=1345',
          'basis_flexible=1120',
          'standard_basis=896',
          'projective=280',
          'one_double=840',
          'orbits=280,840',
          'stabilizers=72,24',
          'algorithms_agree=true')
    print('core_result_sha256='+result['core_result_sha256'])

if __name__=='__main__': main()
