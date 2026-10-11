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

The derivation requires no external computation: additive orthogonality gives the convolution expression, \(u\mapsto u^{2^k}+u\) has kernel \(\mathbb F_{2^{\gcd(m,k)}}\), Cauchy--Schwarz bounds each nonzero fiber, and the equalities are determined by the three exact nonnegative deficit terms. In particular, the zero-sum contribution is \(\left|\sum f(x)^2\right|^2\), not generally \(\|f\|_2^4\).

Run `python3 artifacts/verify.py` from the directory containing the embedded artifact. It performs finite-field arithmetic directly with irreducible binary polynomials, recomputes every derivative fiber, computes the fourth moment through a separately accumulated convolution, and checks both a nonaffine trace-quadratic phase subfamily and negative controls. Four small fields also use an explicit sum over Fourier characters. The expected successful output is `VERIFY_OK exact_Gold_cases=21 nonaffine_quadratic_extremizer_cases=4 nonextremizer_tests=8 Fourier_orthogonality_checks=4`.

Checks are limited to \(m\le6\), \(1\le k\le m\), and selected phase inputs; they do not enumerate all complex coefficients or all infinite parameters. The universal theorem rests on the supplied analytic proof. Independent audit has not been performed.
