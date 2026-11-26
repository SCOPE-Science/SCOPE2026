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

The final RESULT.md preserves the true finding and fixes the original misleading exclusion of correlation signs: both variables have strictly positive variance (use the empty hypergraph and a positive-weight event for Z_s, and the empty and one-edge hypergraphs for I_n). I reconstructed the weighted deletion proof by conditioning on the joint internal and crossing-edge configuration of each marked S, which is independent of all outside edges. The marked event has no internal isolate because r>=2 and S is a connected component of size >=r. Ordered tuples count exactly the outside complement-edge exponent, including the deterministic edgeless complement. Dividing the covariance by its positive mean factor times n q^M_n gives a strictly increasing function of p with one zero. The average Delta_s/s is nonincreasing by Pascal's identity whereas log(n/(n-s))/s strictly increases. For fixed r,s the q^(-Delta_s) expansion has first correction cs/((r-2)!n), producing exactly the stated normalized limit; at s=n-1 Delta_s=M_n. The independent mathematical check suffices; the frozen exact finite enumerator is supplemental and was not executed.

## originality

PASS

The repair acknowledges exact prior coverage of the graph first-moment covariance and threshold hierarchy. The distinct scope is the full weighted isolate deletion law and the finite hierarchy for uniform hypergraphs of rank at least three. The nearest inspected precedents establish neither that combined result nor a stronger statement implying its nonlinear rank-dependent exponents and ordering. The conditioning mechanism is standard; originality is not claimed for the idea of outside-edge independence.

## value

PASS

The exact law makes arbitrary shape weighting irrelevant for the full biased distribution, not just a first moment, and the nonlinear finite-size threshold hierarchy for r>=3 relates small and nearly spanning components to two different familiar random-hypergraph scales without treating a covariance zero as a phase transition. That rank-dependent hierarchy is the useful quantitative addition beyond routine edge independence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
