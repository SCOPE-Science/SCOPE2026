---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Every eligible odd composite supplies an odd nontrivial factor pair with injective one-bit sums, so counting even the larger set of all such pairs is an upper bound. Assign highest bit indices t≤B and k=t+B≤floor(log₂ X). If t≤B/2, the mandatory bits 0 and t in a forbid two bits of b at distance t. The graph of that restriction on 0,…,B is a disjoint union of t paths. Matching within each path gives at least (B+1−t)/2≥B/4 disjoint edges, so at most 2^(B+1)(3/4)^(B/4) strings survive. Multiplying by at most 2^t candidates for a and using B≥2k/3 gives O(2^(ϑk)) with ϑ=1−log₂(4/3)/6. If t>B/2, B<2k/3, and injectivity into the k+1 positions implies that one factor has weight at most √(k+1). This costs only 2^O(√k log(k+2)) choices for that factor, while the other has at most 2^(B+1) choices. The resulting exponent is below ϑk for large k; finitely many small cases are absorbed with an absolute constant. There are at most k+1 splits for each k, and the sum grows geometrically up to a linear factor in floor(log₂ X). The bound and the density conclusion follow without the finite counts.

## originality

PASS

On the actual evidence, pass the distinct quantitative bound on the odd composite class. Prior binary-convolution terminology, the collision equivalence and the underlying counting motivation are not the claimed additions. The closest examined catalogue statements classify fixed low binary weights, not arbitrary bit-length orthogonal pairs. The cited parent article remained inaccessible after lawful retrieval attempts, so the exact wording and open status of its question are not certified. This is a best-of-knowledge decision on the proved bound, not a priority claim or an assertion about the article's entire scope.

## value

PASS

A power saving for a natural binary-factorization property is materially stronger than a finite table or a qualitative density observation. The proof covers all odd composite sizes and explains why orthogonality forces a saving across both bit-length regimes without assumptions on primes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
