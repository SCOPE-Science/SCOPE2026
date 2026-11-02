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

# Reproduction
Execute `python3 checks/verify_clebsch.py` in this directory; no third-party dependencies or external files are required.

The checker enumerates all 65,536 subsets of the sixteen-vertex graph, obtains 392 nonempty faces with face numbers (16,80,160,120,16), constructs an explicitly specified matching with 191 ordinary matched pairs and ten critical cells, verifies acyclicity by a complete directed Hasse-graph topological sort (392 nodes, 1,200 arrows), checks all 1,920 distinct automorphisms, and computes every signed fixed-face Lefschetz trace.

The resulting trace distribution is -5:20, -3:60, -1:884, 1:865, 3:80, 5:10, 9:1. Every trace agrees with the stated rational module; group-average traces yield four translation-fixed and zero full-group-fixed third homology classes.

Expected success marker: `CLEBSCH_WD5_NINE_SPHERES_CHARACTER_OK`.

The finite Morse computation proves the homotopy claim, not merely rational Betti numbers. The group representation is asserted over rational coefficients; the checker does not claim a splitting over the integers or decide integral torsion in quotient spaces. This is a reproducible self-review, not independent validation.
