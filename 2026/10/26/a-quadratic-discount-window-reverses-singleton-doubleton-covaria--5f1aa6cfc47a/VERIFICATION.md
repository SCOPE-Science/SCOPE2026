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

# Verification

Execute `python verification.py` using Python 3. This independent state-enumeration implementation of the Chinese restaurant process, together with exact rational factorial-moment calculations, produced `PASS 2315 exact assertions` in the development environment. The checks include all state probabilities through eight labels for specified rational parameters, direct mixed moments, the exact Ewens boundary identity, and near-boundary sign examples for \(\theta=2\). The finite computations are not being promoted to an infinite-size proof.

The general theorem is verified analytically in `RESULT.md`: the marked-block probabilities give the exact ratio, the derivative at zero approaches \(1/\theta\), and a uniformly bounded second derivative controls the \(n^{-2}\) neighborhood and local root. The relevant limitations are fixed positive strength, small nonnegative discount, and no sign assertion for the asymptotically critical coefficient.
