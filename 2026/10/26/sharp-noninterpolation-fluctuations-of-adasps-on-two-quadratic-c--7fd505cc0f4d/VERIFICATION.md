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

The standalone `verify_adasps.py` in this package executes 6,144 finite binary sampling paths of length eleven (three scales times \(2^{11}\) paths), comparing the original source-defined loss/gradient/minimum step with the analytically reduced recurrence. It also performs seeded independent-sign simulations for 14,000 paths at length 8,192 for each of the fixed scales \(c=1\) and \(c=2\). The observed square-root-scaled second moments are compared with \(1/(2\sqrt2 c)\) at a finite-sample tolerance, and the accumulated sampled loss with its limiting per-observation value \(1/2\).

Run from the package directory with `python verify_adasps.py`; NumPy is the only nonstandard dependency. The verified executable checks finite algebra and empirical agreement only. It does not constitute a proof of convergence in distribution or a priority assessment. The analytical proof is contained in `RESULT.md` and requires no random-simulation assumption. Independent scientific audit has not been performed.
