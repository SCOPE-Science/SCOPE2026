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

For fixed r>=2, clone each threshold demand and use Hall marriage: disjoint witnesses iff every nonempty J has |union S_i|>=sum k_i. Independent centered Bin(n,p_n) counts converge jointly to N(a_i,1). The overcount B_J=sum_i |S_i|-|union| has expectation binom(|J|,2) n p_n^2+O(np_n^3), variance O(np_n^2), so B_J/s_n concentrates at binom(|J|,2)tau_n when tau_n bounded, uniformly over the finitely many J. Gaussian boundary probabilities vanish, yielding the exact order-statistic Hall polytope and crossover p_n~n^(-1/3). If tau_n diverges, a pair intersection scaled by s_n diverges while binomial margins stay tight, so success tends to zero. The small tau^2 pair-triangle law and large tau Gaussian total-sum tail follow by finite inclusion-exclusion and conditional Gaussian concentration. The claims assume fixed r and offsets and np_n->infty; finite simulations are not the proof.

## originality

PASS

Best-of-knowledge original as a fixed-r, sparse triangular-array, multi-threshold Gaussian Hall crossover for product-space disjoint certificates. Cerf–Tesio provide the two-event product-space framework, Tesio examines quantitative BK gap and fixed-bias threshold examples. Neither inspected statement supplies the r-way n^(-1/3) scaling with unequal offsets and exact asymptotic endpoints; relevant matchings/normal-approximation literature could yield an equivalent formulation.

## value

PASS

The theorem gives a full nondegenerate collision-to-obstruction phase transition and exact endpoint onset/tail laws in a canonical random-set matching problem. Its capacitated Hall geometry connects probabilistic dependence to Gaussian polyhedral feasibility for any fixed number of demands, resolving more than a central-limit triviality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
