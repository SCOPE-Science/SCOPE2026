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
The proof derives the lattice central-probability expansion from Stirling's formula and the midpoint correction, then expands it along the parity-constrained sample sizes. The standalone `verify.py` recomputes all ten exact phase coefficients and exact binomial probabilities on a finite stress range.

The finite enumeration is not evidence for the infinite quantifier. Eventual positivity follows from the uniform asymptotic remainder and the minimum leading coefficient \(3/4\). No least eventual-monotonicity index is certified.
