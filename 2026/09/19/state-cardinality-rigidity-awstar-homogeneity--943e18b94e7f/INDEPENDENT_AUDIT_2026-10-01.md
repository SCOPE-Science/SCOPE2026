# Independent mathematical audit — 2026-10-01

## Final claim assessed

State-cardinality rigidity for transfinite AW-star homogeneity

## Correctness — PASS

PASS. The cardinal argument is sound. A state can be positive on only countably many members of a pairwise orthogonal nonzero projection family, because for each positive integer \(n\) only finitely many can have value at least \(1/n\). Hence a separating family \(\mathcal F\) detects at most \(|\mathcal F|\aleph_0\) such projections. A countable separating family has a faithful convex combination, so the state-separation cardinal is either one or uncountable. Applying these facts to a \(\kappa\)-homogeneous decomposition gives \(s(M)=1\) when \(\kappa=\aleph_0\), and \(s(M)=\kappa\) when \(\kappa\) is uncountable under the assumed upper bound. Larger homogeneity cardinals are excluded by the same counting estimate. For every infinite \(\lambda\le\kappa\), partitioning the original \(\kappa\) projections into \(\lambda\) blocks of size \(\kappa\) and using addability of orthogonal partial isometries shows each block join is equivalent to one, proving downward closure of the homogeneity spectrum. The local-corner canonicity then follows because the source construction supplies both hypotheses.

## Originality — PASS

PASS to the best of current knowledge. The current full version of Arulseelan's transfinite Christensen--Pedersen paper was inspected at the definition of \(\kappa\)-homogeneity, the \(\kappa\)-monotone-completeness corollary, the state-separation proposition, and the local faithful-corner proposition. It contains the countable weighted-state observation and constructs some \(\kappa\) in the local-corner argument, but it does not state the exact identity \(\kappa=\max\{\aleph_0,s(M)\}\), the complete downward homogeneity spectrum, or choice-independence of the maximal copy cardinal. Resultary search found no earlier exact statement. Classical Christensen--Pedersen and Berberian projection machinery remain prior ingredients rather than exact coverage.

### equivalent_formulations

Searches: Resultary: AW star kappa homogeneous state separating family cardinal s(M) ordinary states homogeneity spectrum; Arulseelan kappa homogeneous separating states faithful state cardinal

Evidence: The exact Resultary search returned the audited record as the only direct match. The primary source defines the two ingredients but does not identify their exact cardinal equality.

Reasoning: Sigma-finiteness/faithful-state language is analogous in von Neumann algebra theory, but the claimed ordinary-state separator cardinal and full transfinite AW-star homogeneity spectrum are not an inspected equivalent theorem.

### broader_coverage

Searches: arXiv:2609.20718 current full text; Christensen Pedersen properly infinite AW-star monotone sequential completeness; Berberian Baer star rings addability partial isometries

Evidence: Arulseelan proves the transfinite monotone-completeness implications and local construction; Christensen--Pedersen and Berberian supply classical countable/addability ingredients.

Reasoning: Those ingredients do not state a theorem that dominates the exact separator-cardinal identity or full downward spectrum under the simultaneous hypotheses.

### exact_database_or_table

Searches: Resultary semantic search for exact \(\kappa=\max\{\aleph_0,s(M)\}\) AW-star statement

Evidence: No earlier exact theorem-level record was found.

Reasoning: No numerical database is relevant to this structural cardinal theorem.

### claim_vs_prior_implication

Searches: Arulseelan Proposition on \(\kappa\) separating states plus \(\kappa\)-monotone completeness; Arulseelan local faithful-corner proposition

Evidence: The source uses a countable weighted sum and, in the properly infinite case, chooses a maximal orthogonal copy family to obtain a \(\kappa\)-indexed construction. It does not state that every such \(\kappa\) must equal the minimum ordinary-state separator cardinal or that all smaller infinite homogeneity cardinals occur.

Reasoning: The new counting obstruction and addability aggregation are needed to turn the source's existence parameter into an intrinsic exact invariant.

## Scientific value — PASS

PASS. The theorem identifies the cardinal parameter in a new transfinite homogeneity framework as an intrinsic invariant rather than a freely chosen witness. In the uncountable regime it proves cardinal optimality of the state hypothesis, determines the absolute homogeneity ceiling, and makes the local faithful-corner copy cardinal canonical. This is a natural structural synthesis, not an arbitrary cardinal exercise.

## Source inspections

- **Revisiting the Transfinite Christensen--Pedersen Argument** — https://arxiv.org/abs/2609.20718. Material read: Current primary full text at the definition of \(\kappa\)-homogeneity, Corollary 5.6, Proposition 5.7, and Proposition 5.10. Assessment: SOURCE_PROVIDES_INGREDIENTS_NOT_EXACT_CARDINAL_RIGIDITY. Evidence: The paper supplies transfinite monotone-completeness and state-separation implications and constructs a suitable \(\kappa\), but does not state the audited equality or exact spectrum.
- **Properly infinite AW-star algebras are monotone sequentially complete** — https://doi.org/10.1112/blms/16.4.407. Material read: Theorem-level bibliographic context as used by the primary source. Assessment: CLASSICAL_INGREDIENT. Evidence: It supplies the countable Christensen--Pedersen phenomenon, not the audited transfinite separator-cardinal rigidity.

## Limitations and residual risks

The theorem concerns ordinary states and AW-star homogeneity under the simultaneous hypotheses; it does not identify an analogous normal-state invariant or classify all AW-star homogeneity spectra.

- Older AW-star/Baer-star dimension theory may contain an equivalent projection-multiplicity invariant under different terminology; no such exact ordinary-state separator theorem was located.
- The result applies only under the simultaneous homogeneity and separator hypotheses and does not classify arbitrary AW-star algebras.

## Disposition

**passed**
