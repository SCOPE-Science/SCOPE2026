---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

`verify_pairs.py` uses only Python 3 standard library. Run it in a directory containing that file:

```text
python3 verify_pairs.py
```

Actual replay on the packaged version returned `VERIFY_OK`. For each integer \(3\le n\le22\), the script constructs all unordered pairs, compares the explicit distance ranking against an independently computed reverse breadth-first-search metric, verifies the unique descending action and minimal upward-jump structure, computes exact word counts for every pair and all claimed slack lengths using dynamic programming, and checks the first correction at the hardest pair. Literal alphabet-word enumeration supplies a separate check for \(3\le n\le5\); the two-state boundary is also checked. The program does not prove the result for arbitrary \(n\): that coverage is furnished by the symbolic case analysis in RESULT.md. No independent audit has been conducted.
