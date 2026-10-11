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
# Verification of the finite and uniform spectral-determinant law

The standalone file `verify.py` performs the following checks using its own moment integration and determinant implementations.

1. For four integer weights \(\beta\in\{0,1,2,3\}\) and every \(1\le m\le6\), three Jacobi moment Gram determinants are computed with **exact rational arithmetic** from the binomial expansion of the weight, and independently compared with rising-factorial Selberg products (72 exact Hankel identities). The corresponding spectral determinant ratios and gamma product are checked on the same 24 parameter pairs (48 further checks).
2. For 20 nonintegral parameter pairs, the gamma-product formula is numerically compared to its three-factor Hankel/Selberg determinant form. These checks validate numerical evaluation, not an independent integration derivation for every nonintegral weight. With the optional multiprecision library, two further noninteger-weight cases are checked by direct numerical quadrature.
3. Strict parameter monotonicity is numerically checked on 56 successive parameter comparisons. The analytic proof supplies the actual strict-all-parameter statement via digamma concavity.
4. If `mpmath` is installed, the checker evaluates the Barnes constant and checks two large-bandwidth scaled determinants, then checks ten finite-bandwidth examples against the uniform dimension/bandwidth approximation. These asymptotic tests use a nonzero finite tolerance and are not infinite proofs.

The completed replay reported:

`VERIFY_OK exact_moment_and_selberg_checks=120 nonintegral_checks=20 monotonic_checks=56 asymptotic_checks=2 crossover_checks=10 quadrature_checks=2`

All numeric checks are finite. Correctness for arbitrary real \(\beta>-1\), nonvanishing centered determinant, and a uniform \(O(m^{-1})\) bound rest on the explicit algebraic and analytic proof in `RESULT.md`. The `mpmath` portion is optional; standard-library exact checks remain runnable without it.
