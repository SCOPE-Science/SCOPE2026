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
# Verification of the three-flow digit-aliasing theorem

The `check.py` program uses exact rational binary radical-inverse samples and exact rational upper-triangular matrix multiplication. It asserts the shuffle identities and the finite-step product identity for each integer \(1\le N\le128\), with no numerical tolerance, and reports larger-prefix diagnostics. Execute `python3 check.py` after extracting this package.

A finite checker cannot establish the all-\(N\) digit count or the infinite limiting error. Those follow from the dyadic interval partition, the Taylor/commutator expansion, an Abel summation bound, and the exact witness formula in RESULT.md. The test does not characterize other shuffle conventions, generators, or unbounded operators.
