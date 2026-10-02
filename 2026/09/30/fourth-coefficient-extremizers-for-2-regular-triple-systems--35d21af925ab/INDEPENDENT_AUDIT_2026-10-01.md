# Independent scientific review

## Final claim

For every finite simple \(3\)-uniform, \(2\)-regular hypergraph on \(n\) vertices, the number of independent \(4\)-sets is at most \(\binom n4-n(2n-7)/3\), with equality exactly for dual cubic multigraphs obtained from disjoint even cycles by alternately doubling one perfect matching.

## Correctness

**PASS.** Double counting gives \(i_3^{(4)}(G)=\binom n4-(2n/3)(n-3)+P(G)\), where \(P(G)\) counts pairs of hyperedges meeting in two vertices. Degree two implies no four-set contains three hyperedges and forces the graph on hyperedges formed by such overlap pairs to have maximum degree one, so \(P(G)\le n/3\). Equality means every dual cubic vertex is incident with exactly one doubled edge and one remaining simple support edge; these two perfect matchings form disjoint alternating even cycles, and multiplicity three is excluded by simplicity. The converse dual construction is valid. The finite enumerators corroborate, but are not used as the infinite proof.

## Originality

**PASS.** The complete Sarantis–Tetali–Zheng preprint states Conjecture 1.7 coefficient-wise and Proposition 3.3 proves the \(k=4\) triple-system case only under the no-cross-edge hypothesis. Its separate degree-two theorem is for the total independent-set count, not individual coefficients. The submitted degree-two argument removes the cross-edge restriction and classifies every equality type. Resultary found no prior unrestricted \((3,2,4)\) coefficient theorem.

## Value

**PASS.** This proves a natural unrestricted parameter slice of an explicit coefficient-wise conjecture and adds a complete structural equality classification. The proof also exposes the exact dual obstruction, so it is more than a finite census.

## Sources inspected

- **On Counting Independent Sets in Regular Hypergraphs** (arXiv:2609.17468v1): Complete 28-page PDF searched; Introduction, Conjecture 1.7, Proposition 3.3 with full proof, and the degree-two dual setup/results were inspected. Assessment: PARTIAL_COVERAGE_WITH_RESTRICTIVE_HYPOTHESIS.

## Residual risks

- The preprint is recent; an independent contemporaneous note on the same coefficient slice could be unindexed.
