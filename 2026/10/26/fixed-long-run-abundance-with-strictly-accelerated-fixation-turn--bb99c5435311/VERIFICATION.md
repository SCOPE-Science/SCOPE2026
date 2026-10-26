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

The accompanying `verify.py` is self-contained and requires only Python 3.9 or later. Run `python verify.py` from the extracted directory. The local verification completed 30,568 assertions successfully. It checks independently sampled hypergeometric payoffs against the telescoped binomial kernel for integer populations and exact rational parameters, verifies all nonnegative derivative coefficients and their support, computes defecting-mutant fixation independently using reverse-state sums, and compares switching probabilities under changed intermediate returns. It also independently checks a closed falling-factorial formula for strictly positive baseline returns and the large-population logarithmic exponent.

These tests confirm finite exact identities and representative numerical limits only. They do not certify the infinite-size asymptotic, prove universal monotonicity on their own, validate finite-mutation stationary distributions, or establish historical priority. The analytical argument in RESULT.md supplies the universal claims. An independent scientific audit has not been performed.
