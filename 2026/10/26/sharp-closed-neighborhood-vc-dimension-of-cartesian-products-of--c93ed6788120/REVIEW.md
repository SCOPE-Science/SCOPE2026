# Scientific review: closed Hamming ball shattering

## Correctness — PASS

The statement quantifies over every \(d\ge1\) and all finite alphabet sizes \(q_i\ge2\), using inclusive radius-one neighborhoods. The key universal argument is geometric: any four-point shattered set is contained in a coordinate star, and three arms from at least two coordinate directions have only the star center as a radius-one common center. The line case supplies the remaining obstruction. The two-dimensional classification uses the complete row–column-cross trace condition and proves necessity of unused row and column, with explicit constructions at every threshold. No probabilistic or asymptotic extrapolation is used. An independent finite checker confirms the claimed small cases; it does not substitute for the proof.

## Originality — PASS (qualified)

Adler–Benediktsson–Macpherson, arXiv:2007.16042v1, Theorems 4.6–4.7, treat open neighborhoods, with closed neighborhoods mentioned only for boundedness. Coudert–Csikós–Ducoffe–Viennot, arXiv:2405.07588v1, treat closed-neighborhood VC dimension for arbitrary graphs algorithmically; their generic bounds do not supply these Cartesian-product exact values. Housholder–Mangiapanello–Senger, arXiv:2505.14641v1, investigate open-neighborhood Hamming traces on induced subsets. The closed-versus-open difference at the binary three-cube proves that the present exact claim does not follow by simply applying the published open-neighborhood formula. A semantic search of published mathematical findings yielded related Hamming/rook graph topology and Hamming-ball harmonic results but no equivalent shattering classification. Terminology and indexing gaps remain possible.

## Mathematical value — PASS

The result supplies a complete exact VC invariant of a natural infinite graph family, with heterogeneous clique factors, simultaneously sharpening the boundedness observation in [1] and identifying the precise alphabet threshold for two-factor products. The binary three-cube demonstrates a nontrivial difference between open and closed shattering behavior. The result is self-contained and applicable to closed-ball trace complexity in coding-theoretic and learning-theoretic settings; no downstream theorem is asserted.

## Limitations and closest prior results

The theorem does not address radius-two balls, induced subgraphs, or arbitrary graphs. No independent audit is available. Relevant published sources are arXiv:2007.16042v1, arXiv:2405.07588v1, and arXiv:2505.14641v1, alongside general closed-neighborhood concept-class analysis in the 2026 TU Delft thesis *Bounding the Recursive Teaching Dimension for Concept Classes Induced by Graphs*. The novelty assessment is conditional on the accessible full-text material and searches.

Self-review: passed. Independent audit: not yet performed.
