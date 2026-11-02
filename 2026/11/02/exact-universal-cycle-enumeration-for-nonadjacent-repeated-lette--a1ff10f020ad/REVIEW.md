# Scientific review

## Correctness — PASS

The three-edge overlap description accounts for every allowed four-letter word exactly once. Strong connectivity is established by a rotation, a reversible transposition route, and single-letter support changes. The Schur-complement identity is derived from the order-three rotation matrix; its pair-space decomposition has verified dimensions and explicit eigenfactors. The directed matrix-tree theorem supplies the rooted arborescence count, and the fixed-edge BEST formula removes cyclic-rotation ambiguity. Exact Laplacian cofactors agree at alphabet sizes \(3,4,5\); direct tour enumeration agrees at \(3\). Boundary \(q=3\) is treated separately so no negative factorial occurs. There are no probabilistic, asymptotic, or unproved infinite steps.

## Originality — PASS, qualified

Gardner–Godbole (arXiv:1711.07029v1, pp. 1–4 and augmented-onto theorems) and Leitner–Godbole (arXiv:0808.1309, introduction and Theorem 5) establish existence for different, broader word classes, not exact counts on this three-pattern subclass. Chen–Kitaev–Sun (arXiv:1908.01116v1, abstract and §§1–2) study random removals and binary small cases, not the stated all-alphabet count. Searches for the three literal templates, nonadjacent repeated pairs, restricted de Bruijn Euler-tour enumeration, and the exact small-alphabet count did not identify a covering result. Related adjacent-repeat and two-symbol four-letter languages are disjoint, so their enumerations do not imply this result. Residual risk: a differently indexed or titled exact enumeration may exist; absence from search results is not a uniqueness proof.

## Mathematical value — PASS

The permitted length-four factors form a natural, sharply specified complement to the adjacent-repeat case within three-symbol words. The theorem establishes existence and exact labeled-cycle counts for an entire infinite alphabet family, not merely a finite census or an existence corollary. The explicit decomposition exposes a reusable spectral structure of an induced de Bruijn subgraph. It also detects a small-alphabet boundary where the corresponding adjacent-repeat family has different behavior.

## Limitations

The formula is for rotation classes alone; it is not an orbit count under reversal or relabeling. Independent verification has not been performed, and published literature retrieval may be incomplete. The included program checks finite instances but the infinite statement depends on the proof.

Self-review: passed. Independent audit: not yet performed.
