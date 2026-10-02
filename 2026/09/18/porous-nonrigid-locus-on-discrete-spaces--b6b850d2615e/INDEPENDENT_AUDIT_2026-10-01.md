# Independent audit — 2026-10-01

## Final claim

Uniform rigid holes in the space of metrics on every discrete set

## Correctness — PASS

The lattice rounding \(q(x,y)=\delta\lceil d(x,y)/\delta\rceil\) is a metric and stays within \(\delta\) of \(d\). Adding \(a\rho\) with \(\delta=R/2\) and \(a=R/6\) keeps the center metric within \(5R/6\) of \(d\). Distinct marker values differ by at least \(a\sigma\), including across adjacent lattice levels because \(\delta-a=2\delta/3\). Hence every metric within \(a\sigma/2\) has any self-isometry preserve the marker relation and is rigid. The explicit small-cardinality marker has gap \(1/2\), while the rigid-relation marker for cardinality at least eight has gap \(1\), yielding exactly \(R/24\) and \(R/12\). The final center-plus-radius inequality is strict and places the rigid ball inside the prescribed ball.

## Originality — PASS

Ishiki's full 2026 paper explicitly leaves density of rigid metrics in the uniform topology as Question 6.1, proving only special cases such as strongly zero-dimensional spaces of cardinality at most the continuum, compact spaces, and totally bounded target metrics. For infinite discrete spaces it even notes that proper-metric methods do not cover a neighborhood of the discrete metric. The audited arbitrary-cardinality discrete theorem, and especially the definite-proportion rigid subball/porosity conclusion, is not a corollary of those results. The rigid-relation and lattice-rounding ingredients are classical and are not themselves claimed as new.

### Equivalent formulations

Searches/sources: Ishiki rigid metrics uniform topology discrete spaces; porous nonrigid metrics space of metrics.

Evidence: Ishiki formulates the same uniform metric \(D_X\) and the same rigid locus \(R(X)\).

Reasoning: The audited result answers the same density question on discrete spaces and adds a quantitative subball statement; this is not merely a renaming.

### Broader coverage

Searches/sources: Ishiki 2026 Question 6.1 rigid metrics; Ishiki 2024 strongly rigid metrics spaces of metrics.

Evidence: The full 2026 source restricts its density theorems to special classes and leaves the general question open.

Reasoning: Existing strong-rigidity density under cardinality/dimension restrictions does not cover arbitrary-cardinality discrete sets, and does not imply the explicit uniform porosity constants.

### Exact database or table

Searches/sources: published SCOPE index: rigid discrete metric porous nonrigid locus.

Evidence: No earlier exact subball constants or arbitrary-cardinality discrete theorem was located.

Reasoning: No exact table/database coverage was found; this is best-of-knowledge evidence only.

### Claim versus prior implication

Searches/sources: Hedrlín Pultr rigid undirected graphs; Ishiki lattice rounding metric approximation.

Evidence: The two main ingredients are prior and independently known.

Reasoning: Their combination is short but not stated in the inspected sources; neither ingredient alone implies a rigid ball around every rounded metric without the residue-separation construction.

## Scientific value — PASS

The theorem resolves an explicitly posed density question on a natural broad class, including cardinalities where strong rigidity by distinct real distances is impossible, and strengthens density to dense interior plus uniform local holes. The quantitative porosity statement is a meaningful structural strengthening, not just another isolated rigid metric construction.

## Sources inspected

- **Yoshito Ishiki, Algebraically independent distances and rigid metrics** (https://arxiv.org/abs/2609.19773): OPEN_QUESTION_CONTEXT_NOT_COVERAGE. Question 6.1 asks density for every metrizable space; the paper proves only restricted cases and explicitly discusses why unbounded discrete spaces escape proper-metric methods.
- **Z. Hedrlín and A. Pultr, On Rigid Undirected Graphs** (https://doi.org/10.4153/CJM-1966-121-7): INGREDIENT_ONLY. It supplies a rigid relation, not a theorem about uniform balls of metrics or porosity.

## Residual risks and limitations

- The constants \(1/24\) and \(1/12\) are convenient certified constants, not asserted optimal.
- The result is restricted to discrete underlying topology and does not settle the Borel-complexity question for the full rigid locus.

## Disposition

**passed**
