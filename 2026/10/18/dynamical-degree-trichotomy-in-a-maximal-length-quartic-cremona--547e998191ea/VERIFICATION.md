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

# Verification record

The self-contained `verify.py` file uses integer-coefficient bivariate sparse polynomials and Python's standard library. Executing `python3 verify.py` checks the shear/inverse identities, the normal-form conjugacy at five parameter points, sample Hénon degree growth, diagonal double-iterate degrees, and an exact order-four quartic example. No numerical approximation is used.

The infinite classification relies on an explicit symbolic identity and degree domination induction; the bounded symbolic replay is not an exhaustive test of nonzero complex parameter pairs or of all iterates. The ordinary quadratic length \(7\) is used as the published theorem of Calabri--Giao (arXiv:2610.08416, Theorem 1.3), not recomputed from an algorithm. No independent audit has been performed.
