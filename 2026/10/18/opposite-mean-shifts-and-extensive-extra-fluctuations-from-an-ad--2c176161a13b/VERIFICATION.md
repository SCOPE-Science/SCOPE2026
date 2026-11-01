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

For even cycle C_{2m} (m>=3), independent Exp(1) rim attempts and one Exp(lambda) hub attempt, the path first-arrival recurrence n a_n=n+2sum_{j<=n-2}a_j gives A(z)=(1-e^{-2z})/[2(1-z)^2], so mu_m=(1-e^{-2})m+O(1). Penrose-Sudbury Theorem 11 gives path variance e^{-4} per site; deleting one cycle edge perturbs only factorial-tail descending-priority clusters, yielding Var(K_m)/m ->2e^{-4}. For wheel, hub must be earliest, probability lambda/(2m+lambda), independent of the relative rim order. Its count is 1 on that event and K_m otherwise; exact mixture gives both claimed limits. For gear, the hub is accepted precisely when before the first baseline-accepted even vertex: then final count m+1, else K_m. The accepted-even avoidance H_m(s/m)->e^{-s} follows from no-even-clock probability and a 2m O(t^2) union bound on rejected early even clocks; disjoint triple events yield integrable exp(-cmt) tails, whence m P(hub accepted)->lambda. A descending-clock causal-radius truncation with factorial tails and a bounded 2R-dependence fourth-moment bound O(m^2R^2+mR^3), R=ceil(3log m), yields P(|K_m/m-r|>epsilon)=o(1/m). Thus K_m/m->r conditionally on hub acceptance, for first and second moments. Subtracting squares yields positive gear variance increment lambda e^{-4}m and wheel increment lambda (1-e^{-2})^2m/2, with the respective mean defects lambda e^{-2} and -lambda(1-e^{-2})/2. A separate exact-moment dynamic program checked 15 finite (m,lambda,graph) cases (m=3..7, lambda=1,2,3), and independently checked all 5,040 orders at m=3 for wheel and gear pathwise identities (10,080 cases). These finite tests are corroborative, not the infinite proof.

## originality

PASS

Best-of-knowledge PASS specifically for the pair of opposite order-one occupancy shifts and same-sign extensive variance increases caused by one high-degree hub on wheel versus alternating-spoke gear. Baseline one-dimensional RSA density/variance and general random-greedy MIS models are prior mathematics. Inspected primary complete sources and published exact-family results do not imply both leading defect coefficients for these fixed graphs. The 1989 Pippenger primary paper was not read in full (OA download 403, authorized Oxford vpn_disconnected); unindexed special hub calculations remain a genuine priority risk, not automatic originality failure.

## value

PASS

Wheel and alternating-spoke gear are natural contrasting ways to attach one adsorption hub to a one-dimensional rim. The sign of mean occupancy reverses, but both attachments amplify variance by order system size through a rare probability Theta(1/m) event with a Theta(m) count impact. The exact fixed-rate coefficients reveal a non-local fluctuation mechanism invisible to purely bounded-degree bulk limits; they are meaningful benchmarks for random greedy independent sets/irreversible blocking deposition, not a trivial single-vertex table or a mere restatement of known path variance. Restricted to these two families at fixed lambda, with no higher-order/finite-rate-uniform conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
