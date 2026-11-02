# Scientific review

## Correctness — PASS

The exact one-point-extension type recursion is justified by induction on the number of rounds of the ordinary Ehrenfeucht–Fraïssé game. Both source checkers exhaustively evaluate rank-three and rank-four types on every squared cycle of orders 3 through 24 and compare the complete partitions; they use distinct tuple encodings and integer representations. The separate cyclic-gap Duplicator strategy proves that all sizes at least 12 are rank-three equivalent and all sizes at least 24 are rank-four equivalent. The finite bridge establishes equivalence of 11 with 12 and 19 with 24, so transitivity gives the claimed all-size sharp thresholds. The final adjacency check distinguishes gaps of 0, 1, and at least 2 unselected vertices, correctly handling two-step graph distances. The theorem is not an unproved numerical extrapolation. Independent scientific review is still outstanding.

## Originality — PASS under the inspected literature

Brown and Hoshino (2007) classify ordinary undirected cycles and paths in the same logical game; their degree-two ordinary cycles are not the degree-four squared cycles classified here. Their results plus the first-order definition of squared-cycle adjacency give possible nonsharp eventual bounds but not the asserted sharp rank-three and rank-four partitions. Hng (2019) investigates extremal minimum-degree conditions for powers of cycles, a different invariant. Fagin, Lenchner, Regan, and Vyas (2021) study ordinary EF versus multi-structural games and logical quantifier resources, primarily for linear orders, not these exact cyclic graph-power spectra. Comparisons with accessible published results and related terminology (circulants and four-regular ring lattices) found no covering claim. Historical-priority uncertainty remains, especially in unpublished or differently indexed graph-model-theory work; no absolute novelty certification is asserted.

## Mathematical value — PASS

The result identifies exact finite-model-theoretic distinguishing thresholds for a canonical and structurally natural graph-power family, including a genuine discontinuity between third and fourth logical ranks. It separates the universal large-structure EF strategy from the finite exceptional spectrum, determining all equivalence classes rather than only a computational sample. This fills a substantive logical gap in the study of graph powers; it does not claim to characterize higher ranks or minimum total quantifier count.

## Closest work and limitations

Sources inspected: J. Brown and R. Hoshino, *The Ehrenfeucht–Fraïssé Game for Paths and Cycles*, *Ars Combinatoria* 83 (2007), 193–212; R. Fagin et al., *Multi-Structural Games and Number of Quantifiers*, arXiv:2104.14709 (first publicly available 2021); E. K. Hng, *Minimum degree conditions for powers of cycles and paths*, *Acta Mathematica Universitatis Comenianae* 88 (2019), 795–800. Hng was assessed from the publisher abstract and metadata only because full-text access was not confirmed. The theorem does not address quantifier ranks other than three and four or claim unique historical priority. Verification source files are provided, but independent audit is unperformed.

Self-review: passed. Independent audit: not yet performed.
