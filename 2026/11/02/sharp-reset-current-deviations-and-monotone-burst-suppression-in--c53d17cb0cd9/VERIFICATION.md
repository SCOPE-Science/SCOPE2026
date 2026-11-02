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

# Verification of reset-count deviation laws

The proof defines \(p=\alpha+2\), \(b=(\alpha+1)/(\alpha+2)\), the mean cycle time \(m=L^p/[p(p-1)]\), and \(Z=\tau/m\). The cycle transform and reset-count LDP use the same normalization throughout. The determinant boundary is the first Bessel zero \(j_{b-1,1}\) in the admissible range \(1/2\le b<1\), where the Bessel index lies between \(-1/2\) and zero.

The standalone `verify.py` checks finite instances of the exact rational coefficient monotonicity, and compares a numerical solution of \(u''=s|x|^\alpha u\) with the \({}_0F_1\) expression. It evaluates the normalized Brownian and planar-Bessel endpoint transforms, verifies the tilted-root equation on both sides of the mean, tests the strict normalized upward-rate ordering for multiple tail levels, and evaluates the asymptotic quadratic rate coefficient. It also checks the exact cycle variance from the second logarithmic derivative of the Laplace function.

Run `python verify.py` in the directory containing this file. Dependencies: Python 3, `mpmath` and `scipy`.

A completed replay reported **286 passing assertions**. The checks are finite, do not establish absence of prior coverage, and are not an independent verification of the large-deviation theorem. The complete analytical argument is in `RESULT.md`. The independent audit has not been performed.
