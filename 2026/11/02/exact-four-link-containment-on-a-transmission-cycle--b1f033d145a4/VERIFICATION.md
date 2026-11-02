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

The result is established analytically in `RESULT.md`. The accompanying `verify.py` uses only the Python standard library and computes independent exact rational state sums, formula checks, and finite placement minimizers.

Run `python3 verify.py` from the directory containing these files. Verified checks: all positive ordered four-part arc configurations for totals from four through ten at barrier probability \(2/5\), and exact minimizer classification for totals four through sixteen at probabilities \(1/9\), \(1/2\), and \(9/10\). The program explicitly computes all sixteen edge-state probabilities for its state-sum comparisons.

These finite enumerations do not establish the theorem for arbitrary cycle length or arbitrary real transmission probability. That conclusion rests on the exact pairwise connection identity, orthogonal eigenvalue decomposition, and integer parity argument in `RESULT.md`. Numerical simulation and external independent audit were not used.
