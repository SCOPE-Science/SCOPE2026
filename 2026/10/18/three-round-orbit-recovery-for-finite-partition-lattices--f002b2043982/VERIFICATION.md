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

For a partition with k blocks, exactly B_k-1 strict coarsenings determine k at round one. At fixed k=n-r+1, the round-two count of strict atomic refinements with one pair is sum_i C(s_i,2), uniquely maximized at C(r,2) by type (r,1^(n-r)) for r>=3; T_2 was detected by round one. At round three, the counts of strict T_r predecessors yield b_r=sum_i C(s_i,r) after correcting the known self-exclusion. Upper-triangular binomial inversion reconstructs the full block-size multiplicity vector, exactly the S_n/full-order-automorphism orbit. The proof handles n=1,2. Independent construction of full strict-order pairs and bidirectional 1-WL for all partition lattices n=1..7 matched exactly the type classes.

## originality

PASS

Block-type orbit classification is classical and not treated as new. The identified primary partition-lattice papers study Möbius functions, filters, homology and representation theory, not colour-refinement depth; Arvind et al. describe graph refinability generally but give no constant three-round partition-lattice result. The full strict-order relation is a material hypothesis. Semantic and focused literature searches found no theorem dominating this exact statement. The priority judgment is best-of-knowledge with possible specialized finite-model-theory overlap.

## value

PASS

Uniform orbit reconstruction in just three local counting rounds, independent of Bell-number-sized lattice order, is a nontrivial structural algorithmic lemma for a canonical combinatorial poset. The explicit mechanisms (atomic extremum and binomial moment inversion) may be reused for other relational structures and distinguish the full strict-order language from the cover graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
