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

PASS: The Prüfer code has length n−2, and conditioning a designated vertex on degree d fixes exactly d−1 occurrences of its letter; remaining n−d−1 code symbols are iid uniform on the other n−1 vertices. Thus L|D=d=E_(n−1)(n−d−1)+1_{d=1}; the Stirling occupancy formula follows. Coupling successive box draws gives strict Q2<st...<st Q(n−1) and Q1>st Q2; star Q(n−1)>st Q1. For 3≤d≤n−2, Q1 has min2/max n−1, while Qd has min d≥3/max n−2, so tails cross. Symmetry and deterministic total degree give Cov(D,L)=0; the exact Δ_n expectation formula changes sign between n8 and n9, with exponential bound thereafter. Independent integer occupancy dynamics checked masses/order/means for all n3..30, complementing source Prüfer-tree enumeration n3..8. No inference beyond its supplied analytic proof.

## originality

PASS

PASS (qualified): Prüfer degree-as-multiplicity and the empty-box law are classical, and the latter is not claimed as an original probability distribution. Addario-Berry et al develop alternative tree encodings and partial orders; Berzunza Ojeda–Holmgren–Janson prove fringe-count asymptotics conditioned on degree statistics. Neither inspected relevant result gives this exact marked-degree first-order leaf-count comparability diagram and mean crossing. The diagram is elementary from coding; older joint-degree generating functions may imply the parts, a risk expressly retained.

## value

PASS

PASS: The full first-order stochastic comparability diagram of leaves conditioned on one fixed degree is a natural dependence question in uniform labeled trees. It explicitly exhibits nonindependence despite zero covariance and a crossing of conditional means; this all-n classification is an identifiable structural probability fact beyond the standard Prüfer degree law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
