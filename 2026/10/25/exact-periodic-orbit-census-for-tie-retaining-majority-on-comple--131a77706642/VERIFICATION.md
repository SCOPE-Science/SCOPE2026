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
The proof in `RESULT.md` handles all positive integer part sizes by exact inequalities; no finite search is treated as an all-size argument.

Run `python verify.py`. The script checks the actual per-vertex rule on all labelled initial states for all ordered positive triples of part sizes with total order at most twelve. It also uses a separate binomial-weighted orbit count on all ordered triples with every part at most twelve, comparing predictions with the number of fixed states and of distinct primitive two-cycles. It prints `VERIFY_OK macro_part_triples=1728 micro_part_triples=220 micro_configurations=376824` on success; every check is an assertion that fails on a discrepancy.

Scientific limits: no independent audit, no exhaustive check for unbounded part sizes, and no claim about transient-length distributions. Exact all-size correctness is supported by the explicit energy and classification proof, not solely by the verifier.
