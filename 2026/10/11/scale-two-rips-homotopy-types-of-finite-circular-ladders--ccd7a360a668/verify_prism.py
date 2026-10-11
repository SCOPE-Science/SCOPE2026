"""Exact finite checks for the scale-two clique complexes of cyclic prism graphs.

Requires only Python 3's standard library. Read cert_small.json and cert_orbits.json
from the same directory. The all-parameter claim also uses the symbolic facet and
free-face analysis in RESULT.md; finite checks are corroborating evidence only.
"""
import collections
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def distance(n, v, w):
    i, a = divmod(v, 2)
    j, b = divmod(w, 2)
    return min((i-j)%n, (j-i)%n) + int(a != b)


def adjacency(n):
    count = 2*n
    return [set(j for j in range(count) if j != i and distance(n,i,j) <= 2) for i in range(count)]


def max_cliques(n):
    adj = adjacency(n)
    out = []
    def bk(R, P, X):
        if not P and not X:
            out.append(tuple(sorted(R)))
            return
        u = max(P|X, key=lambda z:len(P & adj[z])) if P|X else None
        for v in sorted(P - (adj[u] if u is not None else set())):
            bk(R|{v}, P & adj[v], X & adj[v]); P.remove(v);X.add(v)
    bk(set(),set(range(2*n)),set())
    return sorted(out)


def allfaces(n):
    return set(frozenset(comb) for facet in max_cliques(n)
       for k in range(1,len(facet)+1) for comb in itertools.combinations(facet,k))


def cycface(n, pairs, offset):
    return frozenset(2*((i+offset)%n)+a for i,a in pairs)


def collapse(faces,a,b,tag):
    assert a in faces and b in faces and a < b and len(a)+1==len(b),(tag,'not incident')
    superfaces = [c for c in faces if a < c]
    assert superfaces==[b],(tag,'not free',superfaces)
    faces.remove(a);faces.remove(b)


def mod2rank(rows):
    piv={}
    for x in rows:
        while x:
            k=x.bit_length()-1
            if k not in piv:
                piv[k]=x;break
            x^=piv[k]
    return len(piv)


def betti(n):
    faces=allfaces(n)
    by=collections.defaultdict(list)
    for f in faces:by[len(f)-1].append(tuple(sorted(f)))
    rank={0:1} # augmented d_0 (reduced chain complex)
    for k in range(1,max(by)+1):
        index={f:i for i,f in enumerate(by[k-1])}
        rows=[sum(1<<index[face[:j]+face[j+1:]] for j in range(len(face))) for face in by[k]]
        rank[k]=mod2rank(rows)
    b={k:len(by[k])-rank[k]-rank.get(k+1,0) for k in by}
    return {k:v for k,v in b.items() if v}, dict(sorted((k,len(v)) for k,v in by.items()))


def test_small():
    cert=json.loads((ROOT/'cert_small.json').read_text())
    expect={3:{},4:{3:1},5:{2:1},6:{2:3}}
    fvec={3:[6,15,20,15,6,1],4:[8,24,32,16],5:[10,35,50,25,2],6:[12,42,52,18]}
    for n in (3,4,5,6):
        b,f=betti(n)
        assert b==expect[n],(n,'betti',b)
        assert [f.get(j,0) for j in range(max(f)+1)]==fvec[n],(n,'fvec',f)
        if n in (5,6):
            faces=allfaces(n)
            for index,(a,b) in enumerate(cert[str(n)]):
                collapse(faces,frozenset(a),frozenset(b),('small',n,index))
            assert max(map(len,faces))==3,('small residual not 2-complex',n)
    return len(cert['5']),len(cert['6'])


def symbolic_phase_check():
    """Universal local freeness check, using integer rather than cyclic columns.

    All possible cofacets of any free face contain its column-zero anchor.
    Facets through the anchor are supported within [-2,2], and any
    earlier orbit removal through that anchor is supported within [-3,3].
    This band embeds without collisions modulo n for every n >= 7.
    """
    specs=json.loads((ROOT/'cert_orbits.json').read_text())
    def pairs(spec): return frozenset(tuple(q) for q in spec)
    for phase, spec in enumerate(specs):
        a=pairs(spec['free']); b=pairs(spec['cofacet'])
        anchor=next(v for v in a if v[0]==0)
        facets=[]
        for center in (-1,0,1):
            for row in (0,1):
                f=pairs([(center-1,row),(center,row),(center+1,row),(center,1-row)])
                if anchor in f:facets.append(f)
            f=pairs([(center,0),(center+1,0),(center,1),(center+1,1)])
            if anchor in f:facets.append(f)
        cofaces={frozenset(sub) for f in facets
                   for k in range(1,len(f)+1)
                   for sub in itertools.combinations(f,k) if a<=set(sub)}
        for prior in specs[:phase]:
            for name in ('free','cofacet'):
                template=pairs(prior[name])
                for u,row in template:
                    if row==anchor[1]:
                        shifted=frozenset((v-u,w) for v,w in template)
                        cofaces.discard(shifted)
        assert cofaces=={a,b},('symbolic failure',phase,cofaces)
    return True


def test_family():
    specs=json.loads((ROOT/'cert_orbits.json').read_text())
    count=0
    for n in range(7,31):
        faces=allfaces(n)
        facet_expected=set()
        for i in range(n):
            for row in (0,1):
                facet_expected.add(cycface(n,[(-1,row),(0,row),(1,row),(0,1-row)],i))
            facet_expected.add(cycface(n,[(0,0),(0,1),(1,0),(1,1)],i))
        assert set(map(frozenset,max_cliques(n)))==facet_expected,('facet classification',n)
        for phase,spec in enumerate(specs):
            for i in range(n):
                a=cycface(n,spec['free'],i)
                b=cycface(n,spec['cofacet'],i)
                collapse(faces,a,b,('orbit',n,phase,i))
                count+=1
        target={frozenset((2*i,)) for i in range(n)}|{frozenset((2*i,2*((i+1)%n))) for i in range(n)}
        assert faces==target,('not outer circle',n)
    return count

if __name__=='__main__':
    s=test_small(); local=symbolic_phase_check(); t=test_family()
    print(f'VERIFY_OK small_collapses={s[0]}+{s[1]} universal_local={local} orbit_collapses={t} n=7..30')
