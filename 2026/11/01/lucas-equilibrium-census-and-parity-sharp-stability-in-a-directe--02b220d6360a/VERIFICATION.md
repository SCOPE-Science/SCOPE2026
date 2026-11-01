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
# Verification scope

Run `python3 verify.py` in the directory containing `verify.py`; only the standard Python library is required. The executed program checks all independent-set candidates at integer ring sizes 3 through 12 for three rational parameter pairs by exact arithmetic; compares their counts to Lucas numbers; confirms strict odd-ring spectral stability and boundary equalities for sizes 3 through 21; and checks even checkerboard multipliers for selected cases.

These are finite reproducible tests. The unbounded ring-length classification, absence of extra fixed points, instability of noncheckerboard vertices, all-parameter local contraction, and sharp spectral criterion are certified only by the symbolic argument in `RESULT.md`, not by exhaustive numerical experiments. No external scientific audit has been performed. Equality in the spectral criterion is not assigned a nonlinear stability type.
