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
# Reproducible finite verification

Execute `python3 verify_d4_rips.py` in the directory containing `collapse_certificate.json`. Python 3.9+ and its standard library suffice. The program reconstructs the root coordinates and all simplices from squared Euclidean distances, verifies all 736 free-face removals, checks the 10-vertex sphere core and its tetrahedral facet list, verifies the octahedral vertex link and the 15-tetrahedron shelling of the deletion, and separately checks all 42 deletion collapse pairs. The successful output is recorded in `verification_output.txt` and ends with `VERIFY_OK`.

A complete finite replay is a proof of the listed elementary-collapse and shelling combinatorics, coupled with the stated topological gluing lemma. It does not test other metrics, minimality, equivariance, or independent publication priority. Previously tabulated integral homology data are acknowledged, not independently audited here.
