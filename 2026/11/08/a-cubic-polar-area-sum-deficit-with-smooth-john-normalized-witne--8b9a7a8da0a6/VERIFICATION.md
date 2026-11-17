---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The distributional curvature of h=1+t|sin(mθ)| is density 1−(m²−1)t|sin(mθ)| plus upward atoms 2mt at contact normals; nonnegative precisely on stated bound. Uniformly distributed 2m contacts fulfill John identity, and max support gap is t. The support-area and polar radial integral yield the two exact area formulas and D=π(m²−4)t²/2+16t³/3+O(t⁴). m=2 cancels quadratic. Smooth fδ=sqrt(sin² 2θ+δ²)−δ (δ=t⁴) has curvature h+h″≥1−4t>0 and same John contacts; Dirichlet Poincaré and H1 approximation make quadratic deficit O(t⁴), leaving D/d_H³→16/3. Independently expanded exact polar integral with SymPy for m=2,4,7; inspected supplied polygon/checker code. Neither these finite checks nor smooth approximants prove a global cubic lower bound.

## originality

PASS

Böröczky–Makai 2026 Theorem 1.1 proves the John/Löwner normalized area-sum upper bound, but their stability Theorem 1.3 and Example 1.4 address a different quantity, the area product. No inspected earlier source gives the smooth John-position cubic area-sum deficit witness or the precise four-contact frequency transition. Originality is best-of-knowledge subject to unindexed convex-geometric stability work.

## value

PASS

Sharp obstruction to a natural anticipated quadratic Hausdorff stability inequality for a newly strengthened Blaschke–Santaló area-sum inequality, with explicit smooth strictly convex examples. The transition at exactly four John contacts and cubic coefficient distinguishes an intrinsic local degeneration, not an arbitrary area calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
