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

# Reproducibility
Run `python3 verify.py` with the Python standard library. The program creates every labelled sunlet directly from the edge definition, then checks ordinary \(P_3\)-convexity by the literal outside-vertex neighbour condition for all \(2^{2n}\) subsets and every integer \(3\le n\le9\), collecting all coefficients by core and leaf selections. Independently it evaluates the cyclic-run binomial formula, an overlap transfer matrix, the scalar Vandermonde sum, and the scalar recurrence for \(3\le n\le22\).

The completed test emitted `BRUTE_JOINT_OK n=3..9`, `TRANSFER_AND_BINOMIAL_OK n=3..22`, and `VERIFY_OK`, with scalar counts for \(n=3,\ldots,10\) equal to \(22,64,184,524,1488,4224,11992,34048\). Finite tests are cross-checks, not proofs for all graph orders. The infinite conclusion is supported by the independent combinatorial decomposition and transfer-matrix calculation in `RESULT.md`. The scalar counts and their recurrence are already known as OEIS A073313 and are not new claims.

This package has not undergone independent external review or mathematical certification. Historical equivalences beyond the specifically inspected sources remain possible.
