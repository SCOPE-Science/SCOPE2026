"""Exact finite incidence search for a conic and seven lines.

A triple of lines uses three unordered line pairs. A conic/line/line
triple uses one pair of secants, and each secant has only two intersection
points with the conic. Only permissible line triples are retained.
"""
from itertools import combinations, permutations


def cases(s):
    T=set(range(s,7))
    edges=list(combinations(range(s),2))
    for q in range(s+1):
        for qset in combinations(edges,q):
            if any(sum(v in e for e in qset)>2 for v in range(s)):
                continue
            Q=set(qset)
            triples=[]
            for tr in combinations(range(7),3):
                if len(set(tr)&T)>2: continue
                pe=set(combinations(tr,2))
                if pe&Q: continue
                triples.append((tr,pe))
            target=5+s-q
            def search(i,used,selected):
                if len(selected)==target:
                    yield (tuple(sorted(Q)),tuple(sorted(selected)))
                    return
                if len(selected)+len(triples)-i<target: return
                for j in range(i,len(triples)):
                    tr,pe=triples[j]
                    if not pe&used:
                        yield from search(j+1,used|pe,selected+[tr])
            yield from search(0,Q,[])


def orbit_signature(s,c):
    best=None
    for pa in permutations(range(s)):
        for pb in permutations(range(s,7)):
            p=pa+pb
            cand=(tuple(sorted(tuple(sorted(p[i] for i in edge)) for edge in c[0])),
                  tuple(sorted(tuple(sorted(p[i] for i in tr)) for tr in c[1])))
            if best is None or cand<best:best=cand
    return best

EXPECTED={3:(18,36),4:(24,),5:(),6:(60,)}
for s in (3,4,5,6):
    classes={}
    for c in cases(s):
        sig=orbit_signature(s,c)
        classes[sig]=classes.get(sig,0)+1
    sizes=tuple(sorted(classes.values()))
    assert sizes==tuple(sorted(EXPECTED[s])), (s,sizes)
    print('secants',s,'orbit_sizes',sizes)
    for signature in sorted(classes):
        print('Q',signature[0],'line_triples',signature[1])
print('EXACT_DEGREE9_CONIC_SEVEN_LINES_INCIDENCE_CLASSES_OK')
