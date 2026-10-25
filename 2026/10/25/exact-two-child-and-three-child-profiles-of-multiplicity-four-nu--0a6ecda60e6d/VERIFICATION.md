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

The reproducible Python script `verify.py` uses only the standard library. Executing it checks all admissible multiplicity-four Kunz triples at genus 3 through 90, reconstructs the minimal generators by direct additive decompositions, determines the full-tree child count, verifies the three pair-family memberships, and checks each coefficient of the two-child rational generating function and the unique three-/four-child conclusions.

Observed output starts `VERIFY_OK genus_3_through 90 degree2_g26 14 degree3_g26 1`. No external verifier was used. The finite calculation is not a substitute for the general proof, and no independent audit has been performed.
