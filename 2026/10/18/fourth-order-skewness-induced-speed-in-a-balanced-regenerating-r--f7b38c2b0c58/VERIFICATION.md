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

# Reproducibility and mathematical limits

Run `python verify.py` with `sympy>=1.12` as listed in `requirements.txt`. The script performs 6 exact symbolic polynomial verifications of the frozen site-walk expectations and 18 independent exact-rational tests via site-environment enumeration and conditional Markov dynamics. All assertions passed in the recorded in-package execution. No internet service, randomized hypothesis test, or external certificate is used.

The path-word formula in RESULT.md enumerates **all** finite paths for each needed length, so the polynomial equalities are finite exhaustive proofs. The almost-sure speed identity and the sixth-order error bound are demonstrated analytically; finite tests alone are not used to infer them.

Limits: no global refresh-rate monotonicity, no quenched CLT, and no sign statement when the environment's centered third moment vanishes. The underlying general renewal identity is prior literature. These are self-review, not an independent audit.
