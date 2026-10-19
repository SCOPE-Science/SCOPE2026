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

# Reproducibility and mathematical limits

Run `python3 verify.py` from the same directory as this document. No network, random seeds, third-party library, or machine tolerance is used. The code forms exact integer affine branches for every weak sign itinerary, eliminates the two unknowns by Fourier–Motzkin pairing, reconstructs every feasible point in rational arithmetic, and replays its stated period and branch conditions independently from the original piecewise map.

A successful run prints the six inventory lines, the canonical period-five and period-eleven cycles with traces, and `EXACT_ODD_PERIOD_CENSUS_OK`; an expected transcript is supplied in `CHECKS.txt`. Crucial finite certificates consist of **all** \(2^n\) sign systems for each \(n\in\{1,3,5,7,9,11\}\) and exact feasibility tests, not a floating-point grid or empirical trajectory search. The proof in `RESULT.md` explains why their enumeration is mathematically exhaustive. Checks do not establish anything at even periods or at periods beyond eleven, and external independent validation has not been performed.
