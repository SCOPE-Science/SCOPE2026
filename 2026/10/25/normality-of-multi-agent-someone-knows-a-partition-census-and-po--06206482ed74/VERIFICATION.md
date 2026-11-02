---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

At each world w, the predicate S(P)=some E_i[w] subset of P is a monotone truth-preserving disjunction of principal filters. It preserves binary intersections (hence normal distribution over all valuations) iff the finite cell family has a least member, necessarily the intersection R[w], so S equals the S5 box for R and nested formulas agree. Fixing R as a t-block partition, each E_i is a partition of the t labelled blocks. Normality means every quotient point is singleton in at least one agent partition, whose exact inclusion-exclusion count is H_r(t)=sum_j(-1)^j C(t,j) (sum_k(-1)^k C(j,k)B_{t-k})^r. The coverage condition forces common refinement exactly R; Stirling transform gives L_{n,r}. Fresh independent Python enumeration of all ordered r=2,3 partition tuples n<=5, including 140,608 cases at n=5,r=3, exactly reproduced 1,8,89,1449,31468; the formula gives 864347 at n=6. For r_n B_{n-1}/B_n−log n→c, factorial moments of uncovered singleton-cell count converge to e^(−kc), since a_{n,k}=1−ks_n+O_k(s_n²) and r_ns_n²→0. The chance R is not discrete is bounded by C(n,2)s_n^{r_n}→0, so the global normality probability converges to exp(−exp(−c)). The Poisson limit is analytic, not certified by finite checks.

## originality

PASS

Ågotnes–Wáng 2021 and Ding–Yang 2026 characterize/axiomatize someone-knows and its nonnormal semantics, not the exact finite-frame distribution schema count or random agent threshold. Pittel’s common-refinement discreteness for fixed agents does not ensure each point singleton in an individual agent relation, the necessary stronger event. The closely related Ding–Liu–Wáng 2023 hypergraph work was available only as its publisher preview despite arXiv/open-search attempts and an authorized full-text request returning vpn_disconnected; the risk is recorded, not turned into automatic failure. The independent exact formula plus Poisson law survive on best-of-knowledge evidence.

## value

PASS

Combines an exact modal-algebraic characterization with a nontrivial complete enumeration of labelled multi-agent S5 frames and a sharp growing-agent random partition coverage transition. Distinguishes normality from the much more common discrete common refinement: a natural logically motivated invariant and an unexpected Poisson critical window, not a mere combinatorial parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
