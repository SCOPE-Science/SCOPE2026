#!/usr/bin/env python3
"""Exact F2 linear classification of quartics with four prescribed ordinary flexes.
Public reproducibility code, no nonstandard libraries required for the classification.
"""
from itertools import product
from collections import Counter
CAP=(1,2,4,7)
MON=tuple(a for a in product(range(5),repeat=3) if sum(a)==4)
assert len(MON)==15

def coef(a,p,q,k):
    # coeff of s^(4-k) t^k in monomial evaluated at s*p+t*q
    z=[1,0,0,0,0]
    for i,e in enumerate(a):
        pi=(p>>i)&1; qi=(q>>i)&1
        w=[int((j&e)==j and ((e-j)==0 or pi) and (j==0 or qi)) for j in range(e+1)]
        z=[sum(z[b]*w[h] for b in range(5) for h in range(e+1) if b+h==t)%2 for t in range(5)]
    return z[k]

def constraints(p,q):
    return [(sum(coef(a,p,q,k)<<j for j,a in enumerate(MON)), int(k==3)) for k in range(5)]

def solve(rows,n=15):
    pivots={}
    for a,b in rows:
        while a:
            i=a.bit_length()-1
            if i not in pivots:
                pivots[i]=(a,b);break
            a^=pivots[i][0];b^=pivots[i][1]
        else:
            if b:return ()
    free=[k for k in range(n) if k not in pivots]
    sols=[]
    for bits in range(1<<len(free)):
        ans=sum(((bits>>j)&1)<<k for j,k in enumerate(free))
        for k in sorted(pivots):
            a,b=pivots[k]
            ans|=(b^((a&ans).bit_count()%2))<<k
        assert all((a&ans).bit_count()%2==b for a,b in rows)
        sols.append(ans)
    return tuple(sols)

if __name__=='__main__':
    allq=tuple(tuple(x for x in range(1,8) if x!=p) for p in CAP)
    tally=Counter();solutions={}
    for qs in product(*allq):
        rows=sum((constraints(p,q) for p,q in zip(CAP,qs)),[])
        vals=solve(rows)
        tally[len(vals)]+=1
        if vals:solutions[qs]=vals
    print('CAP',CAP,'ASSIGNMENTS',6**4,'SYSTEM_SOLUTION_COUNT_HISTOGRAM',dict(tally))
    print('CONSISTENT_ASSIGNMENTS',len(solutions),'TOTAL_FORMS_WITH_MULTIPLICITY',sum(map(len,solutions.values())))
    print('UNION_FORMS',len(set(f for a in solutions.values() for f in a)))
    from check_flexes import smooth
    allforms=sorted(set(f for aa in solutions.values() for f in aa))
    bystatus=Counter()
    smoothforms=set()
    for f in allforms:
        z=smooth(f)
        bystatus[z]+=1
        if z:smoothforms.add(f)
    print('GEOMETRIC_SMOOTHNESS',bystatus,'SMOOTH_MASKS',sorted(smoothforms))
    assert len(smoothforms)==24
    patterns=Counter();seenmaps=set()
    for qs,vals in solutions.items():
        for f in vals:
            if f not in smoothforms:continue
            assert set(qs)<=set(CAP),(qs,f)
            indeg=Counter(qs)
            assert sorted(indeg.get(p,0) for p in CAP)==[0,1,1,2]
            tail=next(p for p in CAP if indeg.get(p,0)==0)
            cycle=[p for p in CAP if p!=tail]
            arrow=dict(zip(CAP,qs))
            assert arrow[tail] in cycle
            assert all(arrow[arrow[arrow[p]]]==p for p in cycle)
            assert qs not in seenmaps
            seenmaps.add(qs)
            patterns['3-cycle plus tail']+=1
    assert patterns=={'3-cycle plus tail':24},patterns
    print('GRAPH_PATTERN',dict(patterns))
    print('REPRESENTATIVE',4418,'IN',4418 in smoothforms)
