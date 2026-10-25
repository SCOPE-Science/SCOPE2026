---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For p,q>=2, K_{p,q} has pq edges and affine tree-base dimension pq-1. The edge-transitive S_p×S_q action and convexity of feasible centers at any lambda reduce the minimum reflection factor to the unique uniform vector t=(p+q-1)/(pq). For inequality L(x)<=u, the exact test is lambda>=(L(c)-min_P L)/(u-L(c)). The independent standard spanning-tree H-description consists of nonnegative edges, x(E)=p+q-1, and induced-edge subset upper bounds. For S meeting the two graph parts in a,b>=1, its induced bipartite graph is connected and max x(E[S])=a+b-1. Deleting its ab edges leaves a connected graph when a<p,b<q, or isolates precisely b right vertices when a=p,b<q, or a left vertices when a<p,b=q; the exact minimum is correspondingly 0,b,a. Thus the three candidate maxima are q-1, p-1 and F(p-1,q-1)=(p-1)(q-1)(p+q-1)/D for D=p^2-2p+q^2-2q+1>0. The interior ratio is increasing in ab/(a+b-1) separately in a,b and maximized at (p-1,q-1), with the denominator positive because c is relatively interior. The nonnegative-edge factor (1-t)/t does not exceed the boundary maxima. Algebraically F(p-1,q-1)-(p-1)=p(p-1)(q-p+1)/D when p>=q, so only p=q contributes a strictly larger interior obstruction, with a tie when p=q+1. At p=q=r, the excess is r(r-1)/(2r^2-4r+1), tending to 1/2. All upper/lower support extremes are realized by trees. This is a complete infinite argument, not a finite-enumeration inference.

## originality

PASS

Best-of-knowledge after original targeted searches and substantial primary full-text inspections: the classical spanning-tree inequalities and general robust Minkowski-center LP are known, but no independent earlier source found evaluating the K_{p,q} two-parameter exact asymmetry or proving the balanced anomaly. The identical published Resultary entry is a copy of the audited record, not separate prior work. The nearby published SCOPE complete-graph, rank-two matroid base, and polymatroid independence-polytope results do not dominate this specific graphic-matroid base-polytope family. No mathematical novelty certification is asserted; unindexed equivalent optimization formulas are a genuine residual risk.

## value

PASS

Graphic-matroid base polytopes of K_{p,q} form a natural edge-transitive two-parameter family, and Minkowski asymmetry is a standard affine-invariant geometric quantity. Its exact family-level evaluation reveals a structural change of the active reflected-facet constraint: for p≠q the dominant obstruction is a boundary subgraph and s=max(p,q)-1, while at exact balance an interior induced-subgraph bound is stronger and gives a positive excess tending to 1/2. This sharp equality/inequality transition is not merely a substitution of parameters or a known table entry; it gives an independently useful exact invariant and a canonical center for a broadly used family. No theorem beyond the proved family or paper-size contribution is required to justify this structural result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
