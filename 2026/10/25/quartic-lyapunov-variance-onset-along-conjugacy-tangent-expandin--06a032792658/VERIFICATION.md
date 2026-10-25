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

The claim follows from an analytic \(C^2\) expansion of the finite smooth conjugation, an explicit uniformly summable symbolic-coding correlation lemma, and exact Fourier orthogonality for the degree-two instance. The ordinary Python 3 verifier `check.py` has no third-party dependencies; run `python3 check.py` from the package directory. The recorded output is `check_output.txt`, and its final line must be `CHECKS_PASS`.

The verifier checks four perturbation sizes and 137 distinct test positions, along with all potentially nonzero doubling-map Fourier correlations using exact fractions. These checks do not certify the asymptotic for all parameter values; that limit is established by the proof in `RESULT.md`. There is no external mathematical or priority audit and no assertion of independent validation.
