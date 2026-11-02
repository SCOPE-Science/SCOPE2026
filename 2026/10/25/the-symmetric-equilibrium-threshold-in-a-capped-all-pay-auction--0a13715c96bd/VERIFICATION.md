---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Bids below reserve except zero are dominated; no positive atom below the cap because an infinitesimal overbid beats ties. Continuous support indifference yields F(b)=(b/V)^{1/(N-1)} with payoff zero. Uniform cap tie probability equals S_N(q)/N, fixing q uniquely for 1<V<N and continuous endpoint Vq^{N-1}. If endpoint≤r the distribution is only atoms at zero and cap; otherwise it has the positive continuous interval [r,endpoint]. For r<V≤1 support ends at V, and V≥N gives all bids at cap. Strictly monotone S_N(q)/q^{N-1} gives unique threshold and checks boundaries including V=Vc; Riemann sums with q_c=exp(-a_N/N) give limit r+a_r. Independent numerics for 24 (N,r) pairs, including N=2 Vc=2-r, corroborate but are not a proof.

## originality

PASS

Best-of-knowledge originality after actual source and implication comparisons. Classical all-pay unbounded-support equilibrium cannot recover cap tie-binomial atom and the reserve-induced zero-versus-continuous threshold; Muratov's small-N cases do not logically determine every N. Muratov 2021 full text explicitly classifies N=2 and N=3, not arbitrary N; Pastine–Pastine 2023 general constraints do not encompass the binding reserve/minimum eligibility model with identical symmetric caps under their stated genericity conditions.

## value

PASS

Reserve eligibility and a bid cap give a natural mixed-strategy all-pay contest. The exact transition from continuous bidding to two-atom play for arbitrary finite populations and its positive finite large-N limit are structural equilibrium facts useful beyond a small numerical example, without claiming asymmetric equilibrium classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
