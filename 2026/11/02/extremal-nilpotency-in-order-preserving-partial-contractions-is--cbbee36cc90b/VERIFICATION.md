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

The directed graph of a nilpotent injective partial map with rank k has k arrows in disjoint chains, so nilpotency index <=k+1; equality requires a single chain of k+1 vertices. Order preservation makes successive forward iterates strictly increasing (or decreasing) by induction, forcing forward/backward shifts along ordered support. For a forward shift contraction, successive positive gaps satisfy d_{i+1}<=d_i; these partitions of span m are counted by p_k(m) with n-m shifts and 2 orientations. The formal partition Euler product produces the stated GF; Hardy–Ramanujan plus a uniform exponentially decaying j/sqrt(n) tail controls E_n~(12/pi²)n p(n) and hence constant sqrt(3)/pi². Independently enumerated every rank-k partial monotone contraction for n=5,6,7,8 and direct composition nilpotency, matching rank vectors and sums. The infinite asymptotic is analytical, not inferred from enumeration.

## originality

PASS

Best-of-knowledge acceptance for the precise final claim after separating prior-covered statements from new structural/quantitative content. Genuine refinement of established enumerations with distinct statistic, precise all-n,k classification and rarity law.

## value

PASS

A natural index-refined extremal subfamily of a well-studied semigroup is classified exactly and exhibits partition-type growth. This separates rank-and-fixed-point counts from nilpotency INDEX, providing a useful generating-function and asymptotic invariant rather than re-listing all nilpotents.

The dated certificate retains the supplied scientific assessment, sources and limitations.
