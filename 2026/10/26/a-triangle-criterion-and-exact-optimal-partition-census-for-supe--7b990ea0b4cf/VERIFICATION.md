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
# Verification evidence

The proof in `RESULT.md` is an unrestricted finite-combinatorial argument. Executing `python3 verify.py` independently constructs each graph's super-dominating sets from private external neighbors, forms the two-deletion graph, enumerates admissible unlabelled partitions, and checks all claimed values. All qualifying isolate-free graphs of order five and deterministic samples of larger graphs at orders six and seven are tested, a total of 2,388 qualifying graphs. The preserved output is in `verify_output.txt`.

These finite experiments do not prove the all-order theorem; its proof is the four-lemma deduction in `RESULT.md`. No outside mathematical certification or independent audit was performed. Originality was compared with the primary arXiv full-text bounds and exact graph-family results; the separate indexed multipartite result's full text was not read, limiting publication-priority assurance for that credited subcase.
