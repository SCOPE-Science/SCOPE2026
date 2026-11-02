---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The uniform integer flex one-cochain α assigning +1 to each sink-to-source directed flex edge is closed: each cubical square has two positive and two negative boundary terms. Kozlov Theorems 5.18 and 6.1 supply the explicitly used non-equivariant deformation retract of every circle component onto an n-edge sink-flip core cycle (and other components contract). Its primitive core generator pairs n with α, so the positive integral generator is unique. Automorphisms preserve sink/source and α, while global reversal J swaps them and sends α to −α; naturality forces the claimed full integral signed permutation action. Rational orbit-space homology equals invariant rational homology for finite cellular group actions after equivariant subdivision, and a signed permutation orbit has a one-dimensional invariant precisely when its stabilizer contains no sign-negative element. The tree corollary uses Kozlov Corollary 6.13. Fresh independent orientation/square enumeration checked path_4 (8 orientations, four squares), cycle_4 (16, two squares), triangle (8, no squares); the general proof depends on the published core theorem, not finite sampling.

## originality

PASS

PASS best of knowledge: Kozlov classifies the underlying flex components and their core cycles, not the global integral cohomological time normalization or combined graph-automorphism/reversal module. A published stronger explicit K_n character covers the complete-graph specialization but not arbitrary connected graphs nor reversal-containing subgroups. The time cochain is a fairly direct but nontrivial general equivariant consequence of those inputs.

## value

PASS

A graph-natural integral orientation of all circular homology classes makes the Aut(G)×C2 action a canonical signed permutation lattice, avoiding reliance on arbitrary cycle orientations. The stabilizer criterion computes rational H1 of every finite symmetry quotient without re-computing homology and is applicable uniformly to noncomplete graphs; this is a meaningful structure theorem, not merely H1 rank restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
