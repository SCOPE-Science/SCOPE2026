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

# Verification record
The standalone Python 3 script `verify_crown_geodetic.py` uses breadth-first-search distances and the condition \(d(u,w)+d(w,v)=d(u,v)\) to compute geodesic intervals without referring to the algebraic classification. It checks all nonempty vertex subsets for \(n=3,4,5,6,7,8,9\), compares actual coverage with the structural criterion and with both claimed coefficient polynomials, and determines minimal sets by checking every one-vertex deletion.

Executed command: `python3 verify_crown_geodetic.py`.

Observed output summary: `VERIFY_OK graph_orders=7 tested_subsets=349497 structural_and_polynomial_agreement=true`.

Observed inclusion-minimal size distributions: \(n=3:\{2:3,3:2\}\); \(n=4:\{2:4,4:2\}\); \(n=5:\{2:5,5:2\}\); \(n=6:\{2:6,6:22\}\); \(n=7:\{2:7,6:140,7:2\}\); \(n=8:\{2:8,6:560,8:2\}\); \(n=9:\{2:9,6:1680,9:2\}\).

Finite exhaustive checks do **not** establish any claim for untested graph orders. The general all-order argument and boundary conditions are in `RESULT.md`. No independent mathematical audit has been performed.
