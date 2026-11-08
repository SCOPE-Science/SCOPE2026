---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For n≥2, SPD A and all symmetric Frobenius-unit-ball E, whitening gives B=I+t A^-1/2 E A^-1/2. The condition-number cap K>1 is exactly all orthonormal-pair quadratic inequalities. Frobenius duality reduces to sqrt(K²a²+d²-2Kb²) for the compression of H=A^-1; its plane-angle quadratic is convex, so extrema align with the top two compression eigenvectors; Poincaré/min-max bounds them by 1/λ1 and 1/λ2. Thus t*=(K-1)/sqrt(K²/λ1²+1/λ2²). Since t*<λ1, all endpoint matrices are SPD. Rank-two commuting E*=(-K h1 w1w1^T +h2 w2w2^T)/L has norm one and saturates K; scaled adversary disproves robustness at every t>t*. Independently checked exact A=diag(1,2),K=2 B eigenvalues 9/17,18/17 and 100 4x4 random perturbations. Repeated minimal eigenvalues covered via orthonormal basis.

## originality

PASS

October 2026 perturbed-system spectral-preconditioner research studies fixed-direction PCG/deflation estimates, while older sensitivity and singularity distances address different metrics/events. The all-Frobenius-E exact condition-cap radius and two-eigenmode optimizer were not derived in inspected sources. PASS with matrix perturbation optimization historical priority risk.

## value

PASS

Uniform all-directions finite-radius conditioning under reused full spectral whitening is a mathematically natural benchmark and exact robustness certificate, improves conservative Weyl norm-only estimates, and identifies the genuinely optimal two-mode commuting perturbation even among all symmetric noncommuting errors; not claimed as a low-rank practical algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
