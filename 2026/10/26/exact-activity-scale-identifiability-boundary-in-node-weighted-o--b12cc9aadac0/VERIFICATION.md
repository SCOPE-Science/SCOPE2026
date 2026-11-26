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

The first-class event has probability theta_t=tW_A/(tW_A+W_B). Conditional first and neighbor probabilities are individually unchanged by the class scale, so the two conditional edge laws are Q_A,Q_B and the difference of two mixtures is (theta_t-theta_s)(Q_A-Q_B). This yields the exact TV factor. Their equality reduces edgewise to S_i/W_B=S_j/W_A; connectivity propagates one common eta in (0,1], and conversely that condition suffices. A complete bipartite graph gives the product law. For a nonedge ib pick a neighbor j of i. The edge polynomial W_B S_j-W_A S_i has coefficient S_j>0 as a polynomial in the missing neighbor's weight w_b; therefore the common zero locus of all edge polynomials is proper and null. It need not be empty (for example equal weights on a six-cycle). With known within-class proportions one edge with unequal conditional probabilities gives theta and thus the active class-total ratio theta/(1-theta), not arbitrary unknown individual weights. On a complete bipartite graph the conditional product law is constant given the past even under adaptive rescaling, and the same sequence of unordered pairs with the same initial profile gives the same symmetric edge-only trajectory. First-selection labels or a physical-time event rate are not covered. The frozen checker uses bounded rational graph/profile examples and does not verify the unbounded or trajectory results. python3 -B /workspace/reproduce_finite.py 1 directly summed the ordered-pair probabilities for 458 connected graph/profile cases at scales 1, 2, and 3, including 12 invariant cases; all equality and TV comparisons agreed. No frozen script was executed.

## originality

PASS

The sampling protocol and the three-vertex path cancellation are already documented, and conditioning and detailed balance are standard. The supported distinct claim is the exact boundary for unordered-edge class-scale identifiability on every finite connected bipartite graph, including its positive-weight exceptional locus and the all-profile characterization, not those ingredients or the isolated path example. The strongest inspected comparisons do not give that classification or the accompanying sensitivity statement for this observation model.

## value

PASS

In a published heterogeneous-activity model, observing pairs without the initiating vertex raises a meaningful inverse problem even when within-class proportions are known. The classification distinguishes parameters that can never be recovered from exceptions caused by the particular weights, and quantifies the change in the observable distribution when recovery is possible. That structural boundary is useful beyond the elementary mixing identity; it makes no claim about inferring unknown proportions or consensus from opinions alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
