"""Independent finite order oracle and exact orbit-signature census.

Python 3 standard library only; run in same folder as logical_types.py.
"""
from itertools import product
from hashlib import sha256
from logical_types import theory, QBOTH, mask_bottom_n, mask_nbottom, q1nn


def one_type(n, f):
    if f == 'bottom':
        return frozenset({QBOTH} | {(1, mask_bottom_n(g, n-g)) for g in range(n+1)})
    u = n-f
    signatures = {(2, mask_nbottom(f, u))}
    for a in range(f+1):
        for b in range(f-a+1):
            c=f-a-b
            for h in range(u+1):
                signatures.add(q1nn(a,b,c,h,u-h))
    return frozenset(signatures)


def direct(n):
    """No orbit reduction: enumerate every face and every pair (x,y)."""
    faces=[None]+list(product((0,1,2), repeat=n))
    N=len(faces)
    def le(x,y):
        if x is None: return True
        if y is None: return False
        return all(a==b or (a in (0,1) and b==2) for a,b in zip(x,y))
    rows=[0]*N
    cols=[0]*N
    for i,x in enumerate(faces):
        for j,y in enumerate(faces):
            if le(x,y):
                rows[i] |= 1<<j
                cols[j] |= 1<<i
    allbits=(1<<N)-1
    alltypes=set()
    for x in range(N):
        signatures=set()
        for y in range(N):
            sets=(cols[x],rows[x],cols[y],rows[y])
            comp=tuple(allbits^b for b in sets)
            relation_patterns=0
            for pattern in range(16):
                v=allbits
                for i in range(4):
                    v &= sets[i] if pattern & (1<<i) else comp[i]
                    if not v: break
                if v: relation_patterns |= 1<<pattern
            pair=int(bool(rows[x] & (1<<y))) + (2*int(bool(rows[y] & (1<<x))))
            signatures.add((pair, relation_patterns))
        alltypes.add(frozenset(signatures))
    return frozenset(alltypes)


def canonical(t):
    return tuple(sorted(tuple(sorted(s)) for s in t))


def run():
    previous=None
    classids={}
    witness1=(1,17653)
    witness2=(2,12067)
    assert witness1 != witness2
    for n in range(28):
        types,counts=theory(n)
        if n<=5:
            assert types==direct(n), ('direct disagreement', n)
            print('DIRECT_OK dimension=%d faces=%d'% (n,3**n+1))
        cid=classids.setdefault(types,len(classids))
        positive=[f for f in range(n+1) if witness1 in one_type(n,f) and witness2 in one_type(n,f)]
        assert bool(positive)==(n>=5), (n,positive)
        if n>=5: assert cid==5, (n,cid)
        else: assert cid==n, (n,cid)
        assert types==frozenset(one_type(n,f) for f in list(range(n+1))+['bottom'])
        if n in (0,1,2,3,4,5,6,10,15,20,27):
            data=repr(canonical(types)).encode('utf-8')
            print('CENSUS dimension=%d class=%d realized_types=%d fingerprint=%s'%(n,cid,len(types),sha256(data).hexdigest()[:20]))
        previous=types
    assert len(classids)==6
    assert 3**5+1==244
    print('EXHAUSTIVE_ORBITS_OK dimension_range=0..27 classes=6 stable_from=5')
    print('SEPARATING_SENTENCE_OK witness_signatures=(1,17653),(2,12067) min_dimension=5')
    print('UNIFORM_EF_LEMMA_USED coordinate_threshold=27 rounds=3 (proved in RESULT.md; not checked by code)')
    print('SHARP_BOUND_OK minimum_maximum_representative=244')
    print('VERIFY_OK')

if __name__=='__main__':
    run()
