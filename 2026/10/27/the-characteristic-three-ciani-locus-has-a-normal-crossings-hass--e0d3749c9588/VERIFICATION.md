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

# Reproducibility and verification

The included `check.py` is a standalone Python 3 program with no nonstandard packages. Run `python3 check.py` from the package directory. It exhaustively checks the parameter counts in \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\), reconstructs the characteristic-three coefficient identities symbolically, and checks explicit representatives of all four Jacobian rank strata over \(\mathbb F_9\). It also counts rational points on those example curves, providing a separate consistency check on the trace interpretation.

Expected parameter-count output: for \(q=3\), ranks \((0,1,2,3)\) have counts \((1,0,0,0)\); for \(q=9\), \((1,18,72,216)\); for \(q=27\), \((1,72,1584,13392)\). The checker ends with `ALL_CHECKS_OK`.

The proofs of smoothness, the simultaneous rank classification, normal crossings and all-\(q\) formulas are in RESULT.md. No finite enumeration constitutes proof for arbitrary \(n\). Historical novelty is qualified in REVIEW.md; independent scientific audit has not been performed.
