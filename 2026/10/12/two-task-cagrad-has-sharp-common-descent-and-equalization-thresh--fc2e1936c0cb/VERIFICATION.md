---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For gradients g1=g0+δ,g2=g0−δ, the ball max-min objective equals <g0,d>−|<δ,d>|. Since a>b, <δ,g0>=(a²−b²)/4>0 and the weaker g2 linear branch supports the ball until its optimizer reaches <δ,d>=0. Evaluating the support vector gives d=g0+R g2/b and the exact c_cd, c_bal radii. At the balanced branch the unique best point of the ball-hyperplane intersection lies in direction of h=proj_{δ^⊥}g0, yielding the stated square-root formula. Squaring positive ratios and simplifying gives c_bal<1 iff ρ<(3q²−1)/(2q); when q≤1/3 this is outside the allowed non-antiparallel interval. Equal norms force δ⊥g0, so d=(1+c)g0. Independent 120 randomly chosen harmful geometric configurations, with seven radii each, matched a dense 3001-point scalar-dual envelope to 1e−5 relative; threshold signs and exact inequalities verified algebraically. No convergence of nonlinear trajectories claimed.

## originality

PASS

The foundational CAGrad theorem already supplies the general implicit simplex-dual optimizer, which is fully credited. The submitted claim isolates a nontrivial exact two-task active-to-balanced branch transition, common-descent zero crossing, and a sharp weaker-gradient norm ratio obstruction inside c<1. The later primary papers use different objectives or clipped/weighted variants. No read source explicitly supplies these radius boundaries and their safe-range ordering.

## value

PASS

Separates two operationally distinct mathematical events: restoration of simultaneous first-order descent and exact equal task improvement. The sharp q≤1/3 safe-radius obstruction provides a natural regime in which CAGrad can improve both objectives without equalizing them. A useful explicit geometric classification of an established optimizer even though not a new algorithm or global theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
