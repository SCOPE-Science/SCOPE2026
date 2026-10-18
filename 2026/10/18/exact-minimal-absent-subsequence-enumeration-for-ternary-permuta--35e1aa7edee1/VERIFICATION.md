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

The exact certificate uses nine integer-polynomial identities \((I-M)Q=DE\), plus a numerator identity. These identities are reproduced from packaged `check.py` using only the Python standard library. Independently, the checker computes the rational coefficients and the finite-state word counts, compares them for eighteen initial coefficients, and exhaustively tests subsequence membership and all one-letter deletions for powers one through three. It also checks all permutations for powers one and two. The recorded output is in `check_output.txt`.

These finite tests do not certify all powers. The proof for every positive repetition count is the greedy embedding equivalence, the exact one-letter-deletion characterization, and the polynomial vector identity, which is valid formally over the rational power-series ring. The bivariate matrix formula is exact but is not presented as a simplified scalar expression for alphabets larger than three. No independent audit has been performed.
