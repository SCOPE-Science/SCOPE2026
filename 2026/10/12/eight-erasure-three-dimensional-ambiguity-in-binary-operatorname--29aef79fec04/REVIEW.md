# Self-review

## Correctness — PASS

The binary row/column parity constraints identify the ambiguity space with the binary cycle space of the bipartite erasure graph. The spanning-forest formula gives dimension \(|E|-|V_E|+c_E\). Connected simple bipartite graphs of cycle rank at least \(1,2,3\) require respectively at least \(4,6,8\) edges. On eight edges a rank-three graph must be connected on exactly six vertices; possible bipartition sizes and eight-edge cap uniquely give the three families. Direct counts and the correspondence with three-dimensional minimum-support subcodes then follow. This argument is uniform in \(m,n\) and handles rectangular/small-boundary cases through zero binomial coefficients. Exhaustive graph and independent subspace enumeration agrees for five finite instances, including \(788035\) three-spaces for the \(4\)-by-\(4\) code.

## Originality — PASS with disclosed literature risk

Theorem 7 of Ribeiro Alves–Cardell (2026) already fixes \(d_3=8\); this is not a novelty claim. The new assertion counts and classifies the exact eight-erasure rank-three kernel, a stronger invariant than the support threshold. The 2019 Cardell–Climent–López Martín complete manuscript was read: Theorem 3 counts strict uncorrectable erasure patterns by their row/column degrees using Kostka numbers. This strong prior margin-enumerator can count the relevant degree classes once cycle-rank-three structural restrictions are independently derived, but neither states nor proves the minimum three-space classification. The 2016 Cardell–Climent complete article was not obtained, although its abstract reports all-failure counts for eight erasures; an implicit graph classification there is the principal risk. No identical ranked count was found in focused published-index and database queries.

## Value — PASS

Binary erasure decoding failure severity distinguishes two, four and eight possible codeword completions; an aggregate uncorrectable-pattern count does not. The first support size allowing eight completions is a natural threshold already identified abstractly by the generalized-weight result; the complete \(K_{2,4}\), \(K_{4,2}\), and \(K_{3,3}-e\) classification and exact multiplicity quantify how often that threshold is attained across every rectangular parameter pair. They also determine all minimum-support third generalized-weight subcodes. This is a finite-configuration structural classification rather than a routine recomputation of the known minimum support size.

## Scope and closest literature

The proof covers binary single parity-check product codes and exactly eight erasures; it does not classify larger ambiguity dimensions at higher erasure sizes or particular iterative decoders. The 2026 arXiv Theorem 7 and Cardell graph papers (2016 and 2019) are the closest sources. The 2019 full text was read and its powerful Kostka margin enumeration explicitly compared; only the 2016 full article remains uninspected.

Self-review: passed. Independent audit: not yet performed.
