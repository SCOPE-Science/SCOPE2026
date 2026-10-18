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

# Verification of the quadratic ETDRK2 claim

The self-contained Python 3 script `verify.py` evaluates the ETDRK2 original predictor--corrector formula and the independently derived amplification for 750 seeded samples, verifies modal stability and necessary large-step violations on 1700 more seeded samples, checks 400 exact integer series coefficients, certifies the rational exponential inequality at the sign-reversal witness, checks the positive-gain example and the exact optimizer against 700 minimax comparisons. The recorded result in `verify_output.txt` is `PASS 3958 deterministic checks; mathematical universality is established by the accompanying analytic proof.`

The proof of the infinite family of coefficient inequalities is by direct inspection of the first five coefficients and positivity of the closed form thereafter. The proof of the full continuous step range uses open strict inequalities and the large-step limit. No finite numerical experiment is used to infer an all-step theorem, nor are checks interpreted as third-party certification.
