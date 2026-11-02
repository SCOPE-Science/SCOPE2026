---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Verified actual RESULT.md claim for every integer k>=2 and all (hub-swap, page-permutation) classes. Morse simplices are directed forests with each graph vertex at most one outgoing edge; reversal of arrows matches the cited bidirected complete-source shellability premise. Jojić 2012 covers the exact K_{1,1,k} nonequivariant rank (k+1)^2. Reduced signed Lefschetz/Hopf trace is chi=(-1)^(k+1) sum over fixed forests of (-1)^(number of arrows) times sign of induced arrow permutation (empty face included). Fixed-hub case factors nontrivial page cycles each with signed sum -1, and fixed-page determinant det(I-L_{B_f})=(-1)^(f-1)(f+1)^2 (with f=0 evaluated separately on K2). Swapped-hub case partitions absent hub arrows, targets at fixed pages, and targets in two-cycles; contributions (-1)^e, -f(-1)^e and 2t(-1)^e exhaust possibilities. Independently enumerated all allowed parent functions, checked directed acyclicity and signed invariant-arrow permutation traces for each of 56 conjugacy classes for k=2..6, all agreeing. Independently calculated mod2 boundary ranks for k=2,3,4, finding sole reduced homology rank (k+1)^2 in degree k. Finite calculations corroborate, but all-k proof rests on the uniform orbit enumeration, determinant and shellability; f=0, k=2 and empty forests included.

## originality

PASS

Best-of-knowledge originality survives only for the full C2 x S_k rational homology character. Jojić 2012 already settles the nonequivariant homotopy type of this exact K_{1,1,k} graph, including rank (k+1)^2; nothing novel is claimed about that. The closest published equivariant K_{2,k} character coincides in the hub-swap sector but differs in the page-permutation sector by 2 sgn(sigma)(f+1), and the prior source does not establish that adding the hub edge induces the stated character change. Direct all-k invariant-forest orbit enumeration supplies the extra information. No inspected primary result implies the complete character, while possible unindexed stronger equivariant directed-forest theory remains a priority risk.

## value

PASS

The triangular book K_{1,1,k} is the natural complete-tripartite family of k triangles sharing an edge; its entire symmetry group C2 x S_k acts canonically on the ordinary graph Morse complex. An all-k rational group character detects page permutation cycle structure and hub interchange, which the already known wedge rank (k+1)^2 alone cannot determine. Explicit page-permutation module identification makes the result a reusable equivariant refinement, not a tiny numerical gain, arbitrary parameter slice or a relabeled shellability theorem. Does not claim integral group-module structure or equivariant homotopy decomposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
