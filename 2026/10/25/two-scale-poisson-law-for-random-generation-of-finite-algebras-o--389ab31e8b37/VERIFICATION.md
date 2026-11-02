---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The finite Boolean-filter pair representation yields exactly binary and ternary coordinates in the signature without a named U. Terms down(x), down(not x), and not(down(x) or down(not x)) separately test T,F,U. Conjunction of word tests isolates a coordinate, and a generator holding U realizes undefinedness at that isolated ternary coordinate. Necessity of pairwise distinct binary words, pairwise distinct ternary words and an U in each ternary word is exhaustive. Thus the two independent injective word assignments give the falling factorial product, including k=0 (only a single binary factor is zero-generated). For r~a sqrt(2^k), binary collision factorial moments converge to Poisson a^2/2; each ternary word avoids U with independent probability (2/3)^k, yielding Poisson b. Expected ternary word collisions at s~b(3/2)^k are O((3/4)^k), so negligible. The high/low probability regimes use exponential collision bounds and union bounds, not finite extrapolation. Independent closure enumeration recomputed primitive-term generation on ten small parameter cases. No nonuniform or pointed-signature conclusion is claimed.

## originality

PASS

Best-of-knowledge PASS specifically for the two-scale random-generation Poisson law, not priority for the finite product representation, coordinate separation criterion or falling-factorial combinatorics alone. Inspected Sipoş normal forms and Ledda–Graziani–Vergottini representation cover the deterministic ingredients; neither inspected material states the joint stochastic law. Closest Resultary occupancy hits concern different objects; no implication of this law was found. Residual older-term-equivalent random-generation literature remains plausible.

## value

PASS

Random generation is a natural finite-algebra question; the exact count has two mathematically different mechanisms, birthday collisions of Boolean coordinate signatures and absent undefined values in ternary coordinates. Their competition at two distinct exponential population scales, joint independent Poisson law and full threshold give information not mechanically supplied by a deterministic generator-rank formula. A future study of random finite ADA generators can use the exact asymptotic and obstruction decomposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
