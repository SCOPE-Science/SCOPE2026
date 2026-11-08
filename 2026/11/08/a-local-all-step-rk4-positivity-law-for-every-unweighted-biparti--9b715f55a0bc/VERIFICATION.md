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

# Reproducibility checks

Run `python3 verify.py` with standard-library Python 3. On the locally inspected copy, the program printed `VERIFY_OK`, with connected labelled bipartite graph counts \(1,3,19,195,3031\) for orders \(2,3,4,5,6\), total \(3249\), and \(18537\) verified edge discriminant inequalities. Every graph was tested at the six rational steps \(1/20,1/5,1/2,1,2,4\); direct rational RK4 matrices were compared against the local signs and exact entry formulas. The seven-vertex double-star central-edge and distance-three witness was additionally checked.

The verifier's enumerations are finite. The proof in `RESULT.md` handles all graph orders, all positive real timesteps and the unique-root and sign assertions analytically. The verifier uses no external dependencies, random seed, opaque state or external data. Independent mathematical review has not been performed.
