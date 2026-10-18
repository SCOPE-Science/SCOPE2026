---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Reconstructed the three exhaustive cases for iid vectors with independent heterogeneous coordinates. All positive top-atom masses p_j give an atom at the joint top vector and a_n≥1−(1−∏p_j)^n→1. Exactly one missing top atom: select measurable marginal maximizing index I_n independent of all remaining coordinate samples, which is top in remaining coordinates with probability p_*=∏_{i≠j}p_i, so a_n≥p_*; with atomless exceptional marginal the unique argmax and an endpoint-absence union bound show a_n→p_*, with d=2 Bernoulli exact a_n=p+(1−p)^n. For ≥2 missing top atoms, projection to two coordinates and g_Y(n)=E[F_Y(Y_1)^{n−1}]→0 yield a_n≤(1−q)^n+nq g_Y(n) for any q=P(X>t)>0. Choose q_k→0 below min(1/k,k/N_k), n_k=ceil(k/q_k), g_Y(n)≤k−2 for n≥N_k, giving a_{n_k}≤e^{−k}+(k+q_k)/k²→0. All tie cases and infinite essential suprema handled. This proves only positive liminf dichotomy, NOT full convergence in the two-missing case.

## originality

PASS

Prior leader-property papers contain product examples and a related maximizing-index-set intersection criterion but do not in their inspected theorems translate it into the necessary-and-sufficient terminal-atom classification across all heterogeneous dimensions. The published Resultary tie criterion is more general samplewise but explicitly leaves one-dimensional distribution conditions open; its oscillation example supports the need for liminf rather than full-limit statement. This is a nontrivial additional distribution-level result, not a restatement of the sample-index formula.

## value

PASS

A natural complete classification of which independent-coordinate laws retain a positive probability of a joint observed leader as sample size grows; resolves a concrete distribution-level question while distinguishing endpoint atoms from cardinality and excluding false full-limit conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
