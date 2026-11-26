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

The first-round predecessor count identifies the two atoms when both factors have size at least two; unequal sides distinguish them by successor count. In the square the points incomparable to exactly one atom give the two axes without the least point at round two. A point at axis position k has k−2 strict predecessors in that union, so round three isolates the axis level pairs. Round-four weak predecessor counts to those pairs give the unordered coordinates, and symmetry prevents a finer split. For unequal sides one tracks the separate axes the same way, giving ordered coordinates; a chain is discrete at round one. In any candidate poset with these profiles, the two axis elements at each level match bijectively to the two at each higher level. Align all levels from the atom pair; transitivity forbids a crossed higher-level matching. Each vertex has an initial segment on each aligned axis below it; counts recover the unordered coordinates and column degrees at the larger axis level force opposite assignments for the two vertices of an off-diagonal class. Transitivity implies every actual comparison is coordinatewise allowed, and the prescribed successor counts exhaust all such allowable successors class by class. Rank-four color formulas plus one inner exact count and one outer quantifier give the rank-six sentence. The unrestricted cases are also correct: all relation blocks are forced except one-regular matches between doubletons. For sides one and two none can vary up to isomorphism; for side three the two matching blocks form a path and relabeling its successive classes removes every choice. For every side at least four crossing T2→T4 leaves the relation asymmetric and irreflexive, and preserves all atomic-pair counts into the equitable orbit classes. A two-variable induction on formulas (a counted fresh vertex is categorized by its class and relation to the retained vertex) therefore proves C² equivalence, while the unchanged T2→T3→T4 chain witnesses nontransitivity. Loops or symmetric pairs cannot alter the positive unrestricted cases because the prescribed same-class strict counts vanish and between two classes at most one comparison direction is allowed.

## originality

PASS

The distinct contribution is uniform bounded-depth reconstruction within the class of strict finite posets, including arbitrarily large squares with nondiscrete colors. The unrestricted boundary is credited to an application of the existing general colored-relation criterion; qualitative orbit recovery already overlaps a broader same-day chain-product result. Neither comparison supplies the transitivity-based identification theorem or a uniform four-round separation proof for the whole two-factor family.

## value

PASS

The proof determines how transitivity restores unique identification for an infinite natural family on which standard unrestricted identification fails. It furnishes a uniform depth guarantee without parameters in the nesting bound and a concrete reconstruction from axis comparison data, rather than just computing finite examples or quoting graph identification machinery. No value judgment relies on treating the unrestricted boundary as new in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
