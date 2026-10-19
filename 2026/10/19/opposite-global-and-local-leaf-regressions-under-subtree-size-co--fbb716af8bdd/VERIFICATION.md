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

# Reproduction and scope

Run `python3 verify_recursive_subtree.py` with an ordinary Python 3 standard library. The script enumerates all uniform-parent recursive trees for sizes \(3\le n\le9\) (\(46{,}232\) tree structures) and computes subtree size, subtree leaves, and global leaves directly, with exact rational comparisons to the theorem. It separately evaluates all \(19{,}899\) pairs \((n,k)\) for \(3\le n\le200\), using the beta-binomial law to verify support probabilities, mean regressions, and the two covariance formulas. Both suites passed on the embedded script as supplied.

The computations test finitely many cases only. General correctness is justified by the Pólya decomposition, exact leaf probabilities, telescoping covariance recurrence, and monotone-regression covariance identity in RESULT.md. The published predecessor on rooted-subtree leaf distributions was not completely inspectable as full text; this is a novelty limitation, not a computational failure. Independent scientific validation has not been performed.
