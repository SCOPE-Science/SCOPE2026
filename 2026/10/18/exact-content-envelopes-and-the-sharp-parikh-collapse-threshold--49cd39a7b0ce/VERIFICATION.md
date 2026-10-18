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

# Verification instructions and limits

Use Python 3 (standard library only): `python3 checker.py`. The expected stdout is stored verbatim in `checker_output.txt`. The program separately computes longest common subsequences by dynamic programming and exhaustive Parikh feasibility by letter counting. For binary alphabets it checks all hosts of length up to \(k+1\), for \(1\le k\le6\), against every target of length up to \(k\). For ternary alphabets it checks all hosts of length up to \(k\), for \(1\le k\le5\), against all such targets. It also tests reverse-block sharpness for three larger alphabets and enumerates all host words of length at most seven (binary) or five (ternary) for content-envelope checks.

The resulting counts are 191852 plateau checks and 34188 host-pattern comparisons for the content envelope. These finite ranges are explicitly bounded. The independent finite program cannot establish the universal claims; the four proof lemmas in `RESULT.md` give the complete infinite argument. There is no claim of external proof certification or independent review.

Public reproducibility requires only these embedded files; no file paths outside this package, proprietary software or downloaded external paper are needed.
