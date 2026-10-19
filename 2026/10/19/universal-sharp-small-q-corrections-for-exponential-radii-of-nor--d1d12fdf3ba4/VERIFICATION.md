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

The exact \(q\)-series has coefficients \(b_{n,s}\) specified in the result and satisfies \(b_{n+1,s}/b_{n,s}\le q^{\kappa_s n}\); this analytically bounds every series tail uniformly on compact \(x\)-sets, including differentiated series. The first two nonconstant terms reproduce the linearized root equations, and both root derivatives have strictly negative sign at the limiting roots. The positive-zero Hadamard factorizations ensure that these locally computed roots are exactly the exponential radii, not merely candidate root branches.

`verify_qbessel_radii.py` runs with Python 3.10+ and `mpmath>=1.3.0`. It evaluates the normalized coefficient series through term 22 in 65-digit arithmetic, computes root equations directly, uses bisection on intervals known to precede the first pole, and checks the two corrections against the predicted \(O(\epsilon_s^2)\) residual. The test grid uses \(\nu=1/4,1/2,1\) and \(q=0.02,0.06,0.12\), both Jackson/Hahn–Exton cases, all three normalizations, and both exponential radii, for 108 root comparisons. Numerical checks cannot replace the infinite-product argument or establish the all-parameter statement.

No external independent audit, validation certificate, or formal proof assistant has been used.
