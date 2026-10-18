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

# Reproduction and scientific limits

The closed formulas and the limit theorem are proved in `RESULT.md`. The following deterministic finite checks are supplementary and do not certify an infinite assertion:

```bash
python3 verify_book_bulk.py
```

The standard-library checker recomputes \(\int_0^t s^r(2-s)^m\,ds\) by independent binomial expansion with exact rational arithmetic. For \(m=2,3,\ldots,10\) and \(t\in\{1/4,1/2,1,3/2,2\}\), it compares that independent integration to the stated power expressions, reconstructs each covariance entry, and verifies its determinant by exact Gaussian elimination without invoking the matrix determinant lemma. Observed output after execution:

`EXACT_WEIGHTED_BOOK_MOMENT_CHECKS_PASS 45 cases`

A separate numerical reconstruction of \(Q_{m,t}\) from its actual halfspace inequalities used halfspace intersection and convex-hull facet triangulation; each simplex second-moment tensor was integrated geometrically. For \(m=2,3,4\) and \(t\in\{1/3,1,3/2,2\}\), 12 instances matched the volume and full covariance formulas, with maximum absolute error below \(3.2\times10^{-15}\). The independent geometric check used NumPy/SciPy and is described as corroboration, not as an embedded certificate or an infinite proof.

The critical-window density and joint independence use dominated convergence, the elementary independent-uniform representation, and the classical central limit theorem. The uniform isotropic-constant limit uses explicit parameter-independent bounds stated in the proof. Neither the checker nor the geometric triangulations establish these asymptotics by finite extrapolation. Only scientific correctness, originality on inspected records, and motivated value were assessed here; external independent audit remains unperformed.
