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

# Reproducibility and limitations

The accompanying standalone `verify.py` runs using Python 3 and its standard library only. Execute `python3 verify.py` from the unpacked directory. It verifies probability normalization, strict likelihood-ratio log-convexity, the central sign interval, exact total variation from that interval in 200 rational parameter sets, and 24 large-parameter numerical comparisons to the three-regime analytic formula or its small-ratio constant.

The Gaussian and small-reinforcement limits are proved in `RESULT.md`. The finite checks do not provide a proof of universal quantifiers, uniqueness of the historical result, or independent validation. Numerical log-gamma calculations have ordinary floating-point rounding; rational finite checks use exact integers and `fractions.Fraction`.

Independent audit has not been performed.
