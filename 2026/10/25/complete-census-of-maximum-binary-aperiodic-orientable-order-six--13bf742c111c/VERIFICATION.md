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

The complete executable `verify.py` uses the Python 3 standard library and runs without third-party datasets. Invoke `python3 verify.py`.

It derives the \(28\) reversal classes of allowed six-bit factors, computes optimal path lengths by an exact memoized recurrence over all \(32\) five-bit initial states, and independently enumerates literal words with reversal checks. The two implementations return identical *sets* of the \(22\) maximizers. Every nonpalindromic length-\(6\) orbit is used at most once, and the recursion exhausts all possible append-bit branches, establishing a global maximum \(21\) edges / \(26\) bits. The program checks the six orbit representatives and sizes under bit complementation and reversal, and their opposite constant length-\(5\) endpoints.

The expected output begins with `ORIENTABLE_ORDER6_PASS best_length=26 total_maxima=22 orbits=6`. The output includes the exact table of maximum transition depths and memoized state count; computations are finite and reproducible, not an inference about other word orders. `maximizers.txt` is the complete set as machine-readable data, distinct from full scientific source texts.

The mathematical proof requires the equivalence between the source problem and non-repeating reversal-class paths and the induction verifying the recurrence. The finite census is valid for this fixed domain only; review by a mathematically independent party has not been performed.
