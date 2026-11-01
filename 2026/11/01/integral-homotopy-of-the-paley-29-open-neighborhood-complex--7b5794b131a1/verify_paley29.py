#!/usr/bin/env python3
"""Reproducible integral computation for the open-neighborhood complex of Paley(29).
Requires Python 3.10+ and SymPy 1.12+ for integer Hermite/Smith calculations.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from math import comb
import hashlib
import json
from pathlib import Path
import sys

P=29
Q={a*a % P for a in range(1,P)}
assert len(Q)==14 and -1 % P in Q
N=[sum(1 << ((i+q)%P) for q in Q) for i in range(P)]
assert all(m.bit_count()==14 and not (m&(1<<i)) for i,m in enumerate(N))
assert all(((N[i]>>j)&1)==((N[j]>>i)&1) for i in range(P) for j in range(P))


def all_faces_by_facets():
    out={0}
    for mask in N:
        s=mask
        while s:
            out.add(s)
            s=(s-1)&mask
    return out


def all_faces_by_common_neighbours():
    # Every nonempty face has a uniquely ordered list of vertices.
    result={0}
    stack=[(0,(1<<P)-1,0)]
    while stack:
        face, common, nxt=stack.pop()
        for v in range(nxt,P):
            remain=common & N[v]
            if remain:
                new=face|(1<<v)
                assert new not in result
                result.add(new)
                stack.append((new,remain,v+1))
    return result


def matching(faces,order):
    remain=set(faces);remain.remove(0)
    paired={}
    for v in order:
        b=1<<v
        low=[f for f in remain if f&b==0 and f|b in remain]
        for f in low:
            remain.remove(f)
            remain.remove(f|b)
            paired[f]=f|b
    return paired,remain


def verify_matching_dag(faces,paired):
    indeg={f:0 for f in faces if f}
    inc=0
    for f in indeg:
        x=f
        while x:
            bit=x&-x;x-=bit
            g=f^bit
            if not g:continue
            inc+=1
            if paired.get(g)==f: indeg[f]+=1
            else: indeg[g]+=1
    pending=deque(f for f,d in indeg.items() if d==0)
    seen=0
    while pending:
        f=pending.popleft();seen+=1
        x=f
        while x:
            bit=x&-x;x-=bit
            g=f^bit
            if g and paired.get(g)!=f:
                indeg[g]-=1
                if indeg[g]==0:pending.append(g)
        if f in paired:
            g=paired[f]
            indeg[g]-=1
            if indeg[g]==0:pending.append(g)
    assert seen==len(indeg),('directed cycle',seen,len(indeg))
    return inc


@lru_cache(None)
def bdry(face):
    terms=[];i=0;x=face
    while x:
        bit=x&-x;x-=bit
        terms.append((face^bit,1 if i%2==0 else -1))
        i+=1
    return terms


def morse_matrix(paired,remaining):
    crit3=sorted(f for f in remaining if f.bit_count()==4)
    crit4=sorted(f for f in remaining if f.bit_count()==5)
    assert Counter(f.bit_count()-1 for f in remaining)==Counter({0:1,3:len(crit3),4:len(crit4)})
    lookup={f:i for i,f in enumerate(crit3)}
    ongoing=set()
    @lru_cache(None)
    def r3(face):
        if face in lookup:return {lookup[face]:1}
        if face not in paired:return {}
        if face in ongoing:raise ArithmeticError('gradient-cycle')
        ongoing.add(face)
        upper=paired[face]
        assert upper.bit_count()==5
        sign=dict(bdry(upper))[face]
        result=defaultdict(int)
        for g,a in bdry(upper):
            if g==face:continue
            for i,b in r3(g).items():result[i]-=sign*a*b
        ongoing.remove(face)
        return {i:v for i,v in result.items() if v}
    columns=[]
    for cell in crit4:
        col=defaultdict(int)
        for face,a in bdry(cell):
            for i,b in r3(face).items():col[i]+=a*b
        columns.append({i:v for i,v in col.items() if v})
    return crit3,crit4,columns


def integral_rank_and_unit_invariants(columns,nrows):
    """Perform exact unit pivots, then use integer HNF and Smith on the small remainder.
    Each pivot is a unimodular row elimination and column deletion, so invariants
    of the original matrix consist of the unit pivots plus remainder invariants.
    """
    from sympy import Matrix,ZZ
    from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
    row={r:{c:columns[c][r] for c in range(len(columns)) if r in columns[c]} for r in range(nrows)}
    col={c:set(columns[c]) for c in range(len(columns))}
    unit_count=0
    while True:
        best=None
        for r,terms in row.items():
            for c,v in terms.items():
                if abs(v)==1:
                    score=(len(terms)-1)*(len(col[c])-1)
                    if best is None or score<best[0]:best=(score,r,c)
        if best is None:break
        _,r,c=best
        s=row[r][c]
        for r2 in list(col[c]):
            if r2==r:continue
            v=row[r2][c]
            for c2,a in row[r].items():
                if c2==c:continue
                value=row[r2].get(c2,0)-v*s*a
                if value:
                    row[r2][c2]=value
                    col[c2].add(r2)
                elif c2 in row[r2]:
                    del row[r2][c2]
                    col[c2].remove(r2)
            del row[r2][c]
        del col[c]
        for c2 in row[r]:
            if c2!=c:col[c2].remove(r)
        del row[r]
        unit_count+=1
    # HNF returns a free integer column basis for the remaining column lattice.
    ri=list(row);ci=list(col)
    R=Matrix([[row[r].get(c,0) for c in ci] for r in ri])
    H=hermite_normal_form(R)
    D=smith_normal_form(H,domain=ZZ)
    invariants=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
    assert all(v==1 for v in invariants),('nonunit invariant',invariants)
    rank=unit_count+len(invariants)
    return {'unit_pivots':unit_count,'residual_shape':[len(ri),len(ci)],
            'residual_hnf_shape':list(H.shape),'residual_smith':invariants,
            'total_unit_smith_invariants':rank,'rank':rank,
            'h3':nrows-rank,'h4':len(columns)-rank}


def main():
    A=all_faces_by_facets()
    B=all_faces_by_common_neighbours()
    assert A==B
    face_counts=dict(sorted(Counter(f.bit_count()-1 for f in A if f).items()))
    assert len(A)==449153
    chi=sum((-1)**d * count for d,count in face_counts.items())
    assert chi == 58 # Euler: 1 - 7 + 64
    reports=[]
    for name,order in [('natural',list(range(P))),('even_then_odd',list(range(0,P,2))+list(range(1,P,2)))]:
        pair,critical=matching(A,order)
        assert 2*len(pair)+len(critical)==len(A)-1
        incidences=verify_matching_dag(A,pair)
        c3,c4,cols=morse_matrix(pair,critical)
        if name=='natural':
            certificate=json.loads(Path(__file__).with_name('morse_boundary.json').read_text('utf-8'))
            assert certificate['critical_3_masks']==c3
            assert certificate['critical_4_masks']==c4
            assert certificate['columns']==[[[i,v] for i,v in sorted(col.items())] for col in cols]
        result=integral_rank_and_unit_invariants(cols,len(c3))
        assert (result['h3'],result['h4'])==(7,64),result
        assert (len(c4)-len(c3))==chi-1
        reports.append({'matching':name,'pairs':len(pair),'critical_counts':dict(sorted(Counter(f.bit_count()-1 for f in critical).items())),
                        'hasse_incidences':incidences,'morse_nonzero_entries':sum(len(v) for v in cols),**result})
    nonresidue=next(a for a in range(1,P) if a not in Q)
    # x -> nonresidue*x is an isomorphism with the complementary graph.
    for i in range(P):
        for j in range(P):
            if i==j:continue
            assert ((N[i]>>j)&1) != ((N[(nonresidue*i)%P]>>((nonresidue*j)%P))&1)
    print(json.dumps({'graph':'Paley(29)','quadratic_residues':sorted(Q),'number_faces_including_empty':len(A),
                      'face_dimension_counts':face_counts,'unreduced_euler':chi,
                      'complement_isomorphism_multiplier':nonresidue,'reductions':reports,
                      'neighborhood_homotopy':'7 copies S3 wedge 64 copies S4',
                      'dominance_reduced_integral_homology':{'degree22':64,'degree23':7},
                      'status':'PALEY29_NEIGHBORHOOD_AND_DUALITY_INTEGRAL_VERIFIED'},
                    sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
