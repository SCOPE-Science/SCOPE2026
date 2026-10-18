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

# Verification notes
The standalone `verify.py` uses direct quadrature of the exact integral for \(\mathbb P(\|(Z_1,Z_2)\|_q/\sqrt2>x)\) and of the conditional first-pivot probability, without sampling a full matrix. Executing `python verify.py` produced `PASS 28 numerical and endpoint assertions`.

Checks include comparison of six non-Euclidean angular-tail constants against saddle-normalized integral ratios at three large radii; seven exact \(q=1\) finite-size identities; three \(q=2\) alternating-sum identities; six three-size tests of the all-\(q\) sharp scaling; four ordered exponent tests of finite-size monotonicity; and the two analytically known endpoint coefficients. All 28 assertions passed.

The asymptotic conclusions are proved using exact polar integration, isolated saddle expansions, the half-normal Mills ratio, and a Laplace/regular-variation transfer; numerical experiments cannot certify those infinite statements. Finite-dimensional calculations do not address convergence uniform in \(q\), subsequent elimination pivots, or an entire-permutation law. Reproduction requires Python 3 and SciPy (`scipy.integrate.quad`).
