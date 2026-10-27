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

# Reproduction checks

Run `python verify.py` with Python 3 and no third-party dependencies. The included `verification.txt` is the exact output from the packaged verifier.

The verifier independently computes all period matrix products with rational entries for seventeen parameter cases and periods 4 through 16, checks the rank-one trace identity, reversal symmetry, strict adjacent maximality, the three determinant regimes for the minimizer, and all three six-year trace difference factorizations. It performs 1,989 exact rational schedule comparisons; it is a bounded test, not a computer proof for unrestricted parameters. The unrestricted proof is the argument in `RESULT.md`.

Not verified experimentally: finite-time response, nonlinear density dependence, stochastic environment schedules, source bibliographic uniqueness, field-data calibration or independent expert validation.
