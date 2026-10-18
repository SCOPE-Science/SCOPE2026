# Scientific assessment

## Correctness

**PASS.** The proof uses the exact diameter-two distance rule for \(\mathrm{KG}(n,2)\), including the \(n=5\) boundary. Intersecting target pairs are unresolved precisely by two isolated ground vertices or an isolated \(K_2\). Disjoint target pairs are unresolved precisely by an edge-closed four-vertex set admitting a balanced bipartition; after excluding the first two obstructions, these are exactly \(P_3\) plus an isolate, \(P_4\), or \(C_4\) components. The random theorem follows by bounding components of sizes two through four and applying the factorial-moment Poisson limit for isolates. An independent implementation of the direct distance test agrees with the component criterion on \(2130944\) exhaustive ground graphs and \(150000\) sampled graphs, but finite agreement is not used as a proof.

## Originality

**PASS, with bibliographic residual risk.** Bailey--Cameron (2011) establishes the scalar metric dimension; Bailey et al. (2013) establishes a general intersection criterion and resolving-set constructions; Bonato--Huggan--Marbach (2020) establishes the hypergraph detectability framework. These works do not state the component-by-component characterization nor the critical-window limit \(e^{-\lambda}(1+\lambda)\). The general intersection criterion supplies a point of departure, not the enumerated component classification or Poisson analysis. Searches by invariant, graph family, equivalence, and probability formula, including mathematical research records, identified no dominating result. No search can establish absolute novelty; overlooked or unindexed equivalent work is possible.

## Value

**PASS.** The component theorem is a complete, linear-time recognition criterion for *every* resolving sensor placement on a natural distance-transitive graph family, unlike the already known minimum cardinality alone. Its probabilistic consequence locates the sharp random-sensor threshold and explains a nonstandard Poisson tail: resolution tolerates one isolated ground vertex, contrary to ordinary random-graph connectivity. The exact critical-window success probability is a natural reliability invariant useful for selecting random landmark density.

## Closest literature and limitations

Relevant primary results are Bailey--Cameron (2011, Theorem 3.32), Bailey et al. (2013, Lemmas 2 and 5), and Bonato--Huggan--Marbach (2020, Section 2). The work concerns \(\mathrm{KG}(n,2)\) for \(n\ge5\) and uniform independent vertex probes only. The analytic limit and deterministic equivalence are proved here; no independent validation or exhaustive priority audit has been performed.

Self-review: passed. Independent audit: not yet performed.
