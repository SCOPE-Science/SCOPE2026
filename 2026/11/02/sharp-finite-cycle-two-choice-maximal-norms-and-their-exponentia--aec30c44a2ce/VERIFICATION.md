---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Read full selector-pattern proof and ground-state/Jacobi argument. Squared max equals maximum Gram Rayleigh quotient over 2^N selectors. Any unaveraged row cuts the positive cyclic tridiagonal Gram into J_L blocks; Perron top eigenvalue strictly increases with block length, proving unique one-hole active pattern. Perron irreducibility gives positive extremizers, rank-one positive perturbation of Q_N with ||Q_N||<1 proves precisely one eigenvalue >1. Ground-state identity for h_j=r^j yields strict 1<λ_N<λ∞, and ghost-boundary determinant relation gives the explicit limit K_b r^{2N}. Fresh enumeration of all selectors for N≤9 at weights .2,.5 and N≤6 at weight .8, plus high-precision λ_N checks at N=8,12,16, independently match. The N→∞ coefficient follows analytically from the secular equation, not finite testing.

## originality

PASS

A known infinite-lattice two-choice limit λ∞ is prior context; finite cyclic one-hole selector rigidity, exact degree-N Jacobi eigenvalue and the explicit exponential finite-size deficit do not follow from it without additional finite spectral work. Madrid studies continuous centered all-radii maximal operators; Zhang–Liu–Zhang finite directed graph balls and star families rather than weighted two-choice cycle. Primary publisher full text unavailable, so equivalent older exact finite-cycle computations remain possible.

## value

PASS

For a canonical nearest-neighbor max/averaging operator on a finite cycle, the complete norm, all extremizing selector patterns and the sharp finite-size spectral deficit are natural operator-theoretic invariants. The exponential coefficient quantifies localization and finite-cycle correction invisible in its known infinite-lattice limit; the proof gives structural eigenvector geometry, not an arbitrary small-N computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
