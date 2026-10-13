"""Independent direct verification of the five shortest blocked-gap witnesses."""
import json
from pathlib import Path

def has_square(w):
    for half in range(1, len(w)//2 + 1):
        for start in range(len(w) - 2*half + 1):
            if w[start:start+half] == w[start+half:start+2*half]:
                return True
    return False

for item in json.loads(Path(__file__).with_name("witnesses.json").read_text(encoding="utf-8"))["witnesses"]:
    q, w, pos = item["alphabet_size"], item["word"], item["blocked_gap_zero_based"]
    assert sorted(set(w)) == [str(i) for i in range(q)]
    assert not has_square(w)
    assert 0 <= pos <= len(w)
    for symbol in map(str, range(q)):
        assert has_square(w[:pos] + symbol + w[pos:])
    print(f"q={q} length={len(w)} gap={pos} direct_insertions={q} checked")
print("VERIFY_OK direct_witness_insertions")
