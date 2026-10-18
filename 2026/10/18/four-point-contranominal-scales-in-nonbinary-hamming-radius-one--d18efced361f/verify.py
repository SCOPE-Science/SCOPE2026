"""Verify size-four contranominal configurations in q-ary radius-one Hamming contexts."""
from itertools import combinations, product
from math import comb


def classify(points, alphabet, dimension):
    varying = [i for i in range(dimension) if len({p[i] for p in points}) > 1]
    if len(varying) == 2:
        a, b = varying
        for row, col in ((a,b),(b,a)):
            counts = {}
            for p in points:
                counts.setdefault(p[row],set()).add(p[col])
            if len(counts)==2 and all(len(v)==2 for v in counts.values()):
                return 'two_row'
    if len(varying) == 3:
        coords = [[p[i] for p in points] for i in varying]
        if all(len(set(c)) == 2 for c in coords):
            mapped = []
            for p in points:
                mapped.append(tuple(sorted(set(c))[1] == p[i] for i,c in zip(varying,coords)))
            if len(set(mapped)) == 4 and len({sum(v)%2 for v in mapped})==1:
                return 'parity'
    return None


def check(q,d,max_samples=None):
    vertices=list(product(range(q),repeat=d)); n=len(vertices)
    covers=[]
    for v in vertices:
        mask=0
        for j,x in enumerate(vertices):
            if sum(a!=b for a,b in zip(v,x)) <= 1:mask |=1<<j
        covers.append(mask)
    masks=[1<<j for j in range(n)]
    predicted = comb(d,2)*q**(d-2)*comb(q,2)**2*(2*comb(q,2)-1)
    predicted += (comb(d,3)*q**(d-3)*2*comb(q,2)**3) if d>=3 else 0
    good=0
    counts={'two_row':0,'parity':0}
    inspected=0
    for ids in combinations(range(n),4):
        inspected+=1
        if max_samples and inspected>max_samples:break
        m=sum(masks[i] for i in ids)
        witness=[]
        for i in ids:
            w=[j for j,c in enumerate(covers) if (c&m)==(m ^ masks[i])]
            if not w:break
            witness.append(w)
        isscale=len(witness)==4
        typ=classify([vertices[i] for i in ids],q,d)
        if isscale!=(typ is not None):raise AssertionError(('classification',q,d,ids,typ,witness))
        if isscale:
            if not all(len(x)==1 for x in witness):raise AssertionError(('uniqueness',q,d,ids,witness))
            counts[typ]+=1;good+=1
    complete=inspected==comb(n,4)
    if complete and good!=predicted:raise AssertionError(('count',q,d,good,predicted))
    print('PARAMETERS',q,d,'tested',min(inspected,comb(n,4)),'count',good,'predicted',predicted,'complete',complete,'types',counts)
    if complete:
        for ids in combinations(range(n),5):
            m=sum(masks[i] for i in ids)
            if all(any((c&m)==(m^masks[i]) for c in covers) for i in ids):
                raise AssertionError(('size_five',q,d,ids))
    return complete

if __name__=='__main__':
    for q,d in ((2,2),(2,3),(2,4),(3,2),(3,3),(4,2)):
        check(q,d)
    check(3,4,25000)
    print('VERIFY_OK 4_scale_structure=PASS unique_witness=PASS exact_formula=PASS five_scale_boundary=PASS')
