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
# Verification of the Bézout lens profile

The normalized quotient is derived in four exact steps in `RESULT.md`: two projection mixed volumes, a spherical integral for the lens support function, differentiation after division by the transverse projection radius, and a beta endpoint. Each is valid for any integer \(n\ge2\) and all \(0<a<1\). In particular, the strict inequality follows from a negative integrand on a positive-measure interval, not sampling.

Run `python3 verify.py` (Python standard library only) to check dimensions \(2,3,4,5,8,20\) and the parameters \(a=0.001,0.2,0.5,0.8,0.999\). The script avoids the integrable endpoint singularity for dimension \(2\) through the change of variables \(t=\sin\theta\), compares values and derivative signs, and verifies the two closed forms. Relative comparisons near the high-dimensional limiting endpoint allow \(10^{-11}\) floating-point tolerance. Observed output: `VERIFY_OK`.

Numerical integrations are diagnostics, not certificates of infinite-dimensional or continuous-parameter assertions. The limiting coefficient for zonoids has a separate exact mixed-volume proof. No independent audit has been performed.
