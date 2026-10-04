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
# Verification

The mathematical reduction is finite because the octagonal norm is the maximum of eight explicit linear functionals. For every admissible pair, active facets of \(x\), \(y\), and \(x-y\) give three independent affine equations; active facets of \(x+y\) and \(2x-y\) select a region where the squared objective is a single quadratic polynomial.

`verify_octagon_tg.py` performs the complete exact enumeration with elements represented as \(a+b\sqrt2\) for rational \(a,b\). It checks every facet inequality, every output-facet dominance inequality, every interval endpoint, and every admissible concave quadratic vertex. It then checks the explicit equality witness. A successful run prints `VERIFY_OK`, `cells 112`, and the exact maximum product represented as \(9-4\sqrt2\).

The verifier proves only the stated regular-octagonal case. It does not numerically extrapolate to other polygonal norms, and no unproved classification is used.
