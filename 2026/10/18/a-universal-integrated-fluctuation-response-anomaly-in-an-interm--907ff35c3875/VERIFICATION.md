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

# Reproduction and verification

From this directory, run `python verification/check_fdt.py` using Python with SymPy and mpmath installed. The program evaluates the two-state generator and stationary moment identity symbolically, checks sixteen Taylor orders, makes 168 high-precision matrix-exponential comparisons, checks fourteen onset and integrated-gap identities, verifies strict dominance of the maximum at 42 non-optimal lags, and reproduces a rational-eigenvalue example.

The analytic proof of the all-parameter claims is in `RESULT.md`. The program does not certify an infinite continuum by enumeration; its algebraic identity checks and finite matrix exponentials are consistency checks. In particular, the uniqueness of the maximum follows from a strictly monotone ratio of exponentials, not from numerical maximization. No independent audit or experimental verification has been performed.
