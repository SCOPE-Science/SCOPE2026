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
Run `python3 verify.py` with Python 3.9 or later; no third-party libraries are required. The stdout record is in `verification_output.txt` and ends with `VERIFY_OK`.

The dynamic-programming checker computes, for each potential forcing word and target pattern, the longest subsequence avoiding the target using greedy matched-prefix states; it enumerates all binary superwords for radii \(1\) through \(5\) and target lengths \(1\) through \(4\). An independent explicit deletion-set enumerator cross-checks radii \(1\) through \(3\). The program also checks the proof's five length-four template types (and the shorter template types) at radii \(1\) through \(50\), and confirms the maximal-family sizes and all alternative deletion targets at radii \(1\) through \(7\).

These are finite tests, not substitutes for the universal arguments in `RESULT.md`. The positive \(0110\) family is established mathematically by the symbol-counting contradiction, with precedence attributed to Xie, Sun, and Ge (2026). The code does not check every integer radius, every code subset, larger alphabets, or outside historical publication records. Independent external verification has not been performed.
