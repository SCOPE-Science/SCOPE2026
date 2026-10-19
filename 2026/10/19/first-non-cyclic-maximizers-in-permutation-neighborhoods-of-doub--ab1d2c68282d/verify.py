"""Reproduce both complete enumerations and their exact extremal assertions.

Requires only Python 3 with its standard library. Run: python verify.py
"""
import hashlib
import json
import math
import pathlib
import subprocess
import sys

HOME = pathlib.Path(__file__).resolve().parent
EXPECTED = {
    2:(2,['12','21'],2),
    3:(9,['231','312'],9),
    4:(33,['2341','4123'],33),
    5:(134,['34521','54123'],123),
    6:(532,['345621','651234'],508),
}


def call(file,k):
    data = subprocess.check_output(
        [sys.executable,str(HOME/file),str(k)],timeout=120
    )
    return json.loads(data)


def main():
    for k, (target, maximizers, max_cyclic) in EXPECTED.items():
        by_shuffle = call('enumerate_interleavings.py',k)
        by_matching = call('enumerate_pairings.py',k)
        assert by_shuffle == by_matching, f'Independent enumerations disagree at k={k}'
        if k in (5,6):
            table = json.loads((HOME/f'degree_table_k{k}.json').read_text())
            assert by_shuffle == table, f'Packaged degree table differs at k={k}'
        assert len(by_shuffle)==math.factorial(k)
        assert max(by_shuffle.values())==target
        assert sorted(p for p,d in by_shuffle.items() if d==target)==maximizers
        assert by_shuffle[''.join(str(i) for i in range(1,k+1))] == math.comb(2*k,k)//(k+1)
        rotations = {''.join(str((i+j)%k+1) for i in range(k)) for j in range(k)}
        assert max(by_shuffle[p] for p in rotations)==max_cyclic
        # Both independently count each labeled pair partition once.
        assert sum(by_shuffle.values())==sum(by_matching.values())
        digest = hashlib.sha256(json.dumps(by_shuffle,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        print(f'k={k}  vertices={math.factorial(k)}  maximum={target}'
              f'  maximizers={maximizers}  best_cyclic={max_cyclic}'
              f'  sum_degrees={sum(by_shuffle.values())}  sha256_degrees={digest}')
    print('ALL_FINITE_THEOREMS_VERIFIED')

if __name__=='__main__':main()
