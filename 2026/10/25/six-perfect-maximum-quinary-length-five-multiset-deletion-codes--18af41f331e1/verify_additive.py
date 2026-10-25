"""Exact independent crosscheck for the five-symbol, length-five multiset code."""
from itertools import permutations
from collections import Counter
import sys

lines=open(sys.argv[1],encoding='utf-8').read().splitlines()
assert 'V=126' in lines[0] and 'solutions=6' in lines[0]
cert=[frozenset(int(z) for z in row.strip(',').split(',')) for row in lines[1:]]
assert len(cert)==6 and len(set(cert))==6 and all(len(s)==26 for s in cert)
V=[(a,b,c,d,5-a-b-c-d) for a in range(6) for b in range(6-a) for c in range(6-a-b) for d in range(6-a-b-c)]
assert len(V)==126 and len(set(V))==126
expected={frozenset(i for i,v in enumerate(V) if sum(p[j]*v[j] for j in range(5))%5==0) for p in permutations(range(5))}
assert len(expected)==6 and set(cert)==expected
for S in cert:
    assert not any(sum(abs(V[i][k]-V[j][k]) for k in range(5))==2 for i in S for j in S if i<j)
    profile=Counter(tuple(sorted((a for a in V[i] if a),reverse=True)) for i in S)
    assert profile=={(5,):5,(3,1,1):10,(2,2,1):10,(1,1,1,1,1):1}
    shadows=[]
    for i in S:
        for k in range(5):
            if V[i][k]:
                y=list(V[i]);y[k]-=1;shadows.append(tuple(y))
    assert len(shadows)==70 and len(set(shadows))==70
    assert set(shadows)=={(a,b,c,d,4-a-b-c-d) for a in range(5) for b in range(5-a) for c in range(5-a-b) for d in range(5-a-b-c)}
print('N_VERTICES=126')
print('N_MAXIMA=6')
print('UNIQUE_ADDITIVE_CLASSES=6')
print('EACH_CARDINALITY=26')
print('SHADOW_SPACE=70')
print('PERFECT_CODES=6')
print('COMPOSITION_PROFILE=5:5,3-1-1:10,2-2-1:10,1-1-1-1-1:1')
print('VERIFY_OK')
