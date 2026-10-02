# Independent mathematical audit — 2026-10-01

## Final claim
For every prime power at least five congruent to one modulo four, the two-cluster join has clique covering number four and clique partition number equal to the field-size square plus three times the field size; for odd orders congruent to three modulo four the cut lower bound is unattainable.

## Correctness — PASS
The finite-field construction and obstruction are correct. For prime powers congruent to one modulo four, nonsquare multipliers with both square and nonsquare values of one minus the multiplier exist by the quadratic-character count. The linear edge maps are invertible and send each Paley edge class to the required target class; the nonsquare factor prevents crossing-edge reuse. The resulting edge-disjoint four-vertex cliques cover all internal edges and all but exactly four times the field size crossing edges, attaining the cut lower bound. Independent prime-field spot checks reproduced the character counts, edge bijections, and crossing uniqueness. The congruence-three obstruction follows from the equality cases of both oriented cut inequalities and the handshake lemma.

## Originality — PASS
Best-of-knowledge originality passes for the two-cluster odd-prime-power attainment and complementary congruence obstruction.

### Equivalent formulations
Searches: two-cluster clique partition Paley pairing; clique partition (2K_q) join (2K_q) odd prime power
Evidence: Ning's 2026 theorem treats balanced cluster joins in the even-clique regime with sufficiently many clusters. The same-day repeated-graph theorem found in Resultary requires the number of copies on each side to be at least the chromatic index, which fails for two copies when the clique order is at least five and odd.
Reasoning: The assigned case is a low-copy regime requiring a different finite-field edge pairing.

### Broader coverage
Searches: Ning arXiv:2608.11536; Resultary exact clique partitions for joins of repeated graph copies
Evidence: Neither checked theorem applies to two copies of an odd complete graph of order at least five.
Reasoning: The Paley construction fills a parameter regime outside the hypotheses of the broader repeated-copy formula.

### Exact database or table
Searches: Resultary exact-topic search; targeted Paley finite-field clique partition searches
Evidence: No prior exact formula or congruence-three obstruction for this two-cluster family was located.
Reasoning: The exact value and obstruction are not printed in the checked broader sources.

### Claim versus prior implication
Searches: Ning balanced even-order formula; repeated-graph chromatic-index theorem
Evidence: Their hypotheses exclude the assigned odd two-copy regime.
Reasoning: The final claim is not a special case of the checked prior theorems.

### Source inspections
- **On the difference between clique partition and clique covering numbers of graphs** (arXiv:2608.11536): Covers the even-order sufficiently-many-clusters regime, not the assigned two-copy odd-prime-power regime. Material read: Abstract and the result context for balanced cluster joins. Evidence: The checked theorem does not reach two clusters when the clique order is odd and at least five.
- **Exact clique partitions for joins of repeated graph copies** (Resultary 2026/9/18/SCOPE-clique-partitions-joins-repeated-graphs--40b72bad9da8): Its sufficient condition is minimum copy count at least the edge-chromatic number, excluding the assigned two-copy odd case. Material read: Complete RESULT.md. Evidence: For an odd complete graph, the edge-chromatic number equals its order, which is greater than two.

Checked sources: arXiv:2608.11536; Erdos--Faudree--Ordman 1988 cut inequality; Resultary repeated-graph theorem; Resultary exact-topic search
Residual risks: Older design-theoretic literature may encode the same finite-field pairing under different terminology.

## Scientific value — PASS
The result gives an exact infinite family in a parameter regime omitted by the newest general constructions and pairs it with a sharp arithmetic obstruction, showing that cut-bound attainment at two clusters has genuine congruence structure.

## Conclusion
The unchanged scientific claim passes correctness, best-of-knowledge originality, and scientific-value review.
