---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The proof was checked against the stated definitions and the primary full text of *Asymptotic density and the Ershov hierarchy*.

- The target density \(r\) is taken from a \(\Delta^0_2\) set; the source's Theorem 2.1 gives the needed \(\Delta^0_3\) characterization and converse.
- The rational baseline \(a\) lies in \([\max(0,r-d),\min(r,1-d)]\); the endpoint choices \(a=0\) for \(r=0\) and \(a=1-d\) for \(r=1\) are valid.
- The density-scaling identity is applied only when both the range and the coded set have densities.
- The restricted bound \(g(j)=f(s_j)\) meets the source theorem's computable, nondecreasing, unbounded hypotheses.
- On \(S\), the coded approximation uses at most \(f(s_j)\) changes; on the complement, the computable baseline uses at most one change, allowed by \(f(n)\ge1\).
- The union is disjoint, so the two densities add exactly to \(r\). Conversely, every \(f\)-c.e. set is \(\Delta^0_2\).

No finite enumeration or experiment is used as a substitute for the proof. The result is sufficient rather than necessary, and the broader literature search cannot rule out an unindexed equivalent observation. Independent audit and independent validation remain unperformed.
