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

Run `python verify.py` with any current Python 3 installation; no third-party packages, downloads, randomness, or external data are needed. `verify.py` contains a fixed graph6 fixture giving every graph-isomorphism representative on one through six vertices, and independently implements power domination, a search through uniquely restricted target-covering matchings, and the constant-width forest polynomial recursion. The full run terminates after the checks described below; `verification_output.txt` contains the captured output from the supplied script.

Exactly 208 graph-isomorphism representatives were checked. Their leaf coronas have 676900 initial vertex subsets, all compared directly with the matching characterization. Exactly 42 of the representatives are forests, accounting for 93924 initial subsets; for every one of those forest graphs, the entire coefficient list from the recursion matched direct subset enumeration. The additional four-cycle counterexample verifies that ordinary matchability without unique restriction can incorrectly predict successful observation. Selected small path-corona coefficient vectors are printed, providing numerical test cases.

The program tests only base graphs with at most six vertices. It supplies finite regression evidence; the arbitrary-order theorems rest on the forcing-sequence bijection, the alternating-cycle argument, Hall's theorem, and the inductive tree-interface recurrence written in `RESULT.md`. No infinite exhaustive enumeration, formal machine proof, independent validation, or complexity certificate is claimed. The recursive polynomial bound assumes arithmetic on nonnegative integers; their bit lengths remain linear in base-graph order.
