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

# Reproducibility

Use Python 3 standard library from the directory containing the attached files:

```sh
python3 verify.py
```

The output must match `verification_output.txt` exactly. This checks every possible subset on the \(3\)-by-\(n\) board for \(3\le n\le7\), totaling \(2{,}396{,}672\) candidates; the independently implemented shortest-geodesic condition is compared on \(37{,}376\) candidates for \(3\le n\le5\). The script compares the complete predicted all-size visibility polynomial, maximal-set cardinalities, all three maximal families, and the small-case orbit formula under row and column permutations.

There is no computational claim of exhaustive verification for \(n\ge8\), and finite replay is not used as an infinite proof. The complete mathematical proof appears in `RESULT.md`. Neither this reproducibility record nor the self-review constitutes independent scientific validation.
