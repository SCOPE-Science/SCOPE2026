# Review of the complete three-exchange blocking-set metric

## Correctness — PASS
The finite domain consists of exactly 21 projective points and 21 lines over the explicitly tabulated four-element field. The incidence verifier enumerates every candidate of cardinality at most seven, proves no smaller nontrivial blocker exists, and obtains all 360 seven-point blockers. A separate verifier independently constructs all Fano subplanes by completing projective quadrangles; both obtain the same exact ordered incidence certificate hash `e569b1b4979da37812f549b11900b52f0981e899e280688543b6626cca930d96`. Each verifier builds every edge and exhaustively traverses all 360 breadth-first layers from each vertex. Both find degree 56, 10080 edges and layers (1,56,287,16); every unordered pair satisfies the exact intersection/distance histogram. The proof is exhaustive on the specified finite plane, and no small-case induction or asymptotic claim is made.

## Originality — PASS, with identified residual risk
The 360-subplane count and intersection numbers are well documented and explicitly excluded from the novelty claim (Brouwer–Haemers and van Lint). The new asserted claim is the *full graph metric for size-four intersection adjacency on all 360 subplanes*, including the first allowed exchange threshold and the disjoint-antipode characterization. Gottschalk's 2000 paper instead constructs a graph on one projective-linear-group orbit, with intersection-*one* adjacency (public abstract). The nearest blocking-set classifications describe sets, not the complete all-pairs optimal-solution reconfiguration metric in their available text. Searches also compared semantically equivalent point swaps, Baer-plane intersection graphs, and finite-geometry databases. The full Gottschalk paper was not accessible and might contain further implications; publication priority cannot be independently certified.

## Value — PASS
Minimum blocking sets are a canonical sharp covering problem in finite geometry, and the smallest allowable local edit is a natural stability/reconfiguration invariant. While the intersection histogram is classical, it does not determine whether repeated three-point replacements connect every optimum, their shortest-path diameter, or which pairs attain it. The exact uniform three-step theorem and geometric characterization of antipodes fill that mathematically motivated finite gap without choosing an arbitrary slice of a large parameter table. The claim does not rely on an unproved broader theorem.

## Limits
No extension to general orders, to other exchange definitions, or to dynamics and mixing is claimed. Publisher full-text restrictions leave a documented literature-overlap risk; independently audited status has not been asserted.

Self-review: passed. Independent audit: not yet performed.
