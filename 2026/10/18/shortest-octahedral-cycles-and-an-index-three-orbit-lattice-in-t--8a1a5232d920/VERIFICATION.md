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

# Exact reproducibility and limits

Run `python3 verify.py` (standard library only, Python 3.10+). All finite computations use integers or rational fractions, never floating-point approximations.

The program reconstructs the twelve-vertex graph from its three-entry repeated LCF chord offsets; checks all 18 edges and all 1,085 nonempty matching simplices; constructs and verifies an acyclic matching with 537 pairs and one critical vertex and ten critical three-faces; checks the full mod-two rank 236 of the 236 matched-upper three-cell boundary columns; checks all 39 signed induced-octahedron chain boundaries and their integral Morse coordinates; verifies 39 primitive class vectors; calculates a displayed unimodular ten-vector basis minor; finds all eight graph automorphisms; and evaluates exact maximal-minor gcds for all nine orbit lattices.

The flag-complex minimum-support argument and discrete-Morse theorem are mathematical premises stated in RESULT.md. The computation certifies their hypotheses for the specific graph. It does not establish any assertion for other graphs, nor does it imply independent publication priority or independent audit.
