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

The proof uses the path continuant, a direct decomposition of the clique adjacency over characteristic two, an exact two-block Kronecker-sum calculation, and finite-dimensional kernel and orbit counting. No external infinite certificate is claimed.

The standalone script `artifacts/verify.py` reconstructs each graph and checks exact binary matrix ranks for 13 parameter cases (50 fixed-space rank comparisons), exhaustive complete state trajectories for four small cases (21,056 configurations), and invertibility after adjoining a column at lengths four and sixteen. `artifacts/verification_output.txt` records the actual output. The finite computations are supporting tests rather than a proof for arbitrary parameters.

The known Dirichlet Rule 90 nilpotence result is prior work; the novel claims concern the clique-fibre split and the complete cycle and transient census. Primary literature and historical comparisons have access and coverage limitations explained in `REVIEW.md` and `AUDIT.json`. Independent audit is not performed.
