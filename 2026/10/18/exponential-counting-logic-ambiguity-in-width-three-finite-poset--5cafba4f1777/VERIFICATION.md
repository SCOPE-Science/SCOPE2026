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

Reconstructed transitive closure from identity edges (a,z)->(a+1,z) and ±1 jumps (2j,z)->(2j+2,z+s_j). Each interval [a,b] permits subsets of nonoverlapping shortcut indices, so attainable Z/3 offsets are {0}, {0,s}, or all residues for 0,1,>=2 shortcuts; uniform q(a,b)=1,2,3 independent of signs. The level sizes and all directed atomic-type counts agree, implying C² sentence equivalence by equitable-refinement/two-variable counting quantification. The three coordinate columns are chains and each level an antichain -> width exactly 3; height 2t+1. Strictly growing predecessor counts force an isomorphism to preserve levels, identity-adjacent matchings force one common permutation of F3, necessarily z->uz+v, and the two-step chords force r=us globally -> exactly 2^(t-1) isomorphism classes. Translations give each level one orbit, and unique predecessor counts separate levels at first counting-refinement round. Independent transitive closure and comparison-count checks at t=2..4 corroborated, not substituted for unrestricted t induction.

## originality

PASS

Best-of-knowledge PASS for an explicit 2^(t-1) family of pairwise nonisomorphic width-three transitive posets that are C²-equivalent while colour refinement is orbit-exact. General regular/biregular C² and graph-refinement results are antecedents but do not specifically imply this exact restricted-poset family and isomorphism quotient.

## value

PASS

The construction exposes a sharp conceptual distinction between recovering the automorphism orbits of a bounded-width poset and identifying its isomorphism type by counting logic. It supplies infinitely many fully classified witnesses on a natural small-width class, relevant to finite-model theory and structure recognition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
