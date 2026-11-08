---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS: The proof correctly uses the Crofton brightness factor det(A)sqrt(u^T A^-2 u), rather than Haar-direction sampling. Completing the line-intersection square gives L=2sqrt(1-|W|^2)/sqrt(u^TA^-2u), and the uniform (d-1)-ball radius gives exponent p=(d-1)/2. The perpendicular sphere marginal has density Gamma(d/2)/(pi^(m/2)Gamma((r+1)/2))(1-|z|^2)^((r-1)/2) and U_{r+1}^2=(1-|z|^2)Beta(1/2,r/2). The z=O(sqrt(epsilon)) scaling produces beta-ball power beta=p+m/2, the stated Gamma normalisation and E[(1-lambda T/2)_+^beta]; dominated convergence is uniform on bounded lambda sets and covers m=0 separately. Rescaling T by 2/lambda verifies the beta-function matching coefficient; no joint lambda→infinity limit is asserted. Independent direct quadrature d=4,r=2,3 gives convergence ratios to the exact profile approaching 1. A finite quadrature cannot establish asymptotics, which follow analytically.

## originality

PASS

PASS, best-of-knowledge: Heinrich 2014 Theorem 3.1 supplies general ellipsoid chord-power integrals, so all fixed-ellipsoid chord distributions are already encoded in prior work. That theorem was inspected including its formula (10) and subsequent ellipsoid inequalities; the precise moving-axis long-chord endpoint crossover and beta scaling law require additional singular two-parameter analysis and were not stated or directly implied by its evaluated identities. Kellerer covers planar/spheroidal lower dimension, Hug–Schneider pair-line integrals and van der Jagt et al hyperplane section volumes do not dominate this Crofton line-chord rare-event claim. An older stereological equivalent could exist.

## value

PASS

PASS: A natural geometric singularity occurs when one formerly shorter semiaxis coalesces with a repeated major axis: the endpoint tail exponent changes by one half and fixed-shape constants diverge. The theorem resolves this instability with a positive nonconstant beta interpolation, explicit scale and coefficient matching throughout r=1,...,d-1. This is a reusable structural result, not a sphere computation or numerically chosen ellipsoid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
