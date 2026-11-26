---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A local power identity makes each map a permutation of its domain. Commutation with the partial idempotent f_j^{d_j} forces f_i to preserve membership in D_j throughout D_i (compare the domains of the two products). This yields independent actions of G_S on the exact support atoms, and conversely these actions give precisely the tuples in the claim. A connected labelled orbit of index k contributes (k-1)!/k!=1/k, once per actual subgroup since G_S is abelian; the empty-support labels contribute exp(x). Product domains are exactly the intersections, including with empty domains, so the rank substitution follows; Boolean Möbius inversion also recovers the atom counts from the ranks and n. In the cyclic pair case one can project a subgroup to eC_b and intersect it with C_a in dC_a: the remaining choice is the graph of a map eC_b to C_d, giving gcd(d,b/e) choices at index de. These arguments verify the stated formal EGF, including n=0 and trivial cyclic factors. The frozen checker was read, not run; its bounded tests are corroborative, not needed for the proof.

## originality

PASS

Credit known partial-injection commutation structure, the standard orbit exponential formula and previously enumerated rank-two subgroup indices. The supported distinction is the exact labelled enumeration with simultaneous marks for every support atom/every subproduct under arbitrary prescribed powers. The closest located equivalent specialization is dated later and is strictly narrower. No priority is claimed for the pair-subgroup arithmetic itself.

## value

PASS

Knowing the full joint profile is useful for exact rank counts under simultaneous commutation: separate ranks and even full-product rank lose information about the proper subproducts. The Boolean enumeration recovers that information for any arity with independent power constraints and reduces exact coefficients to finite subgroup data. This is not a claim of novelty for the standard subgroup counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
