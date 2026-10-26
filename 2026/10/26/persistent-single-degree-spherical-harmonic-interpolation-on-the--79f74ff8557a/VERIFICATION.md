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

The executable `checker.py` uses Python 3 standard-library rational arithmetic (`fractions.Fraction`) and enumerates the 24 signed permutations of \((0,1,2)\). It checks every Legendre Gram rank at degrees \(0\) through \(128\), verifies a nonzero exact degree-eight annihilator arising from \((x^2-y^2)(y^2-z^2)(z^2-x^2)\), and checks the strict rational inequality (using \(\pi>223/71\)) that closes the separate Bernstein/Gershgorin analytic tail at degree \(129\). The general tail uses the proved Legendre bound, not finite sampling or a timeout. No estimate of interpolation conditioning is asserted.

Independent audit and independent external validation have not been performed.
