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

Run `python3 verify.py` with the Python 3 standard library from the extracted package directory. The program builds letter actions directly as cyclic bit rotation and merging the last state into zero. It tests strict cost-to-go inequalities for all 130,918 nonsingleton subsets of the automata of sizes 2–16, each under four positive letter-cost pairs. An independent reverse-Dijkstra shortest-path implementation reproduces the proposed cost for every subset of sizes 2–12, using three positive weight assignments. Finally, direct word replay establishes the proposed word's effect for all nontrivial subsets through size 9 and for selected random subsets through size 128.

The included `verification_output.txt` contains the execution output, ending in `VERIFICATION_OK`. The loops are bounded and finite; they are not mathematical proofs for unbounded state sizes. The proof of the all-size statement appears in `RESULT.md`. The mathematical review is a self-review only; independent audit is not performed.
