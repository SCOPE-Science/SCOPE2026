# Mathematical assessment

## Correctness — PASS

For a spanning tree \(T\) of a wheel with \(m\ge3\) rim vertices, the basis-exchange distance formula and forest-extension argument give \(\operatorname{ecc}(T)=m-\beta(H_T)\). Every rim vertex has complementary degree at most two, forcing distinct complementary cycles to meet only at the hub; thus at most \(\lfloor m/3\rfloor\) cycles occur. An explicit construction attains the bound, and a complementary spanning-tree pair attains eccentricity \(m\). For each nonconstant binary coloring of the rim edges, its even number of monochromatic runs admits exactly two alternating spoke completions; monochromatic colorings admit none. This gives the exact periphery count \(2^{m+1}-4\). The arguments hold for all integers \(m\ge3\). Two separately structured exact verification programs corroborate the all-size formulas for finite ranges, with exhaustive exchange-graph BFS for the smallest wheels.

## Originality — PASS, with stated residual risk

The closest full-text precedent is Mahoney (2016), Section 4.2: its Lemmas 4.4 and 4.7 and Theorem 4.8 relate graph centers to cyclic versus acyclic edge complements; the claimed exact radius and complementary-tree count for every wheel were not present in the inspected sections, wheel discussion, or numerical appendices. The standard graphic-matroid exchange distance and classical total number of wheel spanning trees are credited, not claimed. Restricted triangle-only spanning-tree exchanges were distinguished from the unrestricted graph here, because they do not have the same adjacency relation. Targeted searches by graph, alias, invariant, and explicit formulas located no result with stronger coverage. This does not prove priority against unindexed literature. The older Benjamin–Yerger wheel enumeration article was accessible as an institutional abstract/record but its downloadable full text returned an access error; it was not used to assert full-document exclusion.

## Value — PASS

Tree graphs encode exact costs of transforming one spanning network into another without losing connectivity. Determining the center/periphery of a whole natural infinite family is an intrinsic metric classification, not a choice of arbitrary finite test instances. The cyclic cotree criterion explains which trees are closest to every possible reconfiguration target. The exact complementary-tree count gives the size of the worst-case class and a closed combinatorial enumeration distinct from the classical total spanning-tree count. The formulas and two independent implementations provide benchmarks for tree-exchange methods.

## Scientific limits and closest literature

The full-text Mahoney dissertation proves a qualitative complement-cycle criterion, but not the stated wheel-specific quantitative theorem in the inspected material. The Benjamin–Yerger record concerns total spanning trees, not their exchange eccentricities. An equivalent unindexed result remains possible. Independently performed scholarly validation has not been carried out; finite checks cannot substitute for the proof.

Self-review: passed. Independent audit: not yet performed.
