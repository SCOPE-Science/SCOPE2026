# Scientific assessment

## Correctness — PASS

The graph, clock normalization, starting state, and coverage stopping time are explicit. The one-excursion packet law is obtained by the elementary two-leaf hitting process. Inclusion-exclusion gives the exact finite distribution; independent Poisson splitting gives the product CDF. The second-order Gumbel expansion follows from a fixed-parameter logarithmic expansion, and Poisson concentration transfers its coefficient to discrete excursions at an error smaller than \(n^{-1/3}\). Concentration of geometric excursion lengths transfers the same coefficient to discrete random-walk steps. A dominated-convergence argument, with an exponentially small far-tail bound, proves the integrated correction for the mean. The exact mean identity follows from Wald's identity and the strong Markov property. Independent small-state recurrences, direct finite-state Markov solves, and large-size numerical values passed 137 checks. Numerical checks are not treated as infinite proof.

## Originality — PASS, subject to historical priority

The 2009 graph-general cover-time inclusion-exclusion theorem already encompasses exact finite-graph distributions in principle, so the mere existence of an exact CDF is not claimed as new. Multiple-arrival coupon-collection formulas cover broad finite expectations; one-at-a-time heterogeneous coupon-group Gumbel laws are also known. The 2023 source on sparse-network optimal cover-time scaling addresses first-order \(N\log N\) behavior for other network families. The novel statement assessed here is the sharp **fractional** correction to the distribution and the explicitly integrated \(n^{2/3}\) correction to the expected time for this specific backtracking walk. The closest accessible works do not state or immediately establish that second-order regime. A prior result for non-backtracking walks on petal cycles has a different transition kernel and does not imply this one. Targeted public research-record searches found no covering result; negative search evidence is not a uniqueness certificate. Broader group-coupon asymptotic literature remains a priority risk.

## Value — PASS

Friendship graphs are a natural sparse, highly inhomogeneous family with triangles attached to one hub. Cover-time \(n\log n\) scaling alone does not distinguish the two mechanisms of remaining unvisited vertices. The exact \(n^{-1/3}\) term quantifies the unusually persistent unentered-triangle mode, while the derived mean correction provides a statistically meaningful observable one order below the leading term. The statement is a mathematically motivated second-order law, not an arbitrary fixed-size calculation or mere substitution of constants.

## Boundaries

The claims apply to non-lazy simple walks started at the common hub and fixed centered \(x\). They do not include other petal lengths, nonuniform graph weights, or uniform large-deviation expansions. Historical priority is not independently settled, and there has been no independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
