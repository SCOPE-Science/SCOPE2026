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

For each nonroot edge the indicator of being spanned by a size-k leaf sample is 1 minus its avoidance indicator. Summing and expanding pairs recovers the exact displayed first and second raw moments from clade-size counts a_s and pair-union counts b_s. Binomial coefficients in k=n-j form a triangular system with nonzero diagonal, so both moment profiles are equivalent to (a,b), with b_n set by the total edge-pair count. The independent canonical non-plane rooted-tree recursion enumerated all sizes 1..16 (10905 shapes at 16) and the independently coded bit-clade pair signatures had a single duplicate class at 16 and none below; that class is the stated nonisomorphic assortative/mixed pair. Independent two-leaf enumeration gave third binomial-moment sums 5909 and 5910, difference 1/120. Attaching a new root with an extra leaf keeps all old a,b entries and adds only universal clades, preserving collisions for n>16. Proved scope is unit-edge non-plane full binary shapes; no claim of uniqueness of larger-n collisions or weighted-tree identification. Finite exhaustive search is valid for exactly n<=16, not an infinite uniqueness proof.

## originality

PASS

The old rarefaction theory supplies the forward expectation and variance formula; the new claim is the inverse identification cutoff from both full curves and the unique two-moment collision at 16. Existing subtree-size-multiset/OEIS data concern the one-curve a_s invariant, which mathematically does not determine b_s. Bounded semantically related searches including Resultary located no stronger published inversion theorem; this is best-of-knowledge priority with an uninspected related 2026 manuscript remaining a real risk.

## value

PASS

Recovering rooted topology from observable uniform-rarefaction moments is a natural inverse question in phylogenetics. The sharp first failure, unique obstruction, third-moment separator and extension to every larger leaf count identify a nontrivial identifiability boundary; value is not from reproduction of old mean formulas or numerical coincidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
