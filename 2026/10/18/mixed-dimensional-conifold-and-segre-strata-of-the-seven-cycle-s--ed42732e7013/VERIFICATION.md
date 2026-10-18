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

Run `python verify.py` with Python \(3.10\) or later and SymPy \(1.10\) or later. The exact checker exhausts all \(\binom{15}{7}\) candidate seven-hyperplane intersections, all facet-intersection faces, every normal-cone smoothness test, all maximal singular components, and the primitive lattice circuits of the local transversals.

Actual output from the embedded checker:

```
VERIFY_OK: 29 vertices; 15 facets; 1151 faces; 322 singular orbits;
14 maximal singular faces (7 dim4 conifold, 7 dim3 Segre 2x3);
all simplicial normal cones unimodular; local circuit lattices saturated.
```

The proof's finite computation is exhaustive for this named polytope. The checker does not establish novelty, infer a theorem for arbitrary cycles, or determine nonreduced singular-scheme structure. Independent audit has not been performed.
