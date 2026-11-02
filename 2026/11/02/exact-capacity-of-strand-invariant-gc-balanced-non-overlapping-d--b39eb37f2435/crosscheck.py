"""Alternative numeric encoding verifier (separate from string-prefix checker).
Usage: python crosscheck.py [certificate.json]
"""
import json,itertools,sys,pathlib
COMPLEMENT=(3,2,1,0)
ALPHABET='ACGT'
N=5

def reverse_complement(q):
    v=0
    for i in range(N):
        v=(v<<2) | COMPLEMENT[(q>>(2*i)) & 3]
    return v

def encode(word):
    v=0
    for c in word:
        v=(v<<2)|ALPHABET.index(c)
    return v

def gc(v):
    return sum(((v>>(2*i)) & 3) in (1,2) for i in range(N))

def conflicting(x,y):
    # Leading k letters of x equal trailing k letters of y.
    return any((x>>(2*(N-k)))==(y & ((1<<(2*k))-1)) for k in range(1,N))

def two_orbits_conflict(p,q):
    a=(p,reverse_complement(p)); b=(q,reverse_complement(q))
    return any(conflicting(x,y) or conflicting(y,x) for x in a for y in b)

def run(path):
    doc=json.loads(pathlib.Path(path).read_text('utf-8'))
    allwords=[i for i in range(4**N) if gc(i) in (2,3)]
    assert len(allwords)==640
    reps={min(x,reverse_complement(x)) for x in allwords}
    assert len(reps)==320
    good={x for x in reps if not any(conflicting(a,b) for a in (x,reverse_complement(x))
                                        for b in (x,reverse_complement(x)))}
    assert len(good)==120
    entries=doc['candidate_orbits']
    colors={encode(e['representative']):e['color_class'] for e in entries}
    assert set(colors)==good
    for x,y in itertools.combinations(colors,2):
        if colors[x]==colors[y]:
            assert two_orbits_conflict(x,y)
    chosen=[encode(w) for w in doc['witness_representatives']]
    assert len(chosen)==12 and len(set(chosen))==12
    assert set(chosen)<=good
    assert all(not two_orbits_conflict(x,y) for x,y in itertools.combinations(chosen,2))
    assert len({y for x in chosen for y in (x,reverse_complement(x))})==24
    print('CROSSCHECK_OK: numeric masks, 120 valid orbits, 12 incompatibility cliques, 24-word witness')

if __name__=='__main__':run(sys.argv[1] if len(sys.argv)>1 else pathlib.Path(__file__).with_name('certificate.json'))
