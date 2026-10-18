# Scientific review

## Correctness

**PASS.** Exhaustive generation is justified by a removable non-cut ear for connected outerplanar graphs, independently supplemented by augmentation of every connected seven-vertex atlas graph with an arbitrary nonempty neighbourhood. Exact graph-isomorphism deduplication yields the externally checkable population of 777 eight-vertex types. Direct automorphism enumeration and independent pointed-isomorphism testing agree that precisely four fail orbit-exact refinement, two of them biconnected. Every listed equitable quotient and orbit partition is directly reconstructible from the edge lists. The proof is finite and covers the entire stated order bound, not larger orders.

## Originality

**PASS, qualified by priority risk.** The 2015 Arvind–Köbler–Rattan–Verbitsky paper establishes the definitional refinability framework and general implications, not this outerplanar census. The 2005 Bodirsky–Fusy–Kang–Vigerske enumeration gives the population but not the colour-refinement/orbit distinction. Two of the four exceptions arise already in the cactus subfamily; the sharp biconnected classification comprises two additional genuinely non-cactus graphs. Targeted literature and database searches did not yield a stronger prior theorem or a complete four-graph table. A previously overlooked specialised small-graph table remains the primary originality risk.

## Value

**PASS.** Biconnected outerplanar graphs are a natural non-treewidth-one test class for the limits of two-variable counting descriptions of vertex orbits. The sharp eight-vertex obstruction threshold, complete list of exceptions, and explicit equitable partitions distinguish structural limitations from a single isolated counterexample. The biconnected examples show that no cut vertex is needed for orbit-blindness. This is a bounded classification, not an all-orders or algorithmic-complexity improvement.

## Scientific limits

The claim is restricted to uniform initial colour on finite simple connected outerplanar graphs with at most eight vertices. Both verifiers rely on NetworkX's graph atlas and planarity implementation, although the exhaustive generation and automorphism comparisons are independently organized. A later or overlooked specialist catalogue could change the novelty assessment without changing the computations.

Self-review: passed. Independent audit: not yet performed.
