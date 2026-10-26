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

The self-contained files `verify.py` and `certificate.json` reconstruct an exact 2,833-state rank-three logical transition closure over two binary-word append operations. Run `python3 verify.py` with these files in one directory. The recorded result is `verification_output.txt` and begins with `VERIFY_OK`.

The checker reconstructs every representative graph, all 5,666 table transitions, uniqueness of all 2,833 specialized logical profiles, reachability and breadth-first shortest paths (maximum 21), and all words of length at most 11. A separate generic atomic-diagram Hintikka recursion checks 204 selected representatives and all words of length at most six. This provides finite computational evidence, not external independent validation. The universal argument is the chain-word representation lemma plus preservation of three-round equivalence by both word operations, proved in `RESULT.md`.

Limits: no exhaustive search over all graphs of size 21 was needed or claimed; only complete coverage of the two-operation class and closure is proved. The table and checker must be rerun to confirm the numerical claims. Independent scientific audit has not yet been performed.
