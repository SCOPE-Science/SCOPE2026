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

The standalone `verify.py` constructs the two-particle cubical cell sets for subdivided banana graphs and computes fixed-cell traces with the correct orientation signs. It checks all \(672\) group elements tested in dimensions \(m=3,4,5\) and a selected subset at \(m=6\); it does not prove the infinite-family theorem. The general proof separately establishes degree-two boundary injectivity and uses the Hopf trace identity. Reproduce with `python3 verify.py` using Python's standard library. The expected success marker is `BANANA_TWO_POINT_EQUIVARIANT_CHARACTERS_VERIFIED 672`.

Higher-degree integral homology vanishing follows from the injectivity argument for the two-cell boundary, not from these finite tests. No independent mathematical audit has been conducted.
