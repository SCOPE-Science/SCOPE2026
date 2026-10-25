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

# Reproduction and limits

The proof is entirely analytic and is given in `RESULT.md`. In particular, the coefficient extraction is justified by local finiteness and the integral-test bound for the tail of the zeta series; numerical samples are not relied upon to prove a statement about all integers.

Run `python verify.py` using Python 3 and the `mpmath` package. The script solves the exact defining equation by bisection with 90-digit working precision for \(M=10^4,10^6,10^8,10^{10},10^{12}\). It checks that the residual after all six explicit terms, multiplied by \(M^{\log_2(7/2)}\), stays below 3 in absolute value for the tested values. This is a finite consistency test of the derived coefficients and not a certified uniform error constant.

The computation does not evaluate arbitrary coefficients of the all-orders formal expansion; these are defined uniquely and constructively by the extraction recursion in the proof. No independent audit or external validation is asserted.
