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

# Reproducible verification and limits

Run `python verify.py` with NumPy installed (declared in `requirements.txt`). This program constructs the Gram matrix independently as `P*P`, evaluates its exact rational determinant on a finite barycentric grid, verifies positivity and spectral bounds at interior values, and compares asymptotic axis eigenvalues across six scales. The embedded output reports exactly 28,300 passed assertions. Determinant and gamma-function constants are evaluated separately.

The seed-fixed exploratory `sampling.py` draws 700,000 independent uniform directions (normalized Gaussian triples); `sampling-output.txt` includes the observed lower-tail rates for four thresholds. The ratios approach the proposed constant slowly, as the proof predicts for logarithmic asymptotics. These are **finite checks only** and do not prove an infinite-threshold law.

The proof in `RESULT.md` supplies the determinant algebra, compact spectral separation, off-axis tube bound, six local product-neighborhood contributions, and the limiting squeeze. It establishes the distributional statements for all thresholds tending to zero and the sharp negative-moment threshold. No independent audit or third-party validation was performed.
