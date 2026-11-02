# Scientific review of optimal connected domination on circular ladders

## Correctness — PASS

The exact domain is every simple prism \(C_n\square K_2\), integer \(n\ge6\); the allowed move removes one selected vertex and inserts one arbitrary unselected vertex, maintaining a connected dominating set of minimum cardinality. The occupied-column projection and the domination of empty columns establish that at most two consecutive columns may be empty. The cardinality argument then proves the minimum \(n\) and exhausts all A/B/C configurations. The seven-line exchange table enumerates all possible occupancy and boundary transitions, showing connectedness and the degree/edge formulas. Two standalone standard-library implementations were run: a direct graph-subset enumeration for \(6\le n\le11\), and an independent template/neighbor comparison for \(6\le n\le38\). The finite cases are corroboration, not the basis of the universal quantifier. A remaining verification limit is that this is a mathematical argument and self-review, not independent expert review.

## Originality — PASS, subject to residual literature risk

The nearest research themes include Schurch (2005), whose prism connected-domination chapters give parameter bounds and fixer/doubler characterizations, and general minimal connected-dominating-set enumeration (Golovach–Heggernes–Kratsch, 2015), connected domination as a parameter (Chandran et al., 2010), and connected-domination reconfiguration under token addition/removal (Lokshtanov et al., 2020). Ordinary domination of prisms is a different optimization problem, even when its graph notation matches. In the examined primary texts, the closest results do not imply the explicit \(2n^2+2\) minimum-connected-backbone census or the exact one-for-one exchange graph \(4n(n+2)\) edges and degree law. The related 2014 ordinary-domination reconfiguration model also uses additions/deletions rather than fixed-cardinality exchanges. Searches included the precise formula, synonyms 'cylindrical ladder'/'circular ladder'/'prism', and maximum-leaf spanning-tree equivalence. A result published under another terminology remains a material risk, and a search miss alone is not proof of historical uniqueness.

## Value — PASS

The possible rearrangement of a connected minimum-size communication backbone without temporary loss of domination/connectivity is a natural reconfiguration question. Merely knowing the minimum size or the existence of one optimal set does not give the optimal-set census or feasible movement geometry. The finding resolves all optimal configurations for a natural infinite cubic graph family and proves the exact mobility split: two degree-\(2n\) whole-rail hubs, boundary configurations of degrees five and six, a degree-four bulk, and a shortest exchange path of length \(n\) between disjoint rails. The structured decomposition also supplies explicit routes, not just counts.

## Scope and limitations

The proof applies only to \(n\ge6\) and to one-for-one replacements unrestricted by original graph edges. It does not claim the reconfiguration diameter, a transfer to arbitrary Cartesian products, or novelty of the underlying domination parameter. Independent scholarly audit has not been performed. A historical duplicate not surfaced by the searches cannot be ruled out.

Self-review: passed. Independent audit: not yet performed.
