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

The theorem is verified analytically in `RESULT.md`. The support-function reduction uses closed numerical ranges, guaranteeing compactness in the scalar plane even in infinite-dimensional Hilbert spaces. The numerical deficit integral is split on one angular interval, and the exact antiderivative is explicitly displayed. The phase distance is the norm of the imaginary part after an optimal scalar rotation; the lower-bound inequality is homogeneous under positive rescaling. The exceptional zero operator is excluded from denominators (its extension satisfies the degenerate zero statement).

For the normal diagonal family, direct integration of \(\max\{|\cos\theta|,\varepsilon|\sin\theta|\}^2\) yields the exact closed formula and \(O(\varepsilon^5)\) remainder, while minimizing \(\max\{|\sin\phi|,\varepsilon|\cos\phi|\}\) yields the exact norm distance. Run `python verify_example.py` for supplementary deterministic quadrature of this explicit model. Such finite checks do not establish the infinite-dimensional theorem or literature originality.

Same-model review: passed. Independent audit: not yet performed.
