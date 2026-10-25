---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For G=Cartesian product of finite paths P_ni with ni>=2, one marked origin singles out every distance layer and the unique farthest corner. Stability exposes predecessor colour multisets. Induction reconstructs each vertex’s multiset A={x_i} using triangular deck relations S0=p a0+a1 and Sj=(p-1)aj+a(j+1) for j>=1; reflection from the farthest corner similarly reconstructs B={L_i-x_i}. Comparing A,B predecessor and successor signed-card changes reconstructs actual coordinatewise pairs (x_i,L_i-x_i), including zero coordinates via upper neighbours. Equality of these pairs is exactly the orbit under permutations of equal-length axes fixing origin. Therefore class count product_m binomial(r_m+m-1,m-1) and multinomial sizes follow for all d>=3, also formally d=1,2; no unstated dependence on disjoint factor lengths. I independently checked that A,B alone need not encode the pairing (the supplied example P2×P3×P4), making the combined card argument necessary.

## originality

PASS

Best-of-knowledge, subject to explicitly documented priority risks: searched the available Resultary records and primary literature, compared the exact claimed quantifiers/invariants to prior implications rather than matching titles, and did not treat inaccessible full text as proof of noncoverage.

## value

PASS

A full orbit census for all finite high-dimensional boxes under only unit-edge adjacency and one corner anchor is a natural structural result for 1-WL and symmetry. Recovering factor-length-sensitive coordinate multisets from unlabelled graph colour signatures is a nontrivial inverse problem, with precise class cardinalities useful in refinement benchmarking.

The dated certificate retains the supplied scientific assessment, sources and limitations.
