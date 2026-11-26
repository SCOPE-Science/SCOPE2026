---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

Run the accompanying `verify.py` with Python 3.9 or later. It uses only the standard library. For each of ten finite examples over the trivial, cyclic, Klein four or symmetric group of degree three, it constructs Brandt multiplication and computes the commuting graph, recursively enumerates every clique, and compares its size-coefficient dictionary with the inclusion–exclusion formula. The program's `cliques` assertion in `run_case` is the check for the corrected finding. The script also checks maximal-clique quantities and a graph isomorphism, which are outside the corrected finding. The expected final marker for the whole script is `VERIFY_OK 10 independent finite multiplication checks`.

The tests exhaust the indicated finite examples only. The proof in `RESULT.md` uses the exact local commutation rule and inclusion–exclusion on the occupied sources and targets. No finite run proves the arbitrary-group statement or establishes priority.
