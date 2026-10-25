---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Over F_2, every projective line is {x,y,x+y}, uniquely determined by two distinct points. At an even 1-WL round, any two named points give a singleton line at the next odd round and hence a singleton third point at the next even round. All unnamed y without an expression y=x+z for named x,z have identical line-colour multisets: exactly one line through each named x and uniform all-unnamed remainder. The identity T_j ∪ (T_j+T_j\{0})=T_{j+1}, with T_j all nonzero support weights ≤2^j, proves the exact induction. At the final even point-discrete round, threshold t=2^(k−1), the only possible late line collisions arise when d≥t+3, witnessed by two different t-subsets off coordinates 1,2; d≤t+2 separates already by 2k. Fewer than d named points span a proper subspace fixed pointwise by a nontrivial linear automorphism, so cannot discretize. Independent rebuilt 1-WL checks for d=2..5 returned graph-round depths 0,2,4,5. Original source checkers cover graph d=2..9 and combinatorial tests to 17 but stored logs are not proof.

## originality

PASS

Best-of-knowledge original all-dimension exact support-weight 1-WL partition and dimension-dependent sharp stabilization depths; known generic individualization complexity and binary projective Steiner-system coding do not give the displayed theorem by implication.

## value

PASS

A canonical incidence graph from finite geometry acquires a completely explicit 1-WL filtration, exact logarithmic stabilization complexity, the nonuniform one-round line lag, and optimal number of distinguished landmarks. This motivated sharp invariant is useful for graph-isomorphism refinement and projective incidence structures, not just a small computational coincidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
