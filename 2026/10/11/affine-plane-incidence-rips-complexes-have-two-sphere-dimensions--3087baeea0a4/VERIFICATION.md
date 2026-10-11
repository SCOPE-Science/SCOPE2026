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

# Reproducibility and mathematical checks

Execute `python verify_affine_rips.py` using only the Python standard library. The program enumerates graph-distance cliques and builds exact mod-two simplicial boundary matrices for the incidence graphs of the prime affine planes of orders \(2\) and \(3\). Each graph is reconstructed from coordinate incidence, and all shortest paths are independently computed. In order \(3\), the scale-two face vector is \((21,126,282,255,135,84,36,9,1)\); the boundary ranks are \((20,106,160,79,56,28,8,1)\); the only nonzero reduced Betti numbers are \(\widetilde\beta_2=16\) and \(\widetilde\beta_3=16\). In order \(2\), the scale-two reduced rank is \(\widetilde\beta_2=4\); that boundary order is deliberately excluded from the principal all-order statement. A point vertex has distance at most three from every vertex, so at scale three the complex is a cone; all pair distances are at most four, giving a full simplex at scale four. The checker verifies these statements without enumerating those large simplices.

Successful execution ends with `VERIFY_OK affine_incidence_rips q=2,3 exact_GF2_scales=1,2; scales=3,4 cones`. Exact stdout is included in `verification_output.txt`. A finite check is corroboration, not a proof for arbitrary \(q\). The general proof depends on the explicit incidence axioms, a homotopy-pushout decomposition, and the join homotopy type for the parallel-class complex. Integer homotopy wedges justify all-field persistence, not merely the mod-two test.
