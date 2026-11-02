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

# Reproduction and proof boundaries

Run `python checker.py` with Python 3.8 or newer (standard library only). Its exhaustive raw-structure test enumerates every unary assignment and every directed binary-edge assignment on domains of sizes 1 through 3 under one fixed, realizable, nonnegative-weight network. The resulting exact integer weights are compared to the closed binomial-quadratic factor for each colour count.

The numerical tests evaluate the exact normalized mass function via log-gamma arithmetic for sizes 100, 1000, 10000 and 100000, at three positive interaction parameters. They independently compute the saddle from a bracketed numerical root solve, the theta approximation from a truncated rapidly convergent series and the saddle normalization factor. They output observed total variation and log-partition errors and finish with `ALL_CHECKS_OK` if their finite consistency checks hold.

These tests establish consistency only at their enumerated and numeric parameters. They cannot certify a total-variation limit, the uniformity in lattice phase, an exact identity for arbitrary domain size, any earlier-publication priority, or independent peer validation. The infinite theorem follows from the self-contained exact factorization, Stirling expansion and two-sided summable adjacent-ratio bounds in `RESULT.md`. Potential floating-point drift does not affect the mathematical argument.
