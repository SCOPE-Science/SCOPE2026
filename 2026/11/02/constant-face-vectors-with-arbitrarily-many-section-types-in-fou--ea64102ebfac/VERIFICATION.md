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

The section face lattice is reconstructed theoretically from its ambient crossed edges, triangular faces and tetrahedral facets. The proof uses two cyclic sign transitions, the two antipodal apex pairs and a neighborhood-invariant characterization of split size. All quantifiers concern integer n >= 5 and a generic central hyperplane (no ambient vertex contained).

To reproduce finite checks, run `python3 verify.py`; it checks all contiguous sign runs for 5 <= n <= 100, including vertex and facet counts, section-graph degrees and hub-neighborhood path decomposition. There are 4,944 configurations. The computations are finite corroboration, not an infinite proof. No independent audit has been performed.
