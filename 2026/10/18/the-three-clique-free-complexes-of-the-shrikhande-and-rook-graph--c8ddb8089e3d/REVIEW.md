# Scientific review of the Shrikhande and rook clique-free classifications

## Correctness — PASS
The graph definitions, 32 triangles each, full face enumeration, deterministic Morse matching and complete directed Hasse acyclicity were reconstructed. The computed integer Morse matrices have shapes \(5\times14\) and \(21\times6\), respectively, with explicit full-rank unit minors. The high-dimensional attaching-degree classification makes the resulting integral homotopy wedges rigorous. An independent raw simplicial mod-two boundary calculation confirms the indicated nine and fifteen generators in their respective degrees. The `verify.py` program and the actual run output are enclosed.

## Originality — PASS
The main February 2026 clique-free paper was read at theorem and relevant-proof level, and earlier algebraic clique-ideal treatments were compared. The first establishes shellability under chordality and attachment conditions rather than the asserted classifications. Both graphs contain induced four-cycles, excluding the chordal hypothesis. The exact published independence-complex results for the same graph pair use forbidden edges (\(t=2\)), whereas this statement uses forbidden triangles (\(t=3\)); neither the former nor the known Čech-complex comparison implies this pair of homotopy types. Exact graph names, triangle-hypergraph equivalents, both sphere dimensions and multiplicities, broader clauses and exact-table searches did not identify covering prior work. No uniqueness claim follows from search failures.

## Value — PASS
These graphs share the same strongly regular parameters and all 32 three-cliques, yet the corresponding three-clique-free complexes have homology in **different dimensions** and distinct integral homotopy types. This is an exact naturally paired classification rather than an arbitrary graph choice, small parameter increment, or already known table. It supplies a benchmark for the recently studied clique-free construction and shows standard strongly regular graph data cannot determine this topological invariant.

## Sources and limitations
Main inspected primary sources: Ghosh–Selvaraja, arXiv:2602.09623v1 (2026-02-10), and Moradi, arXiv:1712.00583v1 (2017-12-02). The closest published mathematical research result compares **ordinary independence complexes** of the same graph pair; that does not subsume three-clique-free complexes. The claim is finite and does not address other strongly regular graphs or a general closed formula. An unindexed equivalent calculation or an older example buried in other primary literature remains possible. Independent external examination of the finite certificates has not occurred.

Self-review: passed. Independent audit: not yet performed.
