#!/usr/bin/env python3
from collections import defaultdict, deque
from functools import lru_cache
from math import gcd

TOGGLE_ORDER=[20,22,7,0,3,15,6,21,13,23,8,17,10,12,16,18,11,4,5,9,2,1,14,19]
EXPECTED_F=[24,228,1096,2826,3816,2444,600,33]
EXPECTED_CRIT={0:1,4:10,5:6}
EXPECTED_BETTI_F2={0:1,1:0,2:0,3:0,4:8,5:4,6:0,7:0}

def generalized_petersen_8_3_edges():
    n=8; k=3; e=set()
    for i in range(n):
        e.add(tuple(sorted((i,(i+1)%n))))
        e.add((i,n+i))
        e.add(tuple(sorted((n+i,n+(i+k)%n))))
    return sorted(e)

def enumerate_matchings(edges):
    m=len(edges)
    conflict=[]
    for i,(a,b) in enumerate(edges):
        cm=0
        for j,(c,d) in enumerate(edges):
            if a in (c,d) or b in (c,d): cm|=1<<j
        conflict.append(cm)
    ans=[]
    def rec(avail,chosen):
        if not avail:
            ans.append(chosen); return
        bit=avail & -avail; i=bit.bit_length()-1
        rec(avail^bit,chosen)
        rec(avail & ~conflict[i], chosen|bit)
    rec((1<<m)-1,0)
    return set(ans)

def gf2_rank(columns):
    piv={}; rank=0
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in piv: x ^= piv[p]
            else:
                piv[p]=x; rank+=1; break
    return rank

def incidence(upper,lower):
    diff=upper^lower
    assert diff and not(diff&(diff-1)) and lower==(upper^diff)
    v=diff.bit_length()-1
    pos=(upper & ((1<<v)-1)).bit_count()
    return -1 if pos&1 else 1

def smith_invariants_small(A):
    # Exact SNF diagonal for this small 10x6 matrix via determinantal divisors.
    # We only need rank 2. gcd of entries = d1, gcd of all 2x2 minors = d1*d2.
    rows=len(A); cols=len(A[0]) if rows else 0
    g1=0
    for r in A:
        for x in r: g1=gcd(g1,abs(x))
    g2=0
    for i in range(rows):
      for j in range(i+1,rows):
       for a in range(cols):
        for b in range(a+1,cols):
         det=A[i][a]*A[j][b]-A[i][b]*A[j][a]
         g2=gcd(g2,abs(det))
    # rank >2 check via all 3x3 minors not needed if rational elimination says rank 2.
    B=[row[:] for row in A]; rr=0
    from fractions import Fraction
    Q=[[Fraction(x) for x in row] for row in B]
    for c in range(cols):
      piv=next((i for i in range(rr,rows) if Q[i][c]),None)
      if piv is None: continue
      Q[rr],Q[piv]=Q[piv],Q[rr]
      z=Q[rr][c]; Q[rr]=[x/z for x in Q[rr]]
      for i in range(rows):
        if i!=rr and Q[i][c]:
          z=Q[i][c]; Q[i]=[Q[i][j]-z*Q[rr][j] for j in range(cols)]
      rr+=1
    assert rr==2 and g1==1 and g2==1
    return [1,1]

