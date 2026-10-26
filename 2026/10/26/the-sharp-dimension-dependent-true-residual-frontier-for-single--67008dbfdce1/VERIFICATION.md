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

The accompanying standalone `verify.py` can be run with `python verify.py` (Python 3 standard library only). It executes a rational exact sharpness witness with eigenvalues \(1\) and \(4\), six real-rank-one boundary configurations, finite perturbations to unique DEIM pivots, numerical near-pole constructions, and 2,000 pseudorandom rank-one SPD residual comparisons. During preparation it printed `PASS 2014`. It checks the actual sampled coordinate, full true residual, and finite theorem factor. The computational checks are finite and do not independently prove universal quantifiers. The analytic proof in `RESULT.md` handles all dimensions, boundaries, and the nonsingular limiting blow-up.
