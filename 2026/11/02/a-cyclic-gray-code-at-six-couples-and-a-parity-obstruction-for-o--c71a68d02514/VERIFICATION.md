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

Legal permutations have determinant sign sum det(J-I-P), where J is all ones and P a cyclic shift. The constant-vector eigenvalue is n-2; nontrivial Fourier eigenvalues -1-zeta^k. The product vanishes for even n and yields n-2 for odd n. A legal transposition flips sign, so a bipartite Hamilton path requires parity-class difference <=1, excluding odd n>=5. For n=6 the certificate of 80 distinct indices into the exact lexicographic legal set was fetched from the frozen Git blob. Independent recomputation verifies each cyclic consecutive pair (including last-to-first) is one transposition, all 80 vertices are visited, 207 undirected edges and exhaustive all-source BFS gives eccentricity 5 for 48 vertices and 6 for 32. Exact enumeration also verified parity n=3..9; no finite extrapolation is used for unbounded odd n.

## originality

PASS

Best-of-knowledge originality of the precise final result is retained after direct scope/implication comparisons and meaningful reading, with identified prior machinery and explicit inaccessible-source risks. No failed search is treated as a novelty proof.

## value

PASS

The negative parity obstruction gives a complete infinite Hamilton-path impossibility mechanism for every odd size, while the positive n=6 explicit cyclic Gray code is a nontrivial reconfiguration witness at the first larger even instance. Exact finite graph diameter and boundary cases characterize a natural restricted permutation graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
