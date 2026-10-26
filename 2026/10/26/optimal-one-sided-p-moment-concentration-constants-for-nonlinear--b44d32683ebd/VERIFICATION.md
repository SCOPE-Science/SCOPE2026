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

# Verification and reproducibility

The analytic verification is in RESULT.md. In particular, the optimum of the scalar exponential remainder is unique for \(1<p<2\), and the nonlinear inequality follows from a specifically identified published reverse-KL tensorization proposition. The global optimality proof uses exact binomial large-deviation rates and sequential limits, not an extrapolation from finite numerics.

Run `python3 sharp_one_sided_verifier.py` using the Python standard library to reproduce 3,600 finite nonlinear moment-generating comparisons, the scalar optimizer checks, and Bernoulli rate coefficient comparisons. The program is deterministic and requires no downloads. Its tests are supportive only; they do not certify the infinite theorem or originality.

Scientific limits: only upper tails, integrable functions bounded above, independent coordinates, and finite conditional deficit budget are covered. For \(1<p<2\), infinite variance is permitted. No independent mathematical audit has yet been performed.
