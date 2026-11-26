---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The projection of e2 onto the orthonormal trial basis gives deterministic squared sine error ε². The Haar null line gives the stated Gaussian kernel coordinates; eliminating the pencil eigenvalue produces the exact quadratic and the objective is increasing in the modulus of its root. The additional null event c q2−ε q0=0 makes the compressed mass matrix singular; it has probability zero at fixed ε and is absent for all sufficiently small ε almost surely in the common coupling. The small root differentiates at zero to q2/q1, and the independent exponential squared moduli give tail t⁻². Splitting at U=|q1|²=8ε|q0||c q2−ε q0|/c² gives uniform normalized moments at each exponent below two, hence uniform integrability at any smaller exponent. The good-event analytic-factor error integrates using ∫_t^∞u⁻²e⁻ᵘdu≤1/t; the bad-event product-of-roots bound contributes O(ε²). In the remaining exponential integral the coefficient of log(1/ε) is E|c q2−ε q0|²=1, and the weighted logarithms are bounded by Gaussian moments and Cauchy–Schwarz. The fourth moment is O(ε³) by the same split and E|q0|⁻¹<∞, so replacing squared root modulus by squared sine does not change the coefficient. The supplied checker was inspected, not executed; it is finite numerical corroboration, not the argument for the moments.

## originality

PASS

The example, randomized method, and first-order limiting ratio mechanism are not claimed as new. The distinct supported contribution is the finite-angle best-of-both-roots moment analysis, especially the sharp critical logarithm with a bounded O(ε²) remainder, and subcritical convergence of actual moments.

## value

PASS

The canonical example shows why a high-probability O(ε) Ritz-vector guarantee cannot be read as O(ε²) mean-square error, even with an oracle allowed both eigenvectors. The critical coefficient and convergent subcritical moments quantify this gap for an exact, natural benchmark without making claims for other sketches, oversampling, or dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
