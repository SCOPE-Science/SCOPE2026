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

# Reproducibility and verification

The analytic argument begins with localization at polygon vertices, then the triangle circumradius expression on two rays, the \(c^2\) Jacobian and an elementary \((u^2-2u\cos\theta+1)^{-3/2}\) integral. It continues with exact sample label accounting and strict Jensen convexity. This supports the assertion for each fixed convex polygon on a positive small-radius interval, not for every radius.

To repeat the supplementary numerical checks, run `python3 checker.py` in the same directory as this file. It uses only the standard library and deterministic random seeds. The program checks five nontrivial angular integrals, regular polygon formulas, hundreds of strict convexity comparisons and independent perimeter samples on polygons. It reports finite-sample uncertainty; Monte Carlo is not a proof of the universal theorem.

The small-radius threshold is shown to exist, not optimized. Collinear triples have positive probability when all three points lie on one edge and are assigned infinite circumradius; the law is unconditional. The result has undergone self-review only. No independent audit, external formal verification or publication certification is represented.
