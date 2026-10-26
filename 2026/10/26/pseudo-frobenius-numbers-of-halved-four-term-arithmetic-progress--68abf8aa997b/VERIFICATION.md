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

# Verification

Run `python3 verify.py` with Python 3 standard library. The observed output was:

```
PASS: parameter pairs 1550
PASS: independent quotient membership comparisons 2697707
PASS: complete Apéry, Frobenius and pseudo-Frobenius comparisons 1550
```

The verifier constructs separate shortest-path residue graphs for the original four-generator semigroup and the claimed three-generator quotient, checks the exact quotient membership implication in both directions, and independently enumerates complete Apéry and pseudo-Frobenius sets for every coprime odd pair with `5 <= a < 100` and `1 <= d < 80`. The finite scan does not prove the unrestricted result. The proof in `RESULT.md` establishes it using parity decomposition, the strict Apéry staircase, and maximal-element criteria.

The full 2024 Lee–Nam article could not be inspected, so a general prior-work implication remains a publication-priority risk. No external independent audit is claimed.
