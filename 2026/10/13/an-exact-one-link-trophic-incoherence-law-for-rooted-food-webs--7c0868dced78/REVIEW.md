# Self-review

## Correctness — PASS
The classical unweighted trophic level and standard-deviation normalization are fixed explicitly, including the unique basal root, the one-new-edge constraint, and the prohibition against making that root nonbasal. Both exhaustive cases follow from the level equation at the sole indegree-two vertex: either the new source is outside the target's shifted descendant subtree, or it is inside and forms one directed cycle. In each case only two arc differences depart from one; their deviations are opposite. The proof yields the asserted depth formulas and sharp lower bounds for every finite rooted tree. Counting sources at the preceding depth proves the zero-cost enumeration without assumptions about branch sizes. The independent exact-rational linear-system verifier checked 40,322 modifications across 1,740 rooted-tree instances and returned `VERIFY_OK`.

Risk: weighted or differently normalized trophic measures do not obey the claimed expressions. The proof, not the finite test, is the all-orders certificate.

## Originality — PASS
The foundational 2014 full article material establishes classical trophic level and incoherence definitions, the 2015/2017 full article develops a statistical coherence ensemble and cycle predictions, and the 2020 full article introduces a different symmetric-Laplacian definition. These do not present a closed one-edge rooted-arborescence perturbation law, the universal feedback cost, or the full zero-cost-link count. Searches for arborescence, rooted food-web tree, trophic shortcut, added feedback link, and equivalent depth-difference formulas did not locate the same statement. Published mathematical records and relevant previous claims were compared by scientific implication.

Risk: the two-case formulas are elementary once the special one-indegree-two structure is identified, so an unindexed teaching note or supplementary worked example could contain them; failure of search alone cannot establish novelty.

## Value — PASS
Trophic coherence is a published structural index for food-web stability and feedback studies. Adding predation edges is a natural mechanism in food-web construction. The theorem supplies a reusable local response law without recomputing a network-wide linear system, sharply distinguishes feedback cycles from acyclic omnivory and across-branch links, and counts every exactly coherence-preserving new link from the layer profile alone. The quadratic feedback penalty is independent of remote branching, a structural fact useful as an analytic calibration of this ecological statistic.

The claim does not elevate trophic coherence to a stability theorem; the model assumes equal prey weights and one link modification.

Self-review: passed. Independent audit: not yet performed.
