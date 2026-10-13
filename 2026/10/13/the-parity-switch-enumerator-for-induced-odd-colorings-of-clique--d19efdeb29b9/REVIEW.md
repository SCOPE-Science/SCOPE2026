# Scientific review: induced-odd colorings of clique coronas

## Correctness — PASS

The finite simple graph domain, named colors and empty-color conventions are explicit. In a rooted complete clique, any non-root color must appear an even number of times to give its private vertices odd monochromatic degree; the root color must be absent or appear an odd number of times. Total private-clique parity therefore forces exactly one case for each parity of the clique size. This is equivalent, root by root, to even-colored or odd-colored induced base neighborhoods, with independent choices counted by the stated factorial coefficient. The chromatic-number consequences follow from positivity of those factors, Gallai's two-even-partition theorem, and the impossibility of a single color on an odd-order clique. The \(\mathbf F_2\) equation for binary even coloring is proved and its solution number obtained by elementary orthogonality. This reconstructs the infinite proof without extrapolating from tests. The supplied direct verifier checks 4,467,792 complete assignments over 99 small corona instances and 1,099 base graphs for one- and two-color boundaries. No unproved combinatorial lemma is silently inferred from those samples.

## Originality — PASS

Belmonte and Sau (arXiv:2002.06078, first posted 14 February 2020) already prove a general binary-equations approach to deciding whether a graph has an odd induced two-color partition. Gallai already supplies two even parts, and Scott's large subdivided-clique examples are established. These pieces are acknowledged; the claimed addition is the fully enumerated arbitrary-palette clique-corona transfer for both parity regimes. The original papers inspected do not give this coefficient identity, including for even clique attachments when arbitrary base graphs have unbounded odd chromatic number. The nearest same-title corona article (Mounisha et al., 2026) concerns the different proper neighborhood-parity odd chromatic number, so its corona values do not imply the statement here. The nearest indexed same-sounding records also concern proper neighborhood-parity coloring or other graph parameters. Residual risk: unindexed theses, adjacent enumerative formulations or later papers not retrieved might contain equivalent information. No absence claim is treated as a proof of global novelty.

## Value — PASS

The complete counting identity transfers the entire feasible labeled coloring distribution on every clique corona to intrinsic even/odd coloring functions on the arbitrary base graph. It determines the chromatic number exactly for all base graphs, disconnected cases included, and gives an exact two-color count involving binary Laplacian nullity for odd clique sizes. Its parity switch is substantive: for a family of subdivided cliques of unbounded original induced-odd chromatic number, switching the parity of the attached clique changes the new invariant between a constant and that unbounded value. This addresses natural behavior under a standard graph product, not an arbitrarily selected small example or a restatement of a single earlier scalar bound.

## Closest literature and limits

The 2020 paper's \(\mathbf F_2\) approach and Gallai's even-partition theorem supply prior conceptual tools. The 2023 preprint/2025 journal study describes high-chromatic subdivided cliques and general graph classes. The 2026 corona paper is excluded by a different invariant, not merely by a name mismatch. No proof of efficient unrestricted computation of the two base enumerators is asserted. Numerical tests are supplementary evidence. The research does not claim to have completed an external audit.

Self-review: passed. Independent audit: not yet performed.
