# Scientific review

## Correctness: PASS

The objective is the unordered-pair Kirchhoff index with nonnegative independent edge conductances and positive linear costs. Strict convexity of the Laplacian inverse-trace objective establishes uniqueness and justifies exact symmetrization. Articulation-point resistance additivity yields the two-term formula for each heterogeneous clique blade. A one-variable derivative proves the unique local support phase, including the equality and closure boundaries. Finally, a sharp Cauchy–Schwarz inequality yields the global allocation and the exact minimum; all quantifiers and normalization factors are explicit. The standalone checker passed 480 assertions based in part on independently inverted exact-rational grounded Laplacians. Numerical checks do not replace the proof.

## Originality: PASS, with residual risk

The 2008 Ghosh–Boyd–Saberi full text gives general convexity, symmetry and wheel/barbell examples, not this heterogeneous bouquet classification. The 2014 Nikseresht–Sepasdar full text gives block resistance identities but no conductance-budget optimizer. The 2026 Tovar et al. study gives a general cost/edge KKT threshold and a three-vertex triangle example, not independent heterogeneous blade activation and a coupled exact allocation. A pre-existing equal-size, common-price windmill formula already includes the uniform threshold; that special case is excluded from the new contribution. The assessed new portion is the heterogeneous formula, arbitrary mixed support patterns and square-root budget split. A related 2024 windmill-index article was available only at abstract level; a complete historical equivalence search is not guaranteed.

## Value: PASS

All-pairs resistance minimization is a classical resource-allocation criterion, but its exact support selection is typically implicit in a convex program. Here one can decide, independently for every differently sized and priced blade, whether an entire set of redundant links should receive zero conductance. The shared threshold depends on total network size rather than individual blade size; the exact per-blade spending rule then completes a physically interpretable, implementable heterogeneous design without numerical optimization. This is not an arbitrary parameter slice: it settles the natural class of one-point unions of differently sized cliques with the two physical edge-price classes of each blade.

The conclusion is limited to the stated topology and objective. Scientific independence, independent validation and exhaustive historical coverage are not asserted.

Self-review: passed. Independent audit: not yet performed.
