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

# Reproducible arithmetic verification

Run `python verify.py` using Python 3 standard library. The verifier checks factorial denominator recurrences, exact rational truncations of the Liouville tail, the explicit \(3/Q_k\) Birkhoff-discrepancy upper bound inferred by the analytic estimate, and the growing lower bound for hypothetical transfer Fourier coefficients at the first several frequencies. The completed run reported `VERIFY_OK: 28 exact rational arithmetic assertions`.

The tests establish only finite rational inequalities. Infinite-series convergence, the all-index Birkhoff bound, failure of the continuous cohomological equation, Sturmian fiber descent, and nonmixing of the suspension are established in `RESULT.md` and are not inferred from finite enumeration.
