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

The attached `shelling.json` supplies 105 integer masks, where bit \(i\) denotes vertex \(i\in\{0,\ldots,11\}\). The standard-library file `verify.py` reconstructs the graph from two staggered pentagons and opposite poles, rather than relying on a specialized graph database.

Run `python3 verify.py shelling.json` from the extracted directory. Actual execution returned `ICO_2_SHELLING_VERIFY_OK facets=105 spheres=20`. The checker compares the forbidden-triple and induced-component predicates on all 4096 subsets, confirms exactly 80 minimal forbidden triples, all 324 simplicial faces, the complete facet set, the purity and 104 successive shelling intersections, the unique restriction-face law and 20 top homology facets. It separately evaluates the \(h\)-polynomial and reduced Euler characteristic.

These finite checks are exhaustive for the fixed twelve-vertex object; they do not assert or numerically approximate an infinite-family theorem. The implication from a pure three-dimensional shelling to an integral wedge of three-spheres is standard. No independent mathematical audit has been performed.
