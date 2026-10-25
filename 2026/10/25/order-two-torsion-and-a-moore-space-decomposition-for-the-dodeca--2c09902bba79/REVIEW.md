# Scientific review: dodecahedral perfect-matching complex

## Correctness — PASS

The graph's 20-vertex cubic incidence model is isomorphic to the standard dodecahedral graph; the exact enumeration obtains 36 perfect matchings and all 30,503 faces. A deterministic toggle matching consists of 15,231 disjoint codimension-one pairs. Orienting each of the 163,650 incidences and performing a complete topological sort proves acyclicity; no partial exploration or sampled assertion is used. The remaining critical cells have counts 1, 10 and 30 in dimensions zero, two and three. Integer Morse reduction gives a 10-by-30 matrix with rank nine modulo two, an exact nonzero determinant-two maximal minor and an exact unit nine-minor. These three certificates force Smith factors nine ones and a two. Since the two-skeleton is a wedge of two-spheres, the resulting integer attaching degrees classify the three-cell attachments, yielding a degree-two Moore space and twenty free three-spheres. The packaged standard-library verifier executes these certificates without consulting external data.

## Originality — PASS

The closest checked result for the same dodecahedral graph concerns its ordinary matching complex, which contains additional unextendable matching faces and has a different homotopy type; it does not imply the present classification. A checked perfect-matching complex result concerns the different Heawood graph; the 2023 honeycomb paper, polygonal-line tiling paper, and 2026 ladder paper do not include the dodecahedral graph. The 2013 Fujita paper covers enumeration and symmetry of classical Kekulé/perfect matchings, not homotopy of the complex of their subsets. The 2012 predecessor was accessible only as bibliographic metadata and an abstract; it has therefore not been certified as noncovering. Repeated mathematical research-index searches for dodecahedron, Kekulé complexes, fullerenes, Moore space, integral torsion, and extendable matchings found no statement implying this particular homotopy decomposition. An unindexed or inaccessible equivalent result remains a limitation.

## Value — PASS

The perfect matchings of the dodecahedral skeleton form a natural classical enumerated family, and the resulting simplicial complex is a well-motivated topological construction rather than an arbitrary slice. The finding upgrades the known count of perfect matchings to a complete homotopy classification and detects order-two torsion, invisible over characteristic zero. The distinction from the torsion-free ordinary matching complex is mathematical substance rather than a routine substitution.

## Scope and verification limits

The result is restricted to the 20-vertex dodecahedral graph. The certificate is exhaustive for this one finite complex; it does not constitute an infinite-family theorem or an independent review. Source-inspection and access limits are recorded in the structured scientific assessment.

Self-review: passed. Independent audit: not yet performed.
