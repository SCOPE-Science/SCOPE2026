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

The attached `verify_ferromagnetic_precision.py` is a standalone Python 3 and SymPy verifier using exact fractions throughout. It recomputes all four-spin atom weights, all twenty-four pairwise binary MTP2 inequalities at fixed other coordinates, covariance and inverse covariance, and the \(2\times2\) Schur complement. It checks symbolically that the conditional-mean discrete second difference factors as in the proof. The rational witness has normalizer \(235/8\), positive covariance \(304/55225\), and positive inverse-covariance entry \(235/60966\). A thirty-six-parameter exact rational grid also reproduces the predicted sign rule.

The infinite-domain claims are justified by the direct conditional covariance argument, positive-definite Schur-complement inversion, and explicit logistic-curvature factorization. Finite enumeration is corroborative only. No formal proof assistant or independent validation was performed.
