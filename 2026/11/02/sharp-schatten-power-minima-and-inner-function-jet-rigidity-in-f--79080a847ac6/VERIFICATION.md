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

# Reproducible checks and mathematical limits

Run `python CHECK.py` with Python 3 and NumPy version 1.24 or later. In one execution, 338 assertions passed. The checker forms a Szegő-kernel Gram matrix from distinct finite Blaschke zeros and constructs the compressed backward shift in orthonormal coordinates. It verifies the exact Hilbert–Schmidt identity for every tested power, all five tested positive Schatten exponents, nontrivial strictness, and equality with jet-flat products and regular polygons. The checker is a finite numerical test, not proof for arbitrary degrees, arbitrary finite Blaschke products, repeated zeros, or all real exponents. Those require the rank-one defect, determinant, arithmetic–geometric-mean, and inner-function factorization arguments in RESULT.md.

The first-public date belongs to arXiv:1711.06042 version 1 (2017-11-16); later revisions and journal publication were not substituted. The displayed mathematical claim assumes a fixed nonzero value at the origin, degree \(N\), and a power \(1\le k\le N\). No independent audit has been performed.