def main():
    edges=generalized_petersen_8_3_edges()
    assert len(edges)==24
    faces=enumerate_matchings(edges)
    assert len(faces)==11068
    nonempty=faces-{0}
    byd=defaultdict(list)
    for f in nonempty: byd[f.bit_count()-1].append(f)
    fvec=[len(byd[d]) for d in range(8)]
    assert fvec==EXPECTED_F

    # Direct GF(2) homology from simplicial boundary matrices.
    ranks={}
    for d in range(1,8):
        low=byd[d-1]; pos={f:i for i,f in enumerate(low)}; cols=[]
        for s in byd[d]:
            x=0; mm=s
            while mm:
                b=mm&-mm; x ^= 1<<pos[s^b]; mm^=b
            cols.append(x)
        ranks[d]=gf2_rank(cols)
    betti={d:len(byd[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(8)}
    assert betti==EXPECTED_BETTI_F2

    # Deterministic staged face-poset matching.
    unmatched=set(nonempty); pairs=[]
    for v in TOGGLE_ORDER:
        bit=1<<v
        for s in list(unmatched):
            if not(s&bit) and (s|bit) in unmatched:
                unmatched.remove(s); unmatched.remove(s|bit); pairs.append((s,s|bit))
    prof=defaultdict(int)
    for s in unmatched: prof[s.bit_count()-1]+=1
    assert dict(prof)==EXPECTED_CRIT and len(pairs)==5525
    lower_to_upper=dict(pairs)
    assert len(lower_to_upper)==len(pairs)

    # Every matching pair is a genuine face-poset cover and the full reversed-cover digraph is acyclic.
    nodes=sorted(nonempty); node_id={s:i for i,s in enumerate(nodes)}
    pairset={(a,b) for a,b in pairs}
    indeg=[0]*len(nodes); out=[[] for _ in nodes]; cover_count=0
    for upper in nodes:
        mm=upper
        while mm:
            bit=mm&-mm; lower=upper^bit; mm^=bit
            if not lower: continue
            cover_count+=1
            if (lower,upper) in pairset:
                a,b=lower,upper
            else:
                a,b=upper,lower
            ia=node_id[a]; ib=node_id[b]
            out[ia].append(ib); indeg[ib]+=1
    q=deque(i for i,x in enumerate(indeg) if x==0); seen=0
    while q:
        u=q.popleft(); seen+=1
        for v in out[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    assert seen==len(nodes)

    critical=set(unmatched)
    upper_matched={b for a,b in pairs}

    @lru_cache(None)
    def reduce_p_cell(cell,p):
        if cell in critical:
            assert cell.bit_count()-1==p
            return {cell:1}
        up=lower_to_upper.get(cell)
        if up is None:
            # This p-cell is the upper member of a (p-1,p) matched pair, hence it is not on a p/(p+1) V-path.
            assert cell in upper_matched
            return {}
        a=incidence(up,cell)
        res={}
        mm=up
        while mm:
            bit=mm&-mm; lo=up^bit; mm^=bit
            if lo==cell: continue
            b=incidence(up,lo)
            for c,x in reduce_p_cell(lo,p).items():
                res[c]=res.get(c,0)-a*b*x
        return {c:x for c,x in res.items() if x}

    crit4=sorted(s for s in critical if s.bit_count()-1==4)
    crit5=sorted(s for s in critical if s.bit_count()-1==5)
    A=[[0]*len(crit5) for _ in crit4]
    pos4={s:i for i,s in enumerate(crit4)}
    for j,cu in enumerate(crit5):
        accum={}
        mm=cu
        while mm:
            bit=mm&-mm; lo=cu^bit; mm^=bit
            a=incidence(cu,lo)
            for c,x in reduce_p_cell(lo,4).items(): accum[c]=accum.get(c,0)+a*x
        for c,x in accum.items(): A[pos4[c]][j]=x
    assert smith_invariants_small(A)==[1,1]

    # The Morse CW model has one 0-cell, ten 4-cells and six 5-cells.
    # Its 5-to-4 cellular boundary has SNF diag(1,1,0,0,0,0).
    # Since the 4-skeleton is a wedge of ten 4-spheres and pi_4 of that wedge is Z^10,
    # the attaching maps are determined by these degree vectors; unimodular row/column changes split two contractible 4/5-cell pairs.
    print('graph=generalized Petersen G(8,3) (Möbius-Kantor)')
    print('edges=24 matchings_including_empty=11068')
    print('f_vector='+str(fvec))
    print('face_poset_nodes=%d covers=%d matched_pairs=%d critical=%s' % (len(nodes),cover_count,len(pairs),dict(sorted(prof.items()))))
    print('mod2_betti='+str(betti))
    print('morse_boundary_5_to_4_snf=[1, 1, 0, 0, 0, 0]')
    print('homotopy=wedge^8 S^4 vee wedge^4 S^5')
    print('VERIFY_OK')
if __name__=='__main__': main()
