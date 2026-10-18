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
# Reproduction and checks

Execute `python3 verify_configuration.py` and `python3 verify_cycles.py` with the six accompanying research documents and verification programs in one working directory. Their outputs should match `CONFIGURATION_CHECK.txt` and `CYCLE_CHECK.txt` verbatim. The programs use only the Python standard library and require no network access.

The first checker reconstructs the Fano incidence relation, the Abrams unordered two-particle model with cell counts 91, 252 and 168, signed boundary matrices with zero composition, matrix ranks modulo 2, 3, 5, 7, and 101, all 336 automorphisms with their exact signed chain traces, and both invariant-average equalities. The second checks all vertex deletions of size zero, one and two for connectivity, enumerates the 28 six-cycles, establishes girth at least six and their eight-dimensional mod-three cycle span.

The proof of integral degree-one homology relies on Ko–Park, *Characteristics of graph braid groups*, Theorem 3.16 (arXiv:1101.2648); the integral degree-two group is free as a subgroup of a free cellular group and has rank fixed by Euler characteristic. The equivariant degree-one identification uses a mathematical lifting of graph cycles, not merely the finite-field tests. The new degree-two rational character is computed from an exact cellular trace identity and all finite graph automorphisms. These are reproducibility checks and self-review, not an independent audit.

No claim is made about integral equivariant decomposition, configuration cup products, higher-particle cases or absolute novelty against material unavailable in the consulted literature.
