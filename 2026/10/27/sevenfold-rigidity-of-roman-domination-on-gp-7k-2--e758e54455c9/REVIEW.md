# Scientific assessment: rigidity of optimal Roman functions on \(GP(7k,2)\)

## Correctness — PASS

The domain is every integer \(k\geq1\), with labelled outer and inner vertex sets and ordinary Roman labels \(0,1,2\). Direct residue checks verify a period-seven function of weight \(8k\). A precise five-column local constraint turns every RDF into a cyclic walk on 6,561 states; the arc-cost sum equals \(7w-8n\). The compiled standalone certificate checks all 48,681 admissible arcs and an integer potential with nonnegative reduced costs, then confirms that the zero-slack digraph has one cyclic component: a directed seven-cycle. The argument that an equality walk must stay on this cycle is exact for all lengths. An independently implemented Python critical-graph search reproduces the component data, while separate brute-force enumeration checks orders seven and fourteen. The source and result files were replayed directly, not inferred from log descriptions. Risks: a finite exhaustive lemma necessarily depends on exact code predicates and correct execution; these have been reconstructed and cross-checked, but no external audit has occurred.

## Originality — PASS, with residual uncertainty

The earliest relevant full primary source, Wang–Xu–Yang–Ji (arXiv:1103.2419v1, 2011), proves the minimum weight and exhibits one period-seven construction; it does **not** state the number of minimum functions or their pairwise distances. Zhang–Shao–Xu (2014, ten-page paper inspected) establishes a weighted-closed-walk reduction applicable to \(P(n,2)\), and explicitly attributes the existing number formula to Wang and coauthors. Its theorems proceed to \(P(n,3)\) and bounds for \(P(n,4)\), rather than a unique critical cycle in the \(P(n,2)\) transfer graph. The presently proved finite equality classification does not follow from either published numerical formula without an additional argument. Exact-minimizer, critical-cycle, alias, and domination-polynomial searches in the accessible scholarly literature and mathematical-record index did not locate a covering statement. Search incompleteness and independently undiscovered equivalence in transfer-matrix treatments remain risks; search absence has not been treated as uniqueness proof.

## Value — PASS

The old result determines only the optimum **weight**. The new result determines **all** optimum configurations for an infinite, natural congruence family and shows that their count remains seven while their pairwise Hamming separation grows linearly. This is a sharp equality-case rigidity phenomenon, not a routine restatement of the weight formula or an isolated small numerical census. The classification also exposes a unique critical cycle in the known transfer formulation. It does not purport to solve the other six residue classes or describe more general Petersen graphs.

Self-review: passed. Independent audit: not yet performed.
