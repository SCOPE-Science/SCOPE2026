# Scientific review: sharp tree-vaccination switch

## Correctness — PASS

The exact outbreak expectation is the ordered-pair connectivity sum, equal to \(1+2S_v(p)/(n-1)\). The low-order claim follows from an exhaustive, independently reconstructible Prüfer-code sweep, with every putative universal minimizer confirmed by nonnegative degree-five Bernstein coefficients: the certificates prove inequalities for the whole interval, not only a sampled grid. The eight-vertex profiles are explicit and imply \(S_3-S_0=p(1-p^2-p^3)\), while every other vertex is strictly inferior to vertex 3. For every larger order, a degree argument determines the low-transmission optimizer and an exact component-pair comparison determines that this vertex loses near unit transmissibility. The supplied checker has been executed from its packaged source path. Limit: finite enumeration is used only for the finite \(n\le7\) part; arbitrary-order cases have a separate algebraic proof.

## Originality — PASS, with explicit risk

The underlying independent-edge epidemic/percolation model, pair-connectivity expectations, degree-driven low-transmission behavior, and fragmentation-driven high-transmission behavior are established; none is claimed as new. In Chen et al.'s 2006 paper, node-removal fragmentation is studied for large random and scale-free networks, without a sharp all-tree uniform-optimum threshold. Holme's fully inspected 2017 small-network paper studies the same vaccination question under a different continuous-time SIR process, and its highlighted smallest examples concern disagreements across different node-importance objectives, not the existence of a single optimum for all independent-edge transmission probabilities on every tree with at most seven vertices. Bucur–Holme 2019 considers outbreak size conditioned on the initial source, not this deletion optimization. The exact eight-vertex certificate and the \(n\ge8\) spider family are not implications of these inspected statements. Literature indexing is incomplete, and the full text of Holme 2004 could not be accessed; an unindexed distance-polynomial or vaccination theorem remains a residual risk.

## Value — PASS

Choice of a single vaccination target is a natural finite optimization problem; stability under uncertain transmissibility matters for whether one fixed target remains optimal. The theorem settles the first tree order at which transmissibility alters the optimum, identifies the exact switching parameter and all competing vertices at that order, and supplies a family making the effect unavoidable at every greater tree order. This is a motivated sharp classification, not a routine numerical special case. Its conclusion is limited to trees, independent identical edge transmission, uniform post-vaccination seeding, and mean final outbreak size.

Self-review: passed. Independent audit: not yet performed.
