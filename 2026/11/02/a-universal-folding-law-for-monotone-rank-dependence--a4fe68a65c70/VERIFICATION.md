---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For any bivariate copula and integer k>=1, independent branch J gives F_k C=(jv+C(ku-j,v))/k. The a.e. conditional derivative repeats, preserving population xi; centered section F_v(t)=C(t,v)-tv is Lipschitz with zero endpoints. The least concave majorant of k repetitions has only first-rise and last-fall portions of the original envelope, joined by a maximal plateau; its derivative L2 energy scales by k. Combined with amplitude 1/k this proves xi^up(F_k C)=xi^up(C)/k; reflecting predictor gives xi^down likewise. Integration gives rho_S/k, and Frechet deviations |C-Pi|<=1/4 give uniform closeness <=1/(4k) with equality for comonotone. The proof handles singular copulas and k=1. Independent exact rational PAVA comparison of 6,723 centered profiles length 2..6 for fold factors 2,3,5 corroborated e(F_k)=e/k but finite sampling is not continuum proof.

## originality

PASS

Siburg October 2026 establishes the LCM projection framework and its special deterministic sawtooth Example 5.4 with xi^up=1/k; these are credited. The arbitrary-copula fold law, both monotone directional coefficients, Spearman scaling, and sharp sup distance require a repeated-envelope lemma absent from the reviewed example. Ansari’s copula upper-product transformation is different from randomized equal-width branch-lifting.

## value

PASS

An exact universal structural transformation retaining full directed predictive dependence xi while quantitatively annihilating increasing/decreasing projected components and concordance is mathematically motivated and counterintuitive; the all-copula statement is stronger than a known sawtooth example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
