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

Execute `python3 verification/check.py`. The self-contained script uses only Python's standard library. Observed output in the completed check:

- 119 exact rational determinant identities for distinct triples.
- Exact recovery of the three independent rates at two rational endemic folds from four states.
- At \(\kappa=4\), predicted \(\lim t^6\det\Phi_t=0.03125\); 60,000-step high-precision iterate produced approximately \(0.0308154170516875\), consistent with the rigorously established limit.

The output checks the implementation but does not establish any infinite asymptotic. Those follow analytically by reciprocal differences, Vandermonde factorization, and singular-value estimates in RESULT.md. The full proof assumes perfect known predictors; stochastic observation noise has not been modeled. This scientific review is not independent certification.
