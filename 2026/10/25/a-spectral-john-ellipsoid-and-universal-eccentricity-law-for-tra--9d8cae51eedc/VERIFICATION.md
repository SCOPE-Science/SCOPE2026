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

# Reproducibility and scope

Run `python checker.py` with Python 3 and NumPy. The checker constructs regular connected bipartite graph families, uses their unsigned incidence Gram matrices, solves the scalar equation by bisection, and checks every individual coordinate/edge support equality and both weighted John contact moment identities. The observed run was `VERIFY_OK graphs= 13 facet_norms= 893`; the cases are complete bipartite graphs with part sizes 3, 4, 8, 20, crown graphs with part sizes 4, 5, 7, cube graphs of dimensions 3, 4, 5, and even cycles of lengths 6, 8, 10. The cycle cases are supplementary consistency checks outside the new theorem's degree restriction.

No floating-point tolerance is relied upon for the infinite theorem. Its proof uses exact trace identities, spectral inequalities, bipartite integral polytope inequalities and John's exact contact criterion. The sample cases cannot establish the universal claim. No independent audit has been performed.
