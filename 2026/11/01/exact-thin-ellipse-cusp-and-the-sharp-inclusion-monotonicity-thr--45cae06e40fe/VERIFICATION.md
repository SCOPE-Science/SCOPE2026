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
# Reproducibility and limits

Run `python -m pip install -r requirements.txt`, then `python verify.py`. The high-precision checks integrate the exact ellipse parametrization and its analytic derivative at aspect ratio \(10^{-4}\), compare the resulting cusp coefficient with its gamma-function value for \(p=-0.9,-0.5,-0.1\), and verify strict decrease for pairs of nested thin ellipses. At nonnegative exponents they verify positive changes and the circle derivative formula. On direct execution the program printed `NESTED_ELLIPSE_FINITE_CHECKS_OK`.

The analytic proof, not finite testing, establishes the theorem uniformly for every real \(-1<p<0\). In particular the dominated-convergence majorant and the \(O_p(a\log(1/a))\) remainder estimate are proved in `RESULT.md`. The program does not establish monotonicity sign over all aspect ratios, uniqueness of the interior minimizer, or priority against uncatalogued published literature. Independent scientific audit has not been performed.
