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

Run `python3 verify.py` using Python 3 and no external packages. The included `verification_output.txt` records the output of the same standalone code as executed in the provided scientific package. The verifier constructs unlabeled graphs with one to five vertices from all labeled edge masks and all vertex relabelings, tests every vertex subset for maximal independence, and checks all possible bounded palette assignments for both ordinary packing feasibility and first-fit realizability. The exact small-order graph class totals are 1, 2, 4, 11, 34; well-covered totals are 1, 2, 3, 7, 14; a unique well-covered graph at order five has unequal chromatic parameters, namely 3 and 4. Its graph is checked explicitly against the stated pendant-path triangle.

Additionally, the verifier constructs clique-tail graphs of clique orders 3 to 10, checks the exhibited packing and greedy colorings, and verifies well-coveredness by exhaustive subset testing. For clique orders 3 to 5 it independently enumerates all color maps and determines both chromatic parameters exactly. The infinite-family claim is proved in RESULT.md by structural bounds and explicit colorings; the finite checks are corroboration, not a substitute for that proof. The uniqueness result is genuinely finite and is certified by an exhaustive search whose coverage follows from enumerating every adjacency mask and every color assignment. No assertion is made about other graph families, the order of larger counterexamples, bibliographic exhaustiveness, or independent validation.
