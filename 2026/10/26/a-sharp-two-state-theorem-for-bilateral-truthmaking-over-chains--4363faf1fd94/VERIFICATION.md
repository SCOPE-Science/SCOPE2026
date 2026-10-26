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

# Finite checks and deductive scope

The supplied `truthmaker_chain_checker.py` runs using Python 3 without external packages. It recomputes the formula sets from the exact bilateral non-inclusive clauses and separately computes membership/prefix profiles by Boolean gates. Exhaustive checks cover 835824 formula/profile pairs across all valuations on chains of sizes 1–3 with two atoms and on a size-4 chain with one atom. It also checks 30948 fusion-gate/state cases on all subset pairs on chains of sizes 1–6, plus the singleton absorption identity and explicit 2-state/3-state sharpness models. Command: `python3 truthmaker_chain_checker.py`. Expected success line: `TRUTHMAKER_TWO_POINT_CHECK_OK 835824 30948 SHARP_2 NONCHAIN_3`.

Only the mathematical proof in `RESULT.md` establishes the arbitrary chain cardinality (including infinite), arbitrary formula-depth and arbitrary finite alphabet cases. The checker is finite corroboration, not a substitute for mathematical induction or an external certificate. It does not establish independent expert review or the historical priority of the result.
