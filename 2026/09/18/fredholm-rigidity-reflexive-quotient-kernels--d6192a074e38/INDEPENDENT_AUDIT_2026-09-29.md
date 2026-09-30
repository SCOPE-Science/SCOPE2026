# Independent Audit — 2026/09/18/fredholm-rigidity-reflexive-quotient-kernels--d6192a074e38

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `6b3f30afefaa2d90feb431db71c191f5a198c8fb`
- Disposition: **PASSED**

## Correctness

**PASS** — The finite-defect reduction is valid. A Fredholm map U:M->N splits to an isomorphism U_0:M_0->R after removing its finite-dimensional kernel and finite-codimensional cokernel. Then l_infinity/M_0 and l_infinity/R are finite-dimensional extensions of the given infinite-dimensional reflexive quotients, hence are again infinite-dimensional reflexive. The Lindenstrauss-Rosenthal extension theorem therefore gives a Fredholm extension of U_0 to l_infinity. Its induced map on the reduced quotients is Fredholm, and the canonical maps between reduced and original quotients are Fredholm as well. Composition yields the claimed Fredholm equivalence of l_infinity/M and l_infinity/N. The contrapositive strengthens the current González-Kania kernel family from pairwise nonisomorphism to pairwise Fredholm inequivalence.

## Originality

**PASS** — The 2026 González-Kania article explicitly proves only that pairwise Fredholm-inequivalent reflexive quotients produce pairwise nonisomorphic kernels, applying Lindenstrauss-Rosenthal to an isomorphism of kernels. The classical extension theorem itself likewise starts from an isomorphism. Searches for the stable version with a Fredholm map between kernels did not locate the submitted transfer statement. The novelty is narrow—a finite-dimensional stabilization of a classical argument—but the exact strengthened implication was not found in the sources checked.

## Scientific value

**PASS** — Fredholm equivalence is the natural finite-dimensional-stable relation already used to distinguish the quotient spaces in the motivating paper. Showing that the same maximal family of kernels is separated by this stronger relation upgrades the conclusion in a conceptually aligned way and supplies a reusable stable form of the Lindenstrauss-Rosenthal transfer argument.

## Sources

- Grothendieck and ℓ∞-Grothendieck Subspaces of ℓ∞ (Manuel González; Tomasz Kania): https://onlinelibrary.wiley.com/doi/10.1002/mana.70255 — Current article states the Lindenstrauss-Rosenthal Fredholm-extension theorem and Proposition 2.2 transferring quotient Fredholm inequivalence only to kernel nonisomorphism.
- Automorphisms in c0, l1 and m (Joram Lindenstrauss; Haskell P. Rosenthal): https://doi.org/10.1007/BF02787616 — Classical source of the extension theorem used in the reduction.

## Limitations

- The originality is a stable finite-dimensional refinement of a classical theorem, not a new extension method.
- The original 1969 paper was not needed for theorem-text verification because the current González-Kania article quotes the precise reflexive-quotient Fredholm-extension statement used here.
- The argument is specific to the l_infinity extension theorem and does not assert an analogous transfer in arbitrary ambient Banach spaces.

GitHub was read only as evidence; no repository mutation was performed. The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. Open-access/preprint material was checked before other sources; no Oxford Download was needed for this record.
