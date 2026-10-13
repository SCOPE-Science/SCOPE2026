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

# Verification of the central graph-jet multiplicity formula

The symbolic proof reduces the generic local ring to a quotient by unsigned edge-incidence linear equations and graph-edge quadrics. Per connected component, the linear equations leave one parameter for a bipartite component in characteristics other than \(2\), or for every component in characteristic \(2\); a graph edge then squares that parameter to zero. This gives the local algebra and generic length for all finite graphs under the assumptions.

The companion file `verify_graph_first_jets.py` requires only the Python standard library. Execute `python verify_graph_first_jets.py` from the directory containing the file. The exact finite-field checker exhausts graphs with no isolated vertices on \(2\) through \(5\) labeled vertices and tests five distinct additional six-vertex examples over \(\mathbf F_2\), \(\mathbf F_3\), and \(\mathbf F_5\); the checked statement is equality of the reduced linear-kernel quadratic ideal with independent square-zero relations. Expected output: `EXACT_IDEAL_CHECK_OK cases= 2457 primes=2,3,5 graphs=all isolate-free graphs on 2-5 vertices plus five six-vertex examples`.

These tests do not verify infinite universality, characteristic zero, or the schemes of higher-order jets; those rely on the explicit mathematical proof. No separate independent audit has occurred.
