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

# Reproducibility and verification

`verify.py` is a standalone Python 3 standard-library checker. Execute it from the directory containing the file with `python verify.py`.

The script constructs Euler cycles in the restricted overlap graphs for \(q=2,3,4\) and orders \(n=2,3,4,5,6\), checks the exact trace sequence, distinct cyclic windows, repeated shorter windows, and exact cylinder counts via integer adjacency powers. It also performs an exhaustive small-period census and a rational spectral-sign test. All such calculations are finite and only diagnose the general result. The analytic proof in `RESULT.md` supplies the universal finite-window bound, Euler construction, limiting content and sharp cylinder discrepancy; no infinite proposition is inferred from finite sampling.

Independent audit: not performed. No numerical calculation is offered as a proof of priority or scientific novelty.
