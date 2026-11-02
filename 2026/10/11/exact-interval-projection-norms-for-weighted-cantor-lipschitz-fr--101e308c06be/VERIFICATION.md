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

The weighted prefix/block/tail decomposition p+h+e of d(x,y) is exact. Applied to (P_m-P_n)(delta_x-delta_y), finite 2-by-2 Kantorovich transport gives min(a+b,2p+h) for sources p_mx,p_ny and sinks p_nx,p_my. For p=0 the image ratio is <=1; otherwise p>=a_n and a,b<=B_{n,m}, yielding ratio <=2 min(1,B_{n,m}/a_n). A pair differing in one block coordinate gives ratio 1, and a min-prefix-coordinate pair with a common all-one block gives ratio 2 min(1,B_{n,m}/a_n). This works for m=infinity since weights are summable. Retractions P_n have norm 1, rank 2^n-1, commute, and strongly tend to I; the tail criterion follows exactly. Independent exact-rational all-molecule exhaustive checks on six finite weighted cube configurations verified 66 intervals and 18,648 ordered-as-unordered molecule pairs, with zero discrepancy; no extrapolation from finite tests was used.

## originality

PASS

Qualitative MAP is already known for this compact invariant-metric group by Doucha–Kaufmann. The general monotone FDD and group-action projection results do not give the norms of deterministic coordinate-truncation differences. Read closest published Resultary findings about Walsh spectral and Dirac-diagonal projection operators; they are mathematically different. Four implication/comparison checks with actual searches and primary-source readings identify no direct published coverage; best-of-knowledge priority remains subject to possible unindexed transportation literature.

## value

PASS

The exact norm profile of every consecutive block of an explicit monotone FDD is a canonical quantitative invariant of that fixed decomposition. It distinguishes individual-block contractivity (geometric r<=1/2) from all-tail bimonotonicity (r<=1/3), giving a complete weight-sequence criterion absent from qualitative MAP or generic ||P_m-P_n||<=2. This is a motivated exact classification, not a broad basis optimality claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
