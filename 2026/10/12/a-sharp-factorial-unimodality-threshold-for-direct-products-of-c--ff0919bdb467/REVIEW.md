# Scientific review: factorial unimodality threshold for complete-graph direct products

## Correctness — PASS
The statement concerns precisely integers \(a\ge5\) and \(r\ge2a+4\). The underlying complete-graph direct-product polynomial is reconstructed from diameter-two geodesics and a four-type counting classification, agreeing with the corrected 2026 primary source. The proof establishes the increasing coefficient prefix through degree \(a\), bounds both exceptional rectangle coefficients, and identifies the sole critical junction as \(p_{a+1}-p_a\). Its normalized difference crosses zero between two consecutive explicit integers, and the remaining tail is binomial. These arguments prove the infinite-parameter assertion; finite computation is supplemental. Direct enumeration checked 139,776 vertex subsets and algebraic comparisons checked 747 parameter pairs. Risks: human mathematical proof may contain an unnoticed subtle error; no independent external review is represented.

## Originality — PASS, with risks
Iršič et al. (2024), Problem 5.2, pose parameter classification. The 2024 enumerator must not be used for this analysis because Rather (2026), Theorem 5.3, corrected it. The newer source gives the complete polynomial, a mixed-behavior theorem and a full \(a=3\) characterization, but not the stated sharp uniform threshold for all \(a\ge5\). The work is therefore a new phase theorem *deduced from* an already-published enumerator, not a new enumeration formula. Searches of published records, the survey, and the primary papers did not identify the factorial boundary. Risk remains that this boundary, or an equivalent inequality theorem, appears in less-indexed material or follows from a stronger theorem not located; absence from search is not a novelty proof.

## Value — PASS
The threshold resolves a natural infinite high-imbalance region of an explicitly posed graph-polynomial problem, separating a genuine coefficient valley from eventual unimodality by a closed factorial cutoff. The assumption \(r\ge2a+4\) is structurally motivated: it ensures a strict increase in the binomial tail immediately following degree \(a+1\), so one coefficient comparison controls unimodality. This is an exact global phase classification, not an isolated evaluated parameter, relabeling, or finite numerical table. The lower-imbalance and small-first-parameter regimes remain outside this theorem.

## Closest literature and scientific limits
1. Iršič, Klavžar, Rus, Tuite (2024), *General Position Polynomials*, arXiv:2401.05696, Problem 5.2, formulated the classification question.
2. Rather (2026), *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930, Theorem 5.3 and Corollary 5.7, supplied the corrected entire polynomial and the \(a=3\) phase classification. The exact polynomial is prior work and has been fully credited.
3. *The General Position Problem: A Survey*, arXiv:2501.19385, recounts the correction and known unimodality literature. No broader covering factorial phase statement was found in its relevant discussion.

The theorem does not address all \((r,a)\), does not independently establish priority, and has no external independent audit.

Self-review: passed. Independent audit: not yet performed.
