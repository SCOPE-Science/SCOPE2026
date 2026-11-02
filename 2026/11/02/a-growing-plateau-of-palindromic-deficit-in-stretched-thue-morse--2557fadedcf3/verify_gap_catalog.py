"""Verify the exact length-three Thue--Morse one-to-one gap catalogue."""
from itertools import product

def morph(s):
    return ''.join('01' if a == '0' else '10' for a in s)

b = {'0': '0', '1': '1'}
for _ in range(4):
    b = {a:morph(w) for a,w in b.items()}
witness_blocks = [b[a]+b[c] for a in '01' for c in '01']
assert all(len(w)==32 for w in witness_blocks)
assert '000' not in ''.join(witness_blocks) and all('000' not in w for w in witness_blocks)
expected = {(0,1,2), (0,2,0), (0,2,1), (1,0,1), (1,0,2),
            (1,2,0), (1,2,1), (2,0,1), (2,0,2), (2,1,0)}
actual = {g for g in product(range(3),repeat=3)
          if any('1'+''.join('0'*r+'1' for r in g) in w
                 for w in witness_blocks)}
assert actual == expected, (actual-expected,expected-actual)
print('PASS: exact catalogue of 10 gap triples and absence of 000 from four 32-symbol blocks.')
print('Triples:',sorted(actual))
