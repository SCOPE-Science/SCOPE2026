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

# Reproducibility and limits

Run `python3 semigroup_spectra_verify.py` using standard Python 3; no third-party packages are required. The script enumerates all nonnegative cell-count vectors on the relevant Boolean atoms, evaluates finite defining constraints, and compares the resulting spectrum with independent dynamic-programming semigroup membership.

Observed results:

```
GENERATORS (3, 5) N 12 CELL_VECTORS 125969 SPECTRUM_BITS 001011011111
GENERATORS (2, 3) N 11 CELL_VECTORS 75581 SPECTRUM_BITS 01111111111
GENERATORS (4,) N 16 CELL_VECTORS 4844 SPECTRUM_BITS 0001000100010001
GENERATORS (1,) N 10 CELL_VECTORS 65 SPECTRUM_BITS 1111111111
DISJOINT_UNION_ATOMIC_TESTS 409600
VERIFY_OK
```

Bit strings are indexed from domain size one. The checked vectors sum to 206,459; 409,600 is the count of directly evaluated Boolean-term/atomic-sentence implication instances. The program does not enumerate arbitrary theories or all cardinalities. The proof in `RESULT.md` treats all theories, all finite domain sizes, and all finitely generated additive subsemigroups without relying on bounded enumeration. Originality risk remains possible for unindexed sources; independent validation has not occurred.
