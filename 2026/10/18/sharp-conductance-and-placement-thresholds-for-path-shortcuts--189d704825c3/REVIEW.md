# Scientific review of shortcut-conductance saturation on paths

## Correctness — PASS

The single-link rank-one interlacing ceiling is exactly the path's third-smallest combinatorial-Laplacian eigenvalue, \(2-2\cos(2\pi/n)\). A Rayleigh-quotient test vector eliminates every non-reflection-centered chord. In the surviving reflection-centered case, parity decomposes the spectrum into a positive symmetric sector and an antisymmetric shifted block with exactly one negative eigenvalue. The rank-one Schur-complement inertia criterion reduces saturation to one resolvent quadratic form, computed explicitly using the path's discrete cosine solutions and a sine continuation at the source vertex. The result is \(-\sin((2i+1)2\pi/n)/\sin(2\pi/n)\), giving the necessary-and-sufficient threshold. Maximizing the sine over admissible odd indices gives the exact minimum conductance and the complete unit-weight optimizer count. The all-order proof includes both strict and equality boundaries. The accompanying finite numerical checker reproduced 6,611 tests, but the checker alone would not establish the theorem.

## Originality — PASS, with stated access risk

A. Ghosh and S. Boyd (2006), *Growing Well-connected Graphs*, supply the general link-addition optimization framework and secular bounds but do not state or imply the exact path-specific equality and conductance threshold from their inspected arguments; their paper uses heuristics and examples rather than the reflection-resolvent classification. S. M. Fallat, S. Kirkland and S. Pati (2003), *Maximizing Algebraic Connectivity Over Unicyclic Graphs*, investigate maximization over unrestricted unicyclic graphs with fixed girth, rather than the positive-conductance saturation threshold after adjoining one link to a fixed path. Their accessible abstract and the full-text 2011 secondary exposition were inspected; their 2003 full text could not be obtained, so an unrecognized stronger implication remains a genuine risk. W. C. Shiu, J.-M. Guo and J. Li (2011) prove a minimum-connectivity result for caterpillar unicyclic graphs, not the present maximum of a weighted one-link path augmentation. Equivalent-formulation searches for weighted rank-one perturbations, chorded paths, Fiedler optimization and saturation found no covering claim in inspected sources or available research records. Non-detection is not a proof of novelty.

## Value — PASS

The question is a motivated network-design optimization: how strong must a *single* additional link be for a path consensus system to reach the strongest algebraic connectivity that any rank-one increase can permit? The theorem gives the exact minimal conductance, all equalities at every conductance above it, all unit-cost optima, and the asymptotic \(2\pi/n\) physical strength scaling. Those structural outcomes are not supplied by the generic rank-one interlacing ceiling and specify an unusual family of equally efficient, not necessarily end-to-end connections. The lower-conductance optimization problem is intentionally left open.

## Sources and limitations

Relevant inspected primary full texts: Ghosh–Boyd (2006), https://stanford.edu/~boyd/papers/pdf/growing_fast_graphs.pdf ; Shiu–Guo–Li (2011), https://journals.uwyo.edu/index.php/ela/article/download/957/957/957 . The most significant incomplete comparison is Fallat–Kirkland–Pati (2003), DOI 10.1080/0308108031000069182, whose publisher abstract was accessible but whose complete paper was not. The mathematical statement is restricted to one positive-weight shortcut on a unit-weight undirected path. The demonstration is not an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
