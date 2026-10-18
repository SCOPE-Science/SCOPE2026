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

The proof in RESULT.md is analytic. The accompanying `check_half_tongue.py` uses Python 3 and SciPy for one-dimensional roots, a bounded optimizer, and independent checks of the exact lifted second-iterate equation. Run `python check_half_tongue.py`; successful execution prints `CHECK_OK` and `DIRECT_ITERATE_OK`. The checked couplings are \(K=0.05,0.1,0.2,0.5,0.8,0.95,0.999\). The two width formulae agree to the stipulated numerical tolerance. At \(K=0.8\), off-center detunings inside the tongue give four lifted 2-periodic points (two cycles), while a detuning just outside gives none. The analytic derivation also supplies the exact implicit-root monotonicity and high-order expansion. No collection of numerical samples proves an infinite-domain assertion; those are proved by the mathematical argument. No external independent audit or validation has been conducted.
