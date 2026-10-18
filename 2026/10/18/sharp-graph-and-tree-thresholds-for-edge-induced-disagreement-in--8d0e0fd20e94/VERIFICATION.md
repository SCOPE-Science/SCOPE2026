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

# Reproducible verification

The grounded-Laplacian equilibrium is computed with exact rational arithmetic, including both pinned vertices in the final polarization statistic. Running `python3 verify_harmonic.py` lists connected labeled graphs on \(2\)–\(5\) vertices and labeled trees on \(2\)–\(6\) vertices, compares every possible missing follower–follower edge, and checks explicit six- and seven-vertex witnesses. Independently, `python3 check_determinants.py` uses determinant expansion and Cramer's rule in place of Gauss–Jordan elimination and reproduces the same census counts.

Both methods independently confirm zero strict increases in all cutoff comparisons; the first checks exact witness increases \(\(\frac{43}{36504}\)\) and \(\(\frac{137}{6776}\)\). The count of graph comparisons across sizes \(2\)–\(5\) is \(956\); the count of tree comparisons across sizes \(2\)–\(6\) is \(5417\). These are finite exhaustive statements only. Infinite universality beyond the permitted small-order nonincrease thresholds is not claimed. Scientific literature comparison is part of the self-review and is subject to the residual coverage risks stated in REVIEW.md.
