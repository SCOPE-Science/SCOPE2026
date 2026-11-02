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

# Verification and reproducibility

The proof uses the standard Hilbert variance identity and a reverse triangle inequality, then attains equality using an explicit regular-simplex construction. It covers every integer \(n\ge2\) and arbitrary real Hilbert targets. The included `checker.py` is standalone, requiring only Python's standard library and no network access.

Execute `python checker.py`. Successful output is:

`CHECK_OK exact_field_and_high_precision_assertions=693 exhaustive_coordinate_pairs=3416 n_exact=2..100 n_coordinate=2..17`

The algebraic checker operates on rational pairs representing the quadratic field of the optimal distortion parameter. For integer \(n\) between \(2\) and \(100\), it verifies the defining minimal polynomial, cross-distance identities, monotonicity and sharp bounds. For \(2\le n\le17\) it also enumerates all unordered point pairs in the proposed Euclidean realization and checks the prescribed metric-distortion inequalities and distance classes. The experiment is finite; the unrestricted theorem follows from the complete proof, not these tests.

An independent mathematical audit has not been performed. The literature comparison has a residual inaccessible-full-text risk for an older related distance-matrix paper, and no external novelty certification is asserted.
