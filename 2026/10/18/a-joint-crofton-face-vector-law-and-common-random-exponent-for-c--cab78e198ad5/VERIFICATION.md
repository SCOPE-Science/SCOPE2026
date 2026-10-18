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

# Reproducibility and proof checks

The result is established by the analytic proof in `RESULT.md`. To run supplementary checks, execute `python checker.py` under Python 3.9 or later. The program uses only the standard library and seeds its random number generator explicitly. It checks face counts for all rank ranges in eighty-four independently generated generic sections of dimensions two through eight by enumerating every signed-coordinate face, rather than by reusing the polynomial identity. It also checks the exact binomial level laws, their normalization, the expected face counts computed in two distinct ways, and reports illustrative higher-dimensional samples.

The Gaussian integrals are evaluated with deterministic composite Simpson integration on a finite interval. Their tested accuracy is numerical, not interval-certified. The asymptotic random-exponent theorem and vanishing ratio of typical counts to means are verified through the Gaussian extreme-value and binomial-concentration argument in `RESULT.md`; sample statistics are not offered as an infinite-dimensional proof. No external or independent validation has been performed.
