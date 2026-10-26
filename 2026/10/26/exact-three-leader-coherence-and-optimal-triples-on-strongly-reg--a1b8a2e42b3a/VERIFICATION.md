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

Run `python verify.py` in the directory containing `requirements.txt` after installing its indicated packages. The script performs exact symbolic arithmetic for the four induced triple patterns and their three successive cost gaps; checks the resolvent and strongly regular adjacency identities by matrix multiplication; reconstructs exact inverse grounded Laplacians in nine representative connected strongly regular graphs; and verifies exact counts of optimal triples. Its last line starts `VERIFY_OK` after all assertions pass.

Proof coverage is analytic: Jacobi's complementary-minor identity, the strongly regular resolvent identity, the four determinant/adjugate calculations, and strictly positive exact gap rational functions imply the theorem for all finite admissible graphs. Finite graph enumeration alone is not a proof of the all-parameter theorem. The code is a reproducibility check, not an independent mathematical audit.
