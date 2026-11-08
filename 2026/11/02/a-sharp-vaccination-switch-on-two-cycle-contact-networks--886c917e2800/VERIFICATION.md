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

Deferred-decision independent-bond percolation represents each eventual infected component exactly, so expected infected from a uniform seed equals 1+S_v/r with S_v=sum over unordered connected-pair probabilities. For an r-cycle C_r=rΣ_(1≤j<r)q^j−binom(r,2)q^r, a residual path P_(r−1)=Σ_(1≤j≤r−2)(r−1−j)q^j, and one portal-root connectivity R_r=1+2Σ_(1≤j<r)q^j−(r−1)q^r. Hence S_h=2C_r and S_a=P_(r−1)+C_r+qR_r, giving D_r(q)=−q−Σ_(2≤j<r)(j−1)q^j+(binom(r,2)+2)q^r−(r−1)q^(r+1). Deleting a nonportal cycle vertex yields a residual graph isomorphic to deleting a portal plus an extra bridge edge, strictly increasing some pair connection for every q>0. D_r/q has sign changes −,+,− and hence at most two positive roots; D_r(0+) negative, D_r(1)=1, and D_r(∞)<0 show exactly one root in (0,1). D_r′(1)=r(r²−3r+8)/6 and D_r″=O(r⁴) imply D_r(1−c/r³)=1−c/6+O_c(1/r), proving the sharp scaling. Direct independent exhaustive bond-mask counts for r=3,4,5 and q∈{1/3,1/2,3/4,1} corroborated all candidate scores and strict inequalities (CASE4_OK). No heterogeneous transmission/other seeding result claimed.

## originality

PASS

The standard Reed–Frost and independent-bond percolation coupling is prior (Becchetti et al. and Kenah–Robins). Li–Zhao–Zhang (2022) study vaccination and site-bond percolation in complex networks; only their full abstract/preview was accessible, so possible finite deterministic network optimization in the unread portions remains a documented risk. Chatterjee–Zehmakan uses a different degree-normalized epidemic law. None of the material actually read established the precise q_r switch, its uniqueness, or cubic approach. This is a best-of-knowledge priority judgment, not abstract-based full-paper noncoverage.

## value

PASS

Network vertex vaccination optimization is a motivated graph-percolation statistic; the two-cycle-with-intermediary family makes a natural bridge-versus-portal choice where optimal strategy flips from degree-three portals to degree-two intermediary near q=1 with sharp r^-3 scaling. Exact all-r classification and a unique crossover are substantive rather than a tiny unmotivated graph computation. It does not claim empirical public-health strategy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
