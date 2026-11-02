#!/usr/bin/env python3
"""Independent denominator-cleared integer arithmetic certificate check."""
import json
from itertools import product
from fractions import Fraction
from math import lcm
from pathlib import Path

rows=json.loads(Path(__file__).with_name('CERTIFICATES.json').read_text())['certificates']
for row in rows:
    w=tuple(int(c) for c in row['pattern'])
    S=max(w)+1
    vals=[Fraction(row['initial'])]+[Fraction(x) for x in row['row0']+row['row1']]
    den=lcm(*(x.denominator for x in vals))
    initial=int(vals[0]*den)
    a=[int(Fraction(x)*den) for x in row['row0']]
    b=[int(Fraction(x)*den) for x in row['row1']]
    def numerator(word):
        X=initial
        d=den
        for letter in word:
            X=b[letter]*d+(a[letter]-b[letter])*X
            d *= den
        return X
    tgt=numerator(w)
    vals=[numerator(z) for z in product(range(S),repeat=4) if z != w]
    assert tgt > max(vals),row['pattern']
    assert Fraction(tgt-max(vals),den**5)==Fraction(row['exact_gap'])
    print(row['pattern'], 'strict maximum, integer numerator margin',tgt-max(vals),'scale',den**5)
print('PASS: independent integer arithmetic certificates')
