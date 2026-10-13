"""Independent standard-library verification of a five-cell ternary code."""
from pathlib import Path
from itertools import product

HERE = Path(__file__).resolve().parent.parent
CODE = (HERE / "data" / "codewords.txt").read_text(encoding="utf-8").splitlines()
assert len(CODE) == 45 and len(set(CODE)) == len(CODE)
ALL = {''.join(p) for p in product('012', repeat=5)}
assert set(CODE) <= ALL and len(ALL) == 243

def ball(x):
    out = {x}
    for j, c in enumerate(x):
        if c != '0':
            y = list(x)
            y[j] = str(int(c)-1)
            out.add(''.join(y))
    return out

seen = {}
for x in CODE:
    for y in ball(x):
        if y in seen:
            raise AssertionError((seen[y], x, y))
        seen[y] = x
assert len(seen) > len(CODE)
print(f'CODE_OK size={len(CODE)} distinct_received={len(seen)}')
