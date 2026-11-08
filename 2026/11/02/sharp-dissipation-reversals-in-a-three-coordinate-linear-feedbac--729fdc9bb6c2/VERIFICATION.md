---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For h>0,k>=0 the cubic Routh–Hurwitz coefficients and determinant D=2h²+h+2k²+8k+8 are strictly positive, giving unique stationary covariance solving M S+S M^T=-2I. With Q=M S+I antisymmetric the conventional stationary overdamped EPR is tr(S^{-1}Q^TQ); exact symbolic covariance elimination yields the stated rational function. Independent symbolic differentiation verified derivative 4(h²-h+k+2)(2(h-1)k+2h-5)/D², hence damping monotonic trichotomy h<=1, 1<h<5/2, h>=5/2 and k* formula. Baseline subtraction factors with F(h)=2h³-4h²+8h-9, unique positive h_c, and k_eq. Independent stationary covariance solves at four rational sample values plus exact symbolic factor checks; the two-copy embedding is orthogonal Laplacian mode decomposition. The proof is an exact rational identity plus signs, not numerical extrapolation.

## originality

PASS

Best-of-knowledge after actual Resultary search, direct primary theorem comparison and mathematical equivalence tests. None of the inspected statements logically dominates the complete final claim; sources and access risks below qualify historical-priority uncertainty.

## value

PASS

The effect of increasing one damping strength on irreversible dissipation is a motivated nonequilibrium-design question. This explicit minimal three-coordinate feedback system shows sharp decrease, optimum and increase regimes, with a second exact baseline-reversal boundary, and supplies a two-copy physical embedding. Unlike a vague numerical counterexample the global phase diagram is exhaustive for a natural controlled linear family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
