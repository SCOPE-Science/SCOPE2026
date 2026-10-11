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

# Reproduction and logical limits

Run `python verification.py` in the same directory as this file. It requires Python 3 and its standard library, makes no network requests, and uses deterministic sample values. The script bisection-solves the scalar radius equation, constructs an extremal positive input, checks the conjugate-exponent duality, and tests direct numerical-radius evaluations on normalized real vectors, plus the strict quartic reversal for a finite list of positive unequal weights.

The noncomputational proof appears in `RESULT.md`. Compactness and boundary perturbations ensure an interior maximizer for positive weights; stationarity and strict monotonicity identify its global value. A separate algebraic identity proves the quartic ordering for every positive strict weight pair. The finite program does not establish those infinite statements or a bibliographic novelty claim; it only offers an independently re-runnable arithmetic consistency check. The exact numerical range disk is established by phase isometries and connectedness. No independent mathematical audit has been performed.
