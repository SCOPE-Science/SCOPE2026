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

The theorem is verified analytically rather than by finite sampling.

The upper bound is reference-stable because \(X\mapsto d\operatorname{Tr}(X)I-X\) is completely positive; its Choi matrix is \(dI\otimes I-|\Omega\rangle\langle\Omega|\ge0\). This produces the operator domination used for every reference-assisted input.

The lower bound is a genuine channel-discrimination witness. For any erased-branch state with sector weights \(q_i\), some sector satisfies \(q_i/d_i^2\le1/\sum_jd_j^2\). A maximally entangled state in that protected sector and a binary effect on its support yield the matching trace-norm separation. The same witness proves the factor \(p\) for partial flagged erasure.

The proof covers all finite positive block dimensions and all \(0\le p\le1\). No finite enumeration, numerical optimization, or asymptotic approximation is used.

No independent audit has been performed.
