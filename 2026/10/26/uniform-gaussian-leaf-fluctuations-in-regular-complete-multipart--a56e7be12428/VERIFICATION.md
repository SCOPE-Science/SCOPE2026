---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The known Eğecioğlu–Remmel multipartite multivariate degree enumerator identifies degree−1 counts with n−2 independent uniform assignments, with r−2 over all n sites and k−1 for each part over n−k permitted outside vertices. Absence of any occupation gives p=(1−1/n)^{r−2}(1−1/(n−k))^{(r−1)(k−1)}, same-part two-site s and different-part two-site t exactly as RESULT.md, hence E[L]=np and Var(L)=np(1−p)+n(k−1)(s−p²)+n(n−k)(t−p²). All allowed draw pools have ≥n/2 sites, giving a uniform log Taylor error and σ²=e^(−1)−2e^(−2)>0 for Var(L)/n; E[L]=n/e+O(1) uniformly. For any fixed j distinct vertices, mixed Möbius differences of log joint empty events have size O_j(n^{1−|B|}); connected-hypergraph cancellation bounds joint cumulants O_j(n^{1−j}). Repeated labels contribute O_j(n^{1−d}) for d distinct underlying sites. Summing j-tuples yields κ_j(L)=O_j(n), hence normalized higher cumulants vanish and method of moments gives Gaussian convergence for arbitrary equal-part factorizations. Independently enumerated all labeled spanning trees of seven small (n,k) cases and matched exact rational moments; these finite tests do not establish the CLT.

## originality

PASS

The 1994 Eğecioğlu–Remmel work already provides the full degree generating polynomial and marginal one-vertex leaf probability; finite exact moment identities are immediate consequences and are not credited as independently original. The assessed result is the uniform changing-part-count CLT and a positive universal total-leaf variance constant. The original full primary Section 6, including leaf probability, was examined; it did not state the claimed global uniform CLT. A broader modern occupancy CLT might imply this special consequence, which remains a priority risk.

## value

PASS

A universal Gaussian law for the natural number of leaves in random spanning trees across complete graphs, balanced complete bipartite graphs and intermediate regular multipartite hosts gives nontrivial distributional information beyond a known one-vertex mean. Uniform control across changing host geometry is a meaningful probabilistic refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
