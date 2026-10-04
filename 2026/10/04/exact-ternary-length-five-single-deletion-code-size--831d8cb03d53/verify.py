#!/usr/bin/env python3
from itertools import product
import json
from pathlib import Path

Q = 3
N = 5
SCALE = 14
WITNESS = [
    '00000','00011','00022','00120','01110','01212','02021','02100',
    '02220','10102','10211','11000','11111','11122','11201','12020',
    '12221','20101','21022','21210','22000','22012','22111','22222'
]
WEIGHTS = {
'0000':14,'0001':5,'0002':5,'0010':3,'0011':9,'0012':4,'0020':3,'0021':4,'0022':9,
'0100':3,'0101':2,'0102':2,'0110':4,'0111':5,'0112':4,'0120':4,'0121':2,'0122':4,
'0200':3,'0201':2,'0202':2,'0210':4,'0211':4,'0212':2,'0220':4,'0221':4,'0222':5,
'1000':5,'1001':4,'1002':4,'1010':2,'1011':3,'1012':2,'1020':2,'1021':4,'1022':4,
'1100':9,'1101':3,'1102':4,'1110':5,'1111':14,'1112':5,'1120':4,'1121':3,'1122':9,
'1200':4,'1201':4,'1202':2,'1210':2,'1211':3,'1212':2,'1220':4,'1221':4,'1222':5,
'2000':5,'2001':4,'2002':4,'2010':2,'2011':4,'2012':4,'2020':2,'2021':2,'2022':3,
'2100':4,'2101':2,'2102':4,'2110':4,'2111':5,'2112':4,'2120':2,'2121':2,'2122':3,
'2200':9,'2201':4,'2202':3,'2210':4,'2211':9,'2212':3,'2220':5,'2221':5,'2222':14,
}

def shadow(w):
    return {w[:i] + w[i+1:] for i in range(len(w))}

all4 = {''.join(map(str,x)) for x in product(range(Q), repeat=N-1)}
all5 = [''.join(map(str,x)) for x in product(range(Q), repeat=N)]
assert set(WEIGHTS) == all4
assert len(WITNESS) == 24 and len(set(WITNESS)) == 24
assert all(len(w) == N and set(w) <= set('012') for w in WITNESS)

used = set()
for w in WITNESS:
    s = shadow(w)
    assert used.isdisjoint(s), (w, sorted(used & s))
    used |= s

min_cover = min(sum(WEIGHTS[z] for z in shadow(w)) for w in all5)
assert min_cover >= SCALE
weight_sum = sum(WEIGHTS.values())
assert weight_sum == 348
# Dual certificate: every codeword consumes at least 14 units of shadow weight;
# disjoint shadows have total available weight 348. Hence 14|C| <= 348,
# so |C| <= floor(174/7) = 24.
assert 24 * SCALE <= weight_sum < 25 * SCALE

cert = {
    'schema_version': 1,
    'alphabet_size': Q,
    'word_length': N,
    'witness_size': len(WITNESS),
    'distinct_shadow_outputs_used_by_witness': len(used),
    'dual_scale': SCALE,
    'dual_integer_weight_sum': weight_sum,
    'dual_rational_objective': '174/7',
    'minimum_scaled_shadow_weight_over_all_243_words': min_cover,
    'checked_words': len(all5),
    'checked_shadow_vertices': len(all4),
    'upper_bound': 24,
    'output': 'VERIFY_OK N(5,3,1)=24 dual=174/7 min_scaled_shadow_weight=14'
}
Path(__file__).with_name('certificate.json').write_text(json.dumps(cert, indent=2, sort_keys=True)+'\n', encoding='utf-8')
print(cert['output'])
