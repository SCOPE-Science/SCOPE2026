# Independent mathematical audit — SCOPE-20260918-a84aa8e708f8

Final disposition: **PASS**.

## Correctness
**PASS.** The four adjacency classes for the two vertices outside the clique were reconstructed from the graph definitions. A fresh independent enumerator built every 2-connected parameter graph through order fourteen, computed all-pairs distances and every Szeged edge contribution directly, and found zero discrepancies with the three displayed formulas. In orders ten through fourteen, the only equality parameters were the Zhang-Li family and, at order ten, the one exceptional type, up to exchanging the two outside vertices. This finite replay is supplementary: the all-order classification is supplied by the displayed algebraic formulas and the package's nonnegative-integer case analysis, which was separately checked for the stated boundary cases.

## Originality
**PASS.** The complete 16-page Zhang-Li preprint was inspected. Its Problem 7 asks for all equality cases and Lemma 8 constructs the known infinite family while explicitly saying the construction is not necessary; it does not classify the high-clique regime. Resultary also contains later September 18/19 records with the same near-complete classification, but their corrected provenance sections explicitly identify this assigned record as the earlier broader theorem, committed at 2026-09-18 03:47:31 UTC. They therefore corroborate rather than predate the assigned claim. No earlier external classification of the \((n-2)\)-clique regime was found.

### Equivalent formulations
The equivalent formulations were matched formula-by-formula, including the cell-label permutation.

### Broader coverage
Neither the source lower-bound theorem nor the later corroborative records supply prior coverage that predates the assigned theorem.

### Exact database or table
The database check was decisive about duplicate chronology and avoided falsely treating later rederivations as prior art.

### Claim versus prior implication
The high-clique \(2n\) classification is not a corollary of the inspected prior equality theorems.

## Value
**PASS.** This is a natural partial solution of a newly posed equality-classification problem in the dense regime containing the entire known infinite construction. It gives exact formulas for all two-vertex extensions of a clique, proves uniqueness for every order at least eleven within that regime, and isolates the unique order-ten exception. The restriction is mathematically motivated by the known equality family, not an arbitrary slice.

## Source inspections
- **Improved Bounds on the Szeged-Wiener Gap and the BKLPS Conjecture** (https://arxiv.org/abs/2609.20025): complete 16-page primary preprint, including Theorem 6, Problem 7, Lemma 8, and references Assessment: PRIMARY_SOURCE_LEAVES_THE_CLASSIFICATION_OPEN. Evidence: Problem 7 asks for all \(n\ge10\) unexceptional 2-connected equality graphs, and Lemma 8 gives a sufficient family while stating that it is not necessary.
- **Szeged-Wiener equality for graphs with an (n-2)-clique** (https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-szeged-wiener-equality-near-complete-graphs--a6c30db346eb): complete RESULT.md Assessment: LATER_CORROBORATION_NOT_PRIOR_COVERAGE. Evidence: Its provenance section states that the assigned September 18 record was committed earlier and already proved the same classification and formulas.
- **Exact Szeged-Wiener equality in a co-bipartite class** (https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-szeged-wiener-equality-co-bipartite-k2-side--95dbd4525738): complete RESULT.md Assessment: LATER_SPECIALIZATION_NOT_PRIOR_COVERAGE. Evidence: Its corrected provenance states it was committed later on September 18 and is a specialization of this assigned earlier broader theorem.

## Residual risks
- The source equality problem and this solution appeared within roughly a day of one another, so unindexed simultaneous external work remains possible.
- The theorem is only a high-clique partial classification; the global equality problem for smaller clique number remains open.
