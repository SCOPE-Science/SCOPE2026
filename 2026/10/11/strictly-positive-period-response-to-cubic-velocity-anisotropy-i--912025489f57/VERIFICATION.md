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

The proof is analytical. Independent computations in `verify_period.py` integrate the nonautonomous scalar first-order periodic problem with a standard-library fourth-order Runge–Kutta method, solve its affine periodicity relation, and compare the positive-square representation against the forcing-pair representation. At fixed sampled \(q>0\), the two integrals must agree to numerical error. Values at small \(q\) are also compared with \(\pi q^2/16\). The checks exercise the exact equations written in RESULT.md; they do not certify every real parameter or independently audit novelty. The analytic hyperbolic-continuation, identity, and asymptotic proofs carry those claims.

To reproduce, run `python verify_period.py` with Python 3.9 or later and no third-party dependencies. The script prints numerical values and exits nonzero if a comparison fails.
