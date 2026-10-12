# Scientific review: Jaccard–unweighted-UniFrac rank reversal on a rooted quartet

## Correctness — PASS

The claim explicitly fixes one rooted reference tree, equal presence/absence richness and the union-edge denominator. With at most three tips, and on four tips outside richness two, all distinct pairs have identical Jaccard distance. Among two-species subsets of a quartet, the twelve one-tip-overlap pairs have Jaccard distance \(2/3\) and the three disjoint pairs have distance \(1\). Direct substitution of all rooted edges produces the complete UniFrac score multisets in RESULT.md for both balanced and pectinate shapes. Their extrema give the displayed rational margin identities, with denominators positive throughout the stated parameter domains. For the pectinate tree, the margin is strictly negative; for balanced quartets its sign is exactly the criterion. An explicit common-reference construction attains both extrema. The symbolic proof applies to all admissible real branch fractions; the exact rational checks are finite corroboration, not proof by sampling.

## Originality — PASS, with specified residual risk

The foundational UniFrac paper establishes the normalized unshared-over-union edge metric. Ives–Helmus give an extensive theoretical comparison with other phylogenetic and taxonomic measures, including the phylogenetic Jaccard representation in their Appendix C. Jin et al. empirically report how phylogenetic beta-diversity metrics depend on relatedness and differ from taxonomic Jaccard. The inspected theorem-level statements and worked analyses do not characterize the smallest fixed-richness reversal or the balanced-versus-pectinate branch-age phase boundary. Searches of the mathematical-result index using overlapping and equivalent phrasings yielded unrelated phylogenetic-rank, clustering and richness results. A broader, unindexed result on phylogenetic Jaccard orderings or an alternate rooting convention could subsume this specialized claim; targeted searches are not an exhaustive originality guarantee.

## Value — PASS

The first strict-reversal threshold controls the number of taxa, community richness, tree shape, and two branch ages simultaneously. The result isolates genuine phylogenetic ranking disagreement from unequal-richness differences and gives a sharp signed margin, including a common-reference three-community witness. This is a structural boundary on the interpretation of two standard ecological beta-diversity metrics, not a routine restatement of their definitions or a claim of ecological forecasting.

## Closest literature and limits

Lozupone–Knight (2005), DOI 10.1128/AEM.71.12.8228-8235.2005; Ives–Helmus (2010), DOI 10.1086/656486, including Appendix C; Jin et al. (2015), DOI 10.1111/1365-2745.12385. These underpin the measures and motivation but do not imply the exact quartet margin. The theorem is not extended to non-ultrametric, larger, weighted, or pairwise-rerooted configurations. Finite code checks are supplementary and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
