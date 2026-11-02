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

# Reproducibility and scope

Run `python3 verify.py` with the Python 3 standard library. It exhaustively tests the twenty triple row determinants of each normal matrix, constructs all 123 actual arrangement faces by integer cross-products and sign calculations, counts all ordered commuting pairs and triples directly from the sign-coordinate relation, and compares independently enumerated maximal cliques with the chamber-face incidence sets. It checks the chamber side distributions \(\{3:12,4:16,5:4\}\) and \(\{3:12,4:18,6:2\}\), plus the formula values at \(k=0,1,2,3,4\). Successful output terminates with `VERIFY_OK`. The general proof for all arrangements and all tuple arities is mathematical, not an extrapolation from finite test cases.
