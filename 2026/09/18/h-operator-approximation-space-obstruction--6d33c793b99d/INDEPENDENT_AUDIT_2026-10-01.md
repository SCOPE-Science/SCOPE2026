# Independent mathematical audit — 2026-10-01

## Final claim

A two-dimensional obstruction to H-operator approximation schemes

## Correctness — PASS

PASS. The two displayed \(2	imes2\) matrices are each similar to a real diagonal matrix with eigenvalues \(1\) and \(-1\). Similarity therefore gives the required resolvent bound \(C/|\operatorname{Im}\lambda|\), and finite dimensionality gives compactness. Their sum has characteristic polynomial \(t^2+4\), hence spectrum \(\{2i,-2i\}\) and is not an H-operator. Consequently the class of compact H-operators is not additive and cannot itself be a quasi-Banach linear ambient space. The source approximation-scheme definition requires such a linear ambient space, so this is a genuine type obstruction. The separate observation about operators between unequal spaces is also correct: \(T-\lambda I\) and an ordinary eigenvalue sequence are not canonically defined for a map \(X	o Y\) without identifying domain and codomain.

## Originality — PASS

PASS to the best of current knowledge. Targeted searches of the 2024 article, its title/DOI/arXiv identifier, the relevant definition/theorem labels, correction/erratum terms and the nonadditivity formulation did not locate an earlier published objection. The original article itself supplies the conflicting definitions but does not note the counterexample. The 2026 follow-up was available only at abstract level in this audit, so its detailed treatment could already repair the issue; that uncertainty is recorded as residual risk rather than used as novelty proof.

### Equivalent formulations

Nonadditivity is exactly the obstruction to the source's ambient-space formulation; no equivalent correction was found.

### Broader coverage

Broader operator theory does not cover the paper-specific type correction or make it a known theorem.

### Exact database or table

This is not a database numerical claim; the database check is relevant only to whether a published correction already exists.

### Claim versus prior implication

The objection is not stated or mechanically resolved in the inspected 2024 source; the 2026 follow-up remains an access-limited risk, not affirmative coverage.

## Scientific value — PASS

PASS. This is an explicit two-dimensional counterexample to a published approximation-space setup, not a generic textbook observation presented without context. It pinpoints exactly which ambient-space assumption fails, explains why the representation proof uses unavailable subtraction/addition, preserves the valid set-theoretic eigenvalue estimates, and identifies a coherent repair through a genuine linear compact-operator space. That is a motivated boundary correction with clear future utility.

## Source inspections

- **Approximation spaces for H-operators** (DOI 10.2140/involve.2024.17.709; arXiv:2306.03633): SOURCE_CONTAINS_TYPE_MISMATCH. Primary article text around the quasi-norm/approximation-scheme definitions and the H-operator approximation-space setup; the publisher PDF endpoint was also attempted through the PDF screenshot path but was served as HTML by the retrieval layer. The approximation scheme requires a quasi-Banach linear ambient space, while the H-operator definition imposes real spectrum/resolvent conditions not closed under addition.
- **H-Operator Approximation Spaces via Delayed Riesz Means and Quasi-Banach Moduli** (arXiv:2609.14381v1): ACCESS_LIMITED_RESIDUAL_RISK. Abstract only. The abstract describes a constructive quasi-Banach framework but does not expose enough definitions to establish whether it already incorporates the repair.

## Checked sources and replay paths

- Assigned RESULT.md and exact frozen tree
- Direct matrix similarity/eigenvalue calculation
- 2024 primary article text and publication page
- Targeted correction/erratum searches
- 2026 follow-up abstract
- Resultary semantic search

## Residual risks

- Only the abstract of arXiv:2609.14381v1 was inspectable; its full definitions may already fix the issue.
- The publisher PDF screenshot mechanism failed because the endpoint was returned as text/html; the article's searchable text was nevertheless inspected.

## Disposition

**passed**
