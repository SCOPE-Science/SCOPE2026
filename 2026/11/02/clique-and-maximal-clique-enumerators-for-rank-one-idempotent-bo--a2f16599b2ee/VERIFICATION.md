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

The companion `verify.py` reconstructs every Boolean-rank-one idempotent rectangle and performs direct Boolean matrix multiplication; commutation is determined from the computed products, not imported from the theorem. It builds each finite commuting graph, recursively enumerates every clique, scans all vertices for maximality and separately checks the claimed coordinate-coverage criterion. The observed all-clique and maximal-clique rank vectors agree with both symbolic inclusion–exclusion formulas for \(1\leq n\leq4\). The largest tested graph has \(175\) vertices. Execution ends with `VERIFY_OK`.

The mathematical argument is for every integer \(n\geq1\); finite experiments are corroborative and do not prove the infinite statement. No independent scientific audit was performed. The enumeration excludes zero, higher Boolean-rank idempotents and non-idempotent commuting elements. Originality with respect to broader general enumeration formulas is not independently established.
