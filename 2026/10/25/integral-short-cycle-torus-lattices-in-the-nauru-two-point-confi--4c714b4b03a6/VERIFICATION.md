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
# Reproducible verification

The stand-alone `verify.py` constructs the 24-vertex graph from the generalized Petersen edge formula, lists every graph simple cycle once, reconstructs the unordered two-point cubical chains, checks all cellular boundary compositions, and checks rank lower bounds over prime fields. Every length-six and length-eight disjoint cycle pair is converted to a signed integral product-torus cycle and explicitly checked closed.

The program deterministically selects 54 octagon-pair cycles and 54 two-cell coordinates, verifies the integer determinant is `-1`, and reconstructs all 417 short-cycle torus chains by exact integral basis coordinates. Smith normal forms give the three lattice quotients without relying on modular rank as an index certificate. It also enumerates 144 graph automorphisms and their three orbit partitions.

To replay, install the dependencies in `requirements.txt`, then run `python verify.py`. On success the final line is `VERIFY_OK_NAURU_SHORT_CYCLE_TORUS_LATTICES`. The graph, matrices, bases and determinant witnesses are generated from explicit definitions within that file; no downloaded data, private evidence, or other records are needed.

Limitations: the verifier does not compute the fundamental group, lower-degree integral torsion, cup products, arbitrary longer-cycle lattices, or results for any other graph. This is exact finite computation for one explicitly given graph, with standard deleted-product topology supplying the bridge to the continuous configuration space. No independent audit has been performed.
