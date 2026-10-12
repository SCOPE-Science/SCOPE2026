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

The proof uses exact Weibull moments and the exact unit-rate survival function. The key asymptotic input is the logarithmic Stirling expansion for \(\Gamma(2r+1)\); the term \(\Gamma(r+1)^2/\Gamma(2r+1)\) is exponentially small and therefore does not affect the additive \(o(1)\) exponent needed for a multiplicative tail equivalent.

`verify_weibull_profile.py` independently evaluates the exact logarithmic probability from `loggamma` arithmetic for several small shapes and thresholds, then compares it with the asymptotic logarithm and the predicted two-threshold ratio. Its successful output is:

`VERIFY_OK alpha_min=0.00625 max_terminal_log_error=0.0156609494975 ratio_rel_error=0.012273215192`

The finite calculations check implementation and normalization only. They do not prove the limit, local uniformity, or absence of competing literature. No statement is made for thresholds that move to zero or infinity with the shape parameter.
