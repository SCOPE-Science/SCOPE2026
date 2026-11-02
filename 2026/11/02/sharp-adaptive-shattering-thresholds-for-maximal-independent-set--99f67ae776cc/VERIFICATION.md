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
# Finite exact verification and scope

Run `python3 verify.py` and `python3 independent_check.py` from the directory containing `certificate.json`. Both require only Python standard libraries; the exact expected output is stored in `verification_output.txt`. Each checks all path orders from one through thirteen and all cycle orders from three through thirteen (twenty-four graph cases). The first checks every vertex-support projection, exact minimax ranks, and each leaf of the depth-four and depth-five witnesses; the second independently enumerates concepts using a recursive independence construction and computes shattering and online ranks by a different method.

The mathematical completeness argument is in `RESULT.md`: every maximal independent set is an independent dominating set, every such set appears in the complete binary-mask enumeration, support shattering has a direct projection test, and the recursive rank rule follows by the first query. Thus no unexamined finite cases remain in the claimed ranges. The explicit path and cycle certificates allow a small witness-only replay separate from the dimension search.

The product additivity statement applies only to disjoint query supports and independent component hypotheses. No conclusion about the complete connected-path or connected-cycle dimension sequence above the checked range is claimed. Historical-priority comparisons and independent external scientific validation remain open.
