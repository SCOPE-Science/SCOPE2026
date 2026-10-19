# Scientific review: Sharp six- and fourteen-site positivity transitions for fourth-order Gauss steps on cycles

## Correctness — PASS

For all finite cycle sizes, the method matrix exists and conserves row sums because its scalar denominator is positive on the negative real axis and the constant mode is fixed. The small-step classification follows from Padé coefficients through degree seven and an exact graph-distance walk count, including the zero degree-six coefficient. Positivity for three through five sites and the exact six-site quartic frontier follow by independently checked rational expressions. The large-step classification follows from the explicit cycle Laplacian pseudoinverse kernel, with quantifiers taken at each fixed graph size. The iterated-limit fraction follows from a quadratic distance inequality with only a bounded number of equality positions. The standalone artifact reproduces 438 exact assertions. Its finite verification is corroborative, not a substitute for those proofs.

## Originality — PASS, with residual risk

The zero absolute-monotonicity radius for the fourth-order [2/2] Padé map is established by Lóczi and Ketcheson (arXiv:1303.6651, 2013), and Zappavigna and collaborators (2012) already exhibit positivity loss with eight-state Metzler/nilpotent systems. A published finite-state Markov result identifies eight as the smallest dimension of small-step positivity loss among arbitrary conservative chains, but its witness is a directed pure-birth chain. Accessible same-topic historical results include an exact path-graph small-step cutoff at eight vertices and an unconditional-positivity theorem for complete multipartite graphs, neither of which contains cycle-specific fourteen-vertex and six-vertex size boundaries. Comparison of theorem statements, not only wording, did not reveal exact coverage of the present undirected-cycle classification, explicit six-cycle positive-step set, or large-step spatial sign density. As an inherent limitation of literature search, equivalent unindexed or differently parameterized specialization remains possible. These comparisons are not independent validation.

## Value — PASS

The complete size trichotomy distinguishes unconditional positivity, small-step-only positivity, and immediate small-step failure on the natural periodic-diffusion discretizations, whose shortest positive path exhibits different behavior from a line segment. The six-cycle positivity interval is sharp, and the irrational spatial sign-density law describes a macroscopic large-step failure pattern. These are useful exact structural boundaries for fourth-order time stepping, rather than a routine finite numerical example. The theorem does not assert the complete intermediate-step positivity regions for larger cycles.

## Closest work and limitations

Lóczi–Ketcheson gives a method-level uniform obstruction; Zappavigna et al. and the published eight-state Markov result supply unrestricted-system witnesses; neither derives the undirected-cycle thresholds. Path and complete-multipartite graph results in accessible historical research concern different graph classes and hence do not imply this theorem. The use of a single specific rational method and unit undirected cycles is deliberate; no result is claimed for irregular edge weights, other Padé orders, directed rings, or internal stages.

Self-review: passed. Independent audit: not yet performed.
