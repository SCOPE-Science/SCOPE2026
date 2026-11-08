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

For common-edge-priority greedy matching on cycle C_n and its wheel W_{n+1}, reconstructed the exact one-vertex deletion coupling invariant: unmatched vertex sets remain nested with singleton symmetric difference after every processed edge, implying a deterministic matching-size difference in {0,1}. The path recurrence g_m=1+2/(m-1) sum_{j<=m-2}g_j yields G(z)=z(1-e^-2z)/(2(1-z)^2) and g_m=ρm-e^-2+o(1), ρ=(1-e^-2)/2. Before the accepted hub spoke, each step favors a spoke with conditional probability >=1/2, giving geometric rim-dimer tail; with high probability finitely many early occupied rim blocks separate by distances growing in n. Conditional fresh eligible-edge priorities decompose remaining rim into long paths, cancelling the constant deficits and proving EW=ρ(n+1)+o(1). The Bernoulli total variation limit then follows from {0,1}-valued difference and converging expectation. Independently solved exact rational state recursions for 3<=n<=12 on both cycle and wheel and checked 0<=EW-EC<=1 and convergence trends; not a proof of arbitrary n.

## originality

PASS

Qualified best-of-knowledge originality: compared the exact statement and its logical implications with the cited same-object published results and accessible full texts; prior covered portions are acknowledged, and inaccessible high-relevance papers are recorded explicitly rather than presumed not covering. See four structured checks and source inspections.

## value

PASS

The high-degree hub is a natural finite graph perturbation of one-dimensional irreversible dimer deposition. Showing its effect is deterministically only one edge yet probabilistically survives with a nonzero exactly identifiable Bernoulli limit is a mathematically motivated and potentially useful coupling stability law; it is not merely the already known density formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
