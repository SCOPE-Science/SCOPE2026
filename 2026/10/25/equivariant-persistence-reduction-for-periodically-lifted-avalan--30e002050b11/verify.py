"""Finite independent checks for periodic-lift avalanche complexes.
Run: python3 verify.py (standard library only).
All parameters and assertions are finite; the proof for arbitrary parameters is in RESULT.md.
"""
from itertools import product


def orbit_sequence(k, b):
    state = tuple(b)
    seen = {}
    out = []
    while state not in seen:
        seen[state] = len(out)
        firing = frozenset(i for i, x in enumerate(state) if x >= 1)
        out.append(firing)
        state = tuple(state[i] - (i in firing) + ((i-1) % k in firing) for i in range(k))
    return out, seen[state]


def direct_lift_sequence(k, m, b):
    n = m*k
    state = tuple(b[i%k] for i in range(n))
    seen = set()
    out = []
    while state not in seen:
        seen.add(state)
        firing = frozenset(i for i,x in enumerate(state) if x >= 1)
        out.append(firing)
        state = tuple(state[i] - (i in firing) + ((i-1)%n in firing) for i in range(n))
    return out


def faces(facets):
    fs={0}
    for F in facets:
        a=tuple(F)
        for bits in range(1<<len(a)):
            v=0
            for j,i in enumerate(a):
                if bits>>j&1: v|=1<<i
            fs.add(v)
    return fs


def gf2_rank(columns):
    piv={}
    for x in columns:
        while x:
            j=x.bit_length()-1
            if j not in piv:
                piv[j]=x
                break
            x^=piv[j]
    return len(piv)


def betti(fset):
    layers={}
    for face in fset:
        if face: layers.setdefault(face.bit_count()-1,[]).append(face)
    if not layers: return ()
    dmax=max(layers)
    ranks={}
    for d in range(1,dmax+1):
        rows={face:j for j,face in enumerate(layers.get(d-1,[]))}
        cols=[]
        for f in layers.get(d,[]):
            x=0
            for j in range(f.bit_length()):
                if f>>j&1: x^=1<<rows[f^(1<<j)]
            cols.append(x)
        ranks[d]=gf2_rank(cols)
    return tuple(len(layers.get(d,[]))-ranks.get(d,0)-ranks.get(d+1,0) for d in range(dmax+1))


def main():
    count=0; times=0; faces_compared=0; homology_compared=0
    for k in range(2,7):
        for b in product(range(3),repeat=k):
            if not 1<=sum(b)<=4: continue
            base,preperiod=orbit_sequence(k,b)
            assert base
            for m in (2,3,4):
                n=k*m
                if n>12: continue
                high=direct_lift_sequence(k,m,b)
                assert len(base)==len(high)
                for t,(s,u) in enumerate(zip(base,high)):
                    assert u==frozenset(i for i in range(n) if (i%k) in s)
                    times+=1
                if n<=10:
                    for t in range(len(base)):
                        lhs=faces(high[:t+1]); rhs=faces(base[:t+1]);
                        lifted=set()
                        for f in lhs:
                            idx=0
                            for i in range(n):
                                if f>>i&1: idx|=1<<(i%k)
                            lifted.add(idx)
                        assert lifted==rhs
                        for f in rhs:
                            expanded=0
                            for i in range(n):
                                if f>>(i%k)&1: expanded|=1<<i
                            assert expanded in lhs
                        faces_compared+=len(lhs)
                    if count%11==0:
                        assert list(betti(faces(base)))==list(betti(faces(high)))[:len(betti(faces(base)))]
                        assert not any(betti(faces(high))[len(betti(faces(base))):])
                        homology_compared+=1
                count+=1
    # Disjoint-block and complementary-block benchmark, including k=2.
    for k in range(2,9):
        m=3
        for b in [tuple([1]+[0]*(k-1)),tuple([0]+[1]*(k-1))]:
            seq=direct_lift_sequence(k,m,b)
            assert len(seq)==k
            assert len(set(seq))==k
            if b[0]==1:
                assert all(len(s)==m for s in seq)
                assert all(s.isdisjoint(t) for i,s in enumerate(seq) for t in seq[i+1:])
            else:
                assert all(len(s)==m*(k-1) for s in seq)
                assert not set.intersection(*(set(s) for s in seq))
                assert all(set.intersection(*(set(s) for s in sub)) for r in range(1,k) for sub in __import__('itertools').combinations(seq,r))
    print('VERIFY_OK')
    print('complete_configuration_checks',count)
    print('independent_firing_step_comparisons',times)
    print('enumerated_lift_faces_with_fiber_projection',faces_compared)
    print('independent_mod2_Betti_comparisons',homology_compared)
    print('periodic_class_partition_benchmarks',14)

if __name__=='__main__': main()
