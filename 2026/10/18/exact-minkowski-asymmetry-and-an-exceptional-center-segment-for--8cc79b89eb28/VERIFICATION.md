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

The mathematical proof is in `RESULT.md`. Its central universal steps are the exact layer-cake representation of nonnegative vectors as weighted interval indicators, the reflection-containment identity, the sharp lower bound obtained by adding two alternating-triple inequalities, and the quadruple equality analysis that determines every minimizing center. Each step is justified algebraically, and the finite four-dimensional endpoint list is exhaustive (zero plus ten nonempty intervals).

The standalone `verify_interval_asymmetry.py` uses only Python's standard library `fractions.Fraction`. Running `python3 verify_interval_asymmetry.py` produces `EXACT_REFLECTION_OK dimensions=2..18 checks=1167`, `LOWER_BOUND_CERTIFICATE_OK dimensions=2,3,4..18`, the eleven integer positive-variation values, and `VERIFY_OK`. This was replayed from the packaged script. The finite calculation verifies the proposed reflected vertices at the listed dimensions and the second endpoint of the exceptional segment; it does not prove the infinite-dimensional result or the originality claim.

The affine-invariant Minkowski asymmetry and its center locus are different from the Euclidean Chebyshev-center and inradius classification available for the same polytope. The relevant published primary constructions were compared on definitions, not on titles alone. Unindexed or differently expressed historical statements are a residual bibliographic risk.
