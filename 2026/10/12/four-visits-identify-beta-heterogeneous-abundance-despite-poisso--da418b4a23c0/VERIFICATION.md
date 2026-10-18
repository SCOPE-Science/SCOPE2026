---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The exact compound-Poisson log PGF equals xi Σ(z_t-1)+mu(E_Q∏(1+Q(z_t-1))-1). Its distinct-visit derivatives are c1=xi+mu α/(α+β) and cr=mu(α)_r/(α+β)_r (r>=2); the entire count law is determined by these square-free coefficients. For T=4, c3/c2 and c4/c3 uniquely recover α+β, α, β, then mu and xi. For T<=3, continuity of the explicit one-parameter curve in S preserves all available cumulants and the full count law at every interior xi>0. Independently checked exact rational inversion on three profiles, common c1,c2,c3=(6,2,8/7) for two distinct sets, and fourth difference 1/147. With xi known zero, c2/c1 and c3/c2 give the analogous sharp three-visit inversion. The proof handles positive shape parameters and boundary xi=0 as stated.

## originality

PASS

Royle 2004 basic N-mixture has fixed per-visit detection and no separate unknown Poisson false positives; capture–recapture beta heterogeneity from Dorazio–Royle concerns identity-labeled detection histories. An independent Resultary two-visit theorem concerns the standard constant-p binomial mixture, not individual persistent beta heterogeneity plus unknown false detections. No inspected stronger theorem derives this exact T=4 versus T=3 threshold for the full joint law.

## value

PASS

Sharp structural identifiability with false-positive contamination is central to ecological count modeling: the result determines a minimal survey-design dimension and supplies a pair of genuinely observationally identical three-visit count laws and a complete admissible cross-cumulant region. These are useful independently of finite-sample estimation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
