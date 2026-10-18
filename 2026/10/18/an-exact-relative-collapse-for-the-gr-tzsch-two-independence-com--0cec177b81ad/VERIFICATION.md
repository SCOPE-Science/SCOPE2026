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

# Reproducibility and limits

The certificate file `verification/relative_collapse_pairs.json` contains precisely 105 face pairs. Run `python verification/verify_relative_collapse.py` to regenerate the graph and both entire simplicial complexes, verify each free-face condition against every current strict coface, check the intermediate downward-closure invariant, and confirm the remaining complex is exactly ordinary independence.

Run `python verification/verify_sphere.py` to reconstruct the ordinary independence complex independently, produce 50 discrete-Morse pairs, topologically sort its full 255-incidence oriented Hasse graph, and verify the critical cells. A further calculation of mod-two chain ranks for both complexes agrees with the spherical conclusion. The exact outputs of both scripts are included as text files.

Both checks are finite exhaustive verifications. The relative-collapse proof is finite by construction; no claim about infinite graph families is made. The matching proves an integral homotopy equivalence, not merely a mod-two Betti-number statement. No independent external mathematical review has been performed.
