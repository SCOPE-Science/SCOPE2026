---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the fixed multiaffine seven-coordinate polynomial P=(21+4E_2+4E_3+E_4)/280, its eight cube-vertex value classes are nonnegative, so P>=0 throughout [-1,1]^7; nonnegative Fourier coefficients of products of cosine terms prove positive definiteness of F_q on the circle and F_q(0)=1. For the eight stated nodes and every odd integer q>=3, the limiting quadratic witness is -1/10. The analytic l1 cosine phase error bounded by 5pi^2/q^2 and derivative bound 13/35 give |Delta_q+1/10|<1040/q^2, strictly negative for all odd q>=103. The inspected CHECK.py implements outward-rounded integer scaled intervals for Machin pi bounds, cosine Taylor remainders, all 88 Sylvester principal minors at q=3,..,23 and all 39 witness signs q=25,..,101. Its interval arithmetic and return parity and Taylor sign logic were individually inspected. Independently calculated the entire finite bridge at 55-digit mpmath precision: all 88 small-base leading minors positive (smallest about 0.0002135937573), all 39 large-base witness defects negative (largest about -0.0092531315844); high-precision tests corroborate rather than replace its separate exact integer certificate. Positive constant perturbation 1/100000 retains the dichotomy by the displayed rational inequalities. Precise cutoff restricted to the fixed compression, not all possible circle kernels.

## originality

PASS

The underlying seven-variable polynomial, limiting eight-point obstruction and existence of counterexamples are explicitly prior Vybíral 2026 material, not new here. A rigorous sharp first-failing odd geometric base q=25 and all-base positivity/failure for the specific one-dimensional compressed family were not found in the accessible cited statements or published result database; best-knowledge priority is qualified by inability to read the 2026 paper in full.

## value

PASS

For the canonical one-dimensional lacunary compression of a known seven-variable counterexample, finding the first odd frequency-base ratio at which a proposed PSD lower bound fails is a natural quantitative boundary/invariant. The exact all-base positive/negative classification and a positive-valued kernel variant could be used directly in studying spectral behavior of lacunary positive-positive-definite Fourier kernels. Value attaches to the precise threshold, not the already established existence counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
