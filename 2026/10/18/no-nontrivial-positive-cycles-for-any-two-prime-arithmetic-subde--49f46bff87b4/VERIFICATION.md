---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For arbitrary primes p<q and a positive periodic trajectory n_i, define c_i=qνp(n_i)+pνq(n_i)>0. Exact ratios n_{i+1}/n_i=c_i/(pq) imply product c_i=(pq)^L and every c_i has only p,q prime factors. Valuation updates give c_{i+1}−c_i=q(u_i−1)+p(v_i−1) if c_i=p^{u_i}q^{v_i}. Below pq, smoothness forces c_i to be p^u or q; c=p or q exits positivity, otherwise p^u increases. At/above pq, the half-line is forward invariant, including pure q^v via c_next>=q²−q+p>=pq. Thus no finite positive cycle can contain c<pq; all c_i=pq by product, hence every point is fixed. Integer congruence q a+p b=pq has only exponent solutions (p,0) or (0,q). Independently sampled 35,955 bounded trajectories over prime pairs through 29 with zero nontrivial cycles; this is supplementary to the unrestricted valuation proof.

## originality

PASS

Talukdar and Saikia (2026) Theorem 3.4 already classifies positive fixed points for general supports; those families are explicitly not new. Their discussion names additional periodic points as further work. Published 2026 Resultary theorem excludes nontrivial cycles for {2,3}, but a single prime pair does not imply arbitrary p<q. The new universally quantified two-prime cycle exclusion, using a smooth threshold and orbit-product argument, survives these comparisons. General support size three remains unknown here.

## value

PASS

Nontrivial periodic points in prime-supported arithmetic differential dynamics are a natural open structural problem highlighted by primary literature. Closing it uniformly for the entire family of two-element prime supports is a substantive classification and not just restating the known fixed-point formula or changing numeric parameters in the {2,3} theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
