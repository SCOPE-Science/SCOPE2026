# Scientific review

## Correctness
**PASS.** Every vertex-to-edge distance is derived from the diameter-two doubleton structure. The symmetric-difference identity \(|R|=12-2\binom h2+q\) partitions all pair types by unique union support, and the seven per-support table rows are counted by explicit finite choices. The exact uniform feasible weight \(1/4\) and the summed three-matching constraints on every four-set give equal primal and dual bounds. Boundary \(n=5\) is included; vanishing binomial terms cover smaller support sizes. Independent breadth-first-search enumeration corroborates 99,753 graph-edge pairs for \(5\le n\le9\).

## Originality
**PASS with remaining bibliographic uncertainty.** Yi's 2021 article proves the Petersen instance and presents the definition and basic estimates, not the all-order Kneser result. Goshi et al. provide the pre-existing edge-transitivity reduction, not the ground-support count and six-size neighborhood polynomial. In particular, no originality is asserted for \(\operatorname{edim}_f(G_5)=5/2\) alone or for the generic symmetry theorem. Research-record comparisons found work on other families and other invariants of Kneser graphs, without an implication of the claimed exact size census. Inaccessible or unindexed related papers remain a priority risk.

## Value
**PASS.** The full polynomial counts each type of edge-observation ambiguity in the complements of triangular graphs, a canonical family, and gives a sharp all-order fractional location requirement. The proof shows why a fixed four-probe obstruction persists for arbitrarily large graphs and provides an explicit tight dual witness; the six nonzero resolving-neighborhood sizes encode structural data not contained in the scalar optimum.

## Closest literature and limitations
E. Yi, arXiv:2103.07375v1, especially Proposition 3.5; N. Goshi et al., *Mathematics* 9 (2021), 2364. Only two-subset Kneser graphs are covered; no assertion is made for higher-rank Kneser graphs, integral edge dimension, or uniqueness of fractional optimizers. Computational evidence is finite, and independent validation and exhaustive literature priority assessment remain unperformed.

Self-review: passed. Independent audit: not yet performed.
