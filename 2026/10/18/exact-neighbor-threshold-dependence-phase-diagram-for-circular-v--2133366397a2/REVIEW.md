# Scientific review

## Correctness — PASS

Every gap is a Dirichlet(1) coordinate, and each cell length is half a sum of two neighboring gaps. The single-cell \(\operatorname{Beta}(2,n-2)\) survival and the two distinct two-cell integrations are explicitly derived. The adjacent sign theorem uses exact low-dimensional factorizations and a strict, all-real-threshold derivative inequality for all larger dimensions. Nonadjacent negativity follows by conditioning on one disjoint Beta sum. The two asymptotic expressions are separately obtained from Taylor expansions. A standard-library checker independently performs exact polynomial integrations and finite sign tests. No computation is treated as a substitute for the infinite proof.

## Originality — PASS, subject to residual historical risk

The closest full primary texts inspected were Gabrielli–Torquato (2004, Sections IV–V, an independently shuffled lattice) and Devroye–Györfi–Lugosi–Walk (2015, Sections 1–3 and the proof sections, one-cell Voronoi asymptotics). These do not give the finite iid-circular pair-indicator sign classification. Literature-index searches for neighboring circular Voronoi cell exceedances, overlapping Dirichlet sums, parameter thresholds, and both arXiv source identifiers returned no dominating statement among inspected closest results. Earlier related results on uniform-spacing exceedance counts and circular nearest-neighbor networks do not contain the same overlapping two-gap cell-indicator assertion. Generic beta aggregation explains the formulas but does not itself supply the all-size strict-sign and exceptional-zero proof. The major residual risk is an older exact joint distribution for iid circular Voronoi cells outside the material inspected.

## Mathematical value — PASS

The result provides a full, sharp threshold-dependence sign diagram for a natural fixed-cardinality stochastic tessellation: its entire adjacent/nonadjacent dichotomy, the surprising four-site independence point, and the different local-limit scales. It distinguishes nonlinearly dependent indicators even where the raw neighboring cell lengths have zero covariance. This matters when counting clusters of unusually large Voronoi cells in geometric sampling null models, and is not merely the computation of an arbitrarily selected moment.

## Closest literature and limitations

Gabrielli–Torquato, arXiv:cond-mat/0405115, proves a shuffled-lattice two-cell law under a different underlying point process. Devroye and coauthors, arXiv:1512.04267, study marginal typical-cell asymptotics, including dimension one. The classification here is restricted to finite iid uniform samples on a circle and equal thresholds. It does not establish a general positive-association property for cell lengths or address unequal thresholds and higher-dimensional models.

Self-review: passed. Independent audit: not yet performed.
