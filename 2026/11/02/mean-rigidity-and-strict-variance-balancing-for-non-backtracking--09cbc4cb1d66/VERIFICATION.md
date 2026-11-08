---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Each non-backtracking petal excursion returns to the hub, and the petal label has same-state probability 1/(2k-1) and any distinct-state probability 2/(2k-1). Given r distinct petals seen, next new-petal probability p_r=2(k-r)/(2k-1) yields independent geometric waiting times for coupon completion J; exact cover time is weighted excursion length sum minus one final untraversed return edge. Exchangeability gives E C_i=E J/k, and a two-state marked-petal recurrence evaluates transverse occupation-count covariance eigenvalue b_k. Orthogonal covariance decomposition yields variance L²Var(J)/k²+b_k(Q-L²/k). Because b_k>0, integer unit smoothing strictly reduces variance until lengths differ by <=1. Independent first-principles directed-edge/visited-vertex rational Markov-chain moments agreed for six bouquets, including k=2,3,4.

## originality

PASS

Breen et al investigate non-backtracking Kemeny constant, a stationary mean hitting-time statistic that does not determine cover variance. Matsuo–Kawagishi–Ohsaki study expected non-backtracking cover times in random graph models, not exact fixed bouquet mean-and-variance or balanced-length inequality. Resultary non-backtracking bouquet query returned unrelated cover-time and petal items.

## value

PASS

Separating mean invariance from strict variance sensitivity is a motivated exact stochastic-graph phenomenon: fixed number of cycles and total length give identical expected cover time but quantitatively different risk. The sharp balancing rule is useful in designing finite bouquet networks and interprets memory effects of the non-backtracking walk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
