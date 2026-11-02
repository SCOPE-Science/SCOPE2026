"""Exact combinatorial cross-check of two descriptions of one-deletion conflicts."""
from itertools import combinations
from math import comb

def vectors(n,q=5):
    for div in combinations(range(n+q-1),q-1):
        b=(-1,)+div+(n+q-1,)
        yield tuple(b[j+1]-b[j]-1 for j in range(q))
for n,expected,expected_edges,expected_witness in [(9,715,4950,143),(10,1001,7150,201)]:
    xs=list(vectors(n));assert len(xs)==expected
    ix={x:k for k,x in enumerate(xs)}
    by_shadow=set()
    for y in vectors(n-1):
        parents=[]
        for i in range(5):
            x=list(y);x[i]+=1;parents.append(ix[tuple(x)])
        for a,b in combinations(sorted(parents),2):by_shadow.add((a,b))
    by_transfer=set()
    for a,x in enumerate(xs):
        for i in range(5):
            if not x[i]:continue
            for j in range(5):
                if i==j:continue
                y=list(x);y[i]-=1;y[j]+=1;b=ix[tuple(y)]
                if a<b:by_transfer.add((a,b))
    assert by_shadow==by_transfer
    assert len(by_shadow)==expected_edges
    witness={a for a,x in enumerate(xs) if sum(i*x[i] for i in range(5))%5==0}
    assert len(witness)==expected_witness
    assert all(not(a in witness and b in witness) for a,b in by_transfer)
    print(f'n={n}: {len(xs)} codeword candidates, {comb(n+3,4)} outputs, {len(by_shadow)} conflicts, witness {len(witness)}; formulations identical')
print('QUINARY_COMBINATORIAL_CHECK_OK')
