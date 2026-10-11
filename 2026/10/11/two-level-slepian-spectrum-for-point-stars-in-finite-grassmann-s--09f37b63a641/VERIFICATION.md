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
# Reproducible mathematical checks

The package contains `verify_grassmann.py`. Run with Python 3 and NumPy:

```sh
python verify_grassmann.py
```

The checker explicitly enumerates all rank-\(k\) subspaces in reduced-row-echelon form, enumerates all projective points, and constructs the point–Grassmann incidence matrix. For each case, it forms the two symmetric positive semidefinite Gram matrices, whitens with the full positive incidence Gram matrix, diagonalizes the star-restricted Gram operator in floating-point arithmetic, and compares its ordered eigenvalues with the claimed list \(0,\theta,1\), including multiplicities. The field \(\mathbb F_4\) is represented using binary-polynomial arithmetic modulo \(X^2+X+1\).

Successful extracted-script run: `VERIFY_OK cases=11 prime_power_GF4=true exact_projective_point_enumeration=true`. Parameter cases were \((n,k,q)\in\{(4,2,2),(4,3,2),(5,2,2),(5,3,2),(5,4,2),(6,2,2),(6,3,2),(4,2,3),(4,3,3),(5,2,3),(4,2,4)\}\). Largest reported absolute numerical eigenvalue discrepancy was below \(5\times10^{-15}\).

The finite checks use actual incidence matrices, not mock spectra, but eigenvalue comparisons are floating-point and not certificates of the infinite parameter family. Infinite validity follows from the exact double-transitive Gram structure, quotient-incidence rank, irreducibility, and trace computation proved in `RESULT.md`. There is no external independent audit or mechanical proof certification.
