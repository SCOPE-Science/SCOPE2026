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

# Reproducible integral verification

Run `python3 verify_gamma_tetra.py gamma_tetra_certificate.json` from the folder containing both included files using Python 3's standard library. The checker reconstructs all 228 normalized Γ-two-cubes and 12 ordered nondegenerate one-cubes, derives the exact signed differential, confirms boundary rank nine and composition zero, and checks all 219 selected Γ-three-cube boundaries. The 219 unit pivot reductions establish integral primitivity; together with the 219-dimensional kernel, this proves second Γ-homology is zero over integers rather than merely modulo a prime.

An exhaustive independent census of all 65,536 labelings of the three-cube confirms 32,868 admissible nondegenerate Γ-three-cubes; only the 219 included cube coordinates are required for the proof. The successful run ends with `VERIFY_OK C1=12 C2=228 C3=32868 d1rank=3 d2rank=9 primitive_d3_rank=219 H2Gamma=0`.

The proof does not address higher homology or establish bibliographic priority. Independent scientific verification has not been performed.
