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

# Reproduction and limits

The packaged `checker.py` uses only the Python standard library. From the folder holding it, run `python3 checker.py`; it enumerates all Prüfer sequences for orders two through six, canonicalizes labeled trees, recursively computes the exact indicated total game length for every declared subset, and compares all nested declared-set pairs. The exact stdout of the execution performed for this finding is in `checker_output.txt`.

The completeness theorem for Prüfer encodings establishes the exhaustive coverage of labeled trees. Taking the lexicographically smallest recursively sorted rooted code over all possible roots gives an exact unrooted-tree isomorphism signature. The minimax recurrence is an induction on the number of selected vertices and includes every permitted indication and every possible Staller choice; all transitions strictly increase the selected set. Its exhaustive table yields no violating tree up through order five and one violating class at order six, the class of \(T_0\).

The verifier additionally computes optimal game values for \(0\leq r\leq7\). These are consistency checks, not the argument for all \(r\); the infinite family follows from the independent move-by-move strategies in `RESULT.md`. No assertion is made about larger optimal predomination gaps or an exhaustive census beyond six vertices. Independent validation has not been performed.
