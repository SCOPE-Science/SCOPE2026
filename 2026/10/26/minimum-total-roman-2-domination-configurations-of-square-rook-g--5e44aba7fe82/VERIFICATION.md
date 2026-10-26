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
The included `verify_rook_tr2.py` is standalone Python 3 code using only the standard library. Run `python3 verify_rook_tr2.py` in the directory containing that file. The code directly checks all three-valued labelings on boards \((p,q)=(2,2),(2,3),(2,4),(3,3),(3,4)\), comparing the minimum weights with the rectangular formula. It separately enumerates binary supports on \(n\)-by-\(n\) boards for \(2\le n\le4\), and uses exact rational arithmetic and labeled bipartite spanning-tree weights to compute counts for \(2\le n\le10\). All three closed congruence formulas agree with these counts. Successful execution prints `ALL_TESTS_PASSED`; failures raise assertions.

The infinite-parameter proof is in `RESULT.md`. Finite brute force does not prove its general claim. The checker independently computes the component exponential coefficient but uses the mathematical tree formula; that standard theorem is not machine-certified. The full 2009 rook-graph paper remains inaccessible for definitive priority assessment. No independent audit has been performed.
