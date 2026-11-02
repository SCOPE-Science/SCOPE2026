# Self-review

## Correctness — PASS

The generator calculation is explicit and permits arbitrary hyperedge sizes and weights: a uniformly sampled donor gives conditional count variance equal to the number of disagreeing pairs in the ringing group, hence \(\mathcal L H(s)=-\sum_{i<j}w_{ij}\mathbf 1\{s_i\ne s_j\}\). The all-start exponential identity is equivalent to equal weighted pair-codegrees, by singleton and doubleton cut tests. Positive common rate yields a.s. consensus, exact moment formulas and two-sided tail/time bounds. The Fano and complete-graph absorption times follow from exact transient class generators; the included code checks every state and the rational equations. Finite checks corroborate, but are not used as the proof of the all-size characterization.

## Originality — PASS, with residual bibliographic uncertainty

Golovin, Mölter and Kuehn (arXiv:2308.03640, publicly posted 2023-08-07) describe the simultaneous proportional-copy update and analyze expected magnetization and adaptation. First-moment conservation does not imply this second-moment iff theorem or the differing exact Fano/K7 mean times. Papanikolaou et al. (arXiv:2201.06421) study majority/rewiring effects; Kim et al. (arXiv:2407.11261) study group-driven focal-node updates; Llabrés et al. (arXiv:2601.05169) explicitly distinguish their single-node pairwise reduction from simultaneous hyperedge updates. Semantic searches under pair codegrees, balanced incidence designs, disagreement decay, Fano-plane hitting times and group-copy consensus found no result implying the combined claim. An equivalent unindexed result remains possible; absence in search is not proof of priority.

## Mathematical value — PASS

The criterion characterizes the exact boundary of universally exponential expected binary disagreement for simultaneous group copying. The smallest classical projective-plane design gives a concrete limit to two-body moment reduction: equal pairwise incidence produces identical first two population moments at every time but not equal absorption time. This distinguishes moment closure from full stochastic equivalence in a natural social-dynamics process.

## Scope and limitations

Only finite static hypergraphs, neutral binary states, independent positive-rate edge clocks, and uniformly sampled donors copying to every group member are covered. Mean-time computations refer to fixed seven-vertex examples, not arbitrary group designs. No global novelty guarantee is made.

Self-review: passed. Independent audit: not yet performed.
