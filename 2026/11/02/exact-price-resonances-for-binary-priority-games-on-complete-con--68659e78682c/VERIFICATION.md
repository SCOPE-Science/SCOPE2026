---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

From the stated payoff u_i=-r_i-c s_i, raising one's bid overtakes exactly earlier-index zero bidders and later-index one bidders, giving Δ_i=A_i-c. The adjacent identity A_(i+1)-A_i=1-s_i-s_(i+1) is exact. Adjacent bid switches force A=c, hence integer prices, and any repeat after the switch would violate a Nash inequality; the remaining suffix alternates. Solving its transition index produces two feasible prefix words at each r=1,...,n-1; constant profiles show all zeros is the sole equilibrium for c>n-1 and all ones is never an equilibrium when c>0. Both the n=2 and c=n-1 boundaries are included without duplicate counting. Independently reconstructed direct utilities and exhaustive best responses across 112 (n,c) configurations, n=2..9, corroborated all equilibria; finite enumeration does not prove the universal classification.

## originality

PASS

The all-graph c in (0,1) nonexistence theorem and the all-zero price threshold are genuinely prior. The additional all-positive-price resonance count and explicit alternating strategy profiles for complete conflict with binary bids were not established in the inspected primary comparison. Priority queue/ranking games with different fee or state semantics do not automatically imply the result. Best-of-knowledge distinctness remains conditional on specialist literature.

## value

PASS

The exact complete-conflict family is the first natural robustness test for the priced-priority equilibrium model: it shows all low generic noninteger prices have no pure Nash equilibrium, while each integer price up to n−1 has exactly two and sufficiently high price has one. This all-size sharp classification is a motivated structural equilibrium fact, not a sampled numerical anomaly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
