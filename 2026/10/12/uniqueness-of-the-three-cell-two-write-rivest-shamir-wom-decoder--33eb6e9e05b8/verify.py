from collections import Counter
from hashlib import sha256
from itertools import product
from math import prod

states = range(8)
messages = range(4)
up = [[y for y in states if x | y == y] for x in states]
first = [x for x in states if len(up[x]) >= 4]
decoders = []
common_tables = Counter()
separate_tables = Counter()
for f in product(messages, repeat=8):
    if len({f[x] for x in first}) != 4:
        continue
    if any(len({f[y] for y in up[x]}) < 4 for x in first):
        continue
    assert all(f[x] == f[7-x] for x in states)
    decoders.append(f)
    initial = [next(x for x in first if f[x] == m) for m in messages]
    n = prod(sum(f[y] == m for y in up[x]) for x in first for m in messages)
    k = prod(sum(f[y] == m and (x != 0 or y == initial[m]) for y in up[x])
             for x in first for m in messages)
    separate_tables[n] += 1
    common_tables[k] += 1
assert len(decoders) == 24 and first == [0,1,2,4]
assert common_tables == {1:24} and separate_tables == {16:24}
digest = sha256(''.join(''.join(map(str,r))+'\n' for r in decoders).encode()).hexdigest()
assert digest == '9afddc5cdab8eeea0ca83cf1d4d5261165fd40795d7cc7648cf413d982201081'
print('VERIFY_OK functions=65536 decoders=24 common_tables_per_decoder=1 '
      'separate_second_tables_per_decoder=16 decoder_sha256='+digest)
