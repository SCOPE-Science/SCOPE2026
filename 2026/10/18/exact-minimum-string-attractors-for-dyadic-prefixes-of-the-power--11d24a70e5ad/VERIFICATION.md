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

# Verification

Run `python verify.py` from the directory containing the code. The program constructs the powers-of-two characteristic word with one-based positions. It checks, for every exponent \(2\le m\le14\), the explicit lower-bound factors, the factor occurrence uniqueness, disjointness of their intervals, the claimed lower count, and the proposed upper-set size. For exponents \(2\le m\le9\), it exhaustively enumerates all distinct nonempty factors of each finite prefix and checks the upper attractor by examining every occurrence. See `verification_results.txt` for the run output, including `FINITE_CHECKS_PASS`.

The all-order upper bound uses Schaeffer–Shallit's published Theorem 8, not a new independent reproof of its Walnut computation. The all-order lower bound is established directly by the interval arguments in `RESULT.md`. Enumeration through finite bounds cannot establish an unbounded theorem. Neither independent scientific review nor external certification is asserted.
