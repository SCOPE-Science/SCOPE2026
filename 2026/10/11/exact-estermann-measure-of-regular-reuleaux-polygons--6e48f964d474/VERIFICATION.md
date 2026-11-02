---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Repaired final formal definition explicitly minimizes only over centrally symmetric CONVEX bodies, as the standard Estermann invariant requires. The original omitted convexity inside its displayed set quantifier and is literally false if arbitrary nonconvex symmetric supersets are admitted (e.g. R_n union -R_n has smaller area than the convex antipodal hull). Full corrected RESULT.md supplied with exact blob/hash guard. Independent proof review: alternating Steiner symmetrizations across distinct reflection axes preserve area, convexity, K-containment and centrally symmetric centers, whose projections converge to o; boundedness and Blaschke compactness yield a centered area minimizer. Symmetry plus width w gives support h(±u_j)=w/2 for axes perpendiculars, so R_n lies in n strips whose intersection is regular 2n-gon conv{±v_j}; reverse inclusion follows from vertices. Firey width-one formula gives area R_n=w²(pi/2-n/2 tan(pi/(2n))), hull area=nw²/2 tan(pi/(2n)), ratio and monotonicity and asymptotic. Independent bounded disk-intersection geometry checks n=3,5,7,9 corroborated areas to ~1.1e-6; numerics not universal proof. All odd n>=3 and w>0 only.

## originality

PASS

Qualified best-of-knowledge: the formula for outer-area Estermann symmetry of all regular Reuleaux odd-gons (n>=5) is not given by the materially inspected Firey area paper, Chakerian general extremal theorem, Guo–Jin different Minkowski measure, or the published straight-regular-polygon centering result. The n=3 case, area input and generic two-reflection centering are prior mathematics and are not claimed new. The exact Reuleaux antipodal hull identification and family-specific quotient remain independently useful. The identical indexed SCOPE finding is self-copy, not independent priority evidence.

## value

PASS

Regular Reuleaux polygons are canonical exact constant-width examples, and the classical Estermann outer-area measure is natural for this family. The finite/natural infinite-family classification gives an explicit optimal centrally symmetric containing convex polygon and exact unknown n>=5 area ratio, monotone convergence and two-term asymptotics. The particular value is useful as a benchmark contrasting the distinct inner Kovner–Besicovitch and Minkowski asymmetry measures. It is an elementary motivated exact special-family geometric fact, not a new general centering theorem, an irregular-Reuleaux extremal theorem, or merely a normalization change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
