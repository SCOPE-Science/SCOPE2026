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

The standalone Python 3 checker is `verification/verify.py` and requires only the Python standard library. From the directory containing this file and the `verification` subdirectory, execute `python3 verification/verify.py`.

Actual execution produced `VERIFY_OK: 2131008 fully enumerated masks, 1950012 sparse candidates, 45 threshold checks`.

The graph-level algorithm builds all \(\binom n2\) vertices as two-element sets, constructs their closed neighborhoods using equality or disjointness, and directly determines domination via the union of closed neighborhoods. It is logically different from the inclusion-exclusion formula, which is evaluated separately with exact integer arithmetic.

Full enumeration: all subsets for \(n=4,5,6,7\) (64 + 1,024 + 32,768 + 2,097,152 = 2,131,008 masks). Restricted enumeration: all subsets of cardinalities \(3\), \(4\), and \(5\) for \(n=8,9,10\) (1,950,012 candidates). Also checked the predicted boundary and saturation coefficient identities at 45 values \(n=5,\ldots,49\). Each comparison passed.

Finite checks do not prove an infinite theorem. The general argument is the explicit classification of failure-witness intersections and inclusion-exclusion given in RESULT.md. No independent mathematical audit or formal proof certification has been performed.
