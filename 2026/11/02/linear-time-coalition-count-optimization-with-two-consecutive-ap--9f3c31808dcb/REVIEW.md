# Review: linear-time extrema for adjacent-size approvals

## Correctness — PASS

The exact necessary-and-sufficient condition is divisibility of each size bucket \(a_s+b_s-t_s+t_{s-1}\) by \(s\), with \(0\le t_s\le b_s\). It gives both directions of a constructive bijective assignment criterion. The dynamic program retains exactly all feasible carries and the optimal number of completed groups for each, and the min/max residue comparison follows by multiplying the transition cost by \(s\). Timestamped sparse residues and \(\sum_s b_s\le n\) prove the linear bound; reconstructed assignments satisfy every interval. The extracted standalone checker passed 7536 exhaustive/sample set-partition comparisons and 1250 separate flexible-split comparisons. The checker is supportive rather than an infinite proof.

## Originality — PASS (subject to priority uncertainty)

The closest primary source, Constantinescu et al., arXiv:2311.02067v1, gives an \(O(n^5)\) algorithm for the full interval class and a general two-size modular-orientation representation (Theorem 2.5, Appendix B). Those results imply polynomial-time feasibility on this restricted class, not the claimed linear-time **simultaneous minimum and maximum group-count** optimization and explicit witnesses. Darmann et al., DOI 10.1007/s00182-017-0596-4, Theorem 4, proves hardness of general nonconsecutive two-size approvals and does not supply the claimed algorithm. Searches for width-two hiking, consecutive choices, modular orientations on paths, linear-time bounds, and related source identifiers found no direct covering statement in the inspected material. Equivalent folklore or other literature can remain unlocated; nonappearance in searches alone is not a novelty proof.

## Mathematical value — PASS

The restriction models the smallest nontrivial uncertainty in acceptable hiking-group size: each attendee accepts their ideal size and at most one neighbor size. On this motivated boundary, both cardinality extrema and concrete arrangements are determined in optimal input-linear time rather than by a high-degree general interval algorithm. The exact stage-flow invariant explains why width-one interval choices collapse to a one-dimensional state, while arbitrary two-size approvals already have an NP-complete feasibility problem. This is a structural tractability boundary, not a mere numerical example or parameter substitution.

## Limitations and risk

The theorem does not prove a gap-free spectrum of group counts, and does not extend the algorithmic bound to all intervals. The general two-size graph-orientation reduction is explicitly acknowledged, and an already-known path-orientation optimization theorem could settle priority. No independent external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
