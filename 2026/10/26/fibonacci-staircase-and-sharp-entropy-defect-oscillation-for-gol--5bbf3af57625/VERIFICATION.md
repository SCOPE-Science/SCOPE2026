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

# Verification and reproducibility

The included Python 3 standard-library script `verify.py` computes irrational rotation points with exact field arithmetic in the basis \(1,\alpha\), with \(\alpha=(\sqrt5-1)/2\). For each insertion of the next point up to 2000, it checks both strict ordering and the two Fibonacci predecessor indices, the exact pair of child gap lengths, and the entropy increment within floating-point logarithm error. The run prints `VERIFY_OK` with 2000 passing splits, 16 tested Fibonacci index windows, and maximum floating-point entropy-increment error below \(6\times10^{-14}\). A separate direct sort-and-gap entropy calculation for \(1\le n<120\) agrees with the closed formula. This finite corroboration cannot replace the all-index unimodular-basis proof in `RESULT.md`.

Reproduce with `python3 verify.py` from the extracted package directory. No third-party modules, network calls, hidden data or external files are required.

No independent audit or external mathematical certification has been conducted. The historical-priority comparison is limited to the identified checked sources.
