#!/usr/bin/env python3
"""Exact rational verification of finite constrained deletion-code certificates.
Run: python3 verify.py [certificates.json]
"""
import itertools, json, sys
from fractions import Fraction

def words(n):
    return {''.join(t) for t in itertools.product('01', repeat=n) if '11' not in ''.join(t)}

def shadow(word):
    return {word[:i]+word[i+1:] for i in range(len(word))}

def verify(filename):
    data = json.load(open(filename, encoding='utf8'))
    assert set(data['cases']) == {str(i) for i in range(1,8)}
    A = (1,1,2,2,3,3,5)
    F = (1,1,2,2,3,4,6)
    for n in range(1, 8):
        src = words(n)
        sh = {w:shadow(w) for w in src}
        out = set().union(*sh.values())
        row = data['cases'][str(n)]
        code = row['code']
        assert len(code)==A[n-1] and len(set(code))==len(code) and set(code)<=src
        assert all(not (sh[a]&sh[b]) for i,a in enumerate(code) for b in code[i+1:]), ('witness',n)
        if n<=5:
            cover=row['integral_output_cover']
            assert len(cover)==len(set(cover))==A[n-1] and set(cover)<=out
            assert all(sh[w]&set(cover) for w in src), ('cover',n)
        else:
            xp={w:Fraction(v) for w,v in row['fractional_primal'].items()}
            yd={o:Fraction(v) for o,v in row['fractional_dual'].items()}
            assert set(xp)<=src and set(yd)<=out
            assert all(v>=0 for v in xp.values()) and all(v>=0 for v in yd.values())
            assert sum(xp.values()) == F[n-1] == sum(yd.values())
            for output in out:
                assert sum((xp.get(w,0) for w in src if output in sh[w]),Fraction(0))<=1,('primal',n,output)
            for w in src:
                assert sum((yd.get(o,0) for o in sh[w]),Fraction(0))>=1,('dual',n,w)
            cliques=row['weighted_conflict_cliques']
            assert all(isinstance(c['quarter_units'],int) and c['quarter_units']>0 for c in cliques)
            assert sum(c['quarter_units'] for c in cliques) == (15 if n==6 else 23)
            coverage={w:0 for w in src}
            for c in cliques:
                cc=c['words']
                assert len(cc)==len(set(cc)) and len(cc)>0 and set(cc)<=src
                assert all(sh[a]&sh[b] for i,a in enumerate(cc) for b in cc[i+1:]), ('not a clique',n,cc)
                for w in cc: coverage[w]+=c['quarter_units']
            assert all(u>=4 for u in coverage.values()), ('clique cover',n)
        print(f'n={n} source={len(src)} integral={A[n-1]} fractional={F[n-1]} certificate=OK')
    print('VERIFY_OK')

if __name__=='__main__':
    verify(sys.argv[1] if len(sys.argv)>1 else 'certificates.json')
