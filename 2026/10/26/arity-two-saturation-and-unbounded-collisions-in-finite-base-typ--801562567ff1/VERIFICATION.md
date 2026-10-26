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

Run `python code/check_grid.py` from the package's top-level extracted directory using Python 3 and only its standard library. `verification/check_output.txt` records the output actually obtained by executing this exact embedded checker. It compares orbit counts obtained by canonical row-and-column equality words with the Bell/Stirling closed formula for the four-point witnesses through arity four. It also enumerates all simple bipartite graphs with at most three edges and no isolated used row or column, grouping their side-preserving isomorphism types by edge and support count, and verifies the inverse formula from the first two type counts.

The four-cell witnesses both produce the vector `(1, 8, 82, 1067, 17108)`. The independent finite checks returned `ALL_CHECKS_PASS`. These checks do not establish the formula for all tuple arities or unbounded base size; those statements follow from the group-action and involution proofs in `RESULT.md`. Literature noncoverage likewise cannot be settled by computation. No independent scientific audit has been performed.
