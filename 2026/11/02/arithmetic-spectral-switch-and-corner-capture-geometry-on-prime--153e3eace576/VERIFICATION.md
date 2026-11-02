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

# Exact verification and limits

`CHECKER.py` has no third-party dependencies and is executable with `python3 CHECKER.py`. It constructs the integer grid adjacency, forms each finite Krylov span, and checks the rank over each of two prime fields. `CHECKS.txt` is the actual successful output. Tests cover homogeneous single-, diagonal-double- and adjacent-double-corner configurations on squares of side 4, 6 and 10; rational directional anisotropy on those squares; full single-corner capture on 4×6, 4×10 and 6×10 rectangles; the trace-Gram identity for the first five relevant primes; and one exact irrational-coupling collision.

The general theorem is proved analytically in `RESULT.md`; finite field tests are only consistency checks. The full-span modular ranks certify full rational rank for the particular tested matrices. The all-prime spectral and parity arguments, not a numerical cutoff, establish infinite-family formulas. Source comparisons and limitations are in `REVIEW.md` and `AUDIT.json`. Independent audit is not performed.
