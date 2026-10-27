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

# Reproducibility and limitations

Run `python3 check_moment_lens.py` using Python 3. The script requires no third-party packages and checks exact arc-integration identities with floating point evaluations, both endpoint regimes, the dual polynomial identity, and complex Fourier-coefficient bounds on 4,320 randomly selected measurable unions of subarcs whose integrals are calculated analytically (not sampled by midpoint quadrature). The recorded execution returns 41,864 passed assertions.

The proof for every measurable set and the convexity/purification argument are given in `RESULT.md`; finite tests cannot establish them. Originality was compared against identified earlier literature but has not received independent review. The pair of complex disks is not claimed to characterize all possible complex coefficient pairs jointly.
