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

# Mathematical verification

The complete proof, including the exact cyclic product and the positivity/convergence of the resolvent derivatives, is in `RESULT.md`. To reproduce finite numerical diagnostics from this package, run `python3 verify.py`; a successful run reports `VERIFY_OK 6732`.

The checker directly forms polygon edges as differences of parameterized ellipse vertices, compares them to the cosine-sum perimeter, evaluates the Chebyshev product and its logarithmic derivative, and compares numerical phase derivatives with quadrature of the analytic derivative formula. Its checks use finitely many parameters, floating-point tolerances, and deterministic random sampling. They provide neither exhaustive real-number verification nor an independent mathematical audit.

Hypotheses for the proved statements: an ellipse with \(a>b>0\), integer \(n\ge3\), and maximum-area boundary-inscribed convex polygons. The circular and degenerate cases, arbitrary inscribed polygons that are not area maximizers, and generalized ellipsoids are outside the theorem.
