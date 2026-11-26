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

With period-one Zak measure dx dθ/(2π), the integer modulation calculation yields the bounded Walnut form with overlaps only at shifts 0, ±1. The partition of unity of the hat gives A₀+2A₁=q, and the squared arithmetic progressions on a cell give q−A₀=L_q+2qx(1/q−x). Thus the symbol is q−D(1−cos θ), and its continuous essential range is [q−2 max D,q]=[L_q,q]. For an independent density check, set V=|2U−1| for U uniform on [0,1]; V is uniform and D=L_q+(1−V²)/(2q). Conditional on V=v the arcsine density has support [L_q+v²/q,q]. Integrating gives √q/[π√(q−λ)] times the integral of (q(λ−L_q)−v²)^(−1/2) from v=0 to min(1,√(q(λ−L_q))). It is π/2 below the breakpoint and the stated arcsine above it. This construction normalizes the density. The breakpoint C_q=L_q+1/q lies strictly inside the band for q≥2. The upper-side change from the smooth lower branch uses arcsin((1+qδ)^(−1/2))=π/2−arctan√(qδ), giving the sign, coefficient, and O(δ^(3/2)) remainder. Absolute continuity of the pushforward makes the inverse image of any Lebesgue-null set null, so every scalar spectral measure is absolutely continuous. The uniform V formula gives ED=q/3 and Var(D)=1/(45q²); E(1−cos θ)=1 and E(1−cos θ)²=3/2 then give both moments. D/q→1/3 uniformly and the limit (2+cos θ)/3 has the claimed arcsine law. The supporting script was read, not run.

## originality

PASS

The sharp bounds and exact multiplier are not distinct contributions: both are in the same-day canonical-dual record 85d806d9ebbd for identical parameters, and the sharp upper bound also appears in the published-lineage Buck et al. calculation. Moment and limit checks are short consequences of the symbol; no new frame-property result is supported. The frozen record's expressly identified main contribution is the exact normalized Zak pushforward law, in particular the two elementary density branches and their sharp interior cusp. The known multiplier specifies the input to that calculation, but neither it nor an inspected general frame theorem evaluates this pushforward in closed form or supplies its branch switch and coefficient. The closely related dual record's reference to spectral statistics elsewhere names no matching source or formula. Pass is for the original density finding, not priority on its supporting bounds, symbol, or general technique.

## value

PASS

For this standard redundant spline frame, spectral endpoints tell nothing about the fraction of fibers with a given gain. An exact normalized gain law resolves that question and exhibits a one-sided square-root cusp strictly inside the band rather than merely an edge singularity. That feature is visible for every integer q≥2, and neither endpoint nor the limiting arcsine law reveals it. The exact density is useful without a claim to a new Zak formalism, frame region, or dual-window construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
