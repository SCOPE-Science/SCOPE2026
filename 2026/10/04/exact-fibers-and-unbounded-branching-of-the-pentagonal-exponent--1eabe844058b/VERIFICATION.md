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

The proof is algebraic and covers every positive integer target. The standalone script `verify_fibers.py` is a corroborating exact replay.

It performs an exhaustive comparison for every \(1\le n\le400000\). Direct source enumeration only needs \(1\le m\le200000\), because \(e(m)\ge2m\), so this is exhaustive rather than a truncated source search for those targets. For each target, the direct preimage list is compared to the list produced by the theorem's valuation-and-divisibility formula.

The script also constructs the first three levels of the unbounded-branching family. For \(R=1,2,3\), it verifies each prescribed valuation identity, forms the least common multiple of the required odd factors, constructs every claimed preimage, and directly checks \(e(m_t)=n\).

Observed output:

`VERIFY_OK exhaustive_targets=400000 source_m=200000 constructions=[(1, 1, [0, 1], [3, 1], 2, 3), (2, 9, [0, 1, 3], [11, 5, 1], 3, 15), (3, 2057, [0, 1, 3, 11], [2059, 1029, 257, 1], 4, 2087)]`

The computation does not prove unboundedness; that conclusion uses the arbitrary-\(R\) recurrence argument in `RESULT.md`. The replay uses only exact integer arithmetic and the packaged script has no external dependencies.
