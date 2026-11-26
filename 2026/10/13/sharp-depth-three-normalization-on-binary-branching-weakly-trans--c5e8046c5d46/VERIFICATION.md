---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

R∪Id is transitive by weak transitivity, so the generated part of any pointed model is {w}∪R(w), of size at most three even in an infinite ambient frame. Loops are counted; restriction to the generated model preserves modal truth. Atomic truth vectors are needed only up to their equality partition on the at most six worlds of two such models. Independently generated admissible adjacency lists and their orbits under all permutations (2,10,37 orbit counts), generated the joint color partitions by peeling off the block of the first remaining world, and used direct back-and-forth on pair relations rather than the supplied signature checker. In all 163990 unordered frame-pair × partition cases, depth-three equality was already stable. Testing ordered pairs adds only swapped copies, explaining the supplied 320315 count. Stability gives a bisimulation because atom agreement persists and the fixed relation already matches successors in both directions. For a finite propositional vocabulary every type at depth three has a characteristic formula using exactly that vocabulary or a subset, obtained by atomic literals, diamonds for realized successor types and a box excluding the others; the finite disjunction of the satisfying types normalizes an arbitrary formula. For the sharpness pair, both roots see a non-dead successor and a dead successor, hence have identical depth-two types with constant atom valuations. In Q the two-cycle permits a length-three path; in P all paths have length at most two. Both are weakly transitive with the stated loop-counted cap, so Diamond³ top is a valid proposition-free lower bound.

## originality

PASS

The supported distinct claim is the exact uniform modal-depth threshold for genuine two-successor weakly transitive frames, including the proposition-free sharpness witness. The closest indexed deterministic subcase gives depth two, not the branching result. Local tabularity and finite-model/finite-width selection results do not determine this fixed-depth bound, and standard bisimulation machinery does not supply the class-specific finite lemma. This is a bounded best-of-knowledge assessment, not a priority certification.

## value

PASS

The first branching case beyond deterministic weakly transitive frames is a natural boundary. The exact depth quantifies how much branching raises distinguishability in the ordinary modal language, uniformly in the number of propositional variables, and the proposition-free witness shows this is structural rather than an atom-encoding artifact. The result is strictly more informative than local tabularity or an uncolored frame count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
