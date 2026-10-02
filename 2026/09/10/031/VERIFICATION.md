---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-09-30.md",
      "INDEPENDENT_AUDIT_2026-09-30.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

An independent reconstruction from the committed 42-edge list and 42 signs reproduced signed traces Tr2=84, Tr4=420, Tr6=2436, Tr7=-168, Tr8=14964. Exact rational LDL on (26105/10000)^2 I-A_t^2 had all positive pivots, hence rho<2.6105. Rebuilding the 56x56 fibre lift and the committed integer Rayleigh vector reproduced numerator 2610502980388, denominator 1000001200328, and positive margin 10000*num-26104*den=998470517888, hence rho>=2.6104. The block identity A_s=[[0,A_t],[A_t,0]] gives equality of spectral radii. The girth argument for trace rigidity through length six is correct because every closed walk shorter than the girth reduces by backtracks and therefore uses each edge with even signed parity.

## originality

PASS

Best-of-knowledge searches found the general 2-lift/signing theory and other SCOPE signing constructions, but no prior source with this exact Coxeter balanced fibre-symmetric signing or the [2.6104,2.6105) certificate.

## value

PASS

The result is a concrete two-sided Ramanujan-scale signing datum on a classical distance-regular cubic graph with an additional exact balance/fibre constraint, together with a structural explanation that the first two even trace moments cannot detect signing quality. Such an explicit witness is a useful benchmark for the Bilu-Linial 2-lift problem and is not merely a renamed parameter or tiny arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
