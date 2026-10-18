"""Direct position-by-position certificate check of the three representative cycles."""
import json
import itertools
from pathlib import Path

witnesses = json.loads(Path(__file__).with_name('witnesses.json').read_text(encoding='utf-8'))
allowed = {''.join(t) for t in itertools.product('012', repeat=5)
           if all(t[j] != t[j+1] for j in range(4))}
assert len(allowed) == 48
for requested, w in sorted(witnesses.items()):
    assert len(w) == 48 and set(w) == set('012')
    assert [w.count(ch) for ch in '012'] == [16, 16, 16]
    assert all(w[j] != w[(j + 1) % 48] for j in range(48))
    windows = [''.join(w[(j + h) % 48] for h in range(5)) for j in range(48)]
    assert len(set(windows)) == 48 and set(windows) == allowed
    maximum = 0
    for start in range(48):
        freq = [0, 0, 0]
        for length in range(1, 49):
            freq[int(w[(start + length - 1) % 48])] += 1
            maximum = max(maximum, max(freq) - min(freq))
    assert maximum == int(requested)
    print(f'WITNESS_OK discrepancy={requested} length=48')
print('VERIFY_WITNESSES_OK')
