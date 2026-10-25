# Scientific review: Folkman closed vertex-ball nerves

## Correctness
**PASS.** The graph is defined explicitly as the subdivided double of the five-point complete graph, eliminating ambiguity about the metric or vertex labels. The proof derives the complete radius-one and radius-two ball-facet systems from shortest-path distance. The accompanying executed, standalone checker enumerates 430 and 81,233 nonempty faces, verifies respectively 130 and 39,641 elementary simplicial free-face pairs, and performs full integer unit-pivot reductions on each residual chain complex. Residual boundary ranks are \((19,55)\) at radius one and \((18,141,417,389)\) at radius two, and all remaining integer entries are zero, excluding torsion. Independent binary ranks agree. The endpoints follow from isolated singleton balls and twin eccentricity three. No unverified infinite extrapolation is needed for this finite object.

## Originality
**PASS on the inspected evidence.** The strongest nearby treatments are the general vertex-centered graph Čech definition and hypercube calculations [1], the general closed-neighborhood suspension correspondence [2], the complete-graph-subdivision Rips filtration [3], and the undoubled Steiner-incidence open-neighborhood calculation [4]. The square-completion theorem [5] is excluded by the twins' four common neighbors; the clique-fiber product and complete multipartite hypotheses [6–7] likewise do not hold. Actual searches used Folkman, subdivided double, even-scale Čech, closed graph balls, and the exact rank quadruple. No inspected statement implies this particular pair of integral homology computations or its complete vertex-ball barcode. Unindexed equivalent finite computations remain a bibliographic risk.

## Value
**PASS.** The Folkman graph is the canonical smallest semisymmetric graph, and the vertex-ball Čech nerve is a geometrically motivated graph-topology invariant. The certificate resolves its entire radius-indexed integral persistence, including mixed-dimensional classes in **two consecutive nontrivial stages**, simultaneous degrees \(1,2\) and \(3,4\), and complete torsion exclusion. This is a motivated exact classification of a 20-vertex high-symmetry graph; it is not an arbitrary subgraph slice, a routine reparametrization of a known Rips theorem, or simply a mod-two experiment. A full conventional graph-geometric Čech filtration and a homotopy classification are expressly not claimed.

## Limits and nearest work
The primary reference [1] has first public date 2022-12-12 and primary MSC2020 topology classification `55N31`. The mathematical comparison is statement-based, and the accepted claim is finite, integral, and reproducible; independent external validation has not been performed. References [1]–[7] are identified in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
