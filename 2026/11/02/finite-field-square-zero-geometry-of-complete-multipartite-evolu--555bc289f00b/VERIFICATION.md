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

# Verification
Run `python3 check_multipartite.py` from the package directory. The program uses only the Python standard library and constructs the actual square-zero equations from the multipartite adjacency pattern. It independently enumerates solutions and the rank of their finite-field linear span over \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), \(\mathbb F_9\), and \(\mathbb F_{11}\). Its twenty-one configurations include resonant and nonresonant cases, singleton and nonsingleton parts, and two quadratic-character values of \(-1\).

The recorded successful output is in `checker_output.txt`; the required terminal marker is `MULTIPARTITE_EVOLUTION_ABSOLUTE_NILPOTENTS_OK 21`. The program tests rational-point counts and linear spans only. It does not computationally establish geometric irreducibility, scheme reducedness, or any uniform statement beyond the tested cases; these follow from the written proof. The proof uses classical quadratic Gauss sums, the finite-field isotropy of nondegenerate forms in at least three variables, and standard geometric facts about complete intersections, all explained in `RESULT.md`. No independent external review has been performed.
