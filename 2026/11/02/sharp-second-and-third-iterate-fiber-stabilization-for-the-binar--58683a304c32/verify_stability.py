#!/usr/bin/env python3
"""Exact certificate for two and three tortoise iterations on Rudin--Shapiro factors."""
PHI = {'0':'01','1':'02','2':'31','3':'32'}
TAU = str.maketrans('0123','0011')
PAIRS = ('01','02','10','13','20','23','31','32')

def substitute(word):
    return ''.join(PHI[c] for c in word)

def factors(n):
    assert n>=1
    blocks = {c:c for c in PHI}
    while len(blocks['0']) < n:
        blocks = {c:substitute(blocks[c]) for c in PHI}
    return set((blocks[p[0]] + blocks[p[1]]).translate(TAU)[i:i+n]
               for p in PAIRS for i in range(2*len(blocks['0'])-n+1))

def tortoise(w):
    j = w.find('1')
    return w if j == -1 else w[:j] + w[j+1:] + '1'

def iter_t(w,k):
    for _ in range(k):w=tortoise(w)
    return w

def equivalence_check(n,k):
    ff=factors(n)
    groups={}
    for w in sorted(ff):
        group=iter_t(w,k)
        groups.setdefault(group,[]).append(w)
    tgroups={}
    for w in sorted(ff):
        group=tortoise(w)
        tgroups.setdefault(group,[]).append(w)
    # Compare partitions by collecting exact canonical fibers, not merely image counts.
    same={tuple(v) for v in groups.values()}=={tuple(v) for v in tgroups.values()}
    print(f'n={n:2d}, k={k}, factors={len(ff)}, Tclasses={len(tgroups)}, Tkclasses={len(groups)}, minones={min(x.count("1") for x in ff)}, same={same}')
    return same, ff, groups, tgroups

def run():
    # Exact list of four-letter bigrams: all internal edges and all possible
    # block-boundary edges are in PAIRS, each appears in phi^4(0).
    base='0'
    for _ in range(4):base=substitute(base)
    assert {base[i:i+2] for i in range(len(base)-1)} == set(PAIRS)
    internal={PHI[c] for c in PHI}
    boundary={PHI[a][-1]+PHI[b][0] for a,b in (tuple(p) for p in PAIRS)}
    assert internal|boundary == set(PAIRS)
    assert equivalence_check(13,2)[0] is False
    assert equivalence_check(14,2)[0] is True
    assert equivalence_check(17,3)[0] is False
    assert equivalence_check(18,3)[0] is True
    for k,n in ((2,14),(3,18)):
        ff=factors(n)
        assert min(w.count('1') for w in ff)>=k
    print('VERIFY_STABILITY_OK')
if __name__=='__main__':run()
