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

Exponential edge-weight exploration in a complete (m+1)-vertex petal is an SI pure-birth chain with rates r_k=k(m+1-k), independent waiting times Exp(r_k), and random hub infection rank J uniform 1..m independent of waiting times. Distinct petals share only the already infected hub, giving independent hub-source completion Y_m, M_n=max_i Y_m, and exact leaf-source H+max(R,M_(n-1)). For fixed m>=2 rates at k=1,m both equal m; convolution of these two exponentials with faster internal stages gives tail m(m-1)^2 t exp(-mt)+O_m(exp(-mt)) using telescope E exp(mZ)=(m-1)^2. n-times tail at b=(log n+loglog n+2log(m-1))/m gives Gumbel, with centered maximum UI from exponential bounds; independent H leads to convolution limit and E H=H_m/m. m=1 has single slow pole, no loglog and penalty 1-1/n. Independently checked telescope and harmonic means for m=2,3,4,8,12; the source program separately contains exact full-graph CTMC and Dijkstra simulations. Finite checks do not prove the asymptotics.

## originality

PASS

Known complete-graph epidemic pure-birth rates and Gumbel maxima are standard. The exact coupling of hub/petal sources, repeated-minimal-eigenvalue loglog correction, explicit centering and harmonic additional source delay for deterministic clique bouquets are additional joint statements. Existing bounded-moment configuration-model flooding papers do not apply to degree nm hub. No exact deterministic clique bouquet result detected in Resultary or targeted searches.

## value

PASS

Flooding completion time is a natural FPP statistic on windmill/community bouquets. Identifies the double-pole logarithmic correction absent from stars and an explicit source-location penalty with nontrivial convolution law; such sharp source-sensitive constants matter for network spread beyond leading log growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
