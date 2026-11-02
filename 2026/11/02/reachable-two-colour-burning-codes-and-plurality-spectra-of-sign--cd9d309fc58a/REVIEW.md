# Self-review

## Correctness — PASS

The exact all-positive reachable code is derived from both possibilities for the first ignition; only one leaf can depart from the center colour, and each allowed departure is constructively achievable. The signed case follows from the influence-preserving coordinate switch, with exact Hamming-distance calculations giving plurality for every negative-spoke count. Maximization across all counts yields the covering radius and all deep-hole weights. The direct state-transition verifier replays all labelled signatures for \(3\le n\le8\), and a separately evaluated Hamming-minimization check covers \(9\le n\le15\). Boundary cases \(n=3,4\) are explicit. Finite evidence does not replace the infinite proof.

## Originality — PASS (qualified)

The full first public 2026-10-01 manuscript of Fallat, Gupta, Khodamoradi and Zilles was inspected for the same object, definition, equivalent code formulation, main results and conclusions. Its signed-path results, general switching lemma and general coding identity do not supply the star's exact reachable code or signing enumerator; the general identities are properly attributed. It suggests signed-tree bounds and coding-radius questions. Targeted mathematical-record searches for star burning, plurality, codes and covering radii did not locate an equivalent star result. The main residual risk is an unlocated same-result derivation in work on simple binary covering codes or newly posted signed burning results; absence from search is not proof of novelty.

## Mathematical value — PASS

This is a complete classification on the first branching tree family for a recently introduced nonlocal signed propagation model. It determines the entire reachable-colouring code, every possible signed-star plurality with multiplicities, the exact covering radius, and the signatures attaining the worst plurality. This is directly motivated by the source's signed-tree and coding questions, rather than an arbitrarily chosen numerical slice, and gives a closed-form benchmark for wider signed-tree algorithms. The proof is elementary because the star collapses to a few ignition stages; value is in the natural complete classification, not in proof length.

## Relationship and limitations

Closest source: Fallat–Gupta–Khodamoradi–Zilles, *Burning Signed Graphs*, arXiv:2610.02506v1 (2026-10-01), sections 2–3 and 5. The result uses their process and general switching/coding interpretation, but supplies the star-specific code. It does not cover general trees or restricted ignition/deadline variants. Historical priority and independent verification remain open.

Self-review: passed. Independent audit: not yet performed.
