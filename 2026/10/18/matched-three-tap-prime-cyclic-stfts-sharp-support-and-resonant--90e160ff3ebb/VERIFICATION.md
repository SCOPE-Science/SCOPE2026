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

# Reproducibility and exact checks

The file `checker.py` uses standard-library integer arithmetic and represents Laurent cyclotomic expressions at prime order by exponent dictionaries reduced modulo the prime. An expression at a primitive \(p\)-th root is zero precisely when its \(p\) residue coefficients are all equal. It verifies all labeled three-point supports for prime orders \(5,7,11,13\), checks every allowed progression four-hole pattern and the nonprogression two-hole construction, and prints `CHECK_PASS`.

The core general proof requires no exhaustive finite experiment. It uses the prime cyclic uncertainty inequality for each active STFT row, the classification of differences of three points, nonvanishing of two-by-two Fourier minors, and exact factorization of the constructed row polynomials. In particular, the explicit parameterization proves attainment of the lower bound for every prime \(p\ge5\), not merely at the tested orders. Tests do not establish independent validity or cover composite cyclic groups, approximate sparsity, or the restriction \(f=g\).
