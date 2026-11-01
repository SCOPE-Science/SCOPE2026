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

# Verification and limits

Run `python verify.py` in an environment with Python 3 and the SymPy package. The checker recomputes the exact reduced polynomial map, fixed-branch identity, critical determinant factorization, and the odd multiplier identity. Its rational interval implementation brackets the isolated sextic root and proves strict signs of the other eigenvalues, the pointwise-population admissibility margin, the critical multiplier derivative, and the cubic coefficient of the second iterate.

On the extracted source used in this package, the output is an exact root bracket \((166763953195/10^{12},166763953197/10^{12})\), a critical growth bound \((2.7324800658552,2.7324800659526)\), an even complementary eigenvalue in \((-0.181,-0.178)\), an odd eigenvalue in \((-0.503,-0.500)\), a second-iterate cubic coefficient in \((-19.2,-19.1)\), and critical multiplier derivative in \((-0.98,-0.96)\).

All asserted inequalities are certified by exact rational endpoints, not floating-point tolerances. The analytic conclusion relies additionally on finite Fourier range and the classical smooth flip theorem; algebraic finite checks alone would not imply a global phase portrait. The theorem does not transfer to dispersal kernels with nonzero higher Fourier modes. Independent validation has not been performed.
