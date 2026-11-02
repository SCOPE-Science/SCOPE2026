"""Exhaustive small-design tests of extension types in one-point deletions.

This is a finite corroboration of an arbitrary-parameter proof, not an
exhaustive test of all designs or a substitute for that proof.
"""
from itertools import combinations
from collections import Counter
import json


def f2_blocks(dim):
    n = 1 << dim
    return sorted({tuple(sorted((a,b,c,a^b^c)))
                   for a,b,c in combinations(range(n),3)
                   if (a^b^c) not in (a,b,c)})


def f3_lines():
    pts = [(x,y) for x in range(3) for y in range(3)]
    lines=set()
    for (dx,dy) in ((1,0),(0,1),(1,1),(1,2)):
        for x,y in pts:
            lines.add(tuple(sorted(pts.index(((x+i*dx)%3,(y+i*dy)%3)) for i in range(3))))
    return sorted(lines)


def sqs10_blocks():
    pts = [(x,y) for x in range(3) for y in range(3)]
    out={tuple(sorted((*line,9))) for line in f3_lines()}
    for a,b in pts:
        for c in (1,2):
            circle=tuple(sorted(i for i,(x,y) in enumerate(pts)
                 if ((x-a)**2+(y-b)**2)%3 == c))
            assert len(circle)==4
            out.add(circle)
    assert len(out)==30
    return sorted(out)


def sts7_blocks():
    return sorted({tuple(sorted((a-1,b-1,(a^b)-1))) for a,b in combinations(range(1,8),2)})


def verify(t,v,blocks,puncture):
    blockset={frozenset(b) for b in blocks}
    assert len(blockset)==len(blocks)
    assert all(len(b)==t+1 for b in blockset)
    full={frozenset(x) for b in blockset for x in combinations(b,t)}
    assert len(full)==sum(1 for _ in combinations(range(v),t)), 'not a Steiner system'
    assert len(blocks)*(t+1)==len(full)
    pts=set(range(v))-{puncture}; keep={b for b in blockset if puncture not in b}
    complete={x for b in keep for x in (frozenset(y) for y in combinations(b,t))}
    missing={frozenset(x) for x in combinations(sorted(pts),t)}-complete
    miss_count=0; covered_count=0
    cases=Counter()
    for tup in combinations(sorted(pts),t):
        A=frozenset(tup)
        C=Counter()
        for w in pts-A:
            big=A|{w}
            mc=sum(frozenset(x) in missing for x in combinations(big,t))
            C[(big in keep,mc)] += 1
        if A in missing:
            miss_count +=1
            assert C==Counter({(False,1):v-1-t}), (t,v,tup,C)
        else:
            covered_count +=1
            expected=Counter({(True,0):1,(False,1):t})
            if v>2*t+2: expected[(False,0)]=v-2*t-2
            assert C==expected, (t,v,tup,C,expected)
        cases[tuple(sorted(C.items()))]+=1
    return {'t':t,'v':v,'full_blocks':len(blocks),'puncture':puncture,
            'remaining_vertices':v-1,'missing_t_subsets':len(missing),
            'missing_anchor_cases':miss_count,'covered_anchor_cases':covered_count,
            'distinct_extension_profiles':len(cases),
            'free_witnesses_per_covered_anchor':v-2*t-2}


def main():
    designs=[(2,7,sts7_blocks()),(2,9,f3_lines()),
             (3,8,f2_blocks(3)),(3,10,sqs10_blocks()),(3,16,f2_blocks(4))]
    reports=[]
    for t,v,blocks in designs:
        for p in range(v): reports.append(verify(t,v,blocks,p))
    print(json.dumps({'design_parameters':[[t,v] for t,v,_ in designs],
          'point_deletions_checked':len(reports),
          'distinct_anchor_cases_checked':sum(r['missing_anchor_cases']+r['covered_anchor_cases'] for r in reports),
          'all_extension_types': 'MATCH',
          'examples':[r for r in reports if r['puncture']==0]},indent=2))

if __name__=='__main__':main()
