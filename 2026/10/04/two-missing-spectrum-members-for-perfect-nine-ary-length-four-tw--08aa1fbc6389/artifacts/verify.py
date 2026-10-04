#!/usr/bin/env python3
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

DATA = Path(__file__).with_name("codes.json")
obj = json.loads(DATA.read_text(encoding="utf-8"))
alphabet = tuple(obj["alphabet"])
assert alphabet == tuple(range(9))
assert obj["word_length"] == 4
assert obj["deletions"] == 2
all_pairs = {(a,b) for a in alphabet for b in alphabet}

def descendants(word):
    assert len(word) == 4
    w = tuple(int(ch) for ch in word)
    assert all(x in alphabet for x in w)
    return {(w[i], w[j]) for i,j in combinations(range(4),2)}

for size_text, words in sorted(obj["codes"].items(), key=lambda kv:int(kv[0])):
    expected = int(size_text)
    assert len(words) == expected
    assert len(set(words)) == expected
    count = Counter()
    total = 0
    for word in words:
        ds = descendants(word)
        total += len(ds)
        count.update(ds)
    assert total == 81, (size_text, total)
    assert set(count) == all_pairs, (size_text, len(count))
    assert all(count[p] == 1 for p in all_pairs), size_text
    print(f"size={expected} descendants={total} covered={len(count)} multiplicities=1")
print("VERIFY_OK")
