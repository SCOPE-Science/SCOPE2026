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

A simple random walk started at an A vertex of K_{a,b} visits sides alternately; conditional successive vertex labels within each side are independent uniform coupon streams, independent between sides. If S_A is post-start A visits to collect the remaining types and S_B B visits to collect all B, completion times are 2S_A and 2S_B-1; B is last iff S_B>S_A, and in distribution S_A=C_a-1, S_B=C_b, hence P(C_b>=C_a). Coupon inclusion-exclusion and independent geometric waits yield the source finite rational formula. When a=b=m, exchangeability gives 1/2(1+sum_t p_m(t)^2). For k≈m log m+mx, local coupon finishing identity m p_m(k+1)=P(U_{m,k}=1) converges to Gumbel density g(x)=e^-x exp(-e^-x); tightness and uniform local convergence on compact sets show m sum p_m(t)^2→integral g²=1/4 and correction 1/(8m). Independent coupon Gumbel limits under (b-a)log n/n→delta give the logistic difference of two independent Gumbels; continuity removes weak inequality boundary issues. Independent exact rational occupancy-chain computation verified several (a,b) values including (3,2)=1/5 and balanced (4,4)=0.54945054945; unbounded asymptotics require the analytic argument.

## originality

PASS

The graph-wide last-new-vertex uniformity characterizations (Lovász–Winkler 1993; Buchanan–Horn–Rombach 2022) and the coupon-collector Gumbel limit are established. The inspected four-page primary BHR preprint did not state this complete side-sensitive K_{a,b} law or sharp lattice tie and logistic scale. The original Lovász–Winkler 1993 full paper remained inaccessible despite OA attempts and authorized Oxford request (VPN disconnected); this is a genuine priority risk rather than evidence of noncoverage. Logistic differences are classical, novelty is the exact graph-side event and finite-size correction.

## value

PASS

Last-discovered vertex is a canonical cover-tour statistic and complete bipartite graphs give a natural tractable asymmetric family. A precise non-1/2 balanced bias, exact all-size rational distribution and n/log n transition answer graph-specific quantitative questions beyond broad uniformity characterizations and generic Gumbel convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
