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

The exact projective conjugacy and the phase-angle relation were checked by symbolic rational simplification in `verify.py`; the three-by-three coordinate matrix is nonsingular and the critical numerator norm is checked exactly. The analytic proof in `RESULT.md` uses local expansions at the poles, unique ergodicity of an irrational circle rotation, the layer-cake moment identity, and dominated convergence on bounded local coordinates. All claims for infinitely many iterates and all parameters depend on this proof, not the finite checker.

The standalone checker additionally determines excursion-set lengths by deterministic sign-change bracketing and bisection and compares them with the two asymptotic scaling profiles at three threshold ratios from each side. Running the checker at package creation returned `VERIFY_OK`. The numerical tolerance is only a diagnostic for a finite positive perturbation and is not a certificate for a limit.

The analysis excludes points with an undefined rational iterate; it establishes unique invariance only on the specified carrier, not the whole plane. It does not certify historical priority or independent validation. Full-text comparison was possible for the 2010 and 2013 primary manuscripts; other generic projective-distribution literature may include analogous consequences.
