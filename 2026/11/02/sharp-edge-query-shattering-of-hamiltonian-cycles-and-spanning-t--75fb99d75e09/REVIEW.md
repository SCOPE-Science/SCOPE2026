# Scientific review: sharp edge-query shattering of Hamiltonian cycles and spanning two-factors

## Correctness — PASS

For every labeled order at least five, the upper VC bound follows from the forced completion of an almost-complete two-factor after omission of a path endpoint edge. The lower VC bound has an explicit Hamiltonian cycle completion for every assignment on the edges of a path with one extra isolated vertex; the small numbers of path blocks are treated separately. The finite adaptive values use the exact finite version-space recursion, full hypothesis enumeration and complete decision-tree witnesses for each claimed depth. Independent generation by permutation cycles and an independent fiber-refinement shattering computation agree with the main programs. Numerical certificate replay and graph-degree checks all pass.

## Originality — PASS with stated residual historical risk

Published background on regular graph factors concerns existence in host graphs, whereas published VC-dimension work inspected here concerns adjacency neighborhoods in Johnson/Hamming graphs or practical algorithms for that different graph-neighborhood set system. None of the inspected primary theorems provides the all-size edge-incidence VC formula, the first online gap for complete-graph two-factors and Hamiltonian cycles, or their finite support polynomials. Searches for incidence families, fixed-degree edge predicates, spanning two-factors, Hamiltonian cycles and online mistake trees produced no directly covering result. This is a statement about accessible comparisons, not an assertion of absolute priority. Other graph-family learning invariants may use similar query terminology, but those are not automatically equivalent to the present incidence hypotheses.

## Value — PASS

The result identifies the exact static complexity of two classical spanning graph families at arbitrary order, supplies an explicit shattering support valid even under the connectivity restriction, and locates the first order where adaptive queries strictly outperform fixed queries. At the first two orders exhibiting an adaptive excess, the Hamiltonian and two-factor concept classes have equal dimensions but different intermediate support polynomials. This separates dimension invariants from the finer distribution of shattered supports and motivates the unresolved all-order adaptive dimension question. The finite cutoff is a natural first-transition classification rather than an arbitrary isolated numeral.

## Limits and related literature

Finite support profiles and adaptive dimensions stop at seven vertices; only the VC formula is proved for all larger orders. Relevant literature: Kostochka–Raspaud–Toft–West–Zirlin (arXiv:1806.05347), Adler–Benediktsson–Macpherson (arXiv:2007.16042), and Coudert–Csikós–Ducoffe–Viennot (DOI:10.4230/LIPIcs.SEA.2024.8). The last was examined at its published abstract, rather than in full. Alternative equivalent historical descriptions remain a priority risk.

Self-review: passed. Independent audit: not yet performed.
