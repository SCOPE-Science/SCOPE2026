---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For the unweighted prism G=C3□K2 with six vertices, each vertex lies in six distinct graph-distance balls (singleton, four radius-one neighbor-centered balls, and whole graph). Choosing an averaging ball per row gives exactly 6^6=46656 nonnegative averaging matrices A_s. For real l2, positivity of A_s lets top singular vectors be nonnegative, and finite max interchange gives ||Mtilde||²=max_s λ_max(A_s^T A_s). Exact integer positive-definiteness of 11664I−50R_s^T R_s (R_s=12 A_s), with Sylvester/fraction-free elimination, excludes 46638 cases below squared threshold 81/50; the remaining 18 have common determinant z(z−16)(z−1)(z³−31z²+132z−128) for Gram(4A), and top λ* solves 64λ³−124λ²+33λ−2=0 above 81/50. Explicit strictly positive Perron vector proportional to (1,1,a,b,c,c) with a=(λ−1)/λ, b=(3λ−1)/(λ(8λ−1)), c=(3λ−1)/(λ(16λ−1)) is active against all five alternative row balls for every winning matrix. This gives precisely 18 nonnegative rays and graph automorphism orbit sizes 6+12. Separately all 3^6=729 centered matrices have squared spectral norm <3/2<λ*. The finite exhaustive certificate proves the finite domain claim when integer inequalities are actually checked; logs alone do not.

## originality

PASS

Prior graph maximal-operator works give general finite-graph comparisons, centered sharp constants for selected graph families, and uncentered operator definitions, while 2026 variation results use a different seminorm and at most five vertices. None inspected supplies the six-vertex triangular-prism uncentered real l2 norm, its 18 equality rays or two symmetry orbits. The exact finite graph is natural and not an arbitrarily sliced giant enumeration; an unindexed precomputed graph table could still duplicate the result.

## value

PASS

The triangular prism is a natural small vertex-transitive Cartesian product with a nontrivial center-free ball geometry. The sharp uncentered vs centered l2 gap and two inequivalent symmetry orbits sharing an algebraic extremal value are meaningful finite-network maximal-operator facts, offering a benchmark for graph product sharp inequalities. A single finite graph is acceptable here because the graph and invariant are mathematically motivated and the result is an exact complete extremizer classification, not a random tiny gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
