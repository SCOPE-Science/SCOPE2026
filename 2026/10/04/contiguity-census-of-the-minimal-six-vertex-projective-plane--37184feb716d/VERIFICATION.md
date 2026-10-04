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

Run `python3 verify.py` in the directory containing `CENSUS.json`.

The checker reconstructs the ten-facet complex, confirms all edge degrees and vertex links, computes boundary ranks over \(\mathbf F_2\), enumerates every vertex map, tests simpliciality on every facet, identifies the facet-preserving permutations, builds all one-coordinate contiguity edges, traverses the resulting graph, and evaluates the induced first-homology action on an explicit generator.

The symbolic step relating this graph to full contiguity is: if two simplicial maps are contiguous, any hybrid obtained by replacing source-vertex values one at a time has each simplex image contained in the union of the two original simplex images. Hence every such hybrid is simplicial and consecutive hybrids are contiguous. Therefore connected components of the one-coordinate graph are exactly contiguity classes.

Expected replay output is recorded in `CENSUS.json`. The computation is finite and exhaustive; it does not establish statements about subdivisions or ordinary homotopy classes beyond the standard implication from contiguity to homotopy.
