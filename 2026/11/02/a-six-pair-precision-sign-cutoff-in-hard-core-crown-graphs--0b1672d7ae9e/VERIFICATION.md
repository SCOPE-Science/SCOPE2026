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

The independent-set support consists of all A-only subsets, all B-only subsets and n extra matched pairs; this gives Z=2(1+lambda)^n-1+n lambda^2. Empty and singleton configurations imply covariance positive definiteness. Symmetric/antisymmetric block decomposition into aI+bJ reduces the matched inverse-covariance sign to E_n with strictly positive denominator. Independently recomputed symbolic expansions confirm E2=0, E3=-2 lambda^5(1+3lambda), E4=2lambda^5 P4, E5=2lambda^6 P5, E6=2lambda^5 P6 with every listed coefficient correct. P4/P5 each have one positive root by Descartes and IVT; all P6 coefficients positive. Marginal matched covariance strictly negative for n>=3 by Bernoulli inequality, despite nonadjacent conditional independence. No claim n>=7. The package standard-library finite exhaustive tests were inspected but not used to infer all fugacities.

## originality

PASS

Qualified best-of-knowledge claim concerns the full inverse ordinary covariance sign diagram, not the crown independence polynomial nor Markov conditional independence. Existing inference/precision literature applies to other probability laws; no examined primary result entails the n=4/5 critical roots or all-fugacity n=6 threshold.

## value

PASS

Crown graphs are canonical matching-deleted complete bipartite graphs; their hard-core occupation process supplies a natural example where conditional independence, marginal covariance and full-order linear partial correlation are different notions. The first always-positive inverse-covariance order and two sign transitions form a motivated exact finite classification, not an arbitrary graph invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
