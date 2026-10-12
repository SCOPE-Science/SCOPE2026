# Self-review

## Correctness
**PASS.** The finite domain is the documented complete Graph Atlas through seven vertices, restricted to connected representatives. Degree leaders are exact. Eigenvector leaders are not inferred from floating-point output: the Perron root is isolated by exact rational Sturm sequences, and the adjugate identity reduces eigenvector-coordinate ordering to exact comparisons of principal characteristic cofactors. The replay finds no distinct unique leaders through six vertices and exactly five classes at seven; direct permutation checks reproduce all five orbit sizes and the total \(9240\).

Risk: completeness of the finite input relies on the externally documented Read--Wilson Graph Atlas, while every centrality computation on that input is independently replayed.

## Originality
**PASS.** Prior work directly compares degree and eigenvector centrality and explains why their rankings can differ. That qualitative phenomenon is not claimed as new. The accepted claim is the sharp unique-leader boundary and complete first layer: coincidence through six vertices, exactly five seven-vertex isomorphism classes, and their exact labeled orbit total. Searches by aliases, exact order, exact count, and unique-maximizer language did not locate equivalent coverage.

Risk: the full 2007 Grassi--Stefani--Torriero article was not accessible during inspection, although its abstract states that it derives spectral-radius conditions relating highest degree to highest eigenvector centrality. An unindexed source could contain a small example or finite classification.

## Value
**PASS.** Degree is the canonical local popularity score, while eigenvector centrality recursively values connections to important neighbors. Applications often collapse each score to a single “most central” actor. The smallest network where those two unambiguous choices can conflict is therefore a natural structural boundary. Classifying all five first obstruction types explains the full onset rather than presenting an isolated counterexample.

Self-review: passed. Independent audit: not yet performed.
