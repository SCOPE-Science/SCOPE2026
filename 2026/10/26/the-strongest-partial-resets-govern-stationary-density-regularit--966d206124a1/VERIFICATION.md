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

# Reproducibility and verification limits

Run `python3 verify.py` using standard Python 3 and compare its result with `verify_output.txt`. The checks use exact rational arithmetic for independent-mark enumeration, renewal recursion, deterministic contraction bounds and moment-balance identities. Numeric tests of a finite-product logarithmic asymptotic are separate sanity checks.

The test verifies 223 assertions; it does not prove the infinite Fourier limit, \(C^\infty\) regularity, or nonanalyticity. Those statements depend on the limiting comparisons, Fourier inversion and positive-integrand Laplace argument stated in `RESULT.md`. The exact cusp coefficient follows from a derivative jump of the Laplace density and the zero mass of a contracted continuously distributed random variable. The numerical cusp diagnostic is corroborative only.

The independent audit has not been performed. The prior-work assessment is subject to historical-priority uncertainty, particularly possible general perpetuity smoothing theorems beyond the inspected primary sources.
