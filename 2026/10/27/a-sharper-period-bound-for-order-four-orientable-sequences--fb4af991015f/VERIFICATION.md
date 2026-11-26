---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Checks and limits

For the universal bound, count the reversal-pairs after removing palindromes, check the divergence of the omitted pairs on \(P=\{aab:a\ne b\}\), and use parity at the uniform vertices. Ordinary cyclic-window uniqueness and absence of reverse matches are both required before counting \(2m\) distinct edges in the sequence and its reversal. The proof of the upper bound does not require a computation.

For the two exact cases, obtain `witness.txt` from each of references [5, 6] in `RESULT.md`. The following standalone check accepts the file paths as command-line arguments, in quaternary and six-symbol order respectively:

```python
from pathlib import Path
from sys import argv

assert len(argv) == 3
for path, k, m in zip(argv[1:], (4, 6), (106, 603)):
    s = Path(path).read_text().strip()
    assert len(s) == m and set(s) <= set('012345'[:k])
    cyclic = s + s[:3]
    windows = [cyclic[i:i+4] for i in range(m)]
    assert all(w != w[::-1] for w in windows)
    assert len({min(w, w[::-1]) for w in windows}) == m
    print(k, m)
```

The expected lines are `4 106` and `6 603`. This verifies attainment only at the two stated alphabet sizes, not optimality of the general formula for all even alphabets.
