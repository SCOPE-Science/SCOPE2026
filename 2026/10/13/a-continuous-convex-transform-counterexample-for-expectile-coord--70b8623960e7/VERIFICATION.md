---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The uniform background gives f_X≥η/2 on (0,2); the square-map density of Y is f_X(√y)/(2√y) almost everywhere on (0,4) and is integrable even at zero by substitution. The two cdfs meet the strict interval-support condition, and Q_Y(F_X(x))=x² exactly. At levels (1/6,1/4,1/3), solving the discrete balance equations for J and J² gives coordinates (3/7,3/5,3/4) and (5/7,1,6/5), with successive slopes 5/3 and 4/3. If u_i and v_i are the continuous expectile coordinates, put D=(v₂−v₁)(u₃−u₂)−(v₃−v₂)(u₂−u₁). In the published Eq. (8), the left side minus right side is 2D/[(u₃−u₁)(v₃−v₁)], so D>0 violates it, as well as convexity. The expectile score is strongly decreasing in its threshold with constant min(α,1−α), and Lipschitz in the observation with constant max(α,1−α), hence the root shifts by at most five times the coupling L¹ distance at the three chosen levels. Here those distances are at most 3η and 12η, the latter using the 4-Lipschitz square map. Adjacent abscissa gaps remain positive; the pairwise ordinate and abscissa errors are at most 120η and 30η. The product error bound (372/7)η+7200η² leaves D≥74534937/8750000000>0 at the specified η. The constants and strict inequality were independently reproduced with exact arithmetic; replay: python3 /workspace/branches/3882fb2e-b9e5-407b-a2d5-8087ac90d2b0/record3_exact_check.py. The discrete calculation alone is not the continuous theorem. The implication is answered negatively; it was not a theorem asserted by Eberl–Klar.

## originality

PASS

The primary source asks about precisely this comparison and does not assert the implication. Its symmetric-level theorem is a different statement. The closest catalogue examples also concern continuous laws and expectile orders, but the strongest matching constructions do not provide a counterexample under the ordinary convex transformation hypothesis here. The supported distinct content is the explicit continuous all-triples counterexample preserving that exact premise, not the coordinate formulation or smoothing as generic techniques.

## value

PASS

The example resolves a specific order-implication question raised in the primary paper, without contradicting its positive symmetric-level theorem. It gives a quantitative witness with explicit smoothing, an everywhere positive density on the interior of the support, and an exact convex transformation. Thus it identifies a genuine boundary of the known preservation result rather than exploiting atoms or a change of normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
