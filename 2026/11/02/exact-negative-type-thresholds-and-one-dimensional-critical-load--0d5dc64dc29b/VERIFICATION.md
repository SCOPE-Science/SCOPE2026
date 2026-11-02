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
# Reproducibility and verification limits

The analytical result follows from a direct rooted Gram representation, its branch-symmetric decomposition, the negative-semidefiniteness of the between-branch kernel for exponents between one and two, and finite negative-type strictness. Computation is a supplement to, not a substitute for, the infinite proof.

With Python 3, NumPy, and SciPy installed, from the package root run `python artifacts/check_numeric.py`. The script independently constructs graph distances by breadth-first search rather than using the displayed block expressions for the original distance matrix. It reports:

`CHECK_OK: 448 full spectral comparisons; 64 endpoint multiplicity checks; 448 phase checks; 21 asymptotic checks`

The finite sampled parameter ranges are \(2\le k\le9\), \(1\le m\le8\), and seven interior exponents per tree; the asymptotic test uses additional large leaf counts. The numerical tolerance is at most \(5\times10^{-8}\) for spectral differences, with separate fixed thresholds for zero-eigenvalue and asymptotic checks. These tests do not establish exactness over all integers or validate the literature-priority assessment independently.

The theorem does not include weighted, irregular, or height-three-and-greater trees. At the exceptional five-vertex path, the endpoint embedding dimension is one and not the usual codimension-one case.
