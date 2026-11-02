# Scientific review: second-order locality breaking in many-walker cover times

## Correctness

PASS. The stated general finite-chain result has a complete analytic derivation. Its critical steps are (i) expansion of the first-hit probability through degree \(d+1\), including the correct pre-hit holding-time contribution and all first-hit paths of length \(d+1\); (ii) inclusion-exclusion for the farthest-target cover; (iii) the \(d\geq2\) separation of the quadratic logarithm term from the \(N^{-1/d}\) correction; (iv) a quantitative near-target bound that is little-oh of the proposed correction after integrating any fixed positive moment; and (v) the pendant-leaf path comparison. The exact coefficient checker passed 6,807 rational comparisons on enumerated and weighted finite chains. A separate deterministic numerical quadrature matches the predicted coefficients in the explicit nontrivial two-target example. Those checks do not substitute for the analytic proof.

## Originality

PASS, subject to historical-priority risk. The central comparison is Kim–Lawley (arXiv:2310.07905, first posted 2023-10-11), which proves the leading moments for the same cover-time observable but does not give the displayed next coefficient or the positive pendant-edge response. The antecedent Lawley (arXiv:2008.04496, first posted 2020-08-11) proves leading extreme first-passage distributions/moments and gives the killed-generator survival representation, but not this cover-time expansion. These distinctions concern mathematical implications, not differences in terminology. Standard second-order extreme-value asymptotics may provide an abstract route to the analytic expansion; comprehensive historical exclusivity has not been proved. The intended scientific contribution is the explicit network path/holding-rate coefficient, near-target suppression at that order, and off-geodesic structural response.

## Value

PASS. The motivating cover-time work emphasizes independence of the leading coefficient from network alterations away from geodesic paths. Determining the first order where that independence fails addresses a natural sensitivity question: the same shortest-route network can have different large-population search times at the next sharp scale. The two-target pendant example gives explicit different \(N^{-1}\) corrections, and the general corollary proves a strictly positive response for any geodesic pendant attachment in the unique-farthest-target case. This is more than a routine substitution of parameters or a small numerical refinement.

## Limitations and closest prior literature

The result assumes a fixed finite irreducible continuous-time Markov chain and distance \(d\geq2\); it neither treats the boundary case \(d=1\) nor proves corrections under target growth or infinite-state limits. The finite checks are diagnostics, while all infinite claims rest on the written proof. The two closest original sources are Kim–Lawley (2023/2024) and Lawley (2020), both inspected in accessible full-text form in relevant theorem and method sections. General second-order phase-type or extreme-value results not found in the targeted searches remain a historical priority risk. No independent mathematical validation has occurred.

Self-review: passed. Independent audit: not yet performed.
