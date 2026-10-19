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

The finite check is implemented in `verify.py` with only the Python standard library. Run `python3 verify.py`; the program enumerates all disjoint-source/target partial injections of index at most two, checks commutation by direct partial-function composition, and counts the exact prescribed-product fibers for \(n=0,1,\ldots,7\). The expected counts come from a separate integer recurrence for alternating paths and cycles; the program does not construct expected fibers from its measured totals. Full agreement ends with `VERIFY_OK`.

The checked total pair counts in increasing \(n\) are \(1,1,7,31,277,2101,22891,245827\). In particular, products of ranks greater than \(\lfloor n/4\rfloor\) were absent in each checked case. The proof in `RESULT.md`, not the finite calculation, establishes the assertions for arbitrary \(n\). No computational or formal proof system independently certifies the theorem.
