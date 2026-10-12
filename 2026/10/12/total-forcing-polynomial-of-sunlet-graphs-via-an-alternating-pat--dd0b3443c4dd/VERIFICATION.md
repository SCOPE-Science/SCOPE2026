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

# Verification of the sunlet total-forcing polynomial

Execute `python3 verify_total_sunlet.py` from the directory containing the code and its optional output record. This is standard-library Python code, with no external data or nonstandard package dependency. It defines the original \(2n\)-vertex sunlet graph directly, independently simulates the ordinary forcing process on every subset for \(3\le n\le8\), and requires the initial blue subgraph to contain no isolated vertices.

The transfer matrix implementation explicitly constructs fifteen states and thirty-eight weighted transitions; the matrix characteristic polynomial is verified by exact Newton identities in the integral polynomial ring. A second combinatorial checker independently enumerates all \(3^n\) words and applies alternating-path peeling for \(3\le n\le11\). Every coefficient comparison passed.

The direct enumeration covers 87,360 subsets in total for lengths three through eight. For nine through eleven, only the word classification versus transfer is checked, not every original graph subset. These are finite tests; the general result for arbitrary \(n\) follows from the mathematical proof and is not claimed to have been exhaustively certified by computation. The captured numerical and symbolic checks are preserved in `verification_output.txt`.
