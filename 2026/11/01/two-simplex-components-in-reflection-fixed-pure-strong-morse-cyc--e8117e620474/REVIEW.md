# Mathematical review

## Correctness — PASS
The proof reduces top facets to rooted orientations of the path remaining after the last critical cycle vertex is removed. A matching of maximal cardinality has exactly one pair of adjacent omitted edges and precisely one unmatched vertex on the remaining path. This yields the explicit \(n(n-1)\)-facet model. The geometric fixed-point triangulation uses *complete incidence orbits*, not falsely identified fixed original vertices. The three reflection-axis cases are exhausted by an index table, boundary-orbit obstructions, explicit witnessing facets for every permitted orbit, and a four-sign alternation obstruction that rules out any mixed-type face. The final fixed space is exactly two disjoint simplices, so the PL and Lefschetz consequences follow without any homological concentration assumption.

The standalone verifier agreed between independently generated filtration facets and rooted-path facets for \(n=6,7,8\), checked all \(89\) reflection classes over \(6\le n\le64\), and enumerated \(1{,}988\) nonempty fixed faces in its bounded exhaustive checks. The proof, rather than this finite range, establishes arbitrary \(n\ge6\).

## Originality — PASS, with residual risk
The closest primary article, Knudson--Owens--White, arXiv:2609.06844v1, Sections 3, 4 and 8, defines and computes ordinary homotopy of the pure cycle strong Morse complex. Its Proposition 8.3 already supplies the facet count, which is not claimed as new. The separately inspected published cyclic-rotation character result for the same pure object explicitly excludes reflections. The published full-strong dihedral Euler result treats \(\mathcal{SM}(C_n)\), a different (and generally larger) complex, and cannot be substituted for its pure subcomplex. Chari--Joswig's earlier paper concerns ordinary discrete Morse complexes. Searches using reflection fixed points, orbit faces, equivariant homotopy, pure strong Morse cycles and the exact construction found no statement that implies this PL classification. This is a finite literature comparison, not a proof that equivalent unindexed research does not exist.

## Value — PASS
The calculation answers a natural equivariant question left open by an all-length ordinary homotopy classification: what do **actual fixed spaces** of cycle reflections look like? It gives a complete, axis-sensitive PL result for an infinite family: two components, their full simplex dimensions, and the resulting constant reduced Lefschetz character. These dimensions grow with the cycle and differ between reflection conjugacy classes for even lengths, although their homotopy types agree. This is more geometric information than a Betti-number deduction or a single Euler-character calculation, and it fills the reflection half of an existing virtual dihedral-character calculation. It does not assert a new ambient homotopy type or graded equivariant decomposition.

## Closest literature and limitations
- K. Knudson and A. Owens--White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, especially Proposition 8.3 and Theorem 8.6; primary origin of the object and nonequivariant results.
- *The threefold rotation character of pure strong Morse matching complexes of cycles*, published October 11, 2026; same object but rotation-only.
- *Dihedral Euler characters of full strong Morse complexes of cycles*, published October 11, 2026; different full strong complex.
- M. Chari and M. Joswig, *Discrete Morse Complexes*, arXiv:math/0011234; ordinary, not strong, construction.

Only single-reflection geometric fixed spaces and their virtual reflection traces are determined. Rotational fixed-space homotopy, integral module structures and independent mathematical validation remain open to further checking. Unindexed equivalent literature is a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
