# Research review

## Correctness — PASS

For each labelled state \((c,\ell)\), the center update reduces exactly to the three-case map for even \(n\) and four-case map for odd \(n\), with the leaf update always copying \(c\). The proof analyzes every intermediate-weight boundary, identifies every periodic state, counts all periodic ordered pairs before dividing by temporal orbit size, counts direct preimages of oscillators, and assigns the complement-paired homogeneous basins by conservation of the full \(4^n\)-state space. Sharp three-step witnesses exist at every \(n\ge4\), with separate checks for \(n=2,3\). The analytic proof does not rely on finite extrapolation. The complete-state C++ recurrence check through \(n=10\) and independent Python recurrence check through \(n=8\) agree with every claimed count and first-entry distribution. Residual correctness risk: as with any unformalized handwritten proof, an unnoticed case or transcription error remains possible; the finite checks cannot settle that risk in all orders.

## Originality — PASS, qualified

The classical symmetric-threshold theorem of Goles and Olivos (1980) covers the assertion that eventual periods divide two, not the exact recurrence, basins or uniform entrance cutoff on this graph family. The inspected first-version arXiv full text of Benjamini et al. (2014) studies unimodular and random graphs and does not state the explicit whiskered-clique parity law. Turau (2022) studies trees, covering the four-vertex special member but not the complete-corona family. The nearest published graph-corona research record found was about general-position polynomials, rather than dynamical systems. A previously published parity oscillation law under the aliases whiskered clique, hairy complete graph, or complete-graph corona was not identified by statement-level searches. Unindexed older publications remain a material residual novelty risk, especially since the original 1980 article was available only at the abstract level through the authorized access used.

## Mathematical value — PASS

The family is a natural regular-attachment modification of the complete graph, and oscillatory-basin probability is a natural measure of the prevalence of nonconvergence in finite opinion dynamics. This exact full-orbit classification gives two qualitatively different asymptotic universality classes on consecutive parity subsequences: polynomial \(\sim2/(\pi n)\) oscillation probability at even order versus exponential \(\sim\sqrt{n/\pi}\,2^{-n/2}\) at odd order. It also supplies every individual attractor-basin size and a sharp uniform three-step stabilization-to-periodicity bound. These are structural, nontrivial information beyond the textbook period-at-most-two theorem, rather than isolated small-graph counts.

## Prior literature and limitations

Closest primary works: Goles–Olivos (1980), DOI `10.1016/0012-365X(80)90121-1`; Benjamini et al. (2014), arXiv:1405.2486v1; Turau (2022), arXiv:2202.01580v1. The original 1980 full text was inaccessible, and historical alias coverage may be incomplete. Exact theorem only for one leaf at each complete-graph vertex, binary synchronous neighbor-majority with inertial tie resolution; no conclusion for other graphs or update rules.

Self-review: passed. Independent audit: not yet performed.
