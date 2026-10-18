# Scientific review

## Correctness — PASS

For rooted Yule leaf-splitting trees, uniform root-split sizes and conditional independence give an exact total-covariance recurrence. The only differences between the cherry expectation and its bulk linear law occur at the one- and two-leaf subtree sizes; their contributions produce the harmonic forcing term, which telescopes against the covariance recurrence to yield \(\operatorname{Cov}(C_n,S_n)=-n/9+2/[3(n-1)]\). Small-size boundaries were checked explicitly. A separate total-variance recurrence establishes the cherry variance needed for the regression slope; the published exact Sackin variance independently gives the correlation rate. The included Python checker passed 754 exact-rational assertions, including exhaustive independent leaf-splitting-history enumeration through nine leaves and a separate recurrence verification through 120 leaves. The analytic induction, rather than finite testing, establishes the statement for all admissible sizes.

## Originality — PASS on inspected evidence

The closest papers calculate Yule cherry/pitchfork distributions (Choi, Thompson and Wu, arXiv:2002.12643), Sackin variances and Sackin–cophenetic covariances (Cardona, Mir and Rosselló, arXiv:1202.6573), and model-specific empirical associations among tree metrics (Janzen and Etienne, DOI:10.1016/j.ympev.2024.108168). Inspection found neither the exact cherry–Sackin cross-moment nor a previously evaluated equivalent or stronger formula. The generic recursive-index variance framework of Cardona and colleagues could be adapted through polarization, but does not state or evaluate the present joint moment. The similarly denoted Colless index in that work is not a cherry count. Checked records of other tree ensembles concern different probability measures or observables. The strongest residual risk is an unlocated earlier specialization of a general tree-index moment method; independent bibliographic verification remains outstanding.

## Value — PASS

Cherries are a local two-tip clade statistic, whereas the Sackin index measures aggregate root-to-tip depth. An exact finite-size relation between these widely used but differently motivated phylogenetic summaries supplies a reference calibration under the Yule neutral model, rather than only marginal expectations or numerical correlations. The persistent negative covariance of linear magnitude, exact optimal linear prediction slope, and vanishing Pearson correlation with explicit scaling distinguish dependence at different normalizations. This is a substantive joint-statistic question motivated by comparative phylogenetics, not an arbitrary slice of parameter space.

## Limits

Results apply only to the specified rooted Yule law and combinatorial edge depths, not to uniformly sampled/PDA tree topologies, branch-time distances, or arbitrary empirical trees. The displayed correlation combines the newly computed covariance with previously known marginal variance formulas. No full joint distribution, asymptotic joint normality, independent certification, or bibliographic priority beyond inspected evidence is asserted.

Self-review: passed. Independent audit: not yet performed.
