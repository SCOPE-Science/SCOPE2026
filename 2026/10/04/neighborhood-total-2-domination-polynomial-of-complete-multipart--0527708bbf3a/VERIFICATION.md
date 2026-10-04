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

`verify.py` independently reconstructs the graph from each nondecreasing part-size profile of total order at most \(10\). For every vertex subset it checks the literal two conditions: each outside vertex has at least two selected neighbors, and the graph induced by the union of the selected vertices' open neighborhoods has no isolated vertex. It then compares that result with the theorem's part-profile criterion.

For every cardinality it independently evaluates the coefficient formula by dynamic programming over allowed part occupancies and compares it with brute-force counts. It also checks the closed minimum formula against the first nonzero brute-force coefficient.

Replay command:

`python3 verify.py`

Expected output:

`VERIFY_OK profiles=128 subset_checks=64916 criterion_checks=64916 valid_sets=48021 coefficient_checks=923 gamma_checks=128 max_order=10`

The computation covers a finite range only. It is a stress test and reproducibility check; the proof in `RESULT.md` supplies the argument for arbitrary positive part sizes.
