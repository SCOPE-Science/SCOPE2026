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

The proof reduces arbitrary irreducible totally invariant closed sets to linear subspaces by Luo--Meng's published Linearity Theorem (arXiv:2610.10103v1); that external theorem is an explicit assumption of the argument, not independently reproved. Root-of-unity coordinate scaling then isolates basis directions inside any invariant linear subspace. This yields the necessary-and-sufficient coefficient-block vanishing condition. Directed reachability gives all incidence relations and all counts. Fixed dimension imposes exactly \(\(s(N-s)\)\) independent conditions on the mixing matrix, and a triangular-matrix construction realizes all finite distributive lattices with at least two elements.

To rerun the finite sanity checks, place the embedded `verify.py` beside this document and execute `python verify.py` with Python 3. Its stdout ends in `VERIFY_OK`, as reproduced during the review. It tests all invertible binary off-diagonal support patterns with nonzero diagonal in dimensions two through four and representative graph types. Finite exhaustive examples are not proofs of the all-dimensions theorem.

No independent audit or validation has been performed. The complete text of the earlier Chang--Luo general bound was not accessible through the attempted public routes; overlap beyond its known numerical bound remains possible.
