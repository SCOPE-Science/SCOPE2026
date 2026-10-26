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

The analytic proof applies to every integer \(m\ge2\), \(d\ge1\) and every complex \(d\times d\) matrix, including singular, repeated-spectrum, and zero matrices. It uses exact singular-value splitting, the sine spectrum of real tridiagonal Jordan parts, the finite-dimensional Li–Sze characterization, and a rank-counting inverse algorithm. The proof's lower-bound example demonstrates failure of universal identification at every shorter initial prefix.

`verify.py` requires only Python's standard library. From a directory containing the extracted script run `python verify.py`. The script checks finite product-prefix inversions and sharpness examples across path lengths from two to ten and block dimensions from one to six, plus unitary conjugation in a nontrivial complex example. The executed version reported `PASS: 268 finite recovery, sharpness and unitary-block checks`.

Finite numerical checks cannot prove the general theorem and do not address numerical stability, unindexed-priority questions, or independent validation. No external audit is asserted.
