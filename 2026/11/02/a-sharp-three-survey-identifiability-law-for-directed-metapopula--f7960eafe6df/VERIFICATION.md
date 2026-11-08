---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For p in (0,h), the per-capita colonization term c(h-p)/[phi(1-h)+h+(gamma-1)p] has derivative -c[phi(1-h)+gamma h]/W(p)^2<0, giving a unique positive root precisely under ch>e[h+phi(1-h)]. Rearranged equilibrium balance U=(h-p)/e = (phi/c) + ((1-phi)/c)h + ((gamma-1)/c)p makes the design matrix rows (1,h,p), with a one-to-one map back to strictly positive c,phi,gamma. Full rank implies uniqueness; a nonzero kernel perturbation remains in the open positive parameter domain and maintains observed viable equilibria. The determinant of the three-survey L protocol is (h2-h1)(p3-p1) and strict negative dp*/de excludes zero. Exact rational inversion and counterexample checked; finite grids are corroboration only.

## originality

PASS

The original normalized directed-dispersal model and positive-equilibrium equation are from Purves–Dushoff (2005); neither these formulas nor ordinary linear identifiability are claimed independently as new. The additional precise all-positive-survey iff rank law, universal feasible three-point L protocol and two one-axis no-go theorems were not located as statements or consequences in the inspected main article. This best-of-knowledge comparison retains the older supplementary appendix and more general structural-identifiability priority risk.

## value

PASS

A minimal experimental-design theorem for recovering all three physically meaningful coefficients from exact positive equilibria fills an identifiable model-specific gap. It proves universal feasibility of an economical design and a sharp impossibility for surveys varying only one environmental control; these distinctions matter to mechanistic occupancy inference before statistical noise is considered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
