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

# Reproduction

Run `python3 verify_positive_tail.py` with Python 3 (standard library only). The terminal line must be `CHECK_OK`. This script checks 165 exact-rational three-node cases, positivity against the analytic inequalities, the explicit inverse matrix and moment identities, 12 positive coalescence families, the analytic integral constant against independent numerical integration, and thin-tube importance integration at three thresholds.

# Verification limits

Finite rational cases and stochastic/numerical probes cannot establish a limiting tail formula. The analytic density calculation, collision geometry, uniform local bounds and dominated-convergence passage in `RESULT.md` are the proof. The Frobenius norm uses the monomial moment coordinate normalization; the result is about weight sensitivity to moment perturbations, not integrand-sample-noise conditioning. An independent scientific audit has not been performed.
