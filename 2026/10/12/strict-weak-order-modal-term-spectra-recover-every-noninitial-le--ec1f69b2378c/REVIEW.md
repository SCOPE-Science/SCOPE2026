# Self-review: Strict weak-order modal term spectra recover every noninitial level width

## Correctness — PASS

The domain and quantifiers are finite nonempty ordinal sums of antichains with **strict** later-level accessibility; all arities including \\(r=0\\) are included. The proof establishes that level is detected by path length, that the pair of local color and every later palette is a complete and definable pointed-modal type, and that all Boolean choices on these types are realizable by modal formulas. The resulting count is exact. In the inverse direction, the polynomial factorization and the pairwise distinct alternating-harmonic derivatives recover later widths one by one. Exact-integer and rational tests from `artifacts/verify.py` independently corroborate the stated counts in their specified finite ranges: `VERIFY_OK vectors 56 type_tests 168 pointed_valuation_samples 738094 inverse_polynomials 56 direct_clone_tests 22 direct_term_operations_total 16860 root_invariance_families 5`. No experimental range is used as an infinite proof.

## Originality — PASS with residual risk

The source comparison concerns implication rather than similar vocabulary. Goldblatt (arXiv:1905.11617) treats finite irreflexive/transitive frame logic and complex-algebra generation of varieties, but not the individual algebra's term-operation counts or inverse width recovery. Camerlo–Pistone–Rapallo (arXiv:1712.04191) determine constraints on the **single box operator's range**, which does not supply the full iterative term-clone census. Known finite *reflexive* linear-preorder palette-word spectra concern accessibility within each cluster, and self-reflexive weak-order generator criteria concern a different unary relation and different invariant. No searched exact table or stronger statement establishes this strict-frame result. Residual risk: an unlocated equivalent in older finite modal algebra or bisimulation literature remains possible; absence of a search hit is not proof of absolute priority.

## Mathematical value — PASS

This is an exact natural algebraic invariant for every finite strict weak order in the Gödel–Löb class. The inverse theorem is a complete classification of *which ordered structural parameters are visible*: every later width is recovered in its correct position, while the initial width is provably lost. This resolves a motivated finite-clone reconstruction problem and exhibits a sharp isospectral family, not an arbitrary fixed-size table, a renaming of a known enumeration, or a routine improvement in a constant.

## Relationship to literature and limits

Relevant primary analyses: Goldblatt (2019), full relevant semantic/algebraic sections; Camerlo–Pistone–Rapallo (2017), introductory operator-range theory and closing discussion. General finite modal characteristic formulas are established background and are not claimed as new. A full historic priority audit remains open. The proof does not concern reflexive or multirelational frames or graded modalities.

Self-review: passed. Independent audit: not yet performed.
