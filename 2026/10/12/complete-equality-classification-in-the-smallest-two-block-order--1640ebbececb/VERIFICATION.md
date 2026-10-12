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

The proof of the general statement is symbolic and does not depend on finite enumeration. The supplied checker performs two finite consistency tests.

For \(q=2\), it reconstructs all sixteen ambient words, exhaustively checks every subset, confirms that the maximum size is \(4\), finds exactly sixteen labeled maxima, verifies that all are affine two-flats, and verifies one orbit under the natural affine ordered-metric isometry group.

For \(q=3\), it constructs every one of the \((3!)^6=46{,}656\) codes specified by the permutation classification, checks that the codes are distinct, and verifies minimum ordered distance at least \(3\) for each. This is a check of the constructive side and the count, not an exhaustive search through all \(9\)-subsets of the \(81\)-word ambient space. The converse for general \(q\) is established by the projection argument in RESULT.md.
