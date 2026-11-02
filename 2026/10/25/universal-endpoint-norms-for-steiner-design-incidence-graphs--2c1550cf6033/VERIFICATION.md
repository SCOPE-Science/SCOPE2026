---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Let M be point/block incidence, with r=(v−1)/(k−1), b=vr/k. Point pair uniqueness gives MMᵀ=(r−1)I+J. The Laplacian Schur complement for a dipole from point p0 to incident block B0 is (vI−J)/k. The gauge x=(k/v)e_p0−(1/v)1_B0 and y=(Mᵀx−e_B0)/k satisfy both Kirchhoff equations. The six distinct edge-current types follow from the fact that distinct blocks intersect in at most one point; their count gives total |current| R+5(k−1)(v−k)/(vk)=5−4/k−4(k−1)/v, with diagonal R=1/k+(k−1)/v∈(0,1). Thus the complementary P=I−Q absolute column sum is 1+||Q_col||_1−2R=6−6/k−6(k−1)/v. Every incidence is arbitrary, and Q/P symmetric, giving both endpoint norms. k=2 boundary and strict dominance sign (k−2)v>2k(k−1) are correct. Independent standard-library rational checking verified all 167 individual source-incidence current and complement column sums over five design realizations, including Fano, AG(2,3) and a cyclic STS(13); the quantifiers are proved analytically, not extrapolated from finite cases.

## originality

PASS

Comparison of mathematical implications supports a best-of-knowledge new pair of parameter-only absolute-current endpoint norms for the unweighted point–block incidence graphs of ALL existing Steiner 2-designs. Classical incidence identities and a general graph Hodge projection formula are prior art, but neither automatically determines the required edge-current signs and absolute column sums. The closest published design-incidence record studies neighborhood-complex homotopy, not operator norms; the primary canonical-projection paper computes the Hamming cube and other graph families. An unindexed older transfer-current theorem remains a priority risk.

## value

PASS

Steiner 2-design incidence graphs form a natural infinite family including nonsymmetric systems; exact endpoint norms of canonical electrical cut/cycle projectors are directly relevant to graph transportation and Banach projection geometry. The universal dependence only on (v,k), not on incidence symmetries, and the sharp Q/P dominance change at (k−2)v=2k(k−1) provide motivated exact invariants. This is not a textbook substitution or known-table value; no minimality among all projections is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
