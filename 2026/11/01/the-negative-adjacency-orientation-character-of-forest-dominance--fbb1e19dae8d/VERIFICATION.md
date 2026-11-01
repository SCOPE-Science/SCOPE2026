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
The proof of the all-forest theorem is in `RESULT.md` and depends on the established rank-one forest dominance homology theorem. Its new steps prove coordinate restriction isomorphisms for negative eigenspaces, show local determinant signs agree with oriented crosspolytope-cycle facet coefficients, and establish connectivity of minimum vertex covers by single-edge swaps.

Run `python verify.py` with Python 3, networkx and numpy available. The recorded `verification_output.txt` is reproduced and reports 96 forests and 344 automorphism actions. The code checks all minimum-cover choices per tested action, independent simplicial Lefschetz characters and numerical negative-eigenspace determinants. The code is a finite cross-check, not a proof for arbitrary forests. Floating-point comparisons cannot establish exact infinite-family claims. An independent audit has not been performed.
