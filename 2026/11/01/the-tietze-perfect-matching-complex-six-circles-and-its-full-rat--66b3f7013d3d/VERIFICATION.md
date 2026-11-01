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

The supplied `verify.py` uses only Python's standard library. It was executed successfully on the delivered source prior to packaging, with the following actual, complete checks:

- Constructed the unique-triangle 12-vertex, 18-edge graph from the Petersen triangle inflation.
- Enumerated the eight perfect matchings twice: vertex-recursive dynamic programming and the exhaustive 262,144-subset search with exact degree constraints.
- Constructed 443 nonempty simplices and checked counts in dimensions zero through five: 18, 96, 153, 120, 48, 8.
- Computed the 15 facets of the eight-vertex nerve and its face counts 8, 28, 18, 3.
- Checked each of the 18 displayed simplicial elementary collapses by the literal free-face criterion; the final connected graph has eight vertices and thirteen edges.
- Constructed an independent 218-pair original-face Morse matching and topologically sorted the entire oriented Hasse diagram to certify acyclicity.
- Enumerated the 12 exact graph automorphisms and calculated all 12 rational homology character values on both the original simplex chains and the nerve chains, obtaining identical results.
- Confirmed no rational invariant first-homology vector under the full symmetry group.

The mathematical proof is the displayed finite nerve collapse plus the simplicial nerve theorem and the signed Lefschetz identity. It does not infer an infinite-family theorem from finite experiments. No independent audit was performed, and the rational character does not determine the integral representation lattice.
