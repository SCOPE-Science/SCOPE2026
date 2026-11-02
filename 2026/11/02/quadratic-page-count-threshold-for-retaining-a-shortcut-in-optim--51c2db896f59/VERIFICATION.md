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

# Verification of the book-network resistance theorem

The proof in `RESULT.md` is analytic. The script `verify_book_resistance.py` was executed with Python 3, NumPy and SciPy. It reported:

- Exact rational inversions of \(L+\mathbf1\mathbf1^{\mathsf T}/n\) for \(15\) parameter instances, all matching the proposed inverse-spectrum trace.
- \(49\) budget and spectral equalities and \(49\) support-threshold decisions, all matching.
- \(980\) asymmetric positive-budget feasible comparisons, none better than the proven optimum.
- \(15\) unrestricted nonlinear numerical optimization attempts, with matching objective values or noncontradictory numerical termination.
- Equal-price retention for the two-page graph and deletion for \(3\le m\le44\).

The finite tests do not exhaust unbounded integer \(m\) or continuous price parameters. The matrix-inverse strict-convexity and scalar first-order analysis are the proof. No independent mathematical audit or exhaustive literature priority determination has been performed.
