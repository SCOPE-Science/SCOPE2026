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

# Computational and analytic verification

Run `python verify.py` with the standard Python library. The verifier constructs \(K_3\square K_q\square K_q\) for every \(4\le q\le14\), enumerates the explicit minimum rectangles, validates the tight \(q\)-neighbour threshold in every class, and checks the local capped-square bounds for every directional occupancy. It separately enumerates all \(397593\) nonempty subsets of sizes one through six of the ternary three-cube, verifying the boundary cardinality and all 54 size-six cores; this older balanced case lies outside the new theorem.

The expected final console marker is `VERIFY_OK`. Each finite check supports reproducibility but is not a proof for all \(q\); the full argument is supplied in `RESULT.md`. Independent audit has not been performed.
