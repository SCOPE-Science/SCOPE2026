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

# Reproducible verification

Run `python3 verify.py` using only the Python 3 standard library. It builds all 32 states and their binary input transitions and exhaustively explores the determinized subset product with the saturated integer-value recognizer. Every reachable product state is checked, rather than sampling inputs. The program asserts no predicate mismatch and independently recomputes the three finite exception lists for targets below 3000. Expected exact product-state count is 88 for each parity pair, and the maximum active NFA subset size is 16.

The finite-state invariant and machine definition are fully written in `RESULT.md`. The proof has no external files, input data, random seeds, network requirements, or unbounded search. The external mathematical literature comparison is self-review, not a completed independent validation.
