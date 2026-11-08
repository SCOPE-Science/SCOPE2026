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

For m>=3 and positive prices P,Q,R and budget B, any connected feasible edge allocation makes the grounded Laplacian positive definite. The map of individual conductances to this grounded matrix is injective (off-diagonals and recovered ground-edge diagonals); strict concavity of logdet therefore proves unique unrestricted maximum, invariant under permuting pages. Schur complement gives tau=(x+y)^(m−1)[mxy+z(x+y)] with t=x+y>0, D=mxy+zt>0. Euler homogeneity fixes multiplier lambda=(m+1)/B, and the correct reduced cost is m(Px+Qy)+Rz=B. KKT inequalities F_x<=lambda*mP, F_y<=lambda*mQ, F_z<=lambda*R, equalities at positive weights, yield exactly four exclusive solutions: x=0 iff P>=Q+R, y=0 iff Q>=P+R, z=0 if the remaining price range satisfies R>=R_c with unique positive root Pr²−m(Q−P)r−Q=0; otherwise x,y,z>0 with s,t,z displayed in the frozen result. Threshold equality is assigned to the zero-edge regime. Independent KKT/determinant computations at fifteen parameter instances cover all four regimes and corroborate but cannot replace the global convexity and KKT proof. Check equal P=Q=S gives R_c=4S/(m+1), so hub vanishes at equal all-edge prices for m>=3.

## originality

PASS

Best-of-knowledge: compare the exact theorem and quantifiers with inspected primary results and relevant published summaries, rather than matching titles/numbers. Known ingredients are credited, and any plausible inaccessible or broader literature remains a qualified priority risk; no definitive independence or priority certification is claimed.

## value

PASS

The book graph provides a natural analytically tractable test for optimizing spanning-tree reliability/D-optimality under genuinely independent edge allocations. A complete price-space phase diagram distinguishing spoke loss, hub loss and full support, including the surprising equal-price missing-hub optimum, is a motivated structural classification useful in network design rather than a relabeling of the general logdet KKT condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
