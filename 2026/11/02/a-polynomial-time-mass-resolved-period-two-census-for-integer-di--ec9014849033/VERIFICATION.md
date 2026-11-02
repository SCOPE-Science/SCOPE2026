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
# Reproducibility and exact checks

Run `python3 tree_diffusion_verify.py` in this directory with Python 3 and no third-party dependencies. The output must agree byte-for-byte with `tree_diffusion_verify.log`, including its two final success markers `TREE_DIFFUSION_DP_VERIFIED` and `TREE_MASS_DP_VERIFIED`.

Independent enumeration of all Prüfer-coded labelled trees of orders one through six generated 1,442 cases (1,441 nontrivial). The verifier compares the complete mass-residue vector from rooted coefficient extraction with a separately implemented sign/gap enumeration for every case. It separately checks the unweighted total on all 1,441 nontrivial trees, computes chip-diffusion updates directly on selected bounded integer state grids, and tests larger paths and stars. It reconstructs the two six-vertex degree-multiset twins and their per-residue primitive-orbit populations.

The exhaustive statement is finite (vertex order at most six). The infinite-family conclusion is justified by the published proof's incidence-matrix kernel, exact gap sign reversal, tree integrability and root-mass calculation. No computation is represented as a proof over all trees. Reproducibility verifies the contained code and sample calculations, not uniqueness against every historical publication.
