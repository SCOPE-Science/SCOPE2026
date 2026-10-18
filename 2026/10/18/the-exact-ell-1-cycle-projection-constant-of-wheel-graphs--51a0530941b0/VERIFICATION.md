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

# Mathematical verification

Run `python verify.py` in this directory using Python 3 and its standard library. The program verifies all four dual-certificate coefficient budgets; the adjoint cyclic-difference identity; exact upper-projection column norms; reflection symmetry; the projection identities; and exact rational test-vector identities. It covers every rim length from \(3\) through \(60\), including the known complete-graph boundary. The saved output appears in `verify_output.txt`.

A separately formulated finite-dimensional linear program, minimizing the full matrix \(\ell_1\)-operator norm over all projections, returned the same values for rims of size \(3\) through \(11\). These numerical checks are supporting evidence, not a formal certificate of an infinite theorem. The proof in `RESULT.md` is analytic for all rim lengths: the explicit dual-coefficient template yields a reflection-symmetric residual for every \(n\ge8\), and the remaining cases are tabulated.

No independent audit, formal proof-assistant verification or external certification has been performed. The literature-comparison result is also subject to independent bibliographic review.
