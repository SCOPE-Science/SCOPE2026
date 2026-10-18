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

# Verification and scope

Run `python3 verify_polygynous_founders.py` with Python 3.9 or newer. The script uses only the standard library and was replayed against the embedded source; it reports 600 exact-rational discrete-concavity / half-ratio tests, separately coded exact examples, saturation formulas, and numerical binomial-quantile and asymptotic illustrations. It makes no external service calls.

Universal claims rely on the mathematical proof in RESULT.md: (1) a strict Bernstein second derivative and reflected first derivative, (2) uniform Lipschitz convergence for the leading asymptotic, (3) a binomial CDF identity and triangular-array CLT inversion, and (4) an exact saturated-capacity polynomial. Each step specifies the integer and parameter assumptions. Finite checks, graphical inspection, and a CLT illustration are not proofs of universal results or novelty.

The numerical normal quantile is evaluated by `statistics.NormalDist`; displayed asymptotic values are illustrative. No external auditor has independently validated the calculations. The model is one-generation and does not claim a demographic extinction-time theorem.
