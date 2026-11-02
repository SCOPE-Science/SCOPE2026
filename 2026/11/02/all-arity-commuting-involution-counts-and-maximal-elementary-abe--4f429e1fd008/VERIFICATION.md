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
Run `python ut4_involution_checker.py` under standard Python 3 (no dependencies). The test enumerates all \(64\) group elements when \(q=2\), all \(4096\) when \(q=4\), using exact coordinate arithmetic and a polynomial representation of the latter extension field. It directly checks square-one and pairwise-commutation conditions; enumerates all totally singular two-planes in the corresponding four-dimensional quadratic spaces; and checks all commuting triples and maximal elementary abelian cliques for \(q=2\).

Expected successful marker: `UT4_INVOLUTION_POLAR_CENSUS_OK`. The verified counts are \(C_1(2)=28\), \(C_2(2)=448\), \(C_3(2)=6112\), \(C_1(4)=496\), \(C_2(4)=96256\). Exactly six and ten maximal totally singular two-planes appear at \(q=2\) and \(q=4\). At \(q=2\), maximal elementary abelian subgroup orders are \(16,8,8,8,8,8\).

Finite enumeration does not establish the universal parameter statements; those rely on the matrix and quadratic-form arguments in RESULT.md. Independent audit: not performed.
