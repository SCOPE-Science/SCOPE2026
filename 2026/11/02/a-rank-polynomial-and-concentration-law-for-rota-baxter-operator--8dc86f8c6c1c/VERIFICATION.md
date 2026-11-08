---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The descendant subtree vectors S_i form a unitriangular basis. Black rows equal -S_i; modulo their span a white row is the sum of S_c for its white children. These sets are disjoint for distinct white parents, so rank counts all black vertices plus white vertices with white children. Labeled species of colored rooted trees give B/W EGFs and the full rank polynomial. In a uniform Prüfer tree, degree(i)=1+Bin(n-1,1/(n+1)), and conditional white leaf probability 2^{-deg(i)} yields exact mean. Pairwise covariance is O(1/n) because Prüfer counts are multinomial and adjacency probability 2/(n+1), yielding Var(D)=O(n), L² limit. Independent full colored-tree enumeration matches polynomial coefficients and exact mean for all n=1..5; this is finite corroboration.

## originality

PASS

Best-of-knowledge novelty of the precise final theorem survives comparison with relevant antecedents and currently indexed mathematical literature, but not exhaustive historical priority. Rank under the tree encoding is a genuinely finer statistic than operator cardinality; no primary rank distribution was located, without treating absence as proof.

## value

PASS

The full matrix-rank distribution on a natural, all-field finite algebra is useful beyond the known scalar count of operators or bounds on minimal polynomial degree. It gives exact finite enumerators and a universal typical-rank law, with explicit nullity statistic that can support further random-operator questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
