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

The included standalone Python program enumerates all three-label maps on each crown graph of orders \(n=3,4,5,6\), reconstructing all adjacency neighborhoods from the deleted matching. It checks zero independence, a defender label two for each zero, and total domination of every positive vertex, then calculates minimum weight and multiplicity. The program checks every optimum labeling against its stated structure. Finite checking does not establish the universal theorem; the complete proof appears in RESULT.md. Independent validation is not performed.
