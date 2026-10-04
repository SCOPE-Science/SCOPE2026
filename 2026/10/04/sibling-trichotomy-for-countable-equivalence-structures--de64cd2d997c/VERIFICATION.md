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

# Verification

The proof is structural and does not depend on numerical experiments.

Checks performed:

1. **Embedding constraint.** An embedding preserves both equivalence and non-equivalence, hence induces an injection on equivalence classes and sends each class into a distinct target class of at least the same cardinality.
2. **Bounded regime.** With finitely many infinite classes, mutual embeddings force those counts to agree. Above the largest finite size occurring infinitely often, all finite tail counts are finite, so two opposite injections force equality of every tail count and hence equality of exact multiplicities. At and below the infinitely repeated maximal finite size, all lower classes can be injected into distinct copies of that maximal size.
3. **Unique-sibling boundary.** In the bounded regime, the free lower-multiplicity tuple is empty exactly when the largest infinitely repeated finite size is at most \(1\). This is equivalent to having only finitely many nonsingleton classes.
4. **Countable-sibling regime.** When the largest infinitely repeated finite size is at least \(2\), only finitely many lower size coordinates vary, each in \(\mathbb N\cup\{\aleph_0\}\); therefore there are at most \(\aleph_0\) siblings, and varying the singleton count gives infinitely many.
5. **Unbounded regime.** With finitely many infinite classes and unbounded finite sizes, greedy matching of finite classes works in both directions. A binary choice in the multiplicity of each even class size yields \(2^{\aleph_0}\) nonisomorphic siblings.
6. **Infinitely many infinite classes.** Every countable source class can be assigned to a distinct infinite target class, giving mutual embeddings. Independent presence or absence of one finite class of each finite size yields \(2^{\aleph_0}\) nonisomorphic siblings.
7. **Exhaustion.** Every countable equivalence structure lies in exactly one of: infinitely many infinite classes; finitely many infinite classes with unbounded finite sizes; finitely many infinite classes with bounded finite sizes.

No unproved computational extrapolation is used. The continuum lower-bound families are explicit, and the continuum upper bound follows from the cardinality of the set of countable relational structures up to isomorphism.
