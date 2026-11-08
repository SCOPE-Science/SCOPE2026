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

For fixed integer n>=2, M>=n and arbitrary simplex sampling p, a new completion at the shifted M-window occurs iff the M−1 common middle draws omit exactly one type i, contain every other type, the old departing type is not i and the newly arriving type is i. This proves the exact independent middle-block/inclusion-exclusion identity, with factor p_i(1-p_i). Along any M→∞ subsequence, rates Mp_i have extended limits: diverging rates contribute at most Mp_i e^{−Mp_i}→0; finite rates give independent Poisson rare counts, and each diverging rate type is present w.h.p. Thus every rescaled entrance limit is G_k(c)=Σ_i c_i e^(−c_i)∏_{j!=i}(1−e^(−c_j)) for k<=n−1 finite rates. The extension to [0,infty]^k has zero-coordinate value zero and infinity faces G_{k−1}; adjoining one sufficiently large finite coordinate strictly raises G, so the global maximum is interior, strictly increases with k, and its derivatives force all coordinates equal via strict increase of c/(1−e^−c). Unique diagonal critical point c_k solves 1/c−1+(k−1)/(e^c−1)=0, giving the exact constant C_k. Construction and all-subsequence uniqueness imply one common type with probability→1 and every rare type Mp_i→c_{n−1} after relabeling; no finite-M uniqueness is asserted. Independent enumeration of actual (M+1)-draw words matched the inclusion formula for n=2,3 and bounded windows. This bounded test does not prove global asymptotics.

## originality

PASS

Best-of-knowledge originality PASS based on direct comparison of exact statements, hypotheses and implications. Prior model ingredients and general lemmas are credited; no inspected full-text theorem establishes the precise additional classification. The named inaccessible and abstract-only comparisons remain risks, not proof of priority. Long uniform asymptotics yield exp(−constant*M) for fixed n; they cannot imply C_{n−1}/M optimum or singular-profile rigidity by parameter specialization. The actual proof requires compactification of Mp_i and a unique global Poisson-function optimization.

## value

PASS

Maximizing stationary arrivals into complete expiring windows, rather than maximizing occupancy or minimizing first collection time, is a natural but distinct stochastic optimization target. The sharp 1/M improvement over uniform exponential decay and rigidity of the one-common/equal-rare optimal sampling profile are nontrivial asymptotic structure; a useful exact fixed-alphabet design law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
