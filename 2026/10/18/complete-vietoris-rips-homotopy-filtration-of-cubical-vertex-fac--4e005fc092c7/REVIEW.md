# Independent mathematical audit

## correctness

PASS

Exact BFS-distance logic: vertex-vertex and facet-facet distances are 2 except antipodal/opposite 4, and vertex-facet distance is 1 if incident or 3 otherwise. At scale1 the connected bipartite graph is one-dimensional with cycle rank (d-1)2^d-2d+1. At scale2, each compatible facet set F has cube fiber X_F of size 2^{d-|F|} forming a simplex; decreasing-|F| then decreasing-|U| free-face deletions of F∪U⊂F∪U∪{a_F} remove every facet-containing simplex, leaving the antipodal-pair cross-polytope join, sphere dimension 2^{d-1}-1. At scale3 all cross X-Y pairs appear and the exact join has sphere dimension 2^{d-1}+d-1; scale4 full simplex. Persistence follows from different nonzero homology dimensions for d>=3. Independent BFS and exhaustive 2^14 subset clique checks for d=3 recovered 240 and 2186 nonempty scale2/3 faces, and inspected actual exact d=3,4 free-collapse verifier script. Analytic all-d collapse establishes infinite theorem.

## originality

PASS

Fresh comparison of exact statements and implications, with inspected primary mathematical sources, bounded Resultary searching, and recorded inaccessible potentially relevant sources. The cited general theorems lack needed hypotheses or concern an inequivalent vertex set/metric. The explicit uniform facet-fiber simplicial collapse and scale3 join are not corollaries of the unrelated sphere results on different polyhedra.

## value

PASS

The complete five-stage persistence and uniform sphere dimensions give natural integral topological invariants of an infinite family of canonical polytope incidence graphs. The coordinate-fiber elementary collapse and exact next-stage join explain a structural transition unavailable from numerical Betti tables, and can serve as a benchmark for graph-metric Rips theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
